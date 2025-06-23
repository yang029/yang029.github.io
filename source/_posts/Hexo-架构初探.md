---
title: Hexo 架构初探
date: 2025-06-21 20:07:44
tags:
categories: Tech
---

</br>
<!--more -->

## themes

### _config.yml

- _config.yml 是主题的配置文件，包含了主题的基本设置和选项。其中定义的变量可以在主题的`.ejs`文件中访问

### .ejs 文件

- `.ejs` 文件是 Hexos 主题的模板文件，使用 EJS 模板引擎来渲染 HTML 内容。
- 一些见到的基础语法
  - `<%- %>`：输出未转义的html内容 (即各种tag会起作用)
  - `<%= %>`：输出转义的html内容 (所有的tag都被转义成文本)
  - `<% %>`：执行 JavaScript 代码
  - `<%- partial/<other ejs file> %>`：引入其他模板文件
  - `<%- config.title %>`：访问配置文件中的变量

- 传递变量
  - 在引用其他`.ejs`文件时，可以通过传递变量来动态生成内容。例如：

    ```ejs
    <%- partial('header', { title: 'My Title' }) %>
    ```

### partial

- `partial` 是 EJS 模板引擎中的一个函数，用于引入其他模板文件。
- 如上所示 `partial` 可以在引入其他模板时传递变量。

### Pagination

- 分页是 Hexos 主题中的一个重要功能，通常在文章列表页使用。
- 当调用 `page.posts.each` 时， hexos 会自动处理分页逻辑。
- 分页的配置通常在主题的 `_config.yml` 文件中设置，例如：

  ```yaml
  pagination:
    per_page: 10
  ```

## Comments

### Valine

- 可以使用 [Valine](https://valine.js.org/) 作为评论系统。它是无后端的评论系统，可以无缝和leancloud集成。

具体使用流程

1. 在 [LeanCloud](https://leancloud.cn/) 创建一个免费账号
2. 创建一个新的应用。因为我在国外，所以创建的国际版应用。
3. 在theme的 `_config.yml` 中配置 Valine：

   ```yaml
   valine:
     enable: true
     app_id: 'your_app_id'
     app_key: 'your_app_key'
     serverURLs: { rest_api_url }
   ```
   > 一个大坑就是我们需要去专门设置`serverURLs`, 默认的comment网址会一直`ERROR_TIMEOUT`. `serverURLs` 可以在 LeanCloud 的应用设置中找到。叫`REST API Server URL`。同时我是用的`landscape`的主题在`.ejs`文件中没有set这个field，也需要手动改动并添加。