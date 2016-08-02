## 如何写一个你自己的Python包

title: 如何写一个你自己的Python包
author: Gigi Sayfan
translator: ChengPeter
reviewer: LinkCheng
date: 20160730
permalink: how-to-write-your-own-python-packages
keywords: Python, Package Management

***

>本文作者为 Gigi Sayfan ，发布在知名编程学习网站 Tutsplus。是 Python 翻译组最新发布的一篇译文，希望对大家学习如何打包有帮助。
>
>译者为 ChengPeter，并由 LinkCheng 校对，EarlGrey@编程派定稿。

## 概述

Python 是一门强大的编程语言。它最大的缺点之一就是打包。在 Python 社区里，这是个众所周知的事实。虽然在过去几十年，安装、导入、创建包的过程已经改善了，但是仍然不能和从 Python 的缺点中吸取了很多教训的 Go 和 Rust 这样的新语言，以及其他更加成熟的语言相媲美。

在本教程中，你将会学到创建以及分享自己的包所需要的一切知识。想要了解关于 Python 包的背景知识，请阅读[如何使用 Python 包](http://code.tutsplus.com/tutorials/how-to-use-python-packages--cms-26000)。

## 项目打包

打包一个项目，指的是你创建一系列条理清晰的 Python 模块，可能还有其他文件，并且把它们放到一个很容易使用的结构当中去的过程。有一些不得不考虑的地方，比如对其他包的依赖，内部结构（子包），版本控制，目标用户和包的形式（源文件还是二进制文件）。

### 示例

让我们从一个简单的例子开始。[conman](https://github.com/the-gigi/conman/tree/master/conman) 是一个用来管理配置的包。它支持各种文件格式，还支持使用 [etcd](https://coreos.com/etcd) 进行分布式配置。

一个包的内容通常会保存在一个目录下（尽管通常也会把子包分离在不同的文件目录下），并且有时候会被放在自己的 git 仓库下，就像本文中这样。

根目录包含了各种各样的配置文件（`setup.py` 是一个必须的并且最重要的配置文件），代码本身通常在一个子目录下，目录名就是包的名称。当然最好还有一个测试文件目录。。下面就是 "conman" 的目录结构：

```
> tree
 
.
 
├── LICENSE
 
├── MANIFEST.in
 
├── README.md
 
├── conman
 
│   ├── __init__.py
 
│   ├── __pycache__
 
│   ├── conman_base.py
 
│   ├── conman_etcd.py
 
│   └── conman_file.py
 
├── requirements.txt
 
├── setup.cfg
 
├── setup.py
 
├── test-requirements.txt
 
├── tests
 
│   ├── __pycache__
 
│   ├── conman_etcd_test.py
 
│   ├── conman_file_test.py
 
│   └── etcd_test_util.py
 
└── tox.ini
```

让我们快速地看一眼 setup.py 文件。它从  [setuptools](http://pythonhosted.org/setuptools) 包中导入了两个函数：`setup()` 和 `find_packages()`。然后调用了 `setup()`，并且将 `find_packages()` 作为其中的一个参数。

```python
from setuptools import setup, find_packages
 
 
 
setup(name='conman',
 
      version='0.3',
 
      url='https://github.com/the-gigi/conman',
 
      license='MIT',
 
      author='Gigi Sayfan',
 
      author_email='the.gigi@gmail.com',
 
      description='Manage configuration files',
 
      packages=find_packages(exclude=['tests']),
 
      long_description=open('README.md').read(),
 
      zip_safe=False,
 
      setup_requires=['nose>=1.0'],
 
      test_suite='nose.collector')
```

这是非常普通的配置。`setup.py` 是一个常规的 Python 文件，你可以在文件里面做任何你想做的事情，不过它的主要工作是用适当的参数去调用 `setup()` 函数。因为在安装你的包的时候，`setup()`
函数将会被各种各样的工具以标准的方法调用。在下一节，我将会介绍一些细节。

## 配置文件

除了 `setup.py` ，还有一些其他可选的配置文件，在这里罗列出来，一并介绍一下它们各自的使用目的。

### Setup.py

`setup()` 函数会有很多的命名参数，用来控制包安装的方方面面，并可运行不同的命令。许多的参数指定了在上传包到代码库时搜索和过滤所用到的元数据。

- name:包的名称（以及如何在 PYPI 上呈现）
- version：这对于保持适当的依赖关系至关重要
- url：包的链接，通常为 Github 上的链接，或者是 readthedocs 链接
- packages：需要包含的子包列表，`find_packages()`将帮助我们查找
- setup_requires：指定依赖项
- test_suite：测试时运行的工具

`long_description` 在这里设置为 `README.md` 文件的内容，这是一项最佳实践，只在一个来源处做说明介绍。

### Setup.cfg

setup.py 文件还提供了一个命令行界面来运行各种命令。例如：运行单元测试，你可以输入：`python setup.py test`

```
running test
 
running egg_info
 
writing conman.egg-info/PKG-INFO
 
writing top-level names to conman.egg-info/top_level.txt
 
writing dependency_links to conman.egg-info/dependency_links.txt
 
reading manifest file 'conman.egg-info/SOURCES.txt'
 
reading manifest template 'MANIFEST.in'
 
writing manifest file 'conman.egg-info/SOURCES.txt'
 
running build_ext
 
test_add_bad_key (conman_etcd_test.ConManEtcdTest) ... ok
 
test_add_good_key (conman_etcd_test.ConManEtcdTest) ... ok
 
test_dictionary_access (conman_etcd_test.ConManEtcdTest) ... ok
 
test_initialization (conman_etcd_test.ConManEtcdTest) ... ok
 
test_refresh (conman_etcd_test.ConManEtcdTest) ... ok
 
test_add_config_file_from_env_var (conman_file_test.ConmanFileTest) ... ok
 
test_add_config_file_simple_guess_file_type (conman_file_test.ConmanFileTest) ... ok
 
test_add_config_file_simple_unknown_wrong_file_type (conman_file_test.ConmanFileTest) ... ok
 
test_add_config_file_simple_with_file_type (conman_file_test.ConmanFileTest) ... ok
 
test_add_config_file_simple_wrong_file_type (conman_file_test.ConmanFileTest) ... ok
 
test_add_config_file_with_base_dir (conman_file_test.ConmanFileTest) ... ok
 
test_dictionary_access (conman_file_test.ConmanFileTest) ... ok
 
test_guess_file_type (conman_file_test.ConmanFileTest) ... ok
 
test_init_no_files (conman_file_test.ConmanFileTest) ... ok
 
test_init_some_bad_files (conman_file_test.ConmanFileTest) ... ok
 
test_init_some_good_files (conman_file_test.ConmanFileTest) ... ok
 
 
 
----------------------------------------------------------------------
 
Ran 16 tests in 0.160s
 
 
 
OK
```

setup.cfg 是一个 ini 格式的文件，可能包含传递给 `setup.py` 的命令的可选默认值。在这里，setup.cfg 中包含了 `nosetests`（刚才运行的单元测试）的一些选项：

```
[nosetests]
 
verbose=1
 
nocapture=1
```

### MANIFEST.in

此文件中包含有不属于内部包目录，但你仍想纳入进来的文件。这些文件通常是 `readme` 文件，license 文件以及一些类似的文件。其中，比较重要的一个是 `requirements.txt`。 pip 使用该文件安装其他必须的包。

下面是 conman 的 `MANIFEST.in` 文件：

```
include LICENSE
 
include README.md
 
include requirements.txt
```

### 依赖项

您可以在 `setup.py` 文件的 `install_requires` 部分和 `requirements.txt` 文件中指定依赖项。Pip 将会自动安装 `install_requires` 中列出的依赖项，而不是 `requirements.txt` 文件。要安装后者中指定的依赖项，在运行 pip 时必须明确指定：`pip install -r requirements.txt`。

`install_requires` 选项旨在指定所要求模块的最低主版本号等较抽象的要求。而在 requirements.txt 文件的要求更加具体，通常细致到次版本号。

下面是 conman 的 requirements 文件。你可以看到，所有的版本都被定死了，这也就意味着，当所依赖的包中有一个升级了或者引入了让 conman 无法运行的变化，就会产生负面影响。

```
PyYAML==3.11
 
python-etcd==0.4.3
 
urllib3==1.7
 
pyOpenSSL==0.15.1
 
psutil==4.0.0
 
six==1.7.3
```

然而把版本号固定写死却提供了可预测性，并且这样会让人觉得心安。如果许多人在不同的时间安装软件包，这一点尤其重要。如果不固定下来，每个人在安装包时将会得到不同版本的依赖。版本固定的缺点是，如果你跟不上依赖项的进度，你可能会被困在老化的版本上，可能表现不佳，甚至容易受攻击。

我是在 2014 年写的 conman，之后就没怎么管了。但是现在，为了写这篇教程，我更新了所有的东西，几乎每一个依赖项都有很大的改进。

## 发布

你可以创建一个源代码发布版或二进制发布版。两者我都会介绍。

### 源发布版

你使用 `python setup.py sdist` 这个命令创建源发布文件。下面是 conman 的输出：

```
> python setup.py sdist
 
running sdist
 
running egg_info
 
writing conman.egg-info/PKG-INFO
 
writing top-level names to conman.egg-info/top_level.txt
 
writing dependency_links to conman.egg-info/dependency_links.txt
 
reading manifest file 'conman.egg-info/SOURCES.txt'
 
reading manifest template 'MANIFEST.in'
 
writing manifest file 'conman.egg-info/SOURCES.txt'
 
warning: sdist: standard file not found: should have one of README, README.rst, README.txt
 
 
 
running check
 
creating conman-0.3
 
creating conman-0.3/conman
 
creating conman-0.3/conman.egg-info
 
making hard links in conman-0.3...
 
hard linking LICENSE -> conman-0.3
 
hard linking MANIFEST.in -> conman-0.3
 
hard linking README.md -> conman-0.3
 
hard linking requirements.txt -> conman-0.3
 
hard linking setup.cfg -> conman-0.3
 
hard linking setup.py -> conman-0.3
 
hard linking conman/__init__.py -> conman-0.3/conman
 
hard linking conman/conman_base.py -> conman-0.3/conman
 
hard linking conman/conman_etcd.py -> conman-0.3/conman
 
hard linking conman/conman_file.py -> conman-0.3/conman
 
hard linking conman.egg-info/PKG-INFO -> conman-0.3/conman.egg-info
 
hard linking conman.egg-info/SOURCES.txt -> conman-0.3/conman.egg-info
 
hard linking conman.egg-info/dependency_links.txt -> conman-0.3/conman.egg-info
 
hard linking conman.egg-info/not-zip-safe -> conman-0.3/conman.egg-info
 
hard linking conman.egg-info/top_level.txt -> conman-0.3/conman.egg-info
 
copying setup.cfg -> conman-0.3
 
Writing conman-0.3/setup.cfg
 
creating dist
 
Creating tar archive
 
removing 'conman-0.3' (and everything under it)
```

你会发现，我得到了一个关于未找到标准后缀 README 文件的警告，因为我喜欢使用 Markdown，所以我使用的是 "README.md" 。除此之外，所有的包源文件和附加文件都被包含进去。然后，在 `conman.egg-info` 目录下生成了一堆元数据。最后，一个名为 `conman-0.3.tar.gz` 的压缩文件被创建，并放到 `dist` 子目录当中。

安装该软件包也需要先进行构建（即使它是纯 Python ）。你只需给出压缩包的路径，就能使用 pip 安装它。 例如：

```
pip install dist/conman-0.3.tar.gz
 
Processing ./dist/conman-0.3.tar.gz
 
Installing collected packages: conman
 
  Running setup.py install for conman ... done
 
Successfully installed conman-0.3
```

Conman 被安装在 site-packages 文件夹下，可以和其他包一样导入：

```
import conman
 
conman.__file__
 
'/Users/gigi/.virtualenvs/conman/lib/python2.7/site-packages/conman/__init__.pyc'
```

### Wheels

Wheels 是打包 Python 代码和扩展 C 语言的一个相对新的方法。它们替换了 egg 格式。有好几种类型的 Wheels：纯 Python Wheels，平台 Wheels 以及通用 Wheels。像 conman 这样的纯 Python Wheels 包，没有任何 C 语言的扩展代码。

平台 wheels 包含 C 扩展代码。通用 wheels 是纯 Python Wheels，但同时兼容 Python 2 和 Python 3（它们甚至不需要 2to3 转换）。如果你有需要同时兼容 Python 2 和 Python 3 （这变得越来越重要）的纯 Python 包，你只需要构建一个通用 wheels 即可，不必分别构建 Python 2 wheels 和 Python 3 wheels。

如果你的软件包有 C 语言扩展的代码，你必须针对各个平台分别构建平台 Wheels。对于包含 C 扩展的包来说，构建平台 wheels 的好处巨大，因为不用在目标机器上安装编译器和支持库。Wheel 中已包含一个构建好了的的包，因此你知道肯定不会构建失败，而且安装速度更快，因为只需要拷贝一下即可。使用像 Numpy 和 Pandas 这样的科学计算库的的用户能真正体会到这一点的好处，因为安装这些包需要花费大量时间，并且一旦缺少某些库文件或者编译器配置不恰当，就会导致安装失败。

创建纯 Python 或者平台 Wheels 的命令是：`python setup.py bdist_wheel`。

[Setuptools](http://pythonhosted.org/setuptools) （提供了 `setup()` 函数的引擎）会自动检测是需要纯 Python 还是平台 Wheel 。

```
running bdist_wheel
 
running build
 
running build_py
 
creating build
 
creating build/lib
 
creating build/lib/conman
 
copying conman/__init__.py -> build/lib/conman
 
copying conman/conman_base.py -> build/lib/conman
 
copying conman/conman_etcd.py -> build/lib/conman
 
copying conman/conman_file.py -> build/lib/conman
 
installing to build/bdist.macosx-10.9-x86_64/wheel
 
running install
 
running install_lib
 
creating build/bdist.macosx-10.9-x86_64
 
creating build/bdist.macosx-10.9-x86_64/wheel
 
creating build/bdist.macosx-10.9-x86_64/wheel/conman
 
copying build/lib/conman/__init__.py -> build/bdist.macosx-10.9-x86_64/wheel/conman
 
copying build/lib/conman/conman_base.py -> build/bdist.macosx-10.9-x86_64/wheel/conman
 
copying build/lib/conman/conman_etcd.py -> build/bdist.macosx-10.9-x86_64/wheel/conman
 
copying build/lib/conman/conman_file.py -> build/bdist.macosx-10.9-x86_64/wheel/conman
 
running install_egg_info
 
running egg_info
 
creating conman.egg-info
 
writing conman.egg-info/PKG-INFO
 
writing top-level names to conman.egg-info/top_level.txt
 
writing dependency_links to conman.egg-info/dependency_links.txt
 
writing manifest file 'conman.egg-info/SOURCES.txt'
 
reading manifest file 'conman.egg-info/SOURCES.txt'
 
reading manifest template 'MANIFEST.in'
 
writing manifest file 'conman.egg-info/SOURCES.txt'
 
Copying conman.egg-info to build/bdist.macosx-10.9-x86_64/wheel/conman-0.3-py2.7.egg-info
 
running install_scripts
 
creating build/bdist.macosx-10.9-x86_64/wheel/conman-0.3.dist-info/WHEEL<br>
```

查看 `dist` 目录，你可以看到创建了一个纯 Python Wheel。

```
ls -la dist
 
 
 
dist/
 
total 32
 
-rw-r--r--  1 gigi  staff   5.5K Feb 29 07:57 conman-0.3-py2-none-any.whl
 
-rw-r--r--  1 gigi  staff   4.4K Feb 28 23:33 conman-0.3.tar.gz
```

文件名 “conman-0.3-py2-none-any.whl” 有几个组成部分：包名，包版本，Python 版本，平台版本，最后是扩展名 “whl”。

如需创建通用包，你只需要添加 `--universal` 选项，比如：`python setup.py bdist_wheel --universal`。

生成的 Wheel 会被命名为："conman-0.3-py2.py3-none-any.whl"。

请注意：如果你创建了通用型包，就要确保你的代码的确能兼容 Python 2 和 Python 3。

## 结语

编写自己的Python包要求使用许多工具，指定大量的元数据，并仔细考虑你的依赖项和目标受众。但回报也是巨大的。 

如果你写出有用的代码并正确打包，人们将能够轻松地安装它，并从中受益。

***

[点此查看原文链接](http://code.tutsplus.com/tutorials/how-to-write-your-own-python-packages--cms-26076)。

[Python 翻译组](https://github.com/PythonTG)是EarlGrey@编程派发起成立的一个专注于 Python 技术内容翻译的小组，目前已有近 30 名 Python 技术爱好者加入。翻译组出品的内容（包括教程、文档、书籍、视频）将在编程派微信公众号首发，欢迎各位 Python 爱好者推荐相关线索。推荐线索，可直接在编程派微信公众号推文下留言即可。

