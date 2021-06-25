---
date: "2009-06-23"
tags: ["emacs"]
title: "A few nifty emacs features"
---

I haven’t written anything in a while, and this isn’t a long piece of work either. I’ve been very busy at work, but I figured I’d share a few emacs tricks I discovered while being busy that helped make me a little less busy. I have hyperlinked various emacs functions for further information:

# [M-x fixup-whitespace](https://www.gnu.org/software/emacs/manual/html_node/elisp/User_002dLevel-Deletion.html)
A very useful command that reduces the whitespace around point to a single space, or no space at all if that makes more sense contextually. I edit a lot of Delphi code, with emacs set to use spaces instead of tabs and provide pretty indenting. While this works beautifully, it does have the drawback that I’m left with heaps of whitespace if I turn a multi-line statement into a single-line one, which auto-indenting obviously can’t fix. *fixup-whitespace* does the trick with a single keypress – wish I’d thought to look for something like it long ago.

# M-x count-matches
Return a count for the number of lines matching a regex. Simple, but useful for analysing logs, and something I was settling down to write in Python before I checked to see if such a thing existed.

# [Org Mode](https://orgmode.org/)
Very useful for taking structured notes which can then be output in a variety of formats if desired. Can do way more than just note-taking – many people pretty much use it to organise their lives.

# Batch mode
emacs can be run in batch mode, by passing the *–batch* switch. In batch mode emacs does not expect to have a display device to work with, making it ideal for using in batch files or scripts. Passing an argument after the *–batch* switch will open that argument in a buffer and subsequent actions will be taken on that buffer. The buffer will of course not be visible, but it remains a fully functional emacs buffer.

Batch mode therefore allows you to use emacs to do tasks it is very good at, without needing to interact directly with emacs – great for passing some heavy lifting to emacs in various scripts.

There are a few useful switches to use in conjunction with *–batch*:

* *-f ARG*: Run elisp function ARG on the buffer
* *–eval ARG*: Evaluate elisp snippet ARG

For example, the following line in a Windows batch file will use emacs to properly indent a Delphi source file:

```batch
emacs --batch %1 -f delphi-mode --eval "(indent-region (point-min) (point-max) nil)" -f save-buffer
```
