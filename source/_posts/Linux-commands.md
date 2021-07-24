---
title: Linux_commands
tags: tech
date: 2021-07-05 17:35:29
catagories:
---

<!--more -->
## Useful Linux Linux_commands


### Command + Flags + Arguments(Parameters)

- `pwd` print working directory
  
- `cd` change directory
  - just enter `cd` will bring you back to `~` directory 
  - `cd ..` bring you back to previous directory
  - `cd ../..` bring you to the directory previous to previous directory
  
- `ls` list
  - `ls -l` show details of files
  - `ls dirname` show files under specified directory
  - `ls -a` show all files(including `.` hidding files)


-  `man command` show manuals
   -  exmaple `man ls` 
   -  we can use `/` to search for keywords and press `q` to quit

- `cat` concatenateshow contents of the file

- `less` show contents of the file(vim like operations)

- `head`
  - `head -n 5 furits.txt` print first 5 lines(default is 10)

- `tail` print last 10 lines, can also be used with flag `-n`

- `wc` word count, show number of lines, words, and characters consecutively
  - `wc -l` only show number of lines

- `sort` sort and showthe content of a file, without changing the content.
  
- `grep` look for the pattern in the file
  - `grep "berry" fruit.txt` (`""`, `''` and just without quote are the same)

- `uniq` only show unique element in the file

- Java related commands
  - `javac` compile the .java file
  - `java` run the program

- `xargs`
  * takes input from standard input as the command line input
  * `ls *.java | xargs javac`is the same as `javac *.java`
  * we can also put xargs to the front: `xargs javac < ls *.java`

- `find`
  * `find -name "*.java"`
  * use with xargs `find -name "*.java" | xargs javac`

- `tee`
  * Write into Files and Print to Console at the same time.(duplicate stdout)
  * `java Mystery.java | tee tee_out.txt` By default, only stdout will be written into the txt file.
  * `java Mystery.java 2>&1 | tee tee_both.txt` Both stdout and stderr will be written into tee

- `echo`
  - print the argument

- `cut`
  - `-c` start at index of 1.
    - `cut -c4`  index 4
    - `cut -c4-6` index 4-6
    - `cut -c3,4,5` index 3,4,5
  - `-d` deliminter `-f` the index of field we want to choose
    - `echo "a,b,c,d,e,f" | cut -d, -f1`  -> `a`

## basics about vim
- the mode we first enter is command mode and we can use `h` `j` `k` `l` to move the cursor(h -> left j -> down k -> up l -> right )
- press `i` to enter insert mode
- press `esc` to quit insert mode
- `:w` to save file and `:q` to quit file

## Standard Streams
  Every unix process has three streams, which are abstract locations that tell a program where to read input from and where to write output to.

  There are three standard streams.
  -  stdin
  -  stdout(`System.out.println()`)
  -  stderr
  
  All the streams, in default, will read/output data in console. They can also be redirected.
  
  for example 

  `grep "berry" fruit.txt > berries.txt` **redirect stdout**

  `java HelloWorld < berries.txt"` **redirect sdtin**

  `java HelloWorld 2> out2.txt` **redirect stdout**

  `java HelloWorld >> out.txt` **append the output to the end of the file**

  `java HelloWorld 2>&1 [filename]` **redirect standard error to standard output / other files**

  `java a.java > mystery.txt 2>&1` **redirect both stdout and stderr to the file.**

## Pipes
  `|` read the output before and use it as the input for the command behind it.

  `grep "berry" fruits.txt | wc -l`

## Logics for Linux Command Line

* `&&`, `||` still works for Linux Command Line.
> exmaple:  
> `javac HelloWorld.java && java HelloWorld` will complie then execute HelloWorld.java(if complie failed, the latter command will not be executed)  
> `ls dir || cd dir` if the former part is ture, then the latter part will never be executed.
> `ls dir; cd dir` This just separate the commands, just like typing it line by line.

## 

