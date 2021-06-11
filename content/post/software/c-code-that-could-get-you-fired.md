---
date: "2012-10-03"
tags: ["c", "code"]
title: "C code that could get you fired"
---

Here’s another stupid C trick I’ve carried around in my brain for a while:

```c
#define sizeof(x) (rand() % 20 + 1)
```
The mod and addition are to give a random number in the range from 1 to 21.

This can be demonstrated with a small program:

```c
#include <stdlib.h> 
#include <stdio.h>

#define sizeof(x) (rand() % 20) + 1

void main()
{
  int i;
  printf("Sizeof i: %d\n", sizeof(i));
  printf("Sizeof i: %d\n", sizeof(i));
  printf("Sizeof i: %d\n", sizeof(i));
  return;
}
```
When run, you get:

```bash
# ./random_sizeof
Sizeof i: 4
Sizeof i: 7
Sizeof i: 18
```
Your compiler might warn you about this, although mine didn’t (using GCC 4.3.2 with no flags) – but on a large project, there are probably so many warnings that an extra one wouldn’t be noticed anyhow (if all the large projects you’ve worked on had no warnings at all, you’re luckier than most of us).

Unlike the trick I [posted previously](/c-code-you-should-never-use-in-production), using this in your code will not have your colleagues worry about your competence so much as it will prompt them to fill a box with your things and show you the door….
