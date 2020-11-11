---
title: 搭建一台属于自己的SSR！！（无脚本）
date: 2020-11-10 15:32:31
tags:
catagories: tech
---

今天终于解决了ssr卡的飞起的难题，掐指一算我好像少说也在超过10台的服务器上搞过ssr了，从一开始的手足无措面向Google编程到现在三分钟就可以搭好连接成功，想想也是辛酸呢。若不是网课要回国，孩子为啥要承受这么多的痛苦啊qwq..

<!--more -->

## 前置准备
- 一台Linux服务器
    > ssr的原理其实就是流量的代理和转发，把你向国内无法访问的网址（比如 `google.com`）发送的请求发给你租下的服务器，再由服务器代由发送请求，最后再让服务器把收到的请求转发回本地，就优雅的完成了翻墙。
    
    {% asset_img ssr.png %}

    服务器的选择主要有以下几个因素
    - 供应商   
        服务器速度的关键，尽量选大家试的比较多比较可靠的，比如搬瓦工、vultr等。我当下租用了vultr的服务器，比较好的一个地方是它是按分钟计费，所以当服务器也被墙时可以随时更换。单个服务月流量是1000GB,足够满足使用需求。
    - 服务器类型
        服务器的价格因内存大小, CPU种类, 存储空间等多个因素决定。因为SSR实际上并不怎么吃CPU和内存，所以这方面可以无脑选最低配。
    -  服务器系统  
        系统的话CentOS和Ubuntu二选一，网络上都有很全面的对两个系统的支持，值得注意的是要慎重选择系统的最新版本（可能某些应用不支持）
    - 服务器地区    
        地区的话也是选择的关键之一，尽管网速基本可以达到光速，但地球还是很大的，底去导致的延迟与丢包也会相当恼人。推荐选择诸如日本、新加坡、韩国等地的服务器，血泪教训啊www

        {% asset_img speed_Seattle.png %}

        {% asset_img speed_Germany.png %}

        {% asset_img speed_now.png %}

    西雅图/法兰克福/首尔速度对比（主要看ping）


**安排好一切后点击deploy就可以有自己的服务器啦**

## 安装并运行SSR 

> SSR是开源在Github上的开源软件，尽管好像已经有一段时间未更新了但依然可用。（很多人推荐V2ray也可以尝试）

- 安装必备的软件（CentOS 使用 yum Ubuntu 则为 apt-get)
    ```bash
        yum install git 
        yum install screen 
        yum install python
    ```
- 下载ssr源码  
    `gitclone -b manyuser https://github.com/shadowsocksrr/shadowsocksr.git`   
    执行完毕后此目录会新建一个shadowsocksrr目录，其中根目录的是多用户版（即数据库版，个人用户请忽略这个），子目录中的是单用户版(即shadowsocksrr/shadowsocks)。
- 快速运行
    ```
    cd ~/shadowsocksr/shadowsocks
    python server.py -p 443 -k password -m aes-256-cfb -O auth_sha1_v4 -o http_simple
    #说明：-p 端口 -k 密码  -m 加密方式 -O 协议插件 -o 混淆插件
    ```

    如果要后台运行：

    ```
    python server.py -p 443 -k password -m aes-256-cfb -O auth_sha1_v4 -o http_simple -d start
    ```
    如果要停止/重启：

    ```
    python server.py -d stop/restart
    ```

    查看日志：

    ```
    tail -f /var/log/shadowsocksr.log
    ```

## SSR 客户端下载

**windows端：** [下载地址](https://netfiles.pw/download.php?filename=/ssr/windows/ShadowsocksR-win-4.9.2-tlanyan.zip)  

**Android端：** [下载地址](https://github.com/shadowsocksrr/shadowsocksr-android/releases)


## 关键加速
现在打开客户端，按照服务器的配置填入对应IP、密码和加密方式等信息就可以越过高墙啦~ 但说实话网速的确时有波动，常年可能只有100k/s左右，这时候就需要一些小小的黑科技，让网速直接拉满 —— BBR 加速

{% asset_img speed_before.jpg %}

{% asset_img speed_now.png %}

开启前 vs. 开启后
### BBR介绍

Google BBR (Bottleneck Bandwidth and RTT) 是一种新的TCP拥塞控制算法,它可以高效增加吞吐和降低网络延迟，并且Linux Kernel4.9+已经集成该算法。开启BBR也非常简单，因为它只需要在发送端开启，网络其他节点和接收端不需要任何改变。具体介绍可以点击[这里](https://blog.csdn.net/dog250/article/details/52830576)。 接下来讲讲具体操作：

### 升级内核

1. 打开Terminal

输入

```bash
  uname -r
```

查看内核版本，如果输出类似

> 3.10.0-514.21.2.el7.x86_64

则表示小于4.9，需要升级内核，
 而如果内核大于等于4.9则跳过至开启Google BBR

2. 升级内核

- 安装 ELRepo 仓库

  

  ```bash
  rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
  rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-2.el7.elrepo.noarch.rpm
  ```

- 安装最新版kernel

  ```bash
  yum --enablerepo=elrepo-kernel install kernel-ml -y
  ```

- 确认是否安装成功

  ```bash
  rpm -qa | grep kernel
  ```

  如果输出类似如下，包含kernel-ml-4.13.10-1.el7.elrepo.x86_64，则表示安装成功

  >  kernel-3.10.0-693.el7.x86_64  
  >  kernel-tools-3.10.0-693.el7.x86_64  
  >  kernel-ml-4.13.10-1.el7.elrepo.x86_64  
  >  kernel-tools-libs-3.10.0-693.el7.x86_64  

- 设置开机默认启动项

  ```bash
  egrep ^menuentry /etc/grub2.cfg | cut -f 2 -d \'
  ```

  输出结果类似如下

  > CentOS Linux 7 Rescue f212d2d7754a4a6bb2b98950c20cc0b5 (4.13.10-1.el7.elrepo.x86_64)  
  >  CentOS Linux (4.13.10-1.el7.elrepo.x86_64) 7 (Core)  
  >  CentOS Linux (3.10.0-693.el7.x86_64) 7 (Core)  
  >  CentOS Linux (0-rescue-d1f142097d497f24c021d7de9b81cab4) 7 (Core)

  该列表从0开始索引，所以4.13内核索引为1

- 设置启动项

  ```bash
  grub2-set-default 1
  ```

- 重启

  ```bash
  reboot
  ```

  查看内核版本

  ```bash
  uname -r
  ```

  如果输出类似

  > 4.13.10-1.el7.elrepo.x86_64

  则表示升级完成

### 开启Google BBR

- 修改sysctl配置

  ```bash
  echo 'net.core.default_qdisc=fq' | tee -a /etc/sysctl.conf
  echo 'net.ipv4.tcp_congestion_control=bbr' |  tee -a /etc/sysctl.conf
  sysctl -p
  ```

- 检查是否加载BBR

  ```bash
  lsmod | grep bbr
  ```

  如果输出结果包含tcp_bbr，则表示开启成功

  > tcp_bbr                20480  1

> 也可直接用 `sysctl net.ipv4.tcp_congestion_control`查看 

**感谢那些在我迷茫时给我指引的博客和文章！！**
> https://blog.csdn.net/dog250/article/details/52830576
> https://www.jianshu.com/p/52815c34215e
> https://github.com/shadowsocksrr/shadowsocks-rss/wiki/Server-Setup
> https://tlanyan.me/