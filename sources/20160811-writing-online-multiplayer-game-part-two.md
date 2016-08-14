# 用 Python 和 asyncio 来编写多人在线游戏(第二部分)

title: 码农用Python写了个机器人，租到了满意的房子
author: Kyrylo Subbotin
translator: sleepyjoker
reviewer: EarlGrey
date: 20160811
permalink: writing-online-multiplayer-game-with-python-part-two
keywords: asyncio教程, asyncio游戏, python游戏, python多人游戏, python websockets, 游戏开发, python教程

***

## 3.编写游戏中的循环

游戏循环是每一个游戏的核心。它不断地接收玩家的输入，更新游戏的状态，然后把结果渲染到屏幕上。在线游戏中，这个循环被分成服务端和客户端两部分，两部分通过网络来通信。通常由客户端来获取玩家的输入，例如按键或者鼠标移动，然后传递数据给服务端，并将并返回的数据展现出来。服务端处理来自所有玩家的数据，更新玩家的状态，进行必要的计算来渲染下一帧，并返回结果，比如一个对象在游戏中的新位置。没有必要的原因，千万不要混淆服务端与客户端。如果把游戏中的逻辑计算放在客户端，你会无法与其它客户端同步，而且你的游戏将能够根据客户端传递的数据来轻易的创建。

> 游戏循环迭代常常被称为 tick。Tick 是一个事件，表示当前循环迭代已经完成，用于下一个画面的数据已经准备好了。

在接下来的例子中，我们将使用同一个客户端，通过 WebSocket 连接服务器。客户端上上运行了一个简单的循环，来传递按键给服务端，同时展示所有来自服务端的数据。[点此查看客户端源码](https://github.com/7WebPages/snakepit-game/blob/master/simple/index.html)

## 例 3.1：基本游戏循环

> [例3.1源代码](https://github.com/7WebPages/snakepit-game/blob/master/simple/game_loop_basic.py)

我们将使用 [aiohttp](http://aiohttp.readthedocs.io/en/stable/) 库来创建一个游戏服务端。它允许我们通过 `asyncio` 来创建网络服务端和客户端。这个库的优点就是同时支持普通的 http 请求和套接字。所以我们不需要其它的网页服务器来渲染游戏的 html 页面。

下面展示了我们如何运行服务端：

```python
app ＝ web.Application()
app["sockets"] = []

asyncio.ensure_future(game_loop(app))

app.router.add_route('GET','/connect',wshandler)
app.router.add_route('GET','/',handle)

web.run_app(app)
```
		
`web.run_app` 是一个很方便的快捷方法，可以快速创建服务端的主任务，并使用其 `run_forever()` 方法运行 `asyncio` 的事件轮询。我建议你检查一下这个方法的源代码，去看看服务端究竟是如何建立和终止的。

`app` 是一个类似于字典的对象，可以用于在相互连接的客户端之间分享数据。我们将用它来存储套接字列表，这个列表将被用于向所有已连接的客户端发送消息。调用函数 `asyncio.ensure_future()` 可以安排我们的主循环 `game_loop` 任务，每两秒就向客户端发送一次“tick”信号。这项任务会与网络服务端在同一个 `asyncio` 事件轮询中并发执行。

有两个网络请求处理器：`handle` 只负责提供 html 页面，`wshandle` 是我们的网络套接字任务，负责处理与客户端的交互。每一个已连接的客户端都会加载一个新的 `wshandle` 进入事件轮询。这个任务会把客户端的套接字加入列表，因此 `game_loop` 可以发送信息给每一个客户端。然后，它会把每一次按键信息返回给客户端，并输出相应的消息。

在启动的任务中，我们在 `asyncio` 的主事件轮询中运行工作者轮询。当其中某个工作者使用 `await` 语句等待协程完成时，就会切换为另一个工作者任务。例如，经过一定时间后，`asyncio.sleep` 就会将执行交还给调度器，而 `ws.receive()` 则会等待来自套接字的信息，同时调度器会切换至其他任务。

在你用浏览器打开主页并连上服务器后，可以试着按键。它们所代表的字码将会由服务端输出并返回。返回给客户端的消息每两秒被游戏循环中的 `tick` 消息重写一次。

现在，我们已经创建好了可以处理用户按键的服务端，主循环将在后台工作，并周期性地更新所有客户端。

## 例 3.2：请求开始游戏轮询

> [例 3.2源码](https://github.com/7WebPages/snakepit-game/blob/master/simple/game_loop_handler.py)

之前的例子中，一个游戏循环在整个服务端的生命周期中不断的运行。但实际上，没有人连接的时候运行游戏循环没什么意义。并且，在服务端可能会有不同的“房间”。这个概念指的是，一个玩家“创建”游戏会话（例如多人游戏的竞赛或是一次在线游戏的突袭行动），其他的玩家加入进来。这样的话，游戏循环是在游戏会话继续的时候运行。

本例中我们使用一个全局标志来确认游戏循环是否正在运行，并在第一个玩家连接进来时开始运行。最初的时候，游戏循环不运行，所以这个标志被设置为 `False`。游戏循环是由客户端的处理器启动的：

```python
if app["game_is_running"] == False:
	asyncio.ensure_future(game_loop(app))
```

在 `game_loop()` 开始时，这个标志被设置为 `True`。最终，当所有玩家都断开时，再次被设置为 `False`。

## 例 3.3：管理任务

> [例 3.3](https://github.com/7WebPages/snakepit-game/blob/master/simple/game_loop_global.py)

本例介绍了如何处理任务对象。我们不存储一个标志，而是把游戏循环的任务直接存储在应用程序的全局字典中。情况简单的话，这样也许不是最佳的选择，但是有时候你可能需要去处理一些已经加载好的任务。

```python
if app["game_loop"] is None or app["game_loop"].cancelled():
	app["game_loop"] = asyncio.ensure_future(game_loop(app))
```

这里 `ensure_future()` 返回我们存储在全局字典中的任务对象；当所有用户都断开后，我们取消它：

```python	
app["game_llop"].cancel()
```

`cancel()` 函数告诉调度器不要把运行权再交给这个协程，并把它的状态设置为 `cancelled`，稍后可以用 `cancelled()` 方法来检查这个状态。有一点要提醒：如果任务对象有外部引用，在任务出现异常时并不会引发异常，而是在任务中设置该异常，可通过 `exception()` 方法检验。这样静悄悄地运行失败对于代码调试并不利。所以我们需要引发所有的异常。为此，你只需要显式地调用未完成任务的 `result()` 方法即可，可以使用回调对象实现：
	 
```python	
app["game_loop"].add_done_callback(lambda t: t.result())
```

如果我们想取消这个任务，但又不想引发 `CancelledError` ，可以考虑检查其  `“cancelled”` 状态：

```python
app["game_loop"].add_done_callback(lambda t: t.result() if not t.cancelled() else None)
```

注意，只有当你已经存储了任务对象的引用时才需要这么做。在前面的例子中，所有的异常都是直接引发，而不是使用额外的回调对象。

## 例 3.4：等待多个事件

> [例 3.4源码](https://github.com/7WebPages/snakepit-game/blob/master/simple/game_loop_wait.py)

很多时候，你需要在客户端的处理器等待多个事件。除了来自客户端的信息，你可能还会等待不同类型的事件。举个例子：如果游戏时间有限制，你就可能要等待一个来自计时器的信号。或者你要等待来自其他进程用管道传来的信息。又或者是使用了分布式系统，等待来自网络上其他服务器的消息。

简单起见，本例基于例 3.1 实现。但是在本例中，我们将会使用 `Condition` 对象来同步已连接客户端的游戏循环。因为我们只需要在处理器使用套接字，所以这里不需要套接字的全局列表。当游戏循环迭代结束时，我们使用 `Condition.notify_all()` 方法通知所有的客户端。这个方法支持在 `asyncio`的事件轮询中实现发布/订阅模式。

如需在处理器中等待两个事件，我们首先用 `ensure_future()` 把可用的对象打包进一个任务中。

```python
if not recv_task:
	recv_task = asyncio.ensure_future(ws.receive())
if not tick_task:
	await tick.acquire()
	tick_task = asyncio.ensure_future(tick.wait())
```

在我们调用 `Condition.wait()` 之前，我们需要获取它背后的锁。这就是为什么我们先调用了 `tick.wait()`。这个锁将会在调用了 `tick.wait()` 后释放，好让其他的协程也可能使用。但是当获取消息后，将再次获取一个锁。所以我们必须在收到通知后调用 `tick.release()` 来释放它。

我们使用 `asycino.wait()` 协程等待两个任务：

```python
done, pending = await asyncio.wait(
	[recv_task,
	tick_task],
	return_when = asyncio.FIRST_COMPLETED)
```

它会一直阻塞直到任务列表中的某一项被完成。之后它将返回两个列表：已完成的任务和正在运行的任务。如果某个任务已经完成，我们它的任务状态设置为 `None` ，这样的话下次迭代的时候就可以被再次创建。

## 例 3.5：结合多线程

> [例 3.5源码](https://github.com/7WebPages/snakepit-game/blob/master/simple/game_loop_thread.py)

本例中我们通过在一个单独的线程中运行主游戏循环，把 `asyncio` 循环和多线程结合起来。就像我之前提到的那样，由于全局解释器锁的缘故，Python 代码无法实现真正并行执行的多线程。所以用其他的线程来做沉重的计算并不是个好想法。但是，使用 `asyncio` 和多线程的原因是：我们需要使用其他不支持 `asyncio` 的库。在主线程中使用这些库很容易阻塞循环的运行，所以我们只能用其他的线程来异步运行。

我们使用 `asyncio` 循环的 `run_in_executor()` 方法和 `threadPoolExecutor` 来运行游戏循环。注意 `game_loop()` 不再是协程了。它是一个在其他线程中执行的函数。然而，我们需要和主线程交互去提示客户端游戏信息。由于`asyncio` 本身不是线程安全的，它有一些方法允许我们从其他线程中运行代码。如果是普通函数，则调用 `call_soon_threadsafe()`，如果是协程则调用 `run_coroutine_threadsafe()`。我们将会放一些用于提示用户端消息的代码在 `notify()` 协程中，并从另一个线程下在主事件轮询中运行。

```python
def game_loop(asycino_loop):
	print("Game loop thread id {}".format(threading.get_ident())))
	async def notify():		
		print("Notify thread id {}".format(threading.get_ident()))
		await tick.require()
		tick.notify_all()
		tick.release()
		
	whille 1:
		task = asyncio.run_coroutine_threadsafe(notify(),asyncio_loop)
		# 阻塞线程
		sleep(1)
		# 确保任务已经完成
		task.result()
```

当你运行本例时，你会发现“提示线程 id”和“主线程 id”是一样的。这是因为 `notify()` 协程是在主线程中执行的。 所以当 `sleep(1)` 被另一个线程调用时，就不会阻塞事件轮询。

## 例 3.6：多进程与扩大规模

> [例 3.6 源码](https://github.com/7WebPages/snakepit-game/blob/master/simple/game_loop_process.py)

单线程的服务器也许可以良好的工作，但它受限于单核 CPU。为了把服务端扩展至超出单核，我们需要去运行多个含有自己事件轮询的进程。所以我们得想办法通过进程间交换信息或是共享游戏数据实现通信。同时在游戏中，常常会要求复杂的计算，比如路径搜索之类的。这些任务没有办法快速的在一个单位游戏时间中完成。由于会阻塞事件的进程，所以并不推荐在协程中进行消耗大量时间的计算。故在这种情况下，传递沉重的任务交给其他进程并发进行是比较合理的。

利用多核的最简单方法是加载多个单核服务器，就像之前的例子，不同的端口都有一个。你可以借助 `supervisord` 或是类似的进程控制系统来实现。然后，你可以使用一个负载均衡器，比如 `HAProxy` ，来将连接的客户端分配给不同的进程。进程间通信有很多不同的方法。其中之一就是使用基于网络的系统，同样允许你扩大服务端的规模。已经有适配器用 `asyncio` 实现消息发送和存储系统。下面是一些例子：

* [aiomcache](https://github.com/aio-libs/aiomcache) 用于分布式缓存客户端
* [aiozmq](https://github.com/aio-libs/aiozmq) 用于 zeroMQ
* [aioredis](https://github.com/aio-libs/aioredis) 用于 Redis 数据库存储和发布/订阅

你可以在 github 和 pypi 上发现很多其他的包，大部分都有“aio”前缀。

使用网络服务可能在存储永久数据和交换消息方面的效率高。但如果你需要实现包括进程间通信等实时数据的处理的进程，它的表现就差强人意了。这种情况下，更适当的方法是使用标准的 unix 管道。`asyncio` 支持管道，并且在 `aiohttp` 库中有[非常底层地使用管道的服务端实例](https://github.com/KeepSafe/aiohttp/blob/master/examples/mpsrv.py)


在当前的例子中，我们将会使用 [multiprocessing](https://docs.python.org/3.5/library/multiprocessing.html) 库去创建在不同内核上进行沉重运算的新进程，并通过通过 `multiprocessing.Queue` 来交换信息。不幸的是，目前 `multiprocessing` 的实现与 `asyncio` 不兼容。所以每一个阻塞调用都会阻塞事件轮询。但这正是多线程有用之处，因为我们可以在不同的线程中运行多进程的代码而不会阻塞主线程。我们要做的，只是把所有进程内通信放到另一个线程中去。这个例子展示了这项技术。这和前面的多线程例子很像，但我们是在线程中创建了新的进程。

```python
def game_loop(asyncio_loop):
	#在主线程中运行协程
	async def notify():
		await tick.acquire()
		tick.notify_all()
		tick.release()

	queue = Queue()
	
	#在不同进程中运行函数
	def worker():
		while 1:
			print("doing heavy calculation in process {}".format(os.getpid()))
			sleep(1)
			queue.put("calculation result")
			
	Process(target=worker).start()
	
	while 1:
		# 阻塞本线程而不是主线程的事件轮询
		result = queue.get()
		print("getting {} in processing".format(result, os.getpid()))
		task = asyncio.run_coroutine_threadsafe(notify(),asyncio_loop)
		task.result()
```

我们在其他的进程中运行了 `worker()` 函数。它包含了一个进行沉重计算循环，并把结果放入队列中。队列是 `multiprocessing.Queue` 的实例。之后我们获取结果，并通知在另一个线程的主循环轮询中执行的客户端，和例 3.5 完全一样。本例非常简化，没有正确的终止进程。而且在真实的游戏中，我们可能会使用第二个队列传递数据给 worker 函数。

有一个叫做 [aioprocessing](https://github.com/dano/aioprocessing)的项目，是一个使 `multiprocessing` 与 `asyncio` 兼容的包装器。然而，它使用的也是本例中描述的方法——从线程中创建进程。但除了把复杂的技巧隐藏在简单的接口下之外，不会给你带来任何好处。希望在以后的 Python 版本中，会引入基于协程并支持 `asyncio` 的多进程库。

> 注意！如果你要在不同的线程或是主线程/进程的子进程中运行别的 `asyncio` 事件轮询，你需要用 `asyncio.new_event_loop()` 显式地创建循环，否则它将无法工作。

***

[点此查看原文链接](https://7webpages.com/blog/writing-online-multiplayer-game-with-python-and-asyncio-writing-game-loop/)。

[Python 翻译组](https://github.com/PythonTG)是EarlGrey@编程派发起成立的一个专注于 Python 技术内容翻译的小组，目前已有近 30 名 Python 技术爱好者加入。

翻译组出品的内容（包括教程、文档、书籍、视频）将在编程派微信公众号首发，欢迎各位 Python 爱好者推荐相关线索。

推荐线索，可直接在编程派微信公众号推文下留言即可。