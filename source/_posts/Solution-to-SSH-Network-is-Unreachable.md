---
title: Solution_to_SSH_Network_is_Unreachable
categories: Tech
date: 2020-08-09 16:22:22
---


最近Gitlab一直暴雷，不是没法push就是没法pull,错误日志也是出了奇的一样 
```
ssh: connect to host cs.washington.edu port 22: Network is unreachable
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

<!--more -->

> 2020.8.5

神奇的是这个错误还是间断性的发生，感觉可能是SSR代理的问题，因为前几天没有连接SSR的时候都可以正常访问，然后连接的时候就不行了。以后用gitlab还得先断SSR..太麻烦了吧..


>2020.8.7

结果昨天是彻底不行了，断了SSR睡了一觉起来还是这bug，代码都写好了没法push提交，当场心态大崩。但这个问题也极其不好定位，网上关于这个错误的帖子虽多，但大部分都是发生在与vps的连接途中，基本上都是防火墙设置导致的。而我专门为Windows添加了相关出站入站规则也依然没有任何作用。ddl当前，我最后强行在repository界面把代码粘贴了上去，太丢脸了/捂脸

>2020.8.9

之后我又尝试了ping cs.washington.edu，发现居然可以ping 通！！但是当我打开Telnet去ping 上述问题描述的专用于SSH的22端口时，却又连接失败了。最后问题还是落在了端口上

后来经过不懈尝试，又发现如果先把电脑断网，再连上新的网络的短暂时间内push和clone，就可以成功。初步推测是GFW会检测和封锁22端口的流量，导致连接失败。但目前还没有任何证实，解决办法也极其简陋。后续会尝试通过端口转发让22端口也走SSR这样就能够彻底解决问题了..期待后续更新~