---
date: "2023-08-06"
tags: ["python", "podcast"]
title: "A somewhat convoluted solution to listening to podcasts on my phone"
---

For some time, I've used a somewhat convoluted mechanism to download podcast files to my phone from my laptop. Here's what I do, in the event this might be helpful to someone else as well:

# Managing Podcast Feeds

I use [gPodder](https://gpodder.github.io/) on my Ubuntu laptop to track RSS feeds of podcasts of interest to me and download episodes I want to listen to. I also use gPodder to mark episodes I've listened to and remove any files I've listened to and don't want to keep for later re-listening.

# Downloading Podcast Files

To download individual podcast files (typically MP3s) to my phone, I:

* Use the right-click context menu in gPodder to copy the files to a central directory on my PC
* Visit that directory in a terminal and execute ```python -m http.server```
* On my Android phone, I use [QPython](https://www.qpython.com/) to execute this script:

```python
import requests
from urllib.parse import unquote
from bs4 import BeautifulSoup

import os 

BASEDIR = "/storage/emulated/0/Download/podcasts"
URL = "URL_OF_SERVER"
res = requests.get(URL)
soup = BeautifulSoup(res.text, "html.parser")
links = [link.get("href") for link in soup.find_all("a") if any([ext in link.get("href") for ext in ("mp3", "m4a")])]
for link in links:
    print(f"Downloading {link}")
    with requests.get(f"{URL}/{link}", stream=True) as res:
        with open(os.path.join(BASEDIR, unquote(link)), 'wb') as f:
            for chunk in res.iter_content(chunk_size=8192):
                f.write(chunk)
```

This script is also published as a gist [here](https://gitlab.com/-/snippets/2579352). The script ensures the files have readable names on my phone.

# Playing Podcast Files

I currently use [AIMP](https://www.aimp.ru/) to listen to the files on my phone. I used it mainly to avoid accidentally losing my place when hitting the wrong button on my Bluetooth headphones - at the time I started using it AIMP was very good at always keeping my place in every file I was listening to. It seems to have got worse at that though, so I'm probably on the hunt for a replacement player. Suggestions are most welcome.

