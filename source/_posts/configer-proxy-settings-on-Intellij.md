---
title: configure proxy settings in IntelliJ
date: 2020-08-09 09:58:19
categories: Tech
tags: IntelliJ
---

最近回国了虽然感觉很棒，但网络问题一直是最头疼的问题，虽然已经提前配置好了ssr，但IntelliJ这个软件比较倔强，流量坚决不走代理，导致build gradle巨卡还经常失败。

后来看网上的教程修改maven仓库到国内镜像，效果也不是很好，一个是国内镜像很多资源更新不及时或者干脆没有，再一个就是每一次都要改本地的gradle有点麻烦

我当时有些心急，于是直接冲到gradle里面写的地址，把需要的东西统统下载下来放到 `...\.gradle\wrapper\dists`,虽然很蠢但也work了。

之后学到了更好的方法就是直接设置intelliJ的HTTP代理，亲测速度极快(主要看自己配置的SSR 速度)

<!--more -->

具体设置在`File -> Settings -> Appearance & Behavior -> System Settings -> HTTP Proxy`

![](../../../../assets/pic/6_1.png)

**切记一定要选HTTP Proxy， port则和SSR下面Proxy Port的设置一样**

![](../../../../assets/pic/6_2.png)

> 个人猜测相当于IntelliJ 把所有流量转发到 local host（127.0.0.1） 然后再由 SSR 代理

Reference
>   https://github.com/shadowsocks/shadowsocks-iOS/issues/246


