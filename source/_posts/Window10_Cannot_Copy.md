---
title: 关于windows crtl+C 失灵
date: 2020-08-08 07:25:00
categories: Tech
---

最近几天电脑时常发生crtl c crtl v失灵的现象， 之前基本上都是莫名奇妙过一段时间就好了，就没有多管。

然而今天用Adobe Acrobat Reader 完成老师布置的reading的时候突然就出现了大bug - 居然咋都不能复制了

![](../../../../assets/pic/post5_1.jpg)

<!--more -->

哇我这个reading讲哲学不能复制查单词简直要我小命..

当时没多想以为是Acrobat Reader的问题， 于是凡事不决问Google， 结果网上一查吓到了，这个问题五年前就有人问，adobe community上全都是这问题的吐槽，仔细读了十几篇把所有的解决方法都试了一遍，包括并不限于关闭安全模式，修复安装，以及终极大杀器重装，然而还是没有work..

后来放弃希望用chrome打开pdf，发现还是不能crtl c，于是用中文怒搜一波，第一个csdn的答案就解决了问题
![](../../../../assets/pic/post5_2.png)

2333看来中国软件的bug还得中文搜索来解决, 也是逐渐理解为什么这个bug五六年了adobe还是没法解决，毕竟出现这种情况的原因实在太多了

其实想想刚开始解决Acrobat Reader的问题就有人提出问题的根源是在剪贴板被劫持，如果顺着这个思路下去就能直接定位问题..可惜我当时就略过去直接莽了..果然还是 **要多想** 啊

 reference:
>   https://blog.csdn.net/microcosmv/article/details/103264658
>   https://community.adobe.com/t5/acrobat-reader/there-was-an-error-while-copying-to-the-clipboard-an-internal-error-occurred/td-p/3878922