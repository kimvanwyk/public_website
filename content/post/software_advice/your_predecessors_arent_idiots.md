---
date: "2021-06-06"
tags: ["software development", "advice for new developers"]
title: "Unsolicited advice from a not-so-new developer: Your predecessors weren't idiots"
draft: true
---

I've been a professional software developer (i.e. employers have paid me to write code, possibly against their better judgement) for almost 20 years. Like everyone else with a similar career path, I've picked up some advice for new developers along the way, sometimes somewhat painfully learned. Here's one of those pieces of advice:

# Your predecessors weren't idiots

Almost any system you work on that is more than a few months old or has more than a few hundred lines of code is likely to have some components you think would be better if done differently. It's tempting to assume that you must be a better developer than the people who wrote those parts of the system because you can see a better way to do things. 

It's however very unlikely that the system's previous developers were all incompetent - consider instead that you're looking at the system as a whole after various pieces were written. When some parts of the system were developed the rest of the system either didn't exist or was different to how it is now. What looks like a bad design now may have been perfectly reasonable at the time - it may indeed have been the only way to accomplish the task. 

For example, if some part of the system is using a [SOAP](https://en.wikipedia.org/wiki/SOAP) protocol rather than a RESTful one, it's probably more likely that some third-party requirement only spoke SOAP at the time, not that the developers of the system considered SOAP superior to REST.

Similarly, the circumstances at the time parts of the system were written may have dictated the design decisions:

* Possibly a business opportunity could only be met if a new part of the system was made available as soon as possible, leading to a tightly coupled and quickly written component. We'd all love the luxury of coming back after the deadline is met to fix these rush-job components but that often isn't possible as the business has new requirements that need to be met instead.

* Perhaps the invoicing system outputs a CSV file with very specific columns because the finance department had 3rd party software 15 years ago that could only consume that. That 3rd party software may no longer be around but other parts of the software now cater for and expect that format.

* The technology choices available now aren't the same as they were last year, let alone 5-10 or more years ago. Many large enterprise systems have been around at least that long and in many cases much longer. For example, a document database like MongoDB may be the "obvious" choice for the company's loosely-structured customer data, but when that part of the system was written no one had ever heard of a document database. Design decisions made for perfectly good reasons at the time still have to work now, so in this example a relational table database is still used because it has been extensively bug-tested and improved over the years. Assume also that the developers who came before you are also well aware that a document database would be a better choice now, but in general projects to replace a core part of a large system are going to get less priority and management buy-in than projects that the rest of the business will directly benefit from.

In general, do your fellow developers (and those you've never met who came before you) the courtesy of assuming they knew what they were doing. If some part of the system you're working on could be done differently, you should explore the options for replacing it and discuss those options with the developers who worked on it before - almost all systems definitely have areas that could be improved. Mistakes would certainly also have been made by previous developers - but do those developers the same favour you'd like future developers to extend to you and assume that the parts of the system that seem "bad" were done that way for excellent reasons at the time.
