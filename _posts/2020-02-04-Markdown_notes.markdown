---
layout: post
title:  "Notes For Markdown"
date:   2020-02-05 00:21:00 
categories: Notes
---
# Notes For Markdown

- ## Itatic and Bold
  `_This is itatic_`  
  _This is Itatic_  


  `**This is bold**`  
  **This is bold**

- ## Headers
   `# This is header one`
   # This is header one

   `## This is header two`
   ## This is header two

  `### This is header three`
  ### This is header three

  `#### This is header four`
  #### This is header four
 
  `##### This is header five`
  ##### This is header five

  `###### This is header six`
  ###### This is header six

- ## Inline link

  `This is a link to my [blog page](https://yang029.github.io)`  


   This is a link to my [blog page](https://yang029.github.io)

- ## Reference link
 
   `This is a link to [my blog][my blog]`  
   `This is another link to [my blog][my blog]`  


  `[my blog]: https://yang029.github.io`

  This is a link to [my blog][Blog]  
  This is another link to [my blog][Blog]  


  [Blog]: https://yang029.github.io   
>**The advantage of the reference link style is that multiple links to the same url only need to be updated once. But we should also remember the link should be sepearted with main pages as paragraphs(i.e. double enter)** 


- ## Pictures 
  `This is my favorite picture ![pic](http://imglf3.nosdn.127.net/img/dWwvOUNMdkJ5c0dOa2FYOVFnUlNGRXRoZFNXUjRkV3k0VURzTzkySDBKc3g2ajZ3RjY0MUF3PT0.jpeg)`


This is my favorite picture ![pic](http://imglf3.nosdn.127.net/img/dWwvOUNMdkJ5c0dOa2FYOVFnUlNGRXRoZFNXUjRkV3k0VURzTzkySDBKc3g2ajZ3RjY0MUF3PT0.jpeg)

- ## Blockquotes
  `>This is blockquotes`  
 This is blockquotes

- ## List and sublist
  
```
* 1.   
* 2.  
  * 2.1 
  * 2.2 
* 3.
```

  * 1.  
  * 2.  
    * 2.1 
    * 2.2
  * 3.

- ## Paragraphs
  - ### soft break (double spaces)  
  - ### hard break (double lines) 

- ## Codeblock
  - ### single line ' '
    `cout << hello world << endl` 
  - ### hard break (double lines)  
    ` ``` ``` `
    ```c++
    #include <iostream>
    using namespace std;
    int main() {
        cout << "Hello World" << endl
        return 0;
    }
    ```
- ## Dividing line
  3 or more consective "*" or "-", like:
  ```
    ***
    -----
    - - -
  ```
  ***
- ## Tables 
  ```
  | number | name | age | major |
  | --| :------| ------:| :----: |
  | 1 | Abbay | 20 | AMATH
  | 0 | Peter | 19 | CSE
  ```
  ### The place of the ":" indicates the position of the data in the column.  
  ### :--- -> left 
  ### ---: -> right  
  ### :---: -> middle
  | number | name | age | major |
  | --| :----| ---------:| :----: |
  | 1 | Abbay | 20 | AMATH
  | 0 | Peter | 19 | CSE

- ## Tasks
  ```
    - [x] review CSE
    - [ ] write essay
  ```
  - [x] review CSE
  - [ ] write essay

- ## Strikethrough
  `this is ~~strickthrough~~`  
  this is ~~strickthrough~~
