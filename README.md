# 练习 markdown 语法书写 github 中的 md 文件


## 文本样式


**加粗**

_斜体_

~~删除~~

这是 <sub> 下标 </sub>

这是 <sup> 上标 </sup>


## 引用文本



> 在这里引用文本
>
> > 嵌套引用

## 引用代码



Use `git status` to list all new or modified files that haven't yet been committed.

Some basic Git commands are:

```
git status
git add
git commit
```

## 引用链接



我最喜欢的网站[哔哩哔哩](https://www.bilibili.com/)

<https://www.bilibili.com/>

这是一个链接 [Markdown 语法](https://markdown.com.cn)

[github 文档](https://docs.github.com/zh)

## 相对链接



[py 链接](hello_py/hello_world.py)

## 图像插入



![这是图片](/saibopengke.avif "赛博朋克")

## 列表



- George Washington

* John Adams

- Thomas Jefferson

## 列表排序



1. 动漫
2. 轻小说
3. 漫画

## 嵌套列表



1. First list item
   - First nested list item
     - Second nested list item

## 表情



[参考链接](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md)
:rofl:
:sweat_smile:

## 脚注



Here is a simple footnote[^1].

A footnote can also have multiple lines[^2].

[^1]: My reference.
[^2]:
    To add line breaks within a footnote, prefix new lines with 2 spaces.
    This is a second line.

## 忽略 markdown 格式



在 markdown 字符前加入 `\` ,可以指示忽略 markdown 格式

`Let's rename \*our-new-project\* to \*our-old-project\*.`

Let's rename \*our-new-project\* to \*our-old-project\*.


## 创建mermaid关系图


```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

## 编写数学表达式


This sentence uses `$` delimiters to show math inline:  $\sqrt{3x-1}+(1+x)^2$




# 练习 vscode 和 github 的链接

## 使用git

在`git`中设置用户名和email
```
$ git config --global user.name 
$ git config --global user.email 
```

`git`的三种状态
1. 更改
2. 暂存
3. 提交
>先提交到本地仓库，再推送到远程仓库

克隆别人的库
```
git clone (https)
```

## github 的拉取推送
```
1. fork 一份到直接本地的仓库
2. 进行bug的修改
3. 提交一份PR(pull requests)
4. 等待审核
```

## 拉取操作
Git分支拉取指的是从远程仓库（Remote Repository）中将特定分支的代码复制到本地仓库（Local Repository）中的操作。

将远程仓库中指定分支的代码复制到本地仓库中的操作，通过该操作可以实现团队成员之间的代码同步和协作开发。

```
git fetch
```

# 练习python语言的基本语法