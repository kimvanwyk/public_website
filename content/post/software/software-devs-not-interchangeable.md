---
date: "2022-12-08"
tags: ["software development"]
title: "Software developers are not interchangeable"
---

A topic I and any software developer of similar several-year experience I've discussed it with have come to realise: 

> To people who don't write software or do related work, software developers look interchangeable. 

This does make sense - code can be incomprehensible if you're not in the profession so it doesn't seem overly surprising that non-developers assume it's all the same. Similarly I'm quite sure there are huge differences in accounting work (to pick a random example) that I don't even know exist.

Even as many people will realise for example that there are software developers who work with the website and ones who work with the "server", they may well not realise that there are hundreds of possible specialities. While a grasp of the fundamentals is true of all software developers, this doesn't mean any given developer can do the work of any other without having to gain some knowledge or even experience.

This can manifest in a paid-to-write-software environment as project management or line management assigning tasks the assignee can't do, on the assumption that any developer could do any of the tasks in their list. Junior developers are often scared to say they can't do the task for fear of looking dispensable and a situation arises which helps no one - the developer can't do the task immediately and will in the best case take much longer than anticipated to get it done, the project manager gets frustrated that the work isn't being done after they've made what they quite reasonably see as a valid assignment and the company wastes time and resources.

To illustrate my point with two examples from my own career:

* I was asked to assist on a project which a colleague had been struggling with. My colleague was an exceptional developer - they were literally one of the 2 or 3 most knowledgeable experts in the world on the complexities of very low-level security code for a globally-used television decoder platform. They had been tasked with calibrating the touchscreen interface on a piece of equipment we were developing. The device had a touchscreen module and a non-touchscreen module which the Linux OS saw as a single virtual device. My colleague was trying to use the GUI calibration tool to specify which portion of the virtual device was a touchscreen, but could not find any suitable options. After they'd spent a few days on it, I was able to calibrate the screen in 15 minutes. This doesn't make me a better developer than my colleague - far, **far** from it (see afore-mentioned world-expert status). I just happened to have Linux experience that they didn't and I knew it was likely the GUI tool would take additional arguments on the command line which the GUI itself didn't expose. With the CLI settings calibrating just the touchscreen module became trivial. This boiled down entirely to me having a bit of experience my colleague didn't (nestled amongst thousands of such experiences each of us had that other didn't).

* Another colleague wrote an elegant and clever Javascript tool to parse inconsistent and poorly-specced XML files (which is exactly as fun as it sounds). Some years after they'd moved employers, the XML files changed. I was tasked with updating the tool to work with the new files, and I failed because my Javascript wasn't very good. I could tell by looking at the code that the tool was seriously elegant and well-written, but I couldn't confidently make changes to it that would still work. I ended up re-writing the tool in Python, which obviously took longer than had I been capable of updating the Javascript, but not nearly as long as it would have taken to develop enough confidence in Javascript to update the original tool. This again boils down to experience - I don't consider myself a lesser developer because I couldn't handle this task, just one without the Javascript knowledge I would have needed to make it work in the time I had available.

I could probably list another 10-20 such experiences if I indulged myself and I have no doubt any developer with a few years or more of experience could easily do so as well. *Developers aren't interchangeable*. 

As a non-developer, please don't assume they are and make plans that depend on it. As a developer, particularly a junior one, please never feel you're a lesser developer than a fellow developer might be if they can handle a task that you couldn't do as well. The reverse is probably true as well - you can do some tasks better than they could. Developers aren't interchangeable and its ok not to be.
