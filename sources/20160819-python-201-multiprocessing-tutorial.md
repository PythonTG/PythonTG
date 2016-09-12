## 一文学会Python多进程

title: 一文学会Python多进程
author: Michael Driscoll
translator:cystone
reviewer: EarlGrey
date: 20160820
permalink: python-201-a-multiprocessing-tutorial
keywords: 多进程编程, python进程, multiprocessing, pep 371, 全局解释器锁, GIL, threading

***

> 本文由 Python 翻译组 最新翻译出品，原作者为 Michael Discroll，译者为 cystone，并由编程派作者 EarlGrey 校对。昨天，编程派已经发布了一篇多线程编程的教程，一文学会Python多线程编程。

> 译者简介：cystone，成都信息工程大学，计算机学院学生。擅长领域：图像处理，机器学习。

多进程(multiprocessing)模块是在 Python 2.6 版本加入的。它最初由 Jesse Noller 和 Richard Oudkerk 在 [PEP 371](https://www.python.org/dev/peps/pep-0371/) 中定义。multiprocessing 模块生成进程的方式就和你使用 threading 模块生成线程是一样的。但是在这里，因为你使用的是多进程，所以你可以规避全局解释锁(GIL)，充分利用机器多处理器的优势。

multiprocessing 模块还包含一些 threading 模块没有的一些 API。例如，有一个巧妙的 Pool 类可以让你通过多个输入并行执行一个函数。我们将在后边的章节接触到 Pool。我们将从 multiprocessing 模块的 **Process** 类开始介绍。

### multiprocessing 入门

Process 类和 threading 模块的 Thread 类很像。我们来创建一系列调用同一个函数的进程，看它是如何工作的：

```python
import os

from multiprocessing import Process


def doubler(number):
    """
    A doubling function that can be used by a process
    """
    result = number * 2
    proc = os.getpid()
    print('{0} doubled to {1} by process id: {2}'.format(
        number, result, proc))


if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    procs = []

    for index, number in enumerate(numbers):
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
```

在这个例子中，我们导入了 Process ，并创建一个 **doubler** 函数。在这个函数中，我们将传入的数字扩大二倍。我们还用 Python 中的 **os** 模块得到当前进程的ID（或者说 pid）。这可以告诉我们哪个进程正在调用函数。代码底部的那个循环中，我们创建了一系列进程并启动它们。最下边的那个循环在每一个进程上调用了 **join()** 方法，它将告诉 Python 等待进程结束。如果你需要结束一个进程，你可以调用它的 **terminate()** 方法。

当运行这段代码的时候，你将看到类似下边这样的输出：

```
5 doubled to 10 by process id: 10468
10 doubled to 20 by process id: 10469
15 doubled to 30 by process id: 10470
20 doubled to 40 by process id: 10471
25 doubled to 50 by process id: 10472
```

有时候让进程有一个有可读性的名字会更好。幸运的是，Process 类支持给进程命名。让我们来看一下：

```python
import os

from multiprocessing import Process, current_process


def doubler(number):
    """
    A doubling function that can be used by a process
    """
    result = number * 2
    proc_name = current_process().name
    print('{0} doubled to {1} by: {2}'.format(
        number, result, proc_name))


if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    procs = []
    proc = Process(target=doubler, args=(5,))

    for index, number in enumerate(numbers):
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()

    proc = Process(target=doubler, name='Test', args=(2,))
    proc.start()
    procs.append(proc)

    for proc in procs:
        proc.join()
```

这一次，我们引入了一些其他东西： **current_process**。**current_process** 和 Threading 模块中的 **current_thread** 基本是一样的。我们用它来获取正在调用 doubler 函数的线程的名称。你可能注意到了，我们的前五个进程没有设置名字。第六个进程我们把它的名字设置为"Test"。我们看一下得到的输出：

```
5 doubled to 10 by: Process-2
10 doubled to 20 by: Process-3
15 doubled to 30 by: Process-4
20 doubled to 40 by: Process-5
25 doubled to 50 by: Process-6
2 doubled to 4 by: Test
```

输出显示，multiprocessing 模块默认为每一个进程的名字指派了一个数字。当然，我们设置名字的那个进程没有数字。

### 锁

Multiprocessing 模块和 Threading 模块一样，也支持“锁”。你需要做的就是 **import Lock**，获取它，执行操作后再释放它。我们来看一下：

```python
from multiprocessing import Process, Lock


def printer(item, lock):
    """
    Prints out the item that was passed in
    """
    lock.acquire()
    try:
        print(item)
    finally:
        lock.release()

if __name__ == '__main__':
    lock = Lock()
    items = ['tango', 'foxtrot', 10]
    for item in items:
        p = Process(target=printer, args=(item, lock))
        p.start()
```

这里我们创建了一个函数直接打印传递过来的任何东西。为了防止线程被其他事情干扰，我们用了一个 Lock 对象。这段代码将遍历我们列表中的三项内容，并分别为其创建一个进程。每个进程都会调用该函数，并将可迭代对象中的一个元素传入函数。因为我们用了锁，所以后边的进程将会等到锁释放之后才会继续执行。

## 日志

多进程的日志和多线程的日志有一点区别。原因是 Python 的 logging 包不支持进程共享锁，所以来自不同的进程的日志可能会混在一起。我们尝试一下在上边的例子里加一个基础日志。下边是代码：

```python
import logging
import multiprocessing

from multiprocessing import Process, Lock

def printer(item, lock):
    """
    Prints out the item that was passed in
    """
    lock.acquire()
    try:
        print(item)
    finally:
        lock.release()

if __name__ == '__main__':
    lock = Lock()
    items = ['tango', 'foxtrot', 10]
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    for item in items:
        p = Process(target=printer, args=(item, lock))
        p.start()
```

记录日志最简单的方法是将所有的日志发送给 stderr 。我们可以通过调用函数 **log_to_stderr** 来实现。然后我们调用 **get_logger** 函数得到记录器（logger），并把日志级别设置为 INFO。剩下的代码和原来一样。这里要说明一下，我并没有用 **join()** 函数。相反， 父线程在退出的时候要显式地调用 **join()**。

当你运行上边的代码，会得到像下面这样的输出：

```
[INFO/Process-1] child process calling self.run()
tango
[INFO/Process-1] process shutting down
[INFO/Process-1] process exiting with exitcode 0
[INFO/Process-2] child process calling self.run()
[INFO/MainProcess] process shutting down
foxtrot
[INFO/Process-2] process shutting down
[INFO/Process-3] child process calling self.run()
[INFO/Process-2] process exiting with exitcode 0
10
[INFO/MainProcess] calling join() for process Process-3
[INFO/Process-3] process shutting down
[INFO/Process-3] process exiting with exitcode 0
[INFO/MainProcess] calling join() for process Process-2
```

现在你如果想把日志保存到硬盘，其实还有有些复杂的。你可以参考[ Python 的官方实例](https://docs.python.org/3/howto/logging-cookbook.html#logging-to-a-single-file-from-multiple-processes)。

## Pool 类

Pool 类用于表示一个工作进程的池子。它有一些方法可以让你将任务分配给不同的工作进程。我们看一下这个简单的例子：

```python
from multiprocessing import Pool

def doubler(number):
    return number * 2

if __name__ == '__main__':
    numbers = [5, 10, 20]
    pool = Pool(processes=3)
    print(pool.map(doubler, numbers))
```

在这里，我们创建了一个 Pool 的实例并且告诉它创建三个工作进程。然后我们用 **map** 方法映射一个函数和一个可迭代对象到每一个进程。最后，我们打印出来结果，这里的结果是一个列表：**[10, 20, 40]**。

我们同样可以通过 **apply_async** 方法得到程序的结果：

```python
from multiprocessing import Pool

def doubler(number):
    return number * 2

if __name__ == '__main__':
    pool = Pool(processes=3)
    result = pool.apply_async(doubler, (25,))
    print(result.get(timeout=1))
```

这样做可以让我们得到进程的结果， **get** 函数的功能就是这个。你可能会注意到，我们加了一个超时（timeout）的设置，这是为了防止我们调用的函数发生意外。我们不想让它无限期的被阻塞。

## 进程通信

如果想让两个进程通信， multiprocessing 模块提供了两个主要方法： Queues 和 Pipes。Queue 保证了线程和进程的安全。另一篇[关于线程的文章](http://www.blog.pythonlibrary.org/2016/07/28/python-201-a-tutorial-on-threads/)中也有一个 Queue 实现，我们在此基础上做些修改：

```python
from multiprocessing import Process, Queue

sentinel = -1

def creator(data, q):
    """
    Creates data to be consumed and waits for the consumer
    to finish processing
    """
    print('Creating data and putting it on the queue')
    for item in data:

        q.put(item)


def my_consumer(q):
    """
    Consumes some data and works on it

    In this case, all it does is double the input
    """
    while True:
        data = q.get()
        print('data found to be processed: {}'.format(data))
        processed = data * 2
        print(processed)

        if data is sentinel:
            break


if __name__ == '__main__':
    q = Queue()
    data = [5, 10, 13, -1]
    process_one = Process(target=creator, args=(data, q))
    process_two = Process(target=my_consumer, args=(q,))
    process_one.start()
    process_two.start()

    q.close()
    q.join_thread()

    process_one.join()
    process_two.join()
```

我们需要导入 Queue 和 Process。然后我们创建两个函数，一个创建数据并把它们加入队列里边，另一个取出数据并处理它们。把数据加入队列使用的是 Queue 的 **put()** 方法，取出数据用的是 **get()** 方法。最后一段代码创建了一个队列对象和一些进程，并运行它们。请注意，我们是在进程对象上调用了 **join()** 方法而不是在 Queue自身中。

## 结束语

本文讲述了很多内容。你已经学习了怎么对函数使用多进程，用队列实现进程间的通信，给线程命名等等。在 Python 的官方文档里边还有很多内容在本文里没有涉及到，你也可以去更深入的研究一下。不过现在你已经学会如何通过 Python 利用你的计算机的全部处理性能啦。

## 相关阅读

[Python 官方文档：multiprocessing](https://docs.python.org/3/library/multiprocessing.html)

[Python Module of the Week: multiprocessing ](https://pymotw.com/2/multiprocessing/)

[Python Concurrency – Porting a Queue to multiprocessing](http://www.blog.pythonlibrary.org/2012/08/03/python-concurrency-porting-from-a-queue-to-multiprocessing/)

***

[点此查看原文链接](http://www.blog.pythonlibrary.org/2016/08/02/python-201-a-multiprocessing-tutorial/)。

[Python 翻译组](https://github.com/PythonTG)是EarlGrey@编程派发起成立的一个专注于 Python 技术内容翻译的小组，目前已有近 30 名 Python 技术爱好者加入。

翻译组出品的内容（包括教程、文档、书籍、视频）将在编程派微信公众号首发，欢迎各位 Python 爱好者推荐相关线索。

推荐线索，可直接在编程派微信公众号推文下留言即可。
