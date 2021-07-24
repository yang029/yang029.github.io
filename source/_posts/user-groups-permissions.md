---
title: user/groups/permissions
date: 2021-07-05 17:09:11
tags: chomd
catagories: Linux
---

<!--more -->
* user
  * `whoamI` show current login name
  * `users` show current users
  * `pinky` show the details of all users
  * super user
    * `sudo` super user do 
* groups
  * `groups` display current group user is in
* process
  * `ps` show current processes
  * `ps -u user` show processes that start by specified user
  * `top` show details of all processes
  * `kill pid` kill the processes with specified pid`
> `!!` refers to the last command, such as typing `sudo !!` 

* permissions
  * using `ls -l` to see detailed permissions.
  * the permission will be shown in 10 digits
  > `d rwx rwx rwx`
  > d for is it directory; 
  > 1rd rwx for owner(u)
  > 2nd rwx for group(g)
  > 3nd rwx for others(o)

  * `chmod` command
    * add with "rwx" -- 
      * `chmod u+x test.sh` add owner execute permission
      * `chmod u-x test.sh` remove owner execute permission
      * `chmod ug+x test.sh` add owner & group execute permission
      * `chmod ug+rwx,o+r,o-wx test.sh` 
    * add with number
      * `chomd NNN filename`
        * +4 for read
        * +2 for write
        * +1 for execute 
        * follow (owner group others) pattern

  * `umask` command -> sets the default permissions for newly created files
    * `umask [options] [mask]`
    * remove those permissions for newly created files.
    * `umask 0022`
      * give the owner full privileges and all others read/execute privileges only
      *  leading zero for umask is intended to signify that it is an octal number (base 8)
  * Directory Permissions
    * Read - determines whether or not the user can view the contents of the directory (i.e. can they run ls on that directory)
    * Write - determines whether the the user can add or delete files or directories.
    * Execute - determines whether the user can enter into that directory.

