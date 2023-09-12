---
date: "2023-08-09"
tags: ["python","pyfilesystem","s3fs"]
title: "Changing from writing files to subdirectories on a local filesystem to an S3 bucket with a few lines of code"
draft: false
---

A recent Python tool I developed downloaded media files and related JSON metadata files. For development these files were written to a directory on my local filesystem, into subdirectories named for a date in the metadata. For production use these files are uploaded to an AWS S3 bucket, with /-separated keys using the same date values. My previous experience doing this has involved the *os* and *shutil* built-in Python modules for the filesystem writes and the AWS [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) package for S3 uploads. The code for these 2 types of write are completely different and requires considerable conditional logic to determine what to do with each file.

This time I used the [PyFilesystem](https://docs.pyfilesystem.org/en/latest/) and [FS-S3FS](https://fs-s3fs.readthedocs.io/en/latest/) packages, which made this almost trivially simple. [Will McGugan](https://fosstodon.org/@willmcgugan@mastodon.social) originally developed this amazing package and a team of very capable maintainers has kept it going strong.

As a small example, here's the relevant code for writing files to my local filesystem:

```python
from fs.osfs import OSFS
fs = OSFS(CENTRAL_DIR)
# obtain metadata as a JSON dict
subdir = f"{json_dict['date']:%y%m}"
with fs.makedirs(subdir, recreate=True).open(fn, "w") as fh:
    json.dump(json_dict, fh)
# obtain media file
with fs.opendir(subdir).open(PATH, "wb") as fh:
    fh.write(MEDIA_FILE)
```

This code will make any date-derived subdirectories that don't exist.

To instead write the same files to an S3 bucket, only the first 2 lines need to change, assuming the access credentials are stored as env variables (*AWS_ACCESS_KEY_ID* and *AWS_SECRET_ACCESS_KEY* respectively) or in another standard AWS mechanism such as a credentials file:

```python
from fs_s3fs import S3FS
fs = S3FS(BUCKET_NAME, region=REGION)
```

The rest of the code will upload to the S3 bucket with no further changes at all. 

This kind of abstraction makes working with files that need to be written to a variety of very different locations extremely easy - I both wish I knew about it years ago and thank the team of maintainers for a superb package.
