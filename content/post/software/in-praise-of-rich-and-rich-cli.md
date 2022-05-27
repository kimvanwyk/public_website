---
date: "2022-05-27"
tags: ["python", "terminal"]
title: "In praise of rich, rich-cli and Textual"
---

I've been using [Will McGugan](https://mobile.twitter.com/willmcgugan)'s [rich-cli](https://github.com/Textualize/rich-cli) on my terminal in the last month or so and I cannot recommend it enough. It leverages the astonishing capacity of Will's [rich Python library](https://github.com/Textualize/rich) to provide a viewer for a variety of files which produces beautiful output with no tweaking required. I've used it for CSV and JSON files and it can also do Markdown and a heap of others, with options for text width, choice of theme and much other magic.

I [tweeted](https://mobile.twitter.com/kim_vanwyk/status/1529883188973252608) an example of looking at CSV's recently:

![image](/images/220527_rich_cli_csv.png)

The JSON and Markdown support is also impressive:

![image](/images/220527_rich_cli_json.png)

![image](/images/220527_rich_cli_md.png)


I'm quite sure there are many tools available for each of these use cases that are as good or better for the individual file types - [jq](https://stedolan.github.io/jq/) for JSON, for example. I see the strength of rich-cli as being a very good way of looking at a bunch of different file types with the same tool, without me needing to remember or install a tool per file type. This has become a great productivity boost while also giving gorgeous results.


[rich](https://github.com/Textualize/rich) is also well worth looking at for Python projects - a single line is worth many times the cost of the bytes:

```python
from rich import print
```

A rather contrived example of using it for print():
```python
import rich

d = {
    "owner": "Mary",
    "pets": [
        {
            "type": "lamb",
            "size": "little",
            "specs": {"fleece": "snow"},
            "behaviour": [
                {"action": "follow", "likelihood": 100},
            ],
        }
    ],
}
print(d)
rich.print(d)
```
![image](/images/220527_rich_example.png)


It will also do wonders with your tracebacks and other outputs, and I'm not doing it justice at all by barely scratching the surface. Will covered it in-depth in [this Talk Python episode](https://talkpython.fm/episodes/show/336/terminal-magic-with-rich-and-textual) and still didn't get to cover everything it can do.

I haven't even got to the most ambitious of Will's projects - [Textual](https://github.com/Textualize/textual) is a simple, quick and frankly astonishingly powerful tool for building Terminal User Interfaces (TUIs). I begrudgingly write a terrible looking, clunky GUI when I have to, although my users are normally lucky to even get a CLI. With Textual in my arsenal though I'm going to be much happier to make a TUI instead of a CLI, which has the strong potential to also be the GUI and/or web interface to my tool with no further work on my part.

Keep an eye on [Textualize](https://www.textualize.io), the firm Will has formed to develop rich, Textual and tools in their vein - given the excellence of the tools further fantastic developments will be coming our way.
