---
date: "2025-01-15"
tags: ["pulumi"]
title: "Getting URNs of Pulumi resources"
---

This is another Pulumi related entry mainly intended to help future-me. If you wish to update one or several selected [Pulumi](https://www.pulumi.com/) objects instead of the entire stack, you can specify the URN of each object to update, with the **\-\-target** argument to **pulumi update**. It wasn't obvious *how* to get the URNs - a touch of googling showed me the **-u** argument to **pulumi stack**:

```bash
pulumi stack -u
```
