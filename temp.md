# Hexos 架构理解

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
