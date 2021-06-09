---
date: "2006-08-05"
tags: ["c", "code"]
title: "C code you should never use in production"
---

Here's a stupid little C trick which amuses me. Consider a C array:

```c
char array[3] = {1,2,3};
```
To access element 3, you would use

```c
array[2]
```
This is just shorthand for a pointer dereference

```c
*(array + 2)
```
This is just addition, which is associative, so it’s the exact equivalent of

```c
*(2 + array)
```
which gives you

```c
2[array]
```
which is perfectly valid C.
 

To prove that, consider this simple program

```c
void main()

{

char array[3] = {1,2,3};

printf("array[2]: %d. 2[array]: %d\n", array[2], 2[array]);
}
```
After compilation

```bash
./assoc.out
array[2]: 3. 2[array]: 3
 ```

I would **strongly** caution against ever using this in production. Your colleagues will worry about you if they see it during a code review or when working on code you wrote. If you don’t think they would flag it, you should be worrying about them instead.
