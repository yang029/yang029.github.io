---
title: 通过ssh-key 远程登录服务器
date: 2020-12-23 16:22:39
tags:
catagories: tech
---

之前一直都是 `ssh root@ip` 然后输入服务器密码去登录自己的服务器。但服务器密码又臭又长每次都得登录进服务器的管理页面去复制粘贴。于是终于下决心去给服务器整个ssh-key 发现真的是出乎意料的简单。
<!--more -->

## 前置要求

- 电脑开启 open-ssh feature，具体可以看[这里](https://www.vultr.com/docs/how-do-i-generate-ssh-keys/) 

## 生成ssh key pair

1. 使用 `ssh-keygen` 指令进行生成 

   - **-t rsa** 是生成key的类型.
   - 可以使用 **-b 4096** 去生成4096 bit的key (默认是2048，其实足够安全了) 
   - 使用 **-C [comment]** 可以为自己的key添加注释.

   例子：

   ```
    $ ssh-keygen -t rsa -b 4096 -C "Example comment"
   ```

2. 回车后就可以生成一对ssh key 并储存在默认的 **~/.ssh** directory. 
   ```
   Generating public/private rsa key pair.
   Enter file in which to save the key (/home/example_user/.ssh/id_rsa):
   ```

3. 之后会出现输入密码界面。可以直接点回车跳过。如果输入密码的话则以后每次登录都需要输入自己设定好的密码。

   ```
   Enter passphrase (empty for no passphrase):
   Enter same passphrase again:
   ```

4. 最后出现下列图案就说明ssh key pair 已经成功生成啦

   ```
   Your identification has been saved in /home/example_user/.ssh/id_rsa.
   Your public key has been saved in /home/example_user/.ssh/id_rsa.pub.
   The key fingerprint is:
   SHA256:J3gbQu5GcqB8/9UXwhjYGXJrFSrb1jJJTEBwpaqF/p0 Example comment
   The key's randomart image is:
   +---[RSA 4096]----+
   |      .o=o= o.   |
   |       . O *     |
   |    . . + X      |
   | . . = o * *     |
   |  o + O S O + .  |
   |   o O o * + . . |
   |    o + . . . .  |
   |     o o o   .   |
   |      . E        |
   +----[SHA256]-----+
   ```

>  生成的ssh key pair 会有两部分，一部分以.pub 结尾， 是public key，需要将他复制到你要登录的主机/github ssh key 的地方。另一部分是private key 默认路径和名字为 **~/.ssh/id_rsa**。保存在本地，每次登陆的时候会和public key进行验证。

### **一定不要把private key 上传到公共代码库（github）！！**


>  ssh key 在Linux 上的默认存储位置为  **/home/example_user/.ssh/id_rsa.pub**  Windows 上则是**C:\Users\example_user.ssh\id_rsa.pub** on Windows.


## 将ssh key pair 中的public key 上传进服务器

- 一种方法是在建立服务器的时候就设置好ssh key，但对于半路出家的我来说就没法通过网页控制台去后期添加了。

- 后期添加的话简单来说就是把public key 粘贴进root user的 **~/.ssh/authorized_keys**. 具体方法可以
  - cd 进`/.ssh`，`vi authorized_keys`直接粘贴进去
  - Linux 或者 mac 可以 `ssh-copy-id -i ~/.ssh/id_rsa.pub root@ip`
  - Windows 可以使用powershell `PS> type $:USERPROFILE\.ssh\id_rsa.pub | ssh root@ip "cat >> .ssh/authorized_keys"`

**在个人操作的时候发现了一个问题，如果新建服务器时没有选择ssh key login，那么使用`powershell`时候就会报错 `bash: .ssh/authorized_keys: No such file or directory`**  

**原因是`/root` 目录下面就没有`/.ssh` 的文件夹。需要自己`mkdir .ssh` 再重新跑指令就ok了**