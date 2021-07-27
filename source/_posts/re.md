---
title: regex_and_sed
date: 2021-07-05 17:05:26
tags: regex
catagories: Linux
---
</br>
<!--more -->

## sed

### usage `sed -r 's/REGEX/TEXT/TAGS' filename` 
* `sed -r 's/Taylor/Josh' names.txt` replace 'Taylor' with 'Josh' and print out
* `sed -ri.bkp 's/Taylor/Josh' names.txt` replace 'Taylor' with 'Josh' in the names.txt and save an original copy of names.txt into names.txt.bkp
> by default it only replaces the first match in a line, if we want to replace all the occurences, we need to use `sed -r 's/Taylor/Josh/g' names.txt` '`/g ` stands for global
> escape '/' character -> use `\/` 