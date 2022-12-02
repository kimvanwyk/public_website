---
date: "2022-12-02"
tags: ["python", "aws"]
title: "Uploading a directory tree to AWS S3 in a few lines of Python"
---

I occasionally need to upload a directory tree to an AWS S3 bucket, which can have many levels of subdirectories and files. This is doable with the [Python boto](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) library, but the last time I used it to do this task it was quite tedious.

[Will McGugan](https://fosstodon.org/@willmcgugan@mastodon.social)'s excellent [PyFilesystem](https://docs.pyfilesystem.org/en/latest/) and its [S3FS](https://fs-s3fs.readthedocs.io/en/latest/) interface reduces this task to a few lines. Here's a minimalish but functional example (with bonus *.html* file exclusion):

```python
import fs_s3fs
from fs.copy import (
    copy_dir as fs_copy_dir,
)
from fs.walk import Walker as fs_walker

fs = fs_s3fs.S3FS(
    "BUCKET",
    "ACCESS_KEY",
    "SECRET_KEY",
    "af-south-1",
)

fs_copy_dir(
    "/",
    SRC_DIRECTORY,
    fs,
    TARGET_DIR,
    walker=fs_walker(
        exclude=["*.html"]
    ),
)
```

The first argument to *fs.copy_dir* is the local filesystem, given as the root of a Linux or Docker filesystem in this case.

If [Will McGugan](https://fosstodon.org/@willmcgugan@mastodon.social) sounds familiar, he's also the author of the more recent [rich, rich-cli and textual](/in-praise-of-rich-and-rich-cli). He's a prolific source of brilliant Python modules!
