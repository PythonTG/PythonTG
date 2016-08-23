# 用Python从头开发一个自己的Shell

title: 用Python从头开发一个自己的Shell
author: Supasate Choochaisri
translator: Justin
reviewer: EarlGrey
date: 20160820
permalink: create-your-own-shell-in-python-part-1
keywords: 

***

我很好奇 shell（比如 bash、cash等）内部的工作原理，所以我用 Python 实现了 **yosh**（Your Own Shell）来满足自己的好奇心。我在本文中阐释的概念同样适用于其他语言。

# Step 0: 项目结构

在这个项目中，我使用了下面的结构：

```
yosh_project
|-- yosh
   |-- __init__.py
   |-- shell.py
```

`yosh_project` 是项目根文件夹（你也可以用 `yosh` 来命名）。

`yosh` 是包文件夹，`__init__.py ` 会让包与文件夹同名（如果你不写 python，可以忽略这点）。

`shell.py` 是主要的 shell 文件。

## Step 1: Shell 循环

启动 shell 时，它会立刻展示命令提示符并等待输入。在接收到命令并执行完毕（细节会在后面讲到）后，shell 会再次回到等待循环，准备接收下一条命令。

在 `shell.py` 中，我们通过主函数调用 `shell_loop()`  函数，来启动循环。代码如下：

```python
def shell_loop():
    # Start the loop here


def main():
    shell_loop()


if __name__ == "__main__":
    main()

```

然后在 `shell_loop()` 函数中，使用 `status` 标志来表示循环是否应该继续。在循环开始时，shell 将立即显示命令提示符，并等待输入。

```python
import sys

SHELL_STATUS_RUN = 1
SHELL_STATUS_STOP = 0


def shell_loop():
    status = SHELL_STATUS_RUN

    while status == SHELL_STATUS_RUN:
        # Display a command prompt
        sys.stdout.write('> ')
        sys.stdout.flush()

        # Read command input
        cmd = sys.stdin.readline()

```

接下来，对输入的命令进行切分（tokenize），并执行（稍后会实现 `tokenize` 和 `execute` 函数）。

现在，`shell_loop()` 函数应该如下：

```python
import sys

SHELL_STATUS_RUN = 1
SHELL_STATUS_STOP = 0


def shell_loop():
    status = SHELL_STATUS_RUN

    while status == SHELL_STATUS_RUN:
        # Display a command prompt
        sys.stdout.write('> ')
        sys.stdout.flush()

        # Read command input
        cmd = sys.stdin.readline()

        # Tokenize the command input
        cmd_tokens = tokenize(cmd)

        # Execute the command and retrieve new status
        status = execute(cmd_tokens)

```

上述就是整个的 shell 循环。如果通过 `python shell.py` 启动 shell，会立即显示命令提示符。但是如果我们输入命令并回车，就会抛出错误，因为我们还没有定义 `tokenize` 函数。

要退出 shell，可以使用 `ctrl-c`，稍后我会介绍如何优雅地终止 shell。

# Step 2: 切分（Tokenization）

用户在 shell 中键入命令并按下回车时，输入的命令是一条长长的字符串，其中包含了命令名以及参数。因此，我们必须将其切分（将字符串拆分成多个 token）。  

字符串切分乍一看很简单。我们可能会使用 `cmd.split()` 根据空格来分割输入的命令。对于形如 `ls -a my_folder` 的命令是奏效的，因为 `cmd.split()` 会将其拆分为一个列表 — `['ls', '-a', 'my_folder’]`，这样我们使用起来就比较容易了。

但是，某些情况下，某些参数会带有单引号或者双引号，比如 `echo "Hello World”` 或者 `echo 'Hello World’`。如果我们使用 `cmd.split()`, 将会得到一个包含三个 token 的列表 — `['echo', '"Hello', 'World”’]`，而不是包含两个 token 的列表 — `['echo', 'Hello World’]`。

幸运地是，Python 提供了一个叫做 `shlex` 的库，可以很好地帮助我们分词（注：我们也可以使用正则表达式，但这不是本文的重点）。

```python
import sys
import shlex

...

def tokenize(string):
    return shlex.split(string)

...
```
然后，我们将这些 token 传给执行进程。

# Step 3: 执行

这是 shell 核心，而且也是有趣的部分。shell 执行 `mkdir test_dir` 时会发生什么呢？（注：`mkdir` 是一个程序，传递 `test_dir` 参数执行后会创建名为 `test_dir` 的目录）。

这一步中涉及的第一个函数是 `execvp`。在解释 `execvp` 的功能之前，让我们先来实际使用一下。

```python
import os
...

def execute(cmd_tokens):
    # Execute command
    os.execvp(cmd_tokens[0], cmd_tokens)

    # Return status indicating to wait for next command in shell_loop
    return SHELL_STATUS_RUN

...
```

尝试再次运行 shell 并输入命令 `mkdir test_dir`，然后回车。

现在的问题是，我们敲击回车后，shell 并未等待下一条命令，而是终止了。但是目录成功被创建。

所以，`execvp` 到底做了什么呢？  

`execvp` 是系统调用 `exec` 的一个变种。第一个参数是程序名。`v` 表示第二个参数是程序参数列表（可变的参数个数）。`p` 表示 `PATH` 环境将用于搜索给定的程序名。在我们之前的尝试中，`mkdir` 程序就是基于 `PATH` 环境变量。

（`exec` 还有其他变种，比如 ` execv`、`execvpe`、`execl`、`execlp`、`execlpe`等，你可以google一下获取更多信息。）

`exec` 会将当前调用进程的内存，替换为一个即将执行的进程。在我们的示例中，shell 进程的内存被 `mkdir` 程序替换。然后 `mkdir` 变为主进程，并创建 `test_dir` 目录，最后进程终止。

这里最主要的一点是，**shell 进程已经被 `mkdir` 进程取代**。这也是为什么 shell 会终止而不是等待下一条命令。

所以，我们需要另外一个系统调用 `fork` 来解决这个问题。

`fork` 会分配新的内存，并将现有进程拷贝到新的进程，我们称这个新进程为子进程，调用进程为父进程。之后，执行过 `exec` 的程序将会取代子进程。因此，作为父进程的 shell 就不用进行内存替换了。

下面是修改后的代码：

```python
...

def execute(cmd_tokens):
    # Fork a child shell process
    # If the current process is a child process, its `pid` is set to `0`
    # else the current process is a parent process and the value of `pid`
    # is the process id of its child process.
    pid = os.fork()

    if pid == 0:
    # Child process
        # Replace the child shell process with the program called with exec
        os.execvp(cmd_tokens[0], cmd_tokens)
    elif pid > 0:
    # Parent process
        while True:
            # Wait response status from its child process (identified with pid)
            wpid, status = os.waitpid(pid, 0)

            # Finish waiting if its child process exits normally
            # or is terminated by a signal
            if os.WIFEXITED(status) or os.WIFSIGNALED(status):
                break

    # Return status indicating to wait for next command in shell_loop
    return SHELL_STATUS_RUN

...
```

当父进程调用 `os.fork()` 时，你可以认为所有的源码都被拷贝到子进程。这时父子进程的代码相同，而且并行执行。

运行的代码若属于子进程，`pid` 为 0；若属于父进程，`pid` 为子进程的 id。  

如果 `os.execvp` 在子进程中被调用，子进程的所有源码将被调用程序的源码替换掉。但是，父进程的代码没有改变。  

父进程等待子进程终止后，会返回继续 shell 循环的状态。

# 运行

现在你可以尝试运行我们自己打造的 shell ，并键入 `mkdir test_dir2`。shell应该会正常运转，而且 shell 进程会继续等待你输入下一条命令。尝试 `ls` 命令就会看到已创建的目录。

但是，还是存在一些问题。

第一点，输入 `cd test_dir2` ，然后再输入 `ls`，应该会进入到 `test_dir2`这个空目录中，但是目录并没有切换到 `test_dir2`。

第二点，我们仍不能优雅地退出 shell。

上述问题将会在 Part2 中解决。

***

[点此查看原文链接](https://hackercollider.com/articles/2016/07/05/create-your-own-shell-in-python-part-1/)。

[Python 翻译组](https://github.com/PythonTG)是EarlGrey@编程派发起成立的一个专注于 Python 技术内容翻译的小组，目前已有近 30 名 Python 技术爱好者加入。

翻译组出品的内容（包括教程、文档、书籍、视频）将在编程派微信公众号首发，欢迎各位 Python 爱好者推荐相关线索。

推荐线索，可直接在编程派微信公众号推文下留言即可。



