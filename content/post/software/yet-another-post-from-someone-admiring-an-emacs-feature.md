---
date: "2008-06-26"
tags: ["elisp", "emacs"]
title: "Yet another post from someone admiring an Emacs feature"
---

I’ve been using Emacs for some time now, and I’ve grown to really appreciate it. One of the nifty features introduced in Emacs 22 is the ability to execute arbitrary elisp when replacing text using regular expressions (elisp is the Lisp dialect in which Emacs itself is written and through which it can be extended). I had reason today to use the feature for a silly little problem, and I was impressed, so here’s why.

I had a set of data where I had to replace a placeholder on each line with an integer, which incremented every four lines, starting at 2. i.e:

<code>
x line 1<br>
x line 2<br>
x line 3<br>
x line 4<br>
x line 5<br>
x line 6
</code>

should become:

<code>
2 line 1<br> 
2 line 2<br> 
2 line 3<br> 
2 line 4<br> 
3 line 5<br> 
3 line 6
</code>

This would be quite tricky to solve with a normal regexp replace operation, but under Emacs I simply defined a new function to do the hard work:

```elisp
(setq mod_id 1)

(defun four_inc (y)
        (if (eq 0 (% y 4)) (setq mod_id (1+ mod_id)) mod_id)
)
```

I evaluated those two pieces of elisp in place in the scratchpad I was working in (another massively nifty Emacs capacity) and then ran a regular expression replacement, replacing **x** with **\\,(four_inc \\#))**. The **\\,** tells Emacs to insert the result of calling the four_inc function into the replacement text, and **\\#** is the number of replacements already done.

This is hardly earth-shattering stuff, but it’s the ability both to extend Emacs however one desires (by writing an increment-every-4-times function in this case) and the heaps of nifty features other people have already provided (executing arbitrary elisp code in a regexp replacement for example) that explains to a large degree why I like Emacs so much.
