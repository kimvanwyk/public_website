---
date: "2023-07-13"
tags: ["pulumi"]
title: "Accessing protected Pulumi outputs with a PGP key"
---

I've been using [Pulumi](https://www.pulumi.com/) on a few recent projects to manage the AWS infrastructure. I'm greatly enjoying writing infrastructure config in Python and I find it generally fits my brain a bit better than Terraform. One smallish item that did confuse me when I first used it though was how to access values Pulumi quite reasonably considers to be sensitive - in this case AWS IAM user secret keys IAM users Pulumi creates. Pulumi's [aws.iam.AccessKey](https://www.pulumi.com/registry/packages/aws/api-docs/iam/accesskey/) module specifies that the secret key is available in *encrypted_secret* if a PGP public key is provided to encrypt it with. It took me a bit of time to figure out how to do that (on an Ubuntu OS in my case) - here's what I did in case it's useful to somebody else:

## Make a PGP key
If you don't already have a suitable PGP keypair available, you'll need to generate one. There are many resources for doing this - I've found [GitHub's instructions](https://docs.github.com/en/authentication/managing-commit-signature-verification/generating-a-new-gpg-key) very good, for example. I generated a keypair without a pass phrase, to make using it on the command line and in piped command chains easier.

As part of this process you may need to install **gpg** or a suitable equivalent for your OS.

## Export and Base64 Encode the PGP Key
Once you have a PGP key (or you're using an existing one), find the keypair's public key ID:

```bash
gpg --list-keys --keyid-format=long
```

This will yield a list of keys that will look similar to the below. The ID of the public key is the long string on the second line below, "*1234567890ABCDEF1234567890ABCDEF*" in the example.

```bash
sec   rsa3072/1234567890ABCDEF 2023-05-31 [SC]
      1234567890ABCDEF1234567890ABCDEF
uid                 [ultimate] Key Description <EMAIL_ADDRESS>
ssb   rsa3072/1234567890ABCDEF 2023-05-31 [E]
```

PGP keypairs are not text, so for ease gpg provides an ASCII-armour option to produce a text version of the key information. The armoured format is not however useful to Pulumi, which requires a base64 encoded unarmoured public key. To avoid producing a binary file which can clutter your terminal, its probably easiest to pipe the binary formatted public key into **base64** and then into a file. The **base64** program or OS equivalent may need to be installed.

```bash
gpg --export 1234567890ABCDEF1234567890ABCDEF | base64  > base64ed_public_key.txt
```

## Using in Pulumi

To use the key as a Pulumi input, supply the contents of the above base64'ed file to the *pgp_key* input. As a small Python example:

```python
with open("base64ed_public_key.txt", "r") as fh:
    pgp_key = fh.read()
access_key = aws.iam.AccessKey(
    "access_key",
    user=user.name,
    pgp_key=pgp_key,
)
```

As part of your Pulumi code, output the values which Pulumi will encrypt with the key. For example:

```python
pulumi.export(
    "secret key", access_key.encrypted_secret
)

```

This will produce a long string on your console when the Pulumi stack is executed. To decode that string, pipe it into **base64** and **gpg** (which will use the keypair it already knows about):

```bash
echo LONG_STRING_OF_BASE64_ENCODED_DATA | base64 -d | gpg -d
```

This should output a PGP decrypted string to your console.
