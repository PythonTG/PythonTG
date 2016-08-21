# 一文学会Python多线程编程

title: 一文学会 Python 多线程编程
author: Michael Driscoll
translator: linkcheng
reviewer: EarlGrey
date: 20160819
permalink: python-201-a-tutorial-on-threads
keywords: python线程库, python多线程, threading模块, 多线程模块, I/O密集型操作, 主线程, python教程

***

> 本文作者为 Michael Driscool，是其新书 Python 201 的一节。本文译者为 linkcheng，由EarlGrey@编程派校对。译者简介：linkcheng，专业电子信息工程。已有两年工作经验，从事 c/c++ 开发。目前在学习 flask，希望以后自己可以搭建网站。

**Threading** 模块从 Python 1.5.2 版开始出现，用于增强底层的多线程模块 **thread** 。Threading 模块让操作多线程变得更简单，并且支持程序同时运行多个操作。

注意，**Python 中的多线程最好用于处理有关 I/O 的操作**，如从网上下载资源或者从本地读取文件或者目录。如果你要做的是 CPU 密集型操作，那么你需要使用 Python 的 **multiprocessing** 模块。这样做的原因是，Python 有一个全局解释器锁 (GIL)，使得所有子线程都必须运行在同一个主线程中。正因为如此，当你通过多线程来处理多个 CPU 密集型任务时，你会发现它实际上运行的更慢。因此，我们将重点放在那些多线程最擅长的领域：I/O 操作！

## 线程简介

多线程能让你像运行一个独立的程序一样运行一段长代码。这有点像调用子进程（subprocess），不过区别是你调用的是一个函数或者一个类，而不是独立的程序。在我看来，举例说明更有助于解释。下面来看一个简单的例子：

```python
import threading
 
 
def doubler(number):
    """
    可以被线程使用的一个函数
    """
    print(threading.currentThread().getName() + '\n')
    print(number * 2)
    print()
 
 
if __name__ == '__main__':
    for i in range(5):
        my_thread = threading.Thread(target=doubler, args=(i,))
        my_thread.start()
```

这里，我们导入 threading 模块并且创建一个叫 **doubler** 的常规函数。这个函数接受一个值，然后把这个值翻一番。它还会打印出调用这个函数的线程的名称，并在最后打印一行空行。然后在代码的最后一块，我们创建五个线程并且依次启动它们。在我们实例化一个线程时，你会注意到，我们把 doubler 函数传给 **target** 参数，同时也给 doubler 函数传递了参数。**Args** 参数看起来有些奇怪，那是因为我们需要传递一个序列给 doubler 函数，但它只接受一个变量，所以我们把逗号放在尾部来创建只有一个参数的序列。

需要注意的是，如果你想等待一个线程结束，那么需要调用 **join()** 方法。

当你运行以上这段代码，会得到以下输出内容：

```
Thread-1
 
0
 
Thread-2
 
2
 
Thread-3
 
4
 
Thread-4
 
6
 
Thread-5
 
8
```

当然，通常情况下你不会希望输出打印到标准输出。如果不幸真的这么做了，那么最终的显示效果将会非常混乱。你应该使用 Python 的 logging 模块。它是线程安全的，并且表现出色。让我们用 **logging** 模块修改上面的例子并且给我们的线程命名。代码如下：

```python
import logging
import threading
 
def get_logger():
    logger = logging.getLogger("threading_example")
    logger.setLevel(logging.DEBUG)
 
    fh = logging.FileHandler("threading.log")
    fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)
 
    logger.addHandler(fh)
    return logger
 
 
def doubler(number, logger):
    """
    可以被线程使用的一个函数
    """
    logger.debug('doubler function executing')
    result = number * 2
    logger.debug('doubler function ended with: {}'.format(
        result))
 
 
if __name__ == '__main__':
    logger = get_logger()
    thread_names = ['Mike', 'George', 'Wanda', 'Dingbat', 'Nina']
    for i in range(5):
        my_thread = threading.Thread(
            target=doubler, name=thread_names[i], args=(i,logger))
        my_thread.start()
```

代码中最大的改变就是加入了 **get_logger** 函数。这段代码将创建一个被设置为调试级别的日志记录器。它将日志保存在当前目录（即脚本运行所在的目录）下，然后设置每行日志的格式。格式包括时间戳、线程名、日志记录级别以及日志信息。

在 doubler 函数中，我们把 **print** 语句换成 logging 语句。你会注发现，在创建线程时，我们给 doubler 函数传入了 logger 对象。这样做的原因是，如果在每个线程中实例化 logging 对象，那么将会产生多个 logging 单例（singleton），并且日志中将会有很多重复的内容。

最后，创建一个名称列表，然后使用 **name** 关键字参数为每一个线程设置具体名称，这样就可以为线程命名。运行以上代码，将会得到包含以下内容的日志文件：

```
2016-07-24 20:39:50,055 - Mike - DEBUG - doubler function executing
2016-07-24 20:39:50,055 - Mike - DEBUG - doubler function ended with: 0
2016-07-24 20:39:50,055 - George - DEBUG - doubler function executing
2016-07-24 20:39:50,056 - George - DEBUG - doubler function ended with: 2
2016-07-24 20:39:50,056 - Wanda - DEBUG - doubler function executing
2016-07-24 20:39:50,056 - Wanda - DEBUG - doubler function ended with: 4
2016-07-24 20:39:50,056 - Dingbat - DEBUG - doubler function executing
2016-07-24 20:39:50,057 - Dingbat - DEBUG - doubler function ended with: 6
2016-07-24 20:39:50,057 - Nina - DEBUG - doubler function executing
2016-07-24 20:39:50,057 - Nina - DEBUG - doubler function ended with: 8
```

输出结果不言自明，所以继续介绍其他内容。在本节中再多说一点，即通过继承 **threading.Thread** 实现多线程。举最后一个例子，通过继承 threading.Thread 创建子类，而不是直接调用 Thread 函数。

更新后的代码如下：

```python
import logging
import threading
 
class MyThread(threading.Thread):
 
    def __init__(self, number, logger):
        threading.Thread.__init__(self)
        self.number = number
        self.logger = logger
 
    def run(self):
        """
        运行线程
        """
        logger.debug('Calling doubler')
        doubler(self.number, self.logger)
 
 
def get_logger():
    logger = logging.getLogger("threading_example")
    logger.setLevel(logging.DEBUG)
 
    fh = logging.FileHandler("threading_class.log")
    fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)
 
    logger.addHandler(fh)
    return logger
 
 
def doubler(number, logger):
    """
    可以被线程使用的一个函数
    """
    logger.debug('doubler function executing')
    result = number * 2
    logger.debug('doubler function ended with: {}'.format(
        result))
 
 
if __name__ == '__main__':
    logger = get_logger()
    thread_names = ['Mike', 'George', 'Wanda', 'Dingbat', 'Nina']
    for i in range(5):
        thread = MyThread(i, logger)
        thread.setName(thread_names[i])
        thread.start()
```

这个例子中，我们只是创建一个继承于 **threading.Thread** 的子类。像之前一样，传入一个需要翻一番的数字，以及 logging 对象。但是这次，设置线程名称的方式有点不太一样，变成了通过调用 thread 对象的 **setName** 方法来设置。不过仍然需要调用 **start** 来启动线程，不过你可能注意到我们并不需要在子类中定义该方法。当调用 **start** 时，它会通过调用 **run** 方法来启动线程。在我们的类中，我们调用 doubler 函数来做处理。输出结果中除了一些添加的额外信息内容几乎差不多。运行下这个脚本，看看你会得到什么。

## 线程锁与线程同步

当你有多个线程，就需要考虑怎样避免线程冲突。我的意思是说，你可能遇到多个线程同时访问同一资源的情况。如果不考虑这些问题并且制定相应的解决方案，那么在开发产品过程中，你总会在最糟糕的时候遇到这些棘手的问题。

解决办法就是使用线程锁。锁由 Python 的 threading 模块提供，并且它最多被一个线程所持有。当一个线程试图获取一个已经锁在资源上的锁时，该线程通常会暂停运行，直到这个锁被释放。来让我们看一个非常典型没有却应具备锁功能的例子：

```python
import threading
 
total = 0
 
def update_total(amount):
    """
    Updates the total by the given amount
    """
    global total
    total += amount
    print (total)
 
if __name__ == '__main__':
    for i in range(10):
        my_thread = threading.Thread(
            target=update_total, args=(5,))
        my_thread.start()
```

如果往以上代码添加 **time.sleep** 函数并给出不同长度的时间，可能会让这个例子更有意思。无论如何，这里的问题是，一个线程可能已经调用 **update_total** 函数并且还没有更新完成，此时另一个线程也有可能调用它并且尝试更新内容。根据操作执行顺序的不同，该值可能只被增加一次。

让我们给这个函数添加锁。有两种方法可以实现。第一种方式是使用 **try/finally** ，从而确保锁肯定会被释放。下面是示例：

```python
import threading
 
total = 0
lock = threading.Lock()
 
def update_total(amount):
    """
    Updates the total by the given amount
    """
    global total
    lock.acquire()
    try:
        total += amount
    finally:
        lock.release()
    print (total)
 
if __name__ == '__main__':
    for i in range(10):
        my_thread = threading.Thread(
            target=update_total, args=(5,))
        my_thread.start()
```

如上，在我们做任何处理之前就获取锁。然后尝试更新 total 的值，最后释放锁并打印出 total 的当前值。事实上，我们可以使用 Python 的 **with** 语句避免使用 try/finally 这种较为繁琐的语句：

```python
import threading
 
total = 0
lock = threading.Lock()
 
def update_total(amount):
    """
    Updates the total by the given amount
    """
    global total
    with lock:
        total += amount
    print (total)
 
if __name__ == '__main__':
    for i in range(10):
        my_thread = threading.Thread(
            target=update_total, args=(5,))
        my_thread.start()
```

正如你看到的那样，我们不再需要 **try/finally** 作为上下文管理器，而是由 **with** 语句作为替代。

当然你也会遇到要在代码中通过多个线程访问多个函数的情况。当你第一次编写并发代码时，代码可能是这样的：

```python
import threading
 
total = 0
lock = threading.Lock()
 
 
def do_something():
    lock.acquire()
 
    try:
        print('Lock acquired in the do_something function')
    finally:
        lock.release()
        print('Lock released in the do_something function')
 
    return "Done doing something"
 
def do_something_else():
    lock.acquire()
 
    try:
        print('Lock acquired in the do_something_else function')
    finally:
        lock.release()
        print('Lock released in the do_something_else function')
 
    return "Finished something else"
 
if __name__ == '__main__':
	result_one = do_something()
	result_two = do_something_else()
```

这样的代码在上面的情况下能够正常工作，但假设你有多个线程都调用这两个函数呢。当一个线程正在运行这两个函数，然后另外一个线程也可能会修改这些数据，最后得到的就是不正确的结果。问题是，你甚至可能没有马上意识到结果错了。有什么解决办法呢？让我们试着找出答案。

通常首先想到的就是在调用这两个函数的地方上锁。让我们试着修改上面的例子，修改成如下所示：

```python
import threading
 
total = 0
lock = threading.RLock()
 
def do_something():
 
    with lock:
        print('Lock acquired in the do_something function')
    print('Lock released in the do_something function')
 
    return "Done doing something"
 
def do_something_else():
    with lock:
        print('Lock acquired in the do_something_else function')
    print('Lock released in the do_something_else function')
 
    return "Finished something else"
 
 
def main():
    with lock:
        result_one = do_something()
        result_two = do_something_else()
 
    print (result_one)
    print (result_two)
 
if __name__ == '__main__':
    main()
```

当你真正运行这段代码时，你会发现它只是挂起了。究其原因，是因为我们只告诉 threading 模块获取锁。所以当我们调用第一个函数时，它发现锁已经被获取，随后便把自己挂起了，直到锁被释放，然而这将永远不会发生。

真正的解决办法是使用**重入锁（Re-Entrant Lock）**。threading 模块提供的解决办法是使用 **RLock** 函数。即把 **lock = threading.lock()** 替换为 **lock = threading.RLock()**，然后重新运行代码，现在代码就可以正常运行了。

如果你想在线程中运行以上代码，那么你可以用以下代码取代直接调用 **main** 函数：

```python
if __name__ == '__main__':
    for i in range(10):
        my_thread = threading.Thread(
            target=main)
        my_thread.start()
```

每个线程都会运行 main 函数，main 函数则会依次调用另外两个函数。最终也会产生 10 组结果集。

## 定时器

Threading 模块有一个优雅的 **Timer** 类，你可以用它来实现在指定时间后要发生的动作。它们实际上会启动自己的自定义线程，通过调用常规线程上的 **start()** 方法即可运行。你也可以调用它的 **cancel** 方法停止定时器。值得注意的是，你甚至可以在开始定时器之前取消它。

有一天，我遇到一个特殊的情况：我需要与已经启动的子进程通信，但是我需要它有超时处理。虽然处理这种特殊问题有很多不同的方法，不过我最喜欢的解决方案是使用 threading 模块的 Timer 类。

在下面这个例子中，我们将使用 **ping** 指令作为演示。在 Linux 系统中，ping 命令会一直运行下去直到你手动杀死它。所以在 Linux 世界里，Timer 类就显得非常方便。示例如下：

```python
import subprocess
 
from threading import Timer
 
kill = lambda process: process.kill()
cmd = ['ping', 'www.google.com']
ping = subprocess.Popen(
    cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
 
my_timer = Timer(5, kill, [ping])
 
try:
    my_timer.start()
    stdout, stderr = ping.communicate()
finally:
    my_timer.cancel()
 
print (str(stdout))
```

这里我们在 lambda 表达式中调用 kill 杀死进程。接下来启动 ping 命令，然后创建 Timer 对象。你会注意到，第一个参数就是需要等待的秒数，第二个参数是需要调用的函数，紧跟其后的参数是要调用函数的入参。在本例中，我们的函数是一个 lambda 表达式，传入的是一个只有一个元素的列表。如果你运行这段代码，它应该会运行 5 秒钟，然后打印出 ping 的结果。

## 其他线程组件

Threading 模块包含对其他功能的支持。例如，你可以创建信号量（**Semaphore**），这是计算机科学中最古老的同步原语之一。基本上，一个信号量管理一个内置的计数器。当你调用 **acquire** 时计数器就会**递减**，相反当你调用 **release** 时就会**递增**。根据其设计，计数器的值无法小于零，所以如果正好在计数器为零时调用 acquire 方法，该方法将阻塞线程。

> 译者注：通常使用信号量时都会初始化一个大于零的值，如 semaphore = threading.Semaphore(2)

另一个非常有用的同步工具就是事件（**Event**）。它允许你使用信号（signal）实现线程通信。在下一节中我们将举一个使用事件的实例。

最后，在 Python 3.2 中加入了 **Barrier** 对象。Barrier 是管理线程池中的同步原语，在线程池中多条线程需要相互等待对方。如果要传递 barrier，每一条线程都要调用 **wait()** 方法，在其他线程调用该方法之前线程将会阻塞。全部调用之后将会同时释放所有线程。

## 线程通信

某些情况下，你会希望线程之间互相通信。就像先前提到的，你可以通过创建 **Event** 对象达到这个目的。但更常用的方法是使用队列（**Queue**）。在我们的例子中，这两种方式都会有所涉及。下面让我们看看到底是什么样子的：

```python
import threading
 
from queue import Queue
 
 
def creator(data, q):
    """
    生成用于消费的数据，等待消费者完成处理
    """
    print('Creating data and putting it on the queue')
    for item in data:
        evt = threading.Event()
        q.put((item, evt))
 
        print('Waiting for data to be doubled')
        evt.wait()
 
 
def my_consumer(q):
    """
    消费部分数据，并做处理

    这里所做的只是将输入翻一倍
 
    """
    while True:
        data, evt = q.get()
        print('data found to be processed: {}'.format(data))
        processed = data * 2
        print(processed)
        evt.set()
        q.task_done()
 
 
if __name__ == '__main__':
    q = Queue()
    data = [5, 10, 13, -1]
    thread_one = threading.Thread(target=creator, args=(data, q))
    thread_two = threading.Thread(target=my_consumer, args=(q,))
    thread_one.start()
    thread_two.start()
 
    q.join()
```

让我们掰开揉碎分析一下。首先，我们有一个创建者（creator）函数（亦称作生产者（producer）），我们用它来创建想要操作（或者消费）的数据。然后用另外一个函数 **my_consumer** 来处理刚才创建出来的数据。Creator 函数使用 Queue 的 **put** 方法向队列中插入数据，消费者将会持续不断的检测有没有更多的数据，当发现有数据时就会处理数据。Queue 对象处理所有的获取锁和释放锁的过程，这些不用我们太关心。

在这个例子中，先创建一个列表，然后创建两个线程，一个用作生产者，一个作为消费者。你会发现，我们给两个线程都传递了 Queue 对象，这两个线程隐藏了关于锁处理的细节。队列实现了数据从第一个线程到第二个线程的传递。当第一个线程把数据放入队列时，同时也传递一个 Event 事件，紧接着挂起自己，等待该事件结束。在消费者侧，也就是第二个线程，则做数据处理工作。当完成数据处理后就会调用 Event 事件的 **set** 方法，通知第一个线程已经把数据处理完毕了，可以继续生产了。

最后一行代码调用了 Queue 对象的 **join** 方法，它会告知 Queue 等待所有线程结束。当第一个线程把所有数据都放到队列中，它也就运行结束了。

## 结束语

以上涵盖了关于线程的诸多方面，主要包括：

* 线程基础知识
* 锁的工作方式
* 什么是事件以及如何使用
* 如何使用定时器
* 通过 Queues/Events 实现线程间通信

现在你们知道如何使用线程以及线程擅长什么了，希望在你们的代码中能有它们的用武之地。

## 相关阅读

* [Threading 模块](https://docs.python.org/3/library/threading.html)的 Python 文档
* Eli Bendersky – [Python 线程：通信与停止](http://eli.thegreenplace.net/2011/12/27/python-threads-communication-and-stopping)

***

[点此查看原文链接](http://www.blog.pythonlibrary.org/2016/07/28/python-201-a-tutorial-on-threads/)。

[Python 翻译组](https://github.com/PythonTG)是EarlGrey@编程派发起成立的一个专注于 Python 技术内容翻译的小组，目前已有近 30 名 Python 技术爱好者加入。

翻译组出品的内容（包括教程、文档、书籍、视频）将在编程派微信公众号首发，欢迎各位 Python 爱好者推荐相关线索。

推荐线索，可直接在编程派微信公众号推文下留言即可。