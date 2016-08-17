# 用 python 和 asyncio 来编写多人在线游戏（第三部分）

title: 用 python 和 asyncio 来编写多人在线游戏（第三部分）
author: Kyrylo Subbotin
translator: oo7ww 
reviewer: EarlGrey
date: 20160817
permalink: writing-online-multiplayer-game-with-python-part-three
keywords: asyncio教程, asyncio游戏, python游戏, python多人游戏, python websockets, 游戏开发, python教程

***

![用 python 和 asyncio 来编写多人在线游戏（第三部分）](hhttp://ww2.sinaimg.cn/mw690/006faQNTgw1f6x2fqpgjqg30k009wjve.gif)

> 在这个系列教程中，我们以多人贪吃蛇游戏为例，开发了一个异步 Python 应用。前一篇文章主要讲了如何编写游戏循环，第一篇则介绍如何实现异步。

> 译者：oo7ww，校对：EarlGrey@编程派。

## 4.制作一个完整的游戏

![制作一个完整的游戏](http://ww4.sinaimg.cn/mw690/006faQNTgw1f6x2fq59gag307806rtmd.gif)

## 4.1 项目总览

在这部分，我们将复习一个完整的在线游戏的设计。
这是一个可增加玩家的经典贪吃蛇游戏。你可以试玩（[http://snakepit-game.com](ttp://snakepit-game.com)）。源代码托管于[github](https://github.com/7WebPages/snakepit-game)。游戏包含以下文件：

* [server.py](https://github.com/7WebPages/snakepit-game/blob/master/server.py) - 一个处理游戏主循环与连接的服务器。

* [game.py](https://github.com/7WebPages/snakepit-game/blob/master/game.py) - 一个主要的 **Game** 类，它实现了游戏的逻辑和大部分网络协议。

* [player.py](https://github.com/7WebPages/snakepit-game/blob/master/player.py) - **Player** 类，它包含了个人玩家的数据和蛇的表示。这个类负责获取玩家的输入，并对蛇做对应的移动。

* [datatypes.py](https://github.com/7WebPages/snakepit-game/blob/master/datatypes.py) - 基本的数据结构。

* [settings.py](https://github.com/7WebPages/snakepit-game/blob/master/settings.py) - 游戏设置，有注释做具体描述。

* [index.html](https://github.com/7WebPages/snakepit-game/blob/master/index.html) - 所有的 html 和 javascript 客户端部分都在这个文件里。

## 4.2 游戏循环内部

由于简单，多玩家贪吃蛇游戏是一个学习的好例子。每一帧，所有的蛇移动一个位置，而帧以很慢的速率改变，这使你能够观察游戏引擎是如何工作的。由于游戏速度慢，对玩家键盘输入没有即时响应。每个被按下的键会被记录下来，然后，在游戏循环迭代的末尾计算下一帧时，按键将被纳入计算。

> 现代动作游戏以相对更高的帧率运行，而且服务器和客户端的帧率并不相等。客户端帧率通常取决于客户端的硬件性能，而服务器帧率是固定的。一个客户端可能在获取对应于一个“游戏 tick ”的数据后呈现几帧。这允许创作仅受限于客户端性能的平滑动画。在这种情况下，服务器应该不仅传递那些目标的当前位置，也传递它们的运动方向、速度和加速度。客户端帧率用 **FPS** （帧数每秒）表示，而服务器帧率则用  **TPS** （tick 数每秒）表示。在这个贪吃蛇游戏例子中，这两个值是相等的，而且呈现在客户端的一帧是在服务器的一个 tick 事件内计算出的。

我们将使用类似文本格式的游戏区域。实际上，这是个包含许多单字符单元格的 **html** 表格。游戏中的所有对象都是由置于单元格中的不同颜色的字符呈现的。大部分时候，用户端传递按键的编码到服务器，并获取对应每个"tick"的游戏区域的更新。从服务器获取的一份更新包含表示生成字符及字符坐标和颜色的信息。所以我们把所有的游戏逻辑保存在服务器，而只向用户端发送生成数据。此外，我们降低了通过替代由网络发送的信息来入侵游戏的可能性。

## 4.3 它如何工作？

这个游戏的服务器和**例 3.2** 的简单例子相似。但我们并没有使用一个全局的 **websockets**
列表，而是用了一个服务器范围的 **Game** 对象。一个 **Game** 实例包含了一个 **Player** 对象列表（在 **self._players** 属性中），表示加入游戏的玩家以及他们的私有数据和 **websocket** 对象。所有游戏相关数据置于一个 **Game** 对象中也允许我们有多个游戏房间。在这种情况下，我们需要维护多个 **Game** 对象，因为每个游戏开始就需要一个。

服务器和客户端之间的所有交互是通过以 json 格式编码的消息完成的。从客户端发出的消息只包含一个数字，是玩家按键的代码。其它从客户端消息都按以下格式发送：

```
[command, arg1, arg2, ... argN]
```

服务器的消息以列表的形式发送，因为通常许多消息需要立刻发送(大部分是渲染数据）：

```
[[command, arg1, arg2, ... argN], ... ]
```

在每个游戏循环迭代末尾，计算下一帧并发送给所有的客户端。当然，我们不是每次都发送完整的帧，只是发送针对下一帧变化的列表。

需要注意的是，玩家连接到服务器后，不会立即加入游戏。连接后开始“观众”模式，这样可以看别人如何玩。如果游戏已经开始，或者之前游戏出现“游戏结束”画面。玩家才可以按“加入”按钮，加入现有的游戏。或者如果游戏当前没有运行，则可以创建一个新的游戏（没有其他活动的玩家）。在后一种情况下，游戏区域在开始之前被清除。

游戏区域保存在 **Game._world** 属性中，这是一个二维数组的嵌套列表。它是用来保存游戏区域的内部状态。数组中的每个元素代表一个区域的单元格，而后单元格才被呈现为 **html** 表格单元。

它有一个  **Char** 类型，这是一个包含单个字符和颜色的 **nametuple**。保持游戏区域与所有连接的客户端同步至关重要，所以所有游戏区域的更新应该连同相应的消息发送给客户。这由 **Game.apply_render()** 方法实现。它接收一个 **Draw** 对象列表，然后使用它在内部更新游戏区域和发送 **render** 信息给客户。

> 我们使用 **namedtuple** ，不仅因为它能很好地表示简单的数据结构，而且因为与 **dict** 相比，它在发送 json 格式的消息时所需的空间更少。如果你在真实游戏应用中发送复杂数据结构，建议将它们序列化到一个普通甚至更短的格式，或打包为一个二进制格式（如 **bson**，而不是  **json**)，从而减少网络流量。


**Player** 对象包含一个表示蛇的 **deque** 对象。此数据类型类似于一个列表，但可以更有效地添加和删除它上面的元素，所以能够理想地表示一条移动的蛇。该类的方法主要是 **Player.render_move()** ，它返回渲染数据从而使玩家的蛇移动到下一位置。

基本上，它在新的位置渲染出蛇头，删除尾巴所在的最后一个元素。考虑到蛇吃了一个数字就会增长，尾巴不会移动相应数量的帧。蛇的渲染数据可以用在 **Game.next_frame()** 方法中，该方法实现了所有的游戏逻辑。它将渲染所有蛇的移动，检查每条蛇前面的障碍，同时产生数字和“石块”。每个 tick 期间，游戏会从 **game_loop()** 直接调用该方法，以生成下一帧。

如果在蛇头前面有一个障碍，会在 **Game.next_frame()** 中调用 **Game.game_over()** 。它将通知给所有在线的客户端（死蛇由 **player.render_game_over()** 变成石头）贪吃蛇已经死了，并更新最高成绩表。**Player** 对象的 **alive** 标志被设置为 **False** ，这样在渲染下一帧时该玩家将被忽略，直到他再次加入游戏。如果没有蛇活着，“游戏结束”消息呈现在游戏区域。同时，主游戏循环将停止并将 **game.running** 标志设置为 **False**，玩家下一次按下 “**Join**” 键时会清空游戏区域。

在每次生成下一帧时，数字和石头也同时由随机值决定出现。出现一个数字还是一块石头的几率可以在  **settings.py** 中修改。请注意，在游戏区域每一条活着的蛇都有相应的数字出现，所以蛇越多，数字也将更多，因而它们将有足够的食物。


## 4.4 网络协议

**从客户端发送的消息列表**

|   命令     |   参数   |    描述        |
|----------- |----------| -------------- |
| new_player |  [name]  | 设置玩家昵称   |
|  join      |          | 玩家将加入游戏 |

**从服务器发送的消息列表**

|命令       |参数                       |描述                       |
|-----------|---------------------------|---------------------------|
|handshake  |[id]                       |将id分配给一位玩家         |
|world      |[[(char, color), ...], ...]|初始化游戏区域地图         |
|reset_world|                           |清理地图,所有字符替换为空格|
|render     |[x, y, char, color]        |在对应位置显示字符         |
|p_joined   |[id, name, color, score]   |新加入游戏的玩家           |
|p_gameover |[id]                       |一位玩家游戏结束           |
|p_score    |[id, score]                |为一位玩家设置得分         |
|top_scores |[[name, score, color], ...]|更新最高得分表             |

**典型的消息交换规则**

|客户端->服务器|服务器->客户端|服务器->所有客户端|注释|
|--------------|--------------|------------------|----|
|new_player    |              |                  |名称传递给服务器|
|              |handshake     |                  |ID分配|
|              |world         |                  |初始游戏地图传递完成|
|              |top_scores    |                  |最近的最高得分表传递完成|
|join          |              |                  |玩家按下“加入”,游戏循环开始|
|              |              |reset_world       |命令客户端清理游戏区域|
|              |              |render, render,...|第一个游戏标志，第一帧渲染|
|(key code)    |              |                  |玩家按下某个按键|
|              |              |render, render,...|第二帧渲染|
|              |              |p_score           |蛇吃了一个数字|
|              |              |render, render,...|第三帧渲染|
|              |              |                  |...重复数帧...|
|              |              |p_gameover        |蛇在吃障碍时死亡|
|              |              |top_scores        |更新最高成绩表(如果有更新)|

## 5.总结

说实话，我真的很喜欢使用最新版 Python 的异步功能。新的语法与之前不同，所以异步代码现在简单易读，很容易就可以分辨出哪些调用时非阻塞的，是否正在切换为 green 协程。现在我可以满怀信心地声称， **Python 是一种异步编程的好工具**。

SnakePit 在 7WebPages 团队中很受欢迎。如果你决定在公司用它放松一下时，请记得通过 [Twitter](https://twitter.com/7WebPages) 或者 [Facebook](https://www.facebook.com/7WebPages/) 给我们反馈。


***

[点此查看原文链接](https://7webpages.com/blog/writing-online-multiplayer-game-with-python-and-asyncio-part-3/)。

[Python 翻译组](https://github.com/PythonTG)是EarlGrey@编程派发起成立的一个专注于 Python 技术内容翻译的小组，目前已有近 30 名 Python 技术爱好者加入。

翻译组出品的内容（包括教程、文档、书籍、视频）将在编程派微信公众号首发，欢迎各位 Python 爱好者推荐相关线索。

推荐线索，可直接在编程派微信公众号推文下留言即可。
