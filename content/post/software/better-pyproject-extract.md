---
date: "2021-07-22"
tags: ["python", "pyproject-toml"]
title: "In search of a better way to extract project details from a pyproject.toml file"
---

I use [poetry](https://python-poetry.org/) to manage my Python projects, which means I have useful information in a *pyproject.toml* file at the root of my project directory, including:
* Author name and possibly contact details
* Project name
* Project description
* Version

A well-behaved tool should obviously include some or all of this information when invoked at the command line or via its GUI. To avoid repeating myself (and having data get out of sync) I prefer to extract the info from the *pyproject.toml* file to use in my Python source. I use a small Python script to do this (see [here](https://gitlab.com/-/snippets/2149079)). This script checks for a *pyproject.toml" file in:

* the **sys._MEIPASS** attribute (present if the tool is running as a [PyInstaller](https://pypi.org/project/pyinstaller/) executable)
* the directory the script is in
* one directory up from the script

If it finds a *pyproject.toml* file in any of those, it stops looking and returns some project details which the source can use. 

This works but it feels rather hacky. I would love to be able to import the *pyproject.toml* file directly into my source and get the project details from it but have not been able to find or figure out a way to do this. If anyone can point me in the right direction I would be very happy to stop using this hacky technique.
