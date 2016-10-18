# 打造数据科学作品集：搭建一个数据科学博客

title: 打造数据科学作品集：搭建一个数据科学博客
author: Vik Paruchuri
translator: cystone
reviewer: EarlGrey
date: 20161008
permalink: making-data-science-blog
keywords: python, matplotlib, pandas, 数据科学, 数据科学博客, github pages, pelican 教程, 静态网站生成器, 静态网站

***

> 这是「打造数据科学的作品集」系列文章的第二篇。如果你喜欢该系列，而且想知道本系列的下一篇文章什么时候发布，你可以订阅我们。读完本文，你将学会如何使用 Pelican 静态网站生成器，搭建一个属于自己的博客，用来展示数据科学作品。

> 全文大约 9500 字，读完需要 15 分钟左右。 

你可以在这里阅读本系列第一篇文章：[「打造数据科学作品集：用数据讲故事」](http://codingpy.com/article/data-science-portfolio-storytelling-with-data/)

写博客是证明你的实力、深入学习和建立读者群的好方法。有许多[数据科学](https://github.com/rushter/data-science-blogs)和[编程类](https://www.quora.com/What-are-the-best-programming-blogs)博客帮助他们的作者找到工作，或者认识了重要人物。定期写博客是有抱负的程序员和数据科学家最应该做的事情之一。

不幸的是，写博客的一大障碍就是先搭建一个博客网站。在这篇文章中，我们将学习如何用 Python 创建一个博客网站，怎么用 Jupyter Notebook 写文章和如何通过 GitHub Pages 部署博客。读完这篇文章，你就可以使用你熟悉的方式，创建自己的数据科学博客了。

## 静态网站

基本上，一个静态网站就是一个全是 HTML 文件的文件夹。我们可以搭建一个允许别人链接到这个文件夹并获取文件的服务器。这样做的好处是不需要数据库或者其他动态部分，可以很简单的部署在像 GitHub 之类的网站上。把你的博客做成静态网站是一个好主意，因为维护起来十分简单。建立静态网站的一种方法是手写 HTML，然后上传所有的 HTML 文件到服务器。这种情况下，你至少要写一个 `index.html` 文件。如果你的网站的 URL 是 `thebestblog.com`，当访问者浏览 `http://www.thebestblog.com` 时，他们就会看到 `index.html` 的内容了。HTML 的文件夹可能是下边的这个样子：

```
thebestblog.com
│   index.html
│   first-post.html
│   how-to-use-python.html
│   how-to-do-machine-learning.html
│   styles.css
```

在上边的这个网站里，访问 `http://www.thebestblog.com/first-post.html` 你就可以看到` first-post.html` 的内容。`first-post.html` 可能是下边这个样子：

```html
<html>
<head>
  <title>The best blog!</title>
  <meta name="description" content="The best blog!"/>
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <h1>First post!</h1>
  <p>This is the first post in what will soon become (if it already isn't) the best blog.</p>
  <p>Future posts will teach you about data science.</p>

<div class="footer">
  <p>Thanks for visiting!</p>
</div>
</body>
</html>
```

你可能会立马发现手工编辑 HTML 的一些问题：

* 手工编辑 HTML 会很枯燥。
* 如果你想写多篇文章，你需要复制很多内容，比如样式、Title、Footer 等。
* 如果你想整合评论系统或者其他插件，你不得不写 Javascript。

一般来说，你写博客的时候，想关注于博客内容，而不是在 HTML 上浪费时间。谢天谢地，你可以用一个叫做静态网站生成器的工具来取代手动编辑 HTML。

## 静态网站生成器

静态网站生成器可以让你用一些简单的格式写文章，通常是 Markdown，然后再定义一些设置。生成器可以自动把你的文章转换为 HTMl。使用静态网站生成器，你可以把 `first-post.html` 极大地简化为 `first-post.md`：


```md
# First post!

This is the first post in what will soon become (if it already isn't) the best blog.

Future posts will teach you about data science.
```

这比处理 HTML 文件要简单的多！通用的元素，比如 Title 和 Footer，可以放在模板里边，这样很容易更改。

静态网站生成器多种多样。最流行的是用 Ruby 开发的 [Jekyll](https://jekyllrb.com/)。因为我们要搭建一个数据科学博客，所以需要网站生成器可以处理 Jupyter Notebooks。

[Pelican](http://blog.getpelican.com/) 是一个用 Python 开发的网站生成器，可以接受 Jupyter Notebook 文件并转换成 HTML 博客文章。Pelican 也可以很容易的把文章部署到 GitHub Pages 让别人阅读。

## 安装 Pelican

开始之前，[这里](https://github.com/dataquestio/jupyter-blog)有一个仓库(repo)，它就是我们最终成果的示例。

如果你还没有安装 Python，在开始之前你还需要做一些前期工作。[这里](https://www.continuum.io/downloads)有一些安装 Python 的说明。我们建议使用 Python3.5。当你安装完成 Python：

* 创建一个文件夹——我们将把博客网站的内容和样式(Styles)放在这个文件夹里。该教程把这个文件夹叫做 `jupyter-blog`，你可以随便起名字。
* `cd` 进入 `jupyter-blog` 文件夹。
* 创建一个叫 `.gitignore` 的文件，然后把[这个](https://github.com/github/gitignore/blob/master/Python.gitignore)文件里的内容加进去。我们最后将要把仓库提交到 git，而这将会排除一些其他东西。
* 创建并激活一个[虚拟环境](http://docs.python-guide.org/en/latest/dev/virtualenvs/)。
* 在 `jupyter-blog` 文件夹里创建一个叫 `requirements.txt` 的文件，内容如下：
```
Markdown==2.6.6
pelican==3.6.3
jupyter>=1.0
ipython>=4.0
nbconvert>=4.0
beautifulsoup4
ghp-import==0.4.1
matplotlib==1.5.1
```
* 在 `jupyter-blog` 文件夹里运行 `pip install -r requirements.txt` 来安装 `requirements.txt` 里边所有的包。

## 创建数据科学博客

完成了前边的设置之后，你就做完创建博客的准备了！在 `jupyter-blog` 文件夹里运行 `pelican-quickstart` 命令，来为你的博客启动一个交互式安装序列。你将看到一些帮助你设置博客属性的问题。大多数问题你只需要点击 `Enter` 使用默认设置就好了。你需要输入的就是你网站的名字、网站的作者，另外就是当问到 URL prefix(URL 前缀) 和 timezone(时区) 的时候选 `n`。下边是个例子：

```
(jupyter-blog)➜  jupyter-blog ✗ pelican-quickstart
Welcome to pelican-quickstart v3.6.3.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can generate the files
needed by Pelican.


> Where do you want to create your new web site? [.]
> What will be the title of this web site? Vik's Blog
> Who will be the author of this web site? Vik Paruchuri
> What will be the default language of this web site? [en]
> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) n
> Do you want to enable article pagination? (Y/n)
> How many articles per page do you want? [10]
> What is your time zone? [Europe/Paris] America/Los_Angeles
> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n)
> Do you want to upload your website using FTP? (y/N)
> Do you want to upload your website using SSH? (y/N)
> Do you want to upload your website using Dropbox? (y/N)
> Do you want to upload your website using S3? (y/N)
> Do you want to upload your website using Rackspace Cloud Files? (y/N)
> Do you want to upload your website using GitHub Pages? (y/N)
```

运行完 `pelican-quickstart` 以后，`jupyter-blog` 文件夹里多了两个文件夹 `content` 和 `output`，还有一些文件，比如 `pelicanconf.py` 和 `publishconf.py`。下边是文件夹目录的示例：

```
jupyter-blog
│   output
│   content
│   .gitignore
│   develop_server.sh
│   fabfile.py
│   Makefile
│   requirements.txt
│   pelicanconf.py
│   publishconf.py
```

## 安装 Jupyter 插件

Pelican 默认不支持使用 Jupyter 写文章，所以我们需要安装一个[插件](https://github.com/danielfrg/pelican-ipynb)来完成这项功能。我们把插件作为一个 git [子模块(git submodule)](https://git-scm.com/docs/git-submodule)来安装，这样便于管理。如果你还没有安装 git，你可以在[这里](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)找到安装说明。当你安装完成 git 之后：

* 运行 `git init` 来把当前文件夹初始化为一个 git 仓库。
* 创建一个叫 `plugins` 的文件夹。
* 运行 `git submodule add git://github.com/danielfrg/pelican-ipynb.git plugins/ipynb` 来添加插件。

现在应该会有一个 `.gitmodules` 文件和一个 `plugins` 文件夹：

```
jupyter-blog
│   output
│   content
│   plugins
│   .gitignore
│   .gitmodules
│   develop_server.sh
│   fabfile.py
│   Makefile
│   requirements.txt
│   pelicanconf.py
│   publishconf.py
```

为了激活插件，我们需要修改 `pelicanconf.py` 文件，在最下边添加几行代码:

```python
MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']
```

这几行代码告诉 Pelican 当生成 HTML 的时候激活插件。

## 写第一篇文章

插件安装完之后，就可以写你的第一篇文章了：

* 创建一个 Jupyter notebook，简单写一些内容。[这里](https://github.com/dataquestio/jupyter-blog/blob/master/content/first-post.ipynb)有一个例子。
* 把 notebook 文件复制到 `content` 文件夹。
* 创建一个和 `notebook` 同名的文件，但是扩展名是 `.ipynb-meta`。[这里](https://github.com/dataquestio/jupyter-blog/blob/master/content/first-post.ipynb-meta)有一个例子。
* 把下边的内容添加到 `ipynb-meta` 文件中，但是根据你自己的文章修改相应字段：

```
Title: First Post
Slug: first-post
Date: 2016-06-08 20:00
Category: posts
Tags: python firsts
Author: Vik Paruchuri
Summary: My first post, read it to find out.
```

这里以上字段的解释：

* `Title`——文章的标题。
* `Slug`——你的文章在服务器上的路径。如果 slug 是 `first-post`，而且你的服务器地址是 `jupyter-blog.com`, 你可以在 `http://www.jupyter-blog.com/first-post` 这个地址找到你的文章。
* `Date`——文章发布的日期。
* `Category`——文章的类别——可以是任何东西。
* `Tags`——文章的标签。可以随便挂标签。
* `Author`——文章作者的名字。
* `Summary`——文章的摘要。

每发布一篇文章，就需要复制一个 notebook 文件，并创建一个 `ipynb-meta` 文件

创建好 notebook 和 meta 文件后，就可以生成博客 HTML 文件了。下边是 `jupyter-blog` 文件夹现在的样子：

```
jupyter-blog
│   output
│   content
    │   first-post.ipynb
    │   first-post.ipynb-meta
│   plugins
│   .gitignore
│   .gitmodules
│   develop_server.sh
│   fabfile.py
│   Makefile
│   requirements.txt
│   pelicanconf.py
│   publishconf.py
```

## 生成 HTML

为了从文章生成 HTML，我们需要先运行 Pelican 来把 notebooks 转换为 HTML，然后运行本地服务器来查看：

* 切换到 `jupyter-blog` 文件夹。
* 运行` pelican content` 来生成 HTML。
* 切换到 `output` 目录。
* 运行`python -m pelican.server`。
* 在浏览器里访问 `localhost:8000` 来预览你的博客。

在浏览器里就可以看到博客里所有文章的列表，以及具体的博客内容了。

## 创建 GitHub Pages

[GitHub Pages](https://pages.github.com/) 是 GitHub 的一项功能，允许你快速部署静态网站，让所有人都可以通过特定 URL 访问。为了完成它的配置，我们需要：

* [注册](https://github.com/)一个 GitHub 帐号，如果你还没有的话。
* 创建一个叫 `username.github.io` 的仓库，这里 `username` 是你的 GitHub 用户名。[这里](https://help.github.com/articles/create-a-repo/)有更详细的说明告诉你怎么做。
* 切换到 `jupyter-blog` 文件夹。
* 运行 `git remote add origin git@github.com:username/username.github.io.git` 把这个仓库作为远程仓库添加到你的本地仓库，把所有的 `username` 参数替换为你的 GitHub 用户名。

GitHub Pages 会把 `username.github.io` 仓库的 `master` 分支下的所有 HTML 文件展示到 `username.github.io` 这个地址（仓库和 URL 是一样的）。

首先我们需要修改 Pelican 使得 URL 指向正确的位置：

* 在 `publishconf.py` 文件里编辑 `SITEURL`，把它设置为 `http://username.github.io` ，`username` 还是你的GitHub用户名。
* 运行 `pelican content -s publishconf.py`。当你想在本地预览你的博客的时候，运行 `pelican content`。在部署之前运行 `pelican content -s publishconf.py`。这将使用正确的配置文件进行部署。

## 提交文件

如果你想把 notebooks 和其他文件作为一个 GitHub Page 放在同一个仓库里，你可以使用分支。

* 运行 `git checkout dev` 切换到一个叫 `dev` 的分支。我们不能用 `master` 分支来存放 notebooks，因为那个分支是用于 GitHub Pages 展示的。
* 创建一个提交，然后和正常一样推送到 Github（使用 `git add`, `git commit`，和 `git push`）。

## 部署到 GitHub Pages

为了让 Github Pages 正常工作，我们需要把文章添加到 `master` 分支中。现在，`HTML` 内容在 `output` 文件夹中，但是我们需要把它放到仓库的根目录，而不是子目录。我们可以使用 `ghp-import` 工具来完成这项工作：

* 运行 `ghp-import output -b master`，把 `output` 目录下的所有东西导入 `master` 分支。
* 使用 `git push origin master` 把你的内容推送到 GitHub。
* 尝试访问 `username.github.io` ——你就可以看到你的页面了！

修改博客后，只要重新运行 `pelican content -s publishconf.py`, `ghp-import` 和 `git push`，你的 GitHub Page 就会更新了。

## 下一步

终于搭建好了！你现在可以创作博客，然后推送到 GitHub Pages。所有人都可以通过 `username.github.io` 来访问你的博客（记得把 username 替换为你的 GitHub 用户名）。这给你提供了一个展示数据科学作品集的渠道。

随着文章数和读者越来越多，你可能就需要在以下方面更深入的研究一下：

* 主题：Pelican 支持主题。在[这里](https://github.com/getpelican/pelican-themes)你可以看到很多主题，随便选一个你喜欢的用吧。
* 自定义URL：使用 `username.github.io` 已经不错了，但是有时候你可能需要自定义域名。[这里](https://help.github.com/articles/using-a-custom-domain-with-github-pages/)是自定义 GitHub Pages 域名的指南。
* 插件：[这里](https://github.com/getpelican/pelican-plugins)有一个插件列表。插件可以帮助你设置网站数据分析，实现评论等功能。
* 推广：试着把你的文章推广到 [DataTau](http://www.datatau.com/), [Twitter](http://www.twitter.com/), [Quora](http://www.quora.com/)或者其他一些网站，可以帮助你获得更多的读者。

