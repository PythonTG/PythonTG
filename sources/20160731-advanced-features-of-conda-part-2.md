## Conda的高级特性（下）

title: Conda的高级特性--第二部分
author: Aaron Meurer
translator: strugglingyouth
reviewer: EarlGrey
date: 20170731
permalink: advanced-features-of-conda-part-2
keywords: conda， anaconda，包管理，科学计算, conda build, conda skeleton, conda convert

***

在[上篇]()中，我们学习了 **`--help`**、配置、**`conda update --all`、`conda list --export`** 和 **`conda create --file`、`conda clean`** 和钉包（pinning package）。在本文中，我们将介绍一些能够简化包构建过程的工具，学习更多有助于管理环境和在命令行下更有效使用 `conda` 的特性。

## conda skeleton

将现有的包构建成 conda 感觉上会有很多重复工作，因为它要求重写包的所有元数据，但这些数据之前就已经写过了。对于已经发布在 [PyPI](https://pypi.python.org/pypi) 上的 Python 包尤其如此。


**`conda skeleton`** 命令将生成一个骨架（skeleton）配方，然后你可以将其编辑完整。通常自动生成的文件就足够好了，没必要进行额外修改。


**`conda skeleton pypi <packagename>`** 将在当前目录下为 `<packagename>` 创建一个配方。例如，`conda skeleton pypi pyinstrument` 将为 [pyinstrument](https://pypi.python.org/pypi/pyinstrument) 包创建一个骨架。


**`--recursive`** 选项将在当前目录中为依赖包递归创建配方。当运行 `conda build` 时，若配方中缺少依赖，它会在当前目录下查找其对应的配方，并会自动递归地其创建依赖。

**`conda skeleton`** 也支持构建来自 [CPAN](http://www.cpan.org/) 的 Perl 包，使用 **`conda skeleton cpan <packagename>`** 即可。例如，**`conda skeleton cpan Math::Prime::Util`** 将为 [Math::Prime::Util](http://search.cpan.org/~danaj/Math-Prime-Util-0.42/lib/Math/Prime/Util.pm) 生成一个骨架配方。

由 skeleton 命令生成的 **`meta.yaml`** 有几个注释，方便你扩展或修正生成的配方。

以后，skeleton 命令可能会增加从除了 PyPI 和 CPAN 之外的其他源中生成骨架配方的功能。

## conda convert

在系统级包管理器中 Conda 是特殊的，因为它能够跨平台：它在 Windows，Mac OS X 和 Linux 上的工作方式完全相同。然而，尽管命令在所有平台上都以相同的方式工作，但每个系统都需要完全不同的包。对于大多数软件包，这是必要的：一个 Python 二进制包如果运行在 Linux 上则不一定能运行在 Windows 上。但对于只有 Python 代码的包，同一个编译包理论上在所有的系统上都能工作。这并不完全正确，这是因为一些细微的差别，例如，在 Windows 上 Python 包的目录结构是不同于 Unix 系统的。但转换起来很简单，它可以自动完成。

`conda convert` 命令将一个平台上构建的纯 Python 包转换为可以在其他平台上工作。使用方式如下所示：

```
$ conda convert sympy-0.7.5-py34_0.tar.bz2 --platform win-32 --platform win-64
```

这会创建 **`win-32`** 和 **`win-64`** 两个子目录并将转换后的包放在里面。子目录的创建是由于包在所有平台上应该使用相同的文件名。


你也可以使用 **`--platform all`** 来生成 conda 所支持五大平台的包：**`win-64`、`win-32`、`osx-64`、`linux-64`** 和 **`linux-32`**。**`-o `** 选项用来改变输出的目录。

**`conda convert`** 命令目前只支持将 conda 包从一个平台转换到另一个平台，但它会不断增加将其他种类的包转换为 conda 包的方法。目前，**`conda convert`** 也能将 [Christoph Gohlke](http://www.lfd.uci.edu/~gohlke/pythonlibs/) 上的 .exe 安装程序转换成 conda 包。要做到这一点，运行:

```
$ conda convert sympy-0.7.5.win32-py3.3.exe
```

## conda 元包

元包是不包含任何文件，只有元数据的包。如果你需要一个抽象的包，其依赖关系是将要实际安装的包，或者本身将是其他包的抽象依赖，那么元包就非常有用。例如，在 Anaconda 中，**`ipython-notebook`** 就是一个元包。包本身不包含任何文件，但它有安装 notebook 所需的所有依赖，比如 **`ipython`、`pyzmq`、`tornado`**和 **`jinja2`**。

元包可以通过在 **`meta.yaml`** 中创建一个包含必要元数据的配方的方式创建，但你也可以使用 **`conda metapackage`** 命令从命令行创建一个完整的元包。

metapackage 命令使用方式如下所示：

```
$ conda metapackage packagename 1.0
```

包名称和版本是必需的，但有几个选项可以添加其他元数据，如依赖项。

```
$ conda metapackage --help
usage: conda-metapackage [-h] [--no-binstar-upload]
                         [--build-number BUILD_NUMBER]
                         [--build-string BUILD_STRING]
                         [--dependencies [DEPENDENCIES [DEPENDENCIES ...]]]
                         [--home HOME] [--license LICENSE] [--summary SUMMARY]
                         [--entry-points [ENTRY_POINTS [ENTRY_POINTS ...]]]
                         name version

tool for building conda metapackages. A metapackage is a package with no
files, only metadata

positional arguments:
  name                  name of the created package
  version               version of the created package

optional arguments:
  -h, --help            show this help message and exit
  --no-binstar-upload   do not ask to upload the package to binstar
  --build-number BUILD_NUMBER
                        build number for the package (default is 0)
  --build-string BUILD_STRING
                        build string for the package (default is automatically
                        generated)
  --dependencies [DEPENDENCIES [DEPENDENCIES ...]], -d [DEPENDENCIES [DEPENDENCIES ...]]
                        The dependencies of the package. To specify a version
                        restriction for a dependency, wrap the dependency in
                        quotes, like 'package >=2.0'
  --home HOME           The homepage for the metapackage
  --license LICENSE     The license of the metapackage
  --summary SUMMARY     Summary of the package. Pass this in as a string on
                        the command line, like --summary 'A metapackage for
                        X'. It is recommended to use single quotes if you are
                        not doing variable substitution to avoid
                        interpretation of special characters.
  --entry-points [ENTRY_POINTS [ENTRY_POINTS ...]]
                        Python entry points to create automatically. They
                        should use the same syntax as in the meta.yaml of a
                        recipe, e.g., --entry-points
                        bsdiff4=bsdiff4.cli:main_bsdiff4 will create an entry
                        point called bsdiff4 that calls
                        bsdiff4.cli.main_bsdiff4()
```

为 **`ipython-notebook`** 创建元包的命令如下所示：

```	
$ conda metapackage ipython-notebook 2.2.0 --dependencies python ipython \
	'tornado >=3.1' 'pyzmq >=2.1.11' jinja2 --license BSD --home \
	http://ipython.org/ --summary "Metapackage for the IPython notebook"
```

## bdist_conda

如果你是一个 Python 软件包的维护者，你可能觉得构建一个 conda 配方有点多余，因为在配方中所需的元数据已在 **`setup.py`** 指定。除了构建和维护一个单独的配方之外，另一种方法是使用 **`setup.py bdist_conda`**。**`bdist_conda`** 是 distutils 的一个扩展，安装 **`conda-build`** 包时会一起安装，因此你需要一个 root 环境中的 conda 版 **`python`**，并且已安装了 **`conda-build`**。使用方式如下：

```
$ python setup.py bdist_conda
```

这会运行构建过程，并会生成一个 conda 配方，但它将会使用 **`setup.py`** 中的元数据和安装说明。

还可以在 **`setup()`** 函数设置特定的 conda 选项，如构建号和构建字符串。更多信息，参见 [bdist_conda](http://conda.pydata.org/docs/bdist_conda.html) 文档。

## 子命令

Conda 可使用自定义命令进行扩展。PATH 上任何以 **`conda-`** 开始的可执行文件都将作为 **`conda`** 的子命令。例如，如果你有一个名为 **`conda-mycommand`** 的可执行文件，**`conda mycommand`** 将调用 **`conda-mycommand`** 命令。**`conda --help`** 还将解析来自此命令（它假定 argparse 的帮助格式）的帮助信息。许多 conda 自带的命令实际上就是子命令，像 **`conda-build`** 和 **`conda-skeleton`**。这样就可以把它们放在一个单独的包中（`conda-build`），能够单独安装和移除。

注意，如果你想在子命令中使用 **`conda`** 的功能，建议使用 **`conda-api`**。见下面的章节。

## Bash tab 补全

如果你使用 Bash，你可以通过以下操作使用 tab 自动补全：安装 **`argcomplete`** 包(**`conda install argcomplete`**)，并在 bash profile (通常是 **`~/.profile`** 或 **`~/.bashrc`**) 中添加 

```
eval "$(register-python-argcomplete conda)"
```

如需测试是否生效，可以打开一个新的终端窗口或标签，并输入：

```
$ conda ins<TAB>
```

它会补全为：

```
$ conda install
```

可以补全选项或者参数，以后也会加入补全包名的功能。

## 历史记录

Conda 会记录当前环境中运行过的所有命令，以及所导致的包修改。你可以通过下面的命令查看所有更改：

```
$ conda list --revisions
```

举个例子：

```
$ conda create -n myenv python
Fetching package metadata: .............
Solving package specifications: .
Package plan for installation in environment /Users/aaronmeurer/anaconda/envs/myenv:

The following NEW packages will be INSTALLED:

    openssl:  1.0.1h-1  defaults
    python:   3.4.1-4   defaults
    readline: 6.2-2     defaults
    sqlite:   3.8.4.1-0 asmeurer
    tk:       8.5.15-0  defaults
    xz:       5.0.5-0   defaults
    zlib:     1.2.7-1   defaults

Linking packages ...
[      COMPLETE      ] |#########################################################| 100%
#
# To activate this environment, use:
# $ source activate myenv
#
# To deactivate this environment, use:
# $ source deactivate
#
$ conda install -n myenv sympy
Fetching package metadata: .............
Solving package specifications: .
Package plan for installation in environment /Users/aaronmeurer/anaconda/envs/myenv:

The following NEW packages will be INSTALLED:

    sympy: 0.7.5-py34_0 asmeurer

Linking packages ...
[      COMPLETE      ] |#########################################################| 100%
$ conda remove -n myenv sympy
Fetching package metadata: .............

Package plan for package removal in environment /Users/aaronmeurer/anaconda/envs/myenv:

The following packages will be REMOVED:

    sympy: 0.7.5-py34_0 asmeurer

Unlinking packages ...
[      COMPLETE      ] |#########################################################| 100%
$ conda list -n myenv --revisions
2014-09-22 14:51:24  (rev 0)

2014-09-22 14:51:26  (rev 1)
    +openssl-1.0.1h
    +python-3.4.1
    +readline-6.2
    +sqlite-3.8.4.1
    +tk-8.5.15
    +xz-5.0.5
    +zlib-1.2.7

2014-09-22 14:51:45  (rev 2)
    +sympy-0.7.5

2014-09-22 14:52:01  (rev 3)
    -sympy-0.7.5
```

注意每一次修改都有一个编号。我们可以使用 **`conda install --revision`**，回滚到以前的版本。

```
$ conda install -n myenv --revision=2
Fetching package metadata: .............

Package plan for installation in environment /Users/aaronmeurer/anaconda/envs/myenv:

The following NEW packages will be INSTALLED:

    sympy: 0.7.5-py34_0 defaults

Linking packages ...
[      COMPLETE      ] |########################################################|100%
```

修订历史记录存储在当前环境下的 **`conda-meta/history`** 文件中。这个文件还跟踪了在每个版本中使用的命令。

```
$ cat ~/anaconda/envs/myenv/conda-meta/history
==> 2014-09-22 14:51:24 <==
# cmd: /Users/aaronmeurer/anaconda/bin/conda create -n myenv python
==> 2014-09-22 14:51:26 <==
# cmd: /Users/aaronmeurer/anaconda/bin/conda create -n myenv python
+openssl-1.0.1h-1
+python-3.4.1-4
+readline-6.2-2
+sqlite-3.8.4.1-0
+tk-8.5.15-0
+xz-5.0.5-0
+zlib-1.2.7-1
==> 2014-09-22 14:51:45 <==
# cmd: /Users/aaronmeurer/anaconda/bin/conda install -n myenv sympy
+sympy-0.7.5-py34_0
==> 2014-09-22 14:52:01 <==
# cmd: /Users/aaronmeurer/anaconda/bin/conda remove -n myenv sympy
-sympy-0.7.5-py34_0
==> 2014-09-22 14:56:32 <==
# cmd: /Users/aaronmeurer/anaconda/bin/conda install -n myenv --revision=2
+sympy-0.7.5-py34_0
```

## conda-api

如果你想自己写代码来扩展 conda，建议使用 [conda-api](https://github.com/conda/conda-api)；通过 **`conda install conda-api`** 来安装。这个 API 以子进程的方式调用 **`conda`** ，并使用 **`--json`** 选项来解析 JSON 输出。如果你想在非 Python 项目中使用 conda，你也可以使用 **`--json`** 选项，这是非常有用的。

用 conda-api 或 **`--json`** API 优于直接使用 conda，因为 conda 的命令行输出格式不是固定的，但是 **`--json`** 输出的结构不会改变。它通常也更容易解析。

强烈建议不要从一个 Python 项目内 **`import conda`**。有两个原因。首先，conda 的 Python API 不保证能稳定使用。第二，任何将 conda 作为一个 Python 库导入的代码，必须是在该根环境下使用 conda 来安装的，因此不能被安装到任意的 conda 环境中。但使用 **`conda-api`** 的代码则可以被安装到任何 conda 环境中。

## 结语

学习 Conda 高级特性这个系列文章到这里就结束了。conda 是开源的（BSD 许可证），我鼓励每一个读者为其做出贡献。[conda](https://github.com/conda/conda) 和 [conda-build](https://github.com/conda/conda-build) 的源代码在 GitHub 上。我也鼓励人们贡献 conda 配方到 [conda-recipes](https://github.com/conda/conda-recipes) 仓库。欢迎加入 [conda 邮件列表](https://groups.google.com/a/continuum.io/forum/#%21forum/conda)来讨论 conda。

***

[点此查看原文链接](https://www.continuum.io/blog/developer/advanced-features-conda-part-2)。

[Python 翻译组](https://github.com/PythonTG)是EarlGrey@编程派发起成立的一个专注于 Python 技术内容翻译的小组，目前已有 30 名 Python 技术爱好者加入。

翻译组出品的内容（包括教程、文档、书籍、视频）将在编程派微信公众号首发，欢迎各位 Python 爱好者推荐相关线索。推荐线索，可直接在编程派微信公众号推文下留言即可。

