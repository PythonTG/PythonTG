# 用Python从头开发一个自己的Shell（二）

title: 用Python从头开发一个自己的Shell（二）
author: Supasate Choochaisri
translator: Justin
reviewer: EarlGrey
date: 20160820
permalink: create-your-own-shell-in-python-part-2
keywords: shell工作原理, python shell, python教程, python项目, 内建命令

***

> 平常工作中经常用到 shell 吧？好不好奇 shell 的具体执行方式？今天推送的这两篇文章，将利用 Python 实现一些简单的 shell 功能。

> 本文原作者为 Supasate Choochaisri ，由 PythonTG 翻译组的 Justin 翻译，校对为 EarlGrey。译者简介：Justin，python工程师一枚，对go、docker感兴趣，还在成长ing。

在第一部分中，我们已经实现了主要的 shell 循环，切分了命令输入，并通过 `fork` 和 `exec` 执行了输入命令。在本文中，我们将解决剩下的问题。第一个问题是 `cd test_dir2` 并未改变当前目录。第二个问题是我们仍不能优雅地退出 shell。

## Step 4: 内置命令

`cd test_dir2` 并未改变当前目录，这种说法在某种意义上说既是对的又是错误的。正确是因为执行命令之后，仍在相同的目录。然而，目录确实改变了，不过是在子进程中改变的。

还记得我们 `fork` 了一个子进程，然后执行命令，这个命令并不会在父进程中执行，导致仅仅改变了子进程的目录，而没有改变父进程的目录。

之后，子进程终止，父进程仍保持原先的目录。

因此，这类命令必须为 shell 本身内置，并得在 shell 进程中执行，而不是通过 `fork`。

### cd

我们先从 `cd` 命令开始。

首先建立一个 `builtins` 目录，来存放内建命令。

```
yosh_project
|-- yosh
   |-- builtins
   |   |-- __init__.py
   |   |-- cd.py
   |-- __init__.py
   |-- shell.py
```

在 `cd.py` 中，通过使用系统调用 `os.chdir` 实现自己的 `cd` 命令：

```python
import os
from yosh.constants import *


def cd(args):
    os.chdir(args[0])

    return SHELL_STATUS_RUN
```

注意到在内建函数中会返回 shell 的运行状态，所以，我们把常量写进 `yosh/constants.py`  中供项目使用。

```
yosh_project
|-- yosh
   |-- builtins
   |   |-- __init__.py
   |   |-- cd.py
   |-- __init__.py
   |-- constants.py
   |-- shell.py
```

在 `constants.py` 中定义 shell 状态常量：

```python
SHELL_STATUS_STOP = 0
SHELL_STATUS_RUN = 1
```

现在，内建的 `cd` 命令已经就绪。接下来修改 `shell.py` 来处理内建函数。

```python
...
# Import constants
from yosh.constants import *

# Hash map to store built-in function name and reference as key and value
built_in_cmds = {}


def tokenize(string):
    return shlex.split(string)


def execute(cmd_tokens):
    # Extract command name and arguments from tokens
    cmd_name = cmd_tokens[0]
    cmd_args = cmd_tokens[1:]

    # If the command is a built-in command, invoke its function with arguments
    if cmd_name in built_in_cmds:
        return built_in_cmds[cmd_name](cmd_args)

    ...
```

使用 Python 字典 `built_in_cmds`，作为存储内建函数的哈希表。在 `execute` 函数中，将命令名及参数取出，如果命令名在哈希表中，就调用对应的函数。

（注意：`built_in_cmds[cmd_name]` 返回可以使用用参数立即调用的函数引用）  

我们马上就可以使用内建的 `cd` 函数了，最后一步是将 `cd` 函数加到 `built_in_cmds` 中。

```python
...
# Import all built-in function references
from yosh.builtins import *

...

# Register a built-in function to built-in command hash map
def register_command(name, func):
    built_in_cmds[name] = func


# Register all built-in commands here
def init():
    register_command("cd", cd)


def main():
    # Init shell before starting the main loop
    init()
    shell_loop()
```

定义 `register_command` 函数来向内建命令哈希表中添加内建函数，然后定义 `init` 函数，并注册内建 `cd` 函数。

注意 `register_command("cd", cd)` 这一行代码。第一个参数是命令名，第二个参数是函数的引用。为了使第二个参数 `cd` 指向 `yosh/builtins/cd.py` 中的 `cd` 函数，我们需要在 `yosh/builtins/__init__.py`中添加下面的代码：

```python
from yosh.builtins.cd import *
```

因此，在 `yosh/shell.py` 中，当从 `yosh.builtins` 中 `import *` 时，就得到了 `cd` 函数的引用。

代码已经准备就绪，来尝试在 `yosh` 同级目录下运行 `python -m yosh.shell`。

现在，我们的 `cd` 命令应该能够正确改变 shell 目录，同时哪些非内建命令也同样有效。

### 退出

下面是最后一步：优雅地退出。

我们需要一个函数将 shell 的状态改变为 `SHELL_STATUS_STOP`，这样 shell 循环将会中断，shell 程序也将会结束并退出。

像 `cd` 一样，如果在子进程中 `fork` 并执行 `exit` 命令，对父进程不会有影响。因此，`exit` 函数必须为内建函数。

在 `builtins` 文件夹下新建 `exit.py`：

```
yosh_project
|-- yosh
   |-- builtins
   |   |-- __init__.py
   |   |-- cd.py
   |   |-- exit.py
   |-- __init__.py
   |-- constants.py
   |-- shell.py
```

`exit.py` 中定义了 `exit` 函数，用来返回终止主循环的状态值：

```python
from yosh.constants import *


def exit(args):
    return SHELL_STATUS_STOP
```

然后，在 `yosh/builtins/__init__.py`  中导入 `exit` 函数的引用：

```python
from yosh.builtins.cd import *
from yosh.builtins.exit import *
```

最后，在 `shell.py` 中的 `init()` 函数中注册 `exit` 函数：

```python
...

# Register all built-in commands here
def init():
    register_command("cd", cd)
    register_command("exit", exit)

...
```

大功告成！

尝试运行 `python -m yosh.shell`，现在输入 `exit` 就可以优雅地退出程序了。

# 一些思考

我希望你像我一样，享受创造 `yosh` (属于自己的shell)的过程，但是 `yosh` 现在还是粗糙，我没有处理可能导致 shell 中断的特殊情况，也有很多内建功能没有覆盖到。一些非内建函数也可以作为内建函数实现，以提高性能（避免创建新进程的时间开销），还有很多功能没有实现（参考[常见功能](http://tldp.org/LDP/Bash-Beginners-Guide/html/x7243.html)和[特殊功能](http://www.tldp.org/LDP/intro-linux/html/x12249.html)）

我在 [github](https://github.com/supasate/yosh) 上提供了源码，欢迎 fork 并把玩。

现在，轮到你来创造属于自己的 shell 了。

祝编码愉快！

***

[点此查看原文链接](https://hackercollider.com/articles/2016/07/06/create-your-own-shell-in-python-part-2/)。

[Python 翻译组](https://github.com/PythonTG)是EarlGrey@编程派发起成立的一个专注于 Python 技术内容翻译的小组，目前已有近 30 名 Python 技术爱好者加入。

翻译组出品的内容（包括教程、文档、书籍、视频）将在编程派微信公众号首发，欢迎各位 Python 爱好者推荐相关线索。

推荐线索，可直接在编程派微信公众号推文下留言即可。

