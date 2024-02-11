---
date: "2024-02-11"
tags: ["aws", "python"]
title: "Building an AWS Lambda layer with non-pure Python modules"
---
An [AWS Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html) is a good way to provide code and resources intended to be common to more than 1 AWS Lambda function. I have several related Lambdas which require a set of common Python modules. The layout of such a layer is fairly simple - the Python package directories are all placed into [a base **python** directory in a zip file](https://docs.aws.amazon.com/lambda/latest/dg/packaging-layers.html#packaging-layers-paths). For example:

```
pillow.zip
│ python/PIL
└ python/Pillow-5.3.0.dist-info
```
Creating such a directory is fairly simple with pip, using the *--target* option:

```bash
pip install PACKAGE --target BASE_DIR
```

This works perfectly well from any Python-capable OS when all the modules are pure Python. It doesn't however work well if at all for modules with non-Python dependencies, such as C or binary components. I needed [psycopg2](https://pypi.org/project/psycopg2/) in my layer, which can include some binary files or require compilation from C. Neither my colleague's Windows 11 machine or my own Ubuntu linux machine are likely to produce a packaged module which a Lambda can run on its AWS-flavoured Linux OS. 

I borrowed a clever idea from [this excellent project](https://github.com/jetbridge/psycopg2-lambda-layer) - using a suitable [AWS Lambda Docker image](https://gallery.ecr.aws/lambda/python) a simple script can:
* build a Docker image using the AWS Lambda image as a base, which uses pip to install required packages into a given directory
* start a container from the newly built image
* copy the package directory out of the running container into a **python** directory
* build a zip file with the **python** directory as its only root-level entry
* stop and remove the running container
* remove the built image

As a simple example, here's a *Dockerfile* suggestion:
```docker
FROM public.ecr.aws/lambda/python:3.12

ARG REQUIREMENTS_FILE=requirements.txt
RUN mkdir /app
COPY $REQUIREMENTS_FILE /app/
RUN pip install -r /app/$REQUIREMENTS_FILE --target /app/package
```

The [**ARG**](https://docs.docker.com/engine/reference/builder/#arg) line allows the file to be used to build more than 1 kind of layer by using a different *pip* requirements file, defaulting to **requirements.txt**. Here's a simple bash script to use this Dockerfile:

```bash
docker build . -t layer --no-cache --build-arg REQUIREMENTS_FILE=$1
CONTAINER=$(docker run -d --rm layer false)
rm -rf python
rm -rf layer.zip
docker cp $CONTAINER:/app/package python
zip layer.zip -r python/
docker stop $CONTAINER
docker rmi layer
```
