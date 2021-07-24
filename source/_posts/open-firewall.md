---
title: Linux centOS 开启防火墙方法
date: 2020-10-28 17:11:31
tags: Tech
---
<!--more -->
前两天我部署在vultr上面的服务器突然挂掉了，能用ssh连接但是ping不通，手机和电脑上ssr也全都连接不上，显示为 `www.***.com 没有返回任何数据`， 第一时间猜测是ip被墙了，所以当天就删去server重新建立了一个，但奇怪的就是新建的还是一样的问题，即使在vultr上面修改inbound rules打开了给 https 的 443 端口和 http 的 80 端口还是无济于事。

{% asset_img inbound_rules.png inbound_rules%}

后来和国外的同学联系后发现国外也连接不上ssr，那么应该不是GFW的问题。（感谢wgh百忙之中的技术援助hhh）再加上一直ping不通服务器的ip，猜测可能还要手动打开服务器的端口。

对centOS 7的主要指令如下
``` bash
#查询开启的端口
firewall-cmd --list-port 

#添加80端口
firewall-cmd --zone=public --add-port=80/tcp --permanent 

--zone #作用域
--add-port=80/tcp #添加端口，格式为：端口/通讯协议
--permanent #永久生效，没有此参数重启后失效

#查询80端口 是否开启：
firewall-cmd --query-port=80/tcp

#重启防火墙
firewall-cmd --reload

```

调整完设置之后就一切恢复正常啦~