# 用 Python 和 Asyncio 编写多人在线游戏（一）

title: 用 Python 和 Asyncio 编写多人在线游戏（一）
author: Kyrylo Subbotin
translator: sleepyjoker
reviewer: EarlGrey
date: 20160811
permalink: writing-online-multiplayer-game-with-python-part-one
keywords: asyncio教程, asyncio游戏, python游戏, python多人游戏, python websockets, 游戏开发, python教程

***

之前 PythonTG 翻译组分享过一篇 Pygame 的入门教程，教的是单机游戏开发。今天和大家分享如何编写一个多人在线游戏，此教程共分为三部分，今天是第一篇，为大致概述。有兴趣的朋友请继续关注后续文章。

本文作者为 Kyrylo Subbotin，是一家 IT 咨询公司的 Python 工程师。本文译者为 sleepyjoker，由编程派作者 EarlGrey 校对。

译者简介：sleepyjoker，东南大学电子科学与工程专业大二学生。虽然暂时还是python菜鸟，但喜欢通过代码完成各种有意思的事。

以下是正文：


** 你有没有试过 Python 的异步操作?我将通过一个支持多人的游戏[实例](http://snakepit-game.com/)——贪吃蛇，来教你如何使用它。 **

[玩游戏](http://snakepit-game.com/)

## 1.介绍

毫无疑问，大规模多人在线游戏（MMOG）无论在技术还是文化领域，都是当今时代的潮流。很长一段时间以来，为了给 MMO 游戏编写服务器，我们得投入高昂的预算，而且得使用复杂的底层编程技术。直到最近几年，事情出现了转机。基于动态编程语言的现代化框架支持在一般硬件上处理成千上万的用户并行连接。与此同时，HTML5 和 WebSockets 标准使得创造一个实时的图形客户端成为可能，而且不需要任何插件，就能直接运行在浏览器上。

Python 可能并不是创建可扩展不阻塞服务最为流行的工具，尤其是相较于 node.js 而言。但最新版本的 Python 有望改变这一点。[asyncio](https://docs.python.org/3/whatsnew/3.5.html#whatsnew-pep-492) 标准库和一个特殊的 [async/await](https://docs.python.org/3/whatsnew/3.5.html#whatsnew-pep-492)语法的引入，使得异步代码和常规的易阻塞代码一样简洁明了，这使得用 Python 来完成一个异步程序成为了一个不错的选择。基于此，我将试着利用这些新特性来展示如何编写多人在线游戏。

## 2.实现异步

一个游戏服务器需要实时处理大量的并行连接。传统的做法是使用多线程，不过在这里却没有什么意义。运行上千个线程意味着需要 CPU 在不同线程间不停的切换（即上下文切换（context switching））。这将产生巨大的开销，从而导致程序的低效。更糟糕的是使用多进程，因为它们还会占用过多的内存。

并且对于 Python，还有一个问题就是常规的 Python 解释器（CPython）是为达到单线程的最佳性能而非多线程操作而设计的。这也就是为什么需要全局解释器锁（GIL）。全局解释器锁是一种防止 Python 代码中多个线程同时运行互相竞争的机制，以避免某个共享对象出现不可控的情况。正常情况下，如果当前的线程在等待某一事件，通常是 I/O 的响应（类似于服务器的响应），解释器便会切换到另一个线程，从而使得一个阻塞的 I/O 只会影响一个线程而不是整个服务器，以保证程序的 I/O 操作畅通无阻。然而，即便是在多核 CPU 上也无法并行执行的 Python 代码，将导致常规的多线程思想一无是处。当然，通过实现无阻塞的单线程来消除沉重的上下文切换负担是完全有可能的。

事实上，实现无阻塞的单线程程序是你在纯 Pyhton 代码中可以做到的。你只需要一个标准的 [select](https://docs.python.org/2/library/select.html) 模块，就能实现事件轮询来监听无阻塞的 I/O 套接字。但是，这就要求你把所有的程序逻辑上定义在一个地方，因此很快你的应用程序将变成复杂的状态机。现有很多流行的框架，如 [tornado](http://www.tornadoweb.org/en/stable/) 和 [twisted](http://twistedmatrix.com/trac/) 可以简化这个工作。它们被用于实现那些带有回调机制的复杂协议（这点和 node.js 是类似的）。这些框架运行自己的事件轮询，以便在你所定义的动作发生时做出反馈。对一些程序来说，这的确是可行的。但仍有弊端，就是在框架下你必须编写易造成代码互相割裂的回调风格的程序。与之相比，我们将要编写的异步代码可以像普通的多线程那样，并发运行多个复制版本。在单线程的程序中，这一点是如何实现的呢？

这就需要引入微线程的概念，目的是实现单线程中并发执行任务。当某个任务中调用的函数被阻塞了，后台将调用“管理员（manager）”（或者叫“计划员（scheduler）”）来运行一个事件轮询。如果有某个事件已经可以运行，管理员将会把运行权交给正在等待该事件的任务。这个任务将一直执行，直到又遇到阻塞，这时运行权将重新交还管理员。

> 微线程又被称为lightweight threads 或green threads。在伪线程中并发运行的任务被称为 tasklets，greenlets，或是 coroutines。

Python 中第一个实现微线程的是 [Stackless Python](https://bitbucket.org/stackless-dev/stackless/wiki/Home)。它因被成功用于在线游戏 [EVE online](https://www.eveonline.com) 而闻名。这款多人在线游戏展现了一个永恒的宇宙，其中有成千上万的玩家参与不同的活动，而这一切都是实时发生的。Stackless 是一个独立的 Python 解释器，取代了标准的函数调用栈来直接控制流对象，从而实现最小的上下文切换开销。尽管非常高效，但这种解决方案不如兼容标准解释器的其他库受欢迎。像 [eventlet](http://eventlet.net) 和 [gevent](http://www.gevent.org) 这样的软件包带有标准 I/O 库补丁包，这样 I/O 函数也能给它们内部的事件轮询。这样就可以通过很简单的方式把原本阻塞的函数变成不阻塞的。副作用就是在代码中无法明显的体现无阻塞性。新版本的 Python 引入了一种由高级生成器来实现、更为自然的协程。在 Python3.4 之后的各个版本中，都包含了 [asyncio](https://docs.python.org/3/library/asyncio.html) 库，可以由原生的协程来提供单线程的并发。在 Python3.5 中，协程才成为了 Python 语言整体的一部分，并加入了新的关键字 `async` 和 `await`。

下面是一个简单的例子，阐明了如何使用 `asyncio` 来运行并发任务：

```python
import asyncio
async def my_task(seconds):
    print("start sleeping for {} seconds".format(seconds))
    await asyncio.sleep(seconds)
    print("end sleeping for {} seconds".format(seconds))

all_tasks = asyncio.gather(my_task(1),my_task(2))
loop = asyncio.get_event_loop()
loop.run_until_complete(all_tasks)
loop.close()
```

我们载入了两个任务，其中一个是睡眠一秒，另一个是睡眠两秒。输出结果为：

```
start sleeping for 1 seconds
start sleeping for 2 seconds
end sleeping for 1 seconds
end sleeping for 2 seconds
```

正如你所见，协程间并没有互相阻塞——第二个任务在第一个任务结束前就开始了，这是因为 `asyncio.sleep` 在给定时间过后返回了运行权给计划员。在下一篇中，我们将利用基于协程的任务来创建游戏的循环。

***

[点此查看原文链接](https://7webpages.com/blog/writing-online-multiplayer-game-with-python-asyncio-getting-asynchronous/)。

[Python 翻译组](https://github.com/PythonTG)是EarlGrey@编程派发起成立的一个专注于 Python 技术内容翻译的小组，目前已有近 30 名 Python 技术爱好者加入。

翻译组出品的内容（包括教程、文档、书籍、视频）将在编程派微信公众号首发，欢迎各位 Python 爱好者推荐相关线索。

推荐线索，可直接在编程派微信公众号推文下留言即可。









