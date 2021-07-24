---
title: regex_intro
date: 2021-07-05 17:09:34
tags: regex
catagories: Linux
---
<!--more -->

## regex - regular expression

### use with grep -E

* `grep -E "." a.txt`
  * "." means any character
  * match every element 
* `grep -E "^a" a.txt`
  * match line start with a
* `grep -E "a$" a.txt`
  * match line end with a
* `grep -E "\\<a" a.txt`
  * match pattern start with a
* `grep -E "s\\>" a.txt`
  * match pattern end with s
* `grep -E "^word$" a.txt`
  * match the line contains exactly the "word"
* `grep -E "\\<word\\>" a.txt`
  * match the exact words
* `grep -E "et|at" a.txt` <=> `grep -E "(e|a)t" a.txt`
  * use "|" as or
* `grep -E "e*t" a.txt`
  * match 0 or more e's 
  * so words with only t will be matched
* `grep -E "e+t" a.txt`
  * match 1 or more e's
* `grep -E "e?t" a.txt`
  * match 0 or one of
* `grep -E "(a|b|c|d|e)" a.txt` <=> `grep -E "[abcde]" a.txt`
* `grep -E "[a-zA-Z0-9]" a.txt` 
* `grep -E "[a-zA-Z0-9]+" a.txt` 
* `grep -E "[a-zA-Z0-9]{3}" a.txt`
  * specify the time of the emergence for these characters 
* `grep -E "[a-zA-Z0-9]{,3}" a.txt`
  * limit the time of the emergence for these characters into 0-3
* `grep -E "[a-zA-Z0-9]{2,3}" a.txt`
  * limit the time of the emergence for these characters into 2-3
* `grep -E "[a-zA-Z0-9]{3,}" a.txt`
  * limit the time of the emergence for these characters into 3 or more of
* `grep -E "[^0-9]" a.txt`
  * match the pattern without numbers
  * `grep -E "^[0-9]" a.txt`
    * match the pattern start with numbers 
* `grep -E "(..)\1" a.txt`
  * back reference 
  * match patterns like abab
  * `grep -E "^(.).*\1$" a.txt`
    * match patterns start and end with same character