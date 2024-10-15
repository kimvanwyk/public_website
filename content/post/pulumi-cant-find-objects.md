---
date: "2024-10-15"
tags: ["pulumi"]
title: "A possible (and simple) solution if Pulumi can't find existing AWS resources"
---

This has happened to me a few times, so this is a blog entry mainly intended to help future-me. If [Pulumi](https://www.pulumi.com/) reports via a **pulumi up** or **pulumi refresh** command that some Pulumi-managed AWS resources don't exist and you know they do via the AWS console or similar, you've quite possibly forgotten to set the region. This leads Pulumi to use *us-east-1* for S3, SQS, SNS and similarly regional resources instead of the *af-south-1* my resources live in. In my case, a simple
```bash
export AWS_REGION=af-south-1
```
sufficed.
