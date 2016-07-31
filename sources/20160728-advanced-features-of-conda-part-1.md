# 学习 Conda 的高级特性：上

title: 学习 Conda 的高级特性：上
author: Aaron Meurer
translator: cystone
reviewer: EarlGrey
date: 20160728
permalink: advanced-features-of-conda-part-1
keywords: conda， anaconda，包管理，科学计算

***

Conda 是 Continuum 公司发布的 Anaconda 里边配备的一个包管理器。Conda 让你更加方便地安装和管理各种扩展包和运行环境，同时支持 Windows，Mac OS X 以及 Linux。

如果你是一个 Conda 的新手，我建议你先学习它的[官方文档](http://conda.pydata.org/docs/)，还有我在 SciPy 2014 上的[演讲](https://www.youtube.com/watch?v=UaIvrDWrIWM&feature=youtu.be)。

在这篇文章里，我就假设你已经熟悉了Conda 以及它安装和编译包的基本用法。我将为你们展示一些甚至对于 Conda 的高级用户也鲜有人知的高级特性。这些特性将帮助你挖掘新特性、定制新用法，同时也能让你以更高级的方式管理扩展包和运行环境。

## --help

学习 Conda 特性最好的方法是在子命令的后边加一个 **`--help`** 选项。例如：查看 install 命令的所有功能， 我们可以运行：

```
$conda install --help
usage: conda install [-h] [--revision REVISION] [--yes] [--dry-run] [-f]
                     [--file FILE] [--unknown] [--no-deps] [-m]
                     [--use-index-cache] [--use-local] [--no-pin] [-c CHANNEL]
                     [--override-channels] [-n NAME | -p PATH] [-q]
                     [--alt-hint]
                     [package_spec [package_spec ...]]
...
...

positional arguments:
  package_spec          package versions to install into conda environment

optional arguments:
  -h, --help            show this help message and exit
  --revision REVISION   revert to the specified REVISION
  --yes                 do not ask for confirmation
  --dry-run             only display what would have been done
  -f, --force           force install (even when package already installed),
                        implies --no-deps
  --file FILE           read package versions from FILE
  --unknown             use index metadata from the local package cache (which
                        are from unknown channels)
  --no-deps             do not install dependencies
  -m, --mkdir           create prefix directory if necessary
  --use-index-cache     use cache of channel index files
  --use-local           use locally built packages
  --no-pin              don't use pinned packages
...
...

examples:
    conda install -n myenv scipy
```

查看所有**`conda`**的命令，可以运行**`conda --help`** 。

## 配置

Conda支持多种配置选项。修改这些选项最简单的方法就是使用**`conda config`**命令。这个命令会修改你的**`.condarc`**文件，这个文件默认在你的用户目录下。**`.condarc`**遵循 [YAML](https://en.wikipedia.org/wiki/YAML) 语法。

Conda 提供了一些很有用的配置。最常用的配置选项是**`channels`**，它可以让人们从 [Anaconda.org](https://anaconda.org/) 安装其他人的扩展包，当然还有一些有用的配置，比如，允许当你创建一个新环境时改变 Conda 的行为，或者它在命令行的交互。

在 Conda 的配置里边有两种键：List 键和 Boolean 键。

List 键的值是一个列表。例如，**`channels`**是 Conda 搜索扩展包时使用的一个频道列表。向 list 键里边添加内容的方法是 **`conda config --add`**。**`conda config --add channels asmeurer`**将添加我的 Binstar 频道（译者注：“asmeurer” 是 Binstar 上的用户名）。还有一些其他有用的 list 键：

**`channels`**：Conda 搜索扩展包的频道列表。**`defaults`**是 Conda 自带的、指向 Continuum 频道的一个特殊频道。频道可以是一个 url，或者是 Binstar 用户名。

**`create_default_packages`**: 新环境中默认包含的一个扩展包列表。

**`envs_dirs`**: 一个 Conda 用来创建环境和缓存扩展包的默认目录。

Boolean键只包含两个值：true 和 false。YAML 允许 true 和 false 有多种拼写方法。**`yes`**、**`YES`**、**`on`**、**`true`**、**`True` 和 **`TRUE`**，都是 “true” 合法的拼写方法，**`no`**、**`NO`**、**`off`**、**`false`**、**`False`**，都是 “false” 合法的拼写方法。

Boolean 键的设置通过**`conda config –set`**进行。一些有用的 Boolean 键：

**`always_yes`**: 阻止弹出 [Y/n] 的确认对话框。如果开启了这个设置，你可以向 **`conda install`** 和 **`conda clean`**之类的命令传递 **`–dry-run`** 选项，查看它们要做而没有做的事情。

**`binstar_upload`**: 如果把这个键设为 true，Conda 会把每次编译成功的文件上传到 Binstar。

**`changeps1`**: 如果把这个键设为 true（默认值），**`activate`**脚本会把环境的名字即时加入命令提示符中。如果你不喜欢这样，或者希望使用**`CONDA_DEFAULT_ENV`**环境变量手动完成，你可以把这项设为 false。

还有一些其他的配置选项，其中有一些现在还不能使用 **`conda config`** 设置。完整的配置选项列表请参看[Conda 配置文档](http://conda.pydata.org/docs/config.html)。

## conda update –all

Conda 通过使用 SAT 求解器加上一个伪布尔约束，来解决包之间的依赖关系。当 Conda 安装扩展包时，它会尝试查找和这个包结合在一起能够使用的那些包的最新版本。

更新全部包，就是尝试安装每个包，让 SAT 求解器找到最新可用的版本。**`conda update –all`** 可以很容易的实现这一功能。例如，如果你现在安装了 Python 2.7.4, Nunpy 1.8.0, 和 SciPy 0.14.0, **`conda update –all`** 就和 **`conda install “python>=2.7.4, <3” “numpy>=1.8.0” “scipy>=0.14.0”`** 的功能一样（除此之外还包括一些Python的依赖关系，比如 readline 和 OpenSSL）。值得注意的是 **`conda update –all`** 不会把 Python 2 升级到 Python 3 。

有时候你的环境可能存在不一致的情况，这时候 Conda 就不能解决包的规格问题。发生这种情况的时候，它会提示你 “Unsatisfiable package specifications” 错误，而且会生成一个线索。你可以按下 Control-C 取消线索的生成，也可以等待它完成（生成的过程可能有点慢，特别是使用 **`conda update –all`** 的时候）。有一个比较常见的问题是，如果你想把某一个包升级到比 **`anaconda`** 元包指定的版本，你可以通过 **`conda remove anaconda`** 来移除它。（这会移除元包，里面不包含任何代码。）

**`anaconda`** 元包是针对想使用稳定版扩展包的人而设计的，它里边的的包都是经过测试的，每几个月会更新一次。如果你想使用这个，你就不要卸载 **`anaconda`** 同时使用 **`conda update anaconda`** 来更新。如果你想将每个包都更新为最新版本，你可以 **`conda remove anaconda`**，然后使用 **`conda update –all`** 来获取更新。

## conda list –export 和 conda create –file

使用 conda 可以很简单地复制环境。 **`conda list --export`** 可以导出所有你已经安装好的包，包括版本和编译字符。你可以把这些保存在文件里，同时使用 **`conda install --file`** 或者 **`conda create --file`** 来安装同样的包。例如：

```
$ conda list --export
# This file may be used to create an environment using:
# $ conda create --name  --file 
# platform: osx-64
openssl=1.0.1h=0
python=3.4.1=0
readline=6.2=2
sqlite=3.8.4.1=0
sympy=0.7.5=py34_0
tk=8.5.15=0
zlib=1.2.7=1

$ conda list --export > exported_packages.txt
$ conda create -n newenv --file exported_packages.txt
Fetching package metadata: .............
Solving package specifications:
Package plan for installation in environment /Users/aaronmeurer/anaconda/envs/newenv:

The following NEW packages will be INSTALLED:

    openssl:  1.0.1h-0     defaults
    python:   3.4.1-0      defaults
    readline: 6.2-2        defaults
    sqlite:   3.8.4.1-0    asmeurer
    sympy:    0.7.5-py34_0 asmeurer
    tk:       8.5.15-0     defaults
    zlib:     1.2.7-1      defaults

Linking packages ...
[      COMPLETE      ] |#######################################################| 100%
#
# To activate this environment, use:
# $ source activate newenv
#
# To deactivate this environment, use:
# $ source deactivate
#

```

## conda clean

使用一段时间之后， Conda 会占用很多硬盘空间，这是因为它不会自动删除一些没用的包。

你可以通过 **`conda clean -p`** 来删除这些没用的包。这个命令会检查哪些包没有在包缓存中被硬链接到其他任何地方，并删除它们。注意，如果你是通过 symlink 等方式或通过一个单独的文件系统安装的包，你就没有办法使用这个命令删除它们，因为它检测不到它们的存在。

Conda 也会保存所有下载下来的 tar 包。它们只是为了缓存才保存下来的，是可以被删除的。你可以通过 **`conda clean -t`**删除它们。

## 钉包（Pinning Packages）

默认情况下，Conda 会在环境中安装一个包的最新版本。但是，有时候你可能会想保留某一个旧版本的包，哪怕你之后安装的包要依赖这个包的新版本（Conda 默认会升级你已经安装的包的依赖包）。

例如，假设你在你的环境里已经安装了 SciPy 0.13.3， 但是你现在还不想升级到 0.14.0（文章发表时的最新版本），虽然你安装了其他依赖于 SciPy 的包，比如 Pandas。

为了达到目的，可以在你的环境中的 **`conda-meta`** 目录下创建一个叫 **`pinned`** 的文件。例如，如果你有一个叫做 **`scipy-0.13`** 的环境，你可以这么写：

```
$ echo "scipy 0.13.3" > ~/anaconda/envs/scipy-0.13/conda-meta/pinned
```

pinned 文件中的每一行都应符合 [conda 匹配规则](http://conda.pydata.org/docs/spec.html#package-match-specifications)。这就允许一些通用的事情，比如说指定 **`scipy<0.14`**。其中以‘#’号开头的行会被忽略。

它的工作原理是，每次 conda 在你的环境里安装扩展包时，conda 会把 pinned 文件里的每一行内容都附带发送给 SAT 求解器，这样就阻止了那些你不想要的升级。

忽视 pinned 文件，可以使用**`conda install --no-pin`** 。

## 结语

这是 Conda 高级特性系列博客的第一部分。在第二部分里，大家将会看到更多的高级特性，包括一些使用 conda 更便捷地编译扩展包和使用 conda 管理环境的技巧。

***

[点此查看原文链接](https://www.continuum.io/blog/developer/advanced-features-conda-part-1)。

[Python 翻译组](https://github.com/PythonTG)是EarlGrey@编程派发起成立的一个专注于 Python 技术内容翻译的小组，目前已有近 30 名 Python 技术爱好者加入。

翻译组出品的内容（包括教程、文档、书籍、视频）将在编程派微信公众号首发，欢迎各位 Python 爱好者推荐相关线索。推荐线索，可直接在编程派微信公众号推文下留言即可。
