---
date: "2021-06-06"
tags: ["python", "poetry", "docker"]
title: "Tagging Docker images with versions of the software in the image"
---

I use [poetry](https://python-poetry.org/) and [Docker](https://www.docker.com/) for many of my [Python](https://www.python.org/) projects, both [personally](https://gitlab.com/kimvanwyk) and at work. To help with that, I maintain a simple [Poetry-enabled Python 3 Docker image](https://hub.docker.com/repository/docker/kimvanwyk/python3-poetry) which can be used as an [ONBUILD](https://docs.docker.com/engine/reference/builder/#onbuild) base for images. I'd like to at least see the view from near the cutting edge, so I schedule the image to build monthly, using the latest **python3-stretch** Docker image available at the time and installing the latest pip and Poetry versions to that image.

To quickly reflect the software versions in the image, I tag the build with a tag reflecting the Python, pip and Poetry versions inside the image. As an example, the image built in June 2021 is tagged:

**210601-python3.7.4-pip21.1.2-poetry1.1.6**

The latest image is also tagged with the conventional "**latest**".

The only way I could think to get this info was to write a manifest file inside the image while it is being built and then read that file when tagging the built image. To make a manifest file at */manifest.txt* I include this line towards the end of the [Dockerfile](https://gitlab.com/kimvanwyk/python3-poetry/-/blob/master/Dockerfile):

```docker
RUN echo "Tag:" >> /manifest.txt; \
echo $(date +%y%m%d)\
-python$(python --version | cut -d " " -f2)\
-pip$(pip --version | cut -d " " -f2)\
-poetry$(poetry --version | cut -d " " -f3)\
>> /manifest.txt; \
echo "\nVersions:" >> /manifest.txt; \
echo $(python --version) >> /manifest.txt; \
echo $(pip --version) >> /manifest.txt; \
echo $(poetry --version) >> /manifest.txt; \
echo "\nPackages:" >> /manifest.txt; \
echo $(pip freeze) >> /manifest.txt; 
```

As I'm already creating a file inside the image, I include the available Python packages as additional info. The manifest file for the June 2021 image looks like this:

<code>
Tag:
210601-python3.7.4-pip21.1.2-poetry1.1.6

Versions:
Python 3.7.4
pip 21.1.2 from /usr/local/lib/python3.7/site-packages/pip (python 3.7)
Poetry version 1.1.6

Packages:
appdirs==1.4.4 CacheControl==0.12.6 cachy==0.3.0 certifi==2021.5.30 cffi==1.14.5 chardet==4.0.0 cleo==0.8.1 clikit==0.6.2 crashtest==0.3.1 cryptography==3.4.7 distlib==0.3.2 filelock==3.0.12 html5lib==1.1 idna==2.10 importlib-metadata==1.7.0 jeepney==0.6.0 keyring==21.8.0 lockfile==0.12.2 msgpack==1.0.2 packaging==20.9 pastel==0.2.1 pexpect==4.8.0 pkginfo==1.7.0 poetry==1.1.6 poetry-core==1.0.3 ptyprocess==0.7.0 pycparser==2.20 pylev==1.4.0 pyparsing==2.4.7 requests==2.25.1 requests-toolbelt==0.9.1 SecretStorage==3.3.1 shellingham==1.4.0 six==1.16.0 tomlkit==0.7.2 urllib3==1.26.5 virtualenv==20.4.7 webencodings==0.5.1 zipp==3.4.1
</code>

Once the image is built, the tag can be extracted by briefly running the container and reading the */manifest.txt"* file (handled by [Gitlab CI](https://gitlab.com/kimvanwyk/python3-poetry/-/blob/master/.gitlab-ci.yml) in this case):

```bash
export TAG=$(docker run --rm "IMAGE_NAME:latest" \
cat /manifest.txt | awk NR==2)
docker tag IMAGE_NAME:latest IMAGE_NAME:$TAG
```

While this method works perfectly well, I would prefer not to include a file in the completed image (albeit a very small one) just to get tag information from. While the manifest file might be useful while running the image, all of the information in it could be obtained during execution if it was needed, so the manifest file feels a bit wasteful. If you come across this post and have a better suggestion on how to get the software version information without modifying the resulting image, please do get in touch.
