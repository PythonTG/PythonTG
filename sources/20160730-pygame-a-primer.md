# 从零开发一个小游戏：PyGame 入门

title: 从零开发一个小游戏：PyGame 入门
author: Real Python
translator: haiyuqiao
reviewer: EarlGrey
date: 20160730
permalink: pygame-a-primer-by-real-python
keywords: pygame 教程, pygame入门, real python, python游戏开发, python小游戏

今天分享的是 Python 翻译组 最新译文，原文来自real python，是一篇比较详细的 PyGame 游戏开发入门指南。

译者：haiyuqiao，华中科技大学（在读研究生），正在使用 Python 做数据分析。Fighting from now！校对：EarlGrey，编程派主页君。

以下是正文，一起来学习吧。

***

[PyGame](http://www.pygame.org/hifi.html)是 [SDL](https://www.libsdl.org/) 库的 Python 包装器（wrapper）。SDL 是一个跨平台库，支持访问计算机多媒体硬件（声音、视频、输入等）。SDL 非常强大，但美中不足的是，它是基于 C 语言的，而 C 语言比较难懂，因此我们采用 PyGame 。

![PyGame logo](https://realpython.com/images/blog_images/pygame/pygame-logo.png)

**在本教程中，我们将介绍 PyGame 的基本逻辑和冲突检测，以及如何在屏幕上绘图和将外部文件导入到游戏中。**

> 提示：教程假定你对 Python 的语法、文件结构和面向对象的程序设计已经有了基本的了解。

## 准备工作

打开[PyGame下载页面](http://www.pygame.org/download.shtml)，根据你的操作系统和 Python 版本下载合适的 PyGame 安装包。如果你使用的是 Python 3，那么请下载[ 1.9.2 版](https://www.pygame.org/wiki/FrequentlyAskedQuestions#Does%20Pygame%20work%20with%20Python%203?).

> EarlGrey：在下载页面找不到 1.9.2 版的下载链接，但是 `pip install` 可以安装。

新建一个 *.py* 文件，然后输入以下代码：

```python
import pygame
from pygame.locals import *

pygame.init()
```

与其他 Python 程序一样，我们首先导入想要使用的模块。这里，我们将导入 `pygame` 和 `pygame.locals` ，后续我们将使用其中的一些常量。最后一行会初始化所有导入的 PyGame 模块，在做其他操作之前必须执行调用该函数。

## 基础对象 

### 屏幕对象

首先，我们需要一张画布，我们称之为“屏幕”，它是我们绘画的平台。为了创建一个屏幕，我们需要调用`pygame.display` 中的 `set_mode` 方法，然后向 `set_mode()` 传递包含屏幕窗口宽度和高度的元组（本教程中使用 800x600 尺寸）。

```python
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800,600))
```

运行上述代码，将会弹出一个窗口，然后当程序退出后又立即消失。一点都不酷嘛，对吧？下一节，我们将介绍游戏的主循环，它将确保只有在我们给它正确的输入时程序才会退出。

### 游戏主循环

[游戏主循环/事件循环](https://www.pygame.org/docs/ref/event.html)是所有操作发生的地方。在游戏过程中，它不断的更新游戏状态，渲染游戏画面和收集输入指令。创建循环时，需要确保我们有办法跳出循环，退出应用。为此，我们将同时介绍一些基本的用户输入指令。所有的用户输入（和我们稍稍后提到的其他事件）都会进入 PyGame 的事件队列，通过调用 `pygame.event.get()` 可以访问该队列。这将返回一个包含队列里所有事件的列表，我们将循环这个列表，并根针对相应的事件类型做出反应。现在我们只关心 `KEYDOWN` 和 `QUIT` 事件：

```python
# 用于保证主循环运行的变量
running = True

# 主循环！
while running:
    # for 循环遍历事件队列
    for event in pygame.event.get():
        # 检测 KEYDOWN 事件: KEYDOWN 是 pygame.locals 中定义的常量，pygame.locals文件开始已经导入
        if event.type == KEYDOWN:
            # 如果按下 Esc 那么主循环终止
            if event.key == K_ESCAPE:
                running = False
         # 检测 QUIT : 如果 QUIT, 终止主循环
        elif event.type == QUIT:
            running = False
```
            
将上述代码添加到之前的代码下，并运行。你应该看到一个空的窗口。只有你按下 ESC 键 或者触发一个 QUIT 事，否则这个窗口不会消失。

### Surface 和 Rects 

`Surface`和 `Rects`是 PyGame 中的基本构件。可以将 Surface 看作一张白纸，你可以在上面随意绘画。我们的屏幕对象也是一个 Surface 。它们可以包含图片。Rects 是 Surface 中矩形区域的表示。

让我们创建一个 50x50 像素的 Surface，然后给它涂色。由于屏幕是黑色的，所以我们使用白色。 我们然后调用 `get_rect()` 在 Surface上 得到一个矩形区域和 Surface 的 x 轴 和 y 轴。

```python
# 创建Surface 并用原则设定它的长度和宽度
surf = pygame.Surface((50,50))
# 设定Surface的颜色，使其和屏幕分离
surf.fill((255,255,255))
rect = surf.get_rect()
```
       
## Blit 和 Flip

仅仅只是创建了 Surface 并不能在屏幕上看到它。为此我们需要将这个 Surface 绘制（[Blit](Blit)）到另一个 Surface 上。Blit 是一个专业术语，意思就是绘图。你仅仅只能从一个Surface Blit 到另一个Surface，我们的屏幕就是一个 Surface 对象。以下是我们如何将 `surf` 画到屏幕上：

```python
# 这一行表示：将surf画到屏幕 x：400.y:300的坐标上
screen.blit(surf,(400,300))
pygame.display.flip()
```

`blit()` 有两个参数：要画的 Surface 和 在源 Surface 上的坐标。此处我们使用屏幕的中心，但是当你运行代码时，你会发现我们的 `surf` 并没有出现在屏幕的中心。这是因为 `blit()` 是从左上角开始画 surf 。

注意在 blit 之后的 `pygame.display.filp()` 的调用。[Flip](https://www.pygame.org/docs/ref/display.html#pygame.display.flip)将会更新自上次 flip 后的整个屏幕，两次 flip 之间发生的修改都将在屏幕上显示。没有调用`flip()`那就什么也不会出现。


### Sprites 

什么是 Sprites ？从编程术语来讲，Sprites 是屏幕上事物的二维表达。本质上来讲，Sprite 就是一个图片。Pygame 提供一个叫做 Sprites 的基础类，它就是用来扩展的，可以包含想要在屏幕上呈现的对象一个或多个图形表示。我们将会扩展[Sprite ](https://www.pygame.org/docs/ref/sprite.html)类，这样可以使用它的内建方法。我们称这个新的对象为 `Player` 。`Plyaer` 将扩展 Sprite，现在只有两个属性：`surf` 和 `rect`。我们也会给 `surf` 涂色（本教程使用白色），如之前 surface 例子，只是现在 Surface 属于 Player ：

```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()
```

现在我们将上述代码整合在一起：

```python
# 调用pygame模块
import pygame

# 调用 pygame.locals 使容易使用关键参数
from pygame.locals import *

# 定义Player对象 调用super赋予它属性和方法    
# 我们画在屏幕上的surface 现在是player的一个属性
class  Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

# 初始化 pygame
pygame.init()

# 创建屏幕对象
# 设定尺寸为 800x600
screen = pygame.display.set_mode((800,600))

# 初始化Player， 现在他仅仅是一个矩形
player = Player()

# 控制主循环的进行的变量
running = True

# 主循环
while running:
     # 事件队列中的循环
    for event in pygame.event.get():
        # check for KEYDOWN event: KEYDOWN is a constant defined in pygame.locals,which we imported earlier
            if event.type == KEYDOWN:
                # if the Esc KEY has been pressed set running to false to exit the main loop
                if event.key == K_ESCAPE:
                    running = False
                # check for QUIT event: if QUIT, set running to false
            elif event.type == QUIT:
                running = False
        

    # 这一行表示：将surf画到屏幕 x：400.y:300的坐标上
    screen.blit(player.surf,(400,300))
    # 更新
    pygame.display.flip()
```

运行上述代码，你将会在屏幕中心看到一个白色的矩形：

![Pygame代码运行效果](https://realpython.com/images/blog_images/pygame/pygame-part1.png)
    
如果将 `screen.blit(player.surf,(400,300))` 改成 `screen.blit(player.surf,player.rect)` ，你觉得会发生什么？修改之后，试着在控制台中打印 `player.rect` 。`rect` 的前两个属性分别是 `rect` 左上角的 x 和 y 轴坐标。当你将 rect 传递给 blit ，它将会根据这个坐标画 surface 。我们后续将使用它控制 player 移动。
 
## 用户输入

现在开始才是有趣的部分。我们要把 Player 变得可控制！之前我们提过，按键事件 `pygame.event.get()` 将把最新的事件从事件堆（event stack）中移除。Pygame 还有另外一个[事件方法](https://www.pygame.org/docs/ref/event.html)，`pygame.event.get_pressed()`。`get_pressed()`方法返回一个队列，其中包含了所有按键事件组成的字典，我们将把它放在主循环中，这样我们将在每一帧上的按键。

```python
pressed_keys = pygame.event.get_presssed()
```

现在我们将写一个方法，接收上面那个字典，并且根据按下的键定义 sprite 的行为，代码如下:

```python
def update(self,pressed_keys):
    if pressed_keys[K_UP]:
        self.rect.move_ip(0,-5)
    if pressed_keys[K_DOWN]:
        self.rect.move_ip(0,5)
    if pressed_keys[K_LEFT]:
        self.rect.move_ip(-5,0)
    if pressed_keys[K_RIGHT]:
        self.rect.move_ip(5,0)
```

`K_UP`、`K_DOWN`、`K_LEFT`、`K_RIGHT` 对应键盘上的上、下、左 右方向键。我们判断这些键是否按下，如果它为真，那么我们就朝相应的方向移动 `rect()`。Rects 有两个内建的移动方法，此处我们使用 [move in place](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.move_ip) `move_ip()` ，因为我们希望移动 rect 并且不用复制它。

将上述方法添加到 `Player` 类，将 `get_pressed()` 调用放在主循环中。整体代码现在应该是这样的：

```python
# 调用pygame模块
import pygame

# 调用 pygame.locals 使容易使用关键参数
from pygame.locals import *

# 定义Player对象 调用super赋予它属性和方法    
# 我们画在屏幕上的surface 现在是player的一个属性
class  Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

def update(self,pressed_keys):
    if pressed_keys[K_UP]:
        self.rect.move_ip(0,-5)
    if pressed_keys[K_DOWN]:
        self.rect.move_ip(0,5)
    if pressed_keys[K_LEFT]:
        self.rect.move_ip(-5,0)
    if pressed_keys[K_RIGHT]:
        self.rect.move_ip(5,0)

# 初始化 pygame
pygame.init()

# 创建屏幕对象
# 设定尺寸为 800x600
screen = pygame.display.set_mode((800,600))

# 初始化Player， 现在他仅仅是一个矩形
player = Player()

# 控制主循环的进行的变量
running = True

# 主循环
while running:
     # 事件队列中的循环
    for event in pygame.event.get():
        # check for KEYDOWN event: KEYDOWN is a constant defined in pygame.locals,which we imported earlier
            if event.type == KEYDOWN:
                # if the Esc KEY has been pressed set running to false to exit the main loop
                if event.key == K_ESCAPE:
                    running = False
                # check for QUIT event: if QUIT, set running to false
            elif event.type == QUIT:
                running = False

    pressed_keys = pygame.event.get_presssed()
 
    player.update(pressed_keys)   

    # 这一行表示：将surf画到屏幕 x：400.y:300的坐标上
    screen.blit(player.surf,(400,300))
    # 更新
    pygame.display.flip()
```

现在你可以使用方向键移动矩阵块了。也许你注意到了，你可以将矩形块移出屏幕，这可能并不是你想要的。所以我们我们需要往 update 方法中添加一些逻辑，检测矩形的坐标是否移出了 800x600 的屏幕边界；如果出了边界，那么就将它放回在边界上：

```python
def update(self,pressed_keys):
    if pressed_keys[K_UP]:
        self.rect.move_ip(0,-5)
    if pressed_keys[K_DOWN]:
        self.rect.move_ip(0,5)
    if pressed_keys[K_LEFT]:
        self.rect.move_ip(-5,0)
    if pressed_keys[K_RIGHT]:
        self.rect.move_ip(5,0)

    # 限定player在屏幕中
    if self.rect.left < 0:
        self.rect.left = 0
    elif self.rect.right > 800:
        self.rect.right = 800
    if self.rect.top <= 0:
        self.rect.top = 0
    elif self.rect.bottom >= 600:
        self.rect.bottom = 600
```

上述代码没有使用 `move` 方法，我们只要修改 上下左右的相应坐标即可。

现在我们添加一些敌人！

首先我们创建一个新的 sprite 类，命名为 `Enemy`。依照创建 player 的格式创建：

```python
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=(820, random.randint  (0, 600)))
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
```

以上有几点需要说明。首先，当我们在 surface 上调用 `get_rect` 时，我们将核心属性 x 设为 820 ，y 的坐标为一个随机数，由 `random.randint()` 生成。

在最终的代码中，我们会在文件的开头导入 [Random](https://docs.python.org/3.5/library/random.html) 库(`import random`)。为什么选择随机数？因为我们希望敌人从屏幕右边（820）的随机位置（0-600）上出现。 我们还将使用 `random` 设置敌人的速度属性，这样敌人就会有快有慢。

敌人的 `update()` 方法没有参数限制（我们不关心敌人的输入），只要让它向着屏幕左边以一定的速度移动就可以了。update 方法中的最后一个 `if` 语句检测敌人右侧是否通过了屏幕左边边界（要确保它们不会一碰到屏幕的边界就消失）。当他们通过屏幕的边界后，我们调用 Sprite 的内建方法 `kill()` ，从 sprite 组中删除它们，这样它们就不会再被渲染出来。kill 不会释放被它们占用的内存， 需要你确保你不再引用它们，以便 Python 的垃圾回收器回收。

## Groups

Pygame 提供的另一个很有用的对象是 Sprite 的 [Groups](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group)。诚如其名，是 Sprite 的集合。为什么我们要使用 sprite.Group 而不是列表呢？ 因为 sprite.Group 有一些内建的方法，有助于解决冲突和更新问题。那现在就创建一个 Group，用来包含游戏中的所有 Sprites 。创建完 Group 后，我们要将 Player 添加到里面，因为它是我们目前唯一的 Sprite 。我们也可以为敌人创建一个 group 。 当我们调用 Sprite 的 `kill()` 方法时，sprite 将会从其所在的全部 group 中删除。

```python
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
```

现在有了 `all_sprites` 的 group ，我们接着改变对象渲染方式，只要渲染 group 中的所有对象即可：

```python
for entity in all_sprites:
    screen.blit(entity.surf,entity.rect)
```

现在，任何放到 `all_sprites` 中的对象都会被渲染出来。

## 自定义事件

现在我们为敌人创建了一个 sprite.Group ，但是并没有实际的敌人。那怎样才能在屏幕上出现敌人呢？我们当然可以在刚开始的时候创建一堆的敌人，但是这样游戏玩不了几秒。为此，我们创建一个自定义事件，它隔几秒钟就会触发创建一批敌人。我们要监听该事件，方式和监听按键或退出事件一样。创建自定义事件十分容易，只要命名即可：

```python
ADDENEMY = pygame.USEREVENT +1
```

这样就可以了！现在，我们有了一个叫做 `ADDENEMY`的事件，可以在主程序中监听它。这里我们只需要注意一点，即自定义事件需要有一个独特的值，要比 `USEREVENT` 的值大，这就是我们为什么设定它为 `USEREVENT + 1`。这里说明一点：自定义事件本质上就是整数常量。又因为比 `USEREVENT` 小的数值已经被内置函数占据，所以创建的任何自定义事件都要比 `USEREVENT` 大。

定义好事件之后，我们需要将它插入事件队列中。因为整个游戏过程中都要创建它们，所以将设置一个计时器。可以通过 PyGame 的 `time()` 对象实现。

```python
pygame.time.set_timer(ADDENEMY,250)
```

这行代码告诉 PyGame 每隔 250 毫秒(四分之一秒) 触发一次 `ADDENEMY` 事件。这是在主游戏循环之外执行的，不过在整个游戏中都处于执行状态。现在我们添加一些监听事件的代码：

```python
while running:
    for event in pygame.event.get():
        if event.type == KAYDOWN:
            if event.key == K_ESCAPE:
                running == False
        elif event.type == QUIT:
            running == False
        elif (event.type == ADDENEMY):
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
```

> 谨记：`set_timer()` 只能用来将事件插入到 PyGame 事件队列中，不做其他任何事情。

现在我们会监听`ADDENEMY`事件，当它触发时，将创建一个 `Enemy`类的实例。然后我们将实例添加到`enemies` 这个 Sprite Group（后续用它来检测冲突）和 `all_sprites` Group（这样它会和其他对象一起渲染）。

## 冲突

这才是 PyGame 的魅力所在！写冲突代码（collision code）很难，但是 PyGame 提供了很多冲突检测方法，你可以在[这里](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.collide_rect)查看其中一部分。本次教程使用 [spritecollideany](https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.spritecollideany)。`spritecollideany()` 接受一个 Sprite 对象和一个 Sprite.Group ，检测 Sprite 对象是否和 Sprite Group 中的其他 Sprites 冲突。这样，我们可以拿 Player 和敌人所在的 Sprite Group 对比，检测 player 是否被敌人击中。代码实现如下：

```python
if pygame.sprite.spritecollideany(player,enemies):
    player.kill()
```

检测 player 是否 `enemies` 中的 Sprites 冲突，如果发生冲突了，那么调用 `player` Sprite 的 `kill()` 方法。因为我们只渲染了 `all_sprites` Group 中的 sprites ，`kill()` 方法将从其所在的全部 Groups 中移出 Sprite ，`player`就不再出现，算是“杀死它了”。目前的完整代码如下：

```python
# 调用pygame模块
import pygame

# 调用random模块
import random

# 调用 pygame.locals 使容易使用关键参数
from pygame.locals import *

# 定义Player对象 调用super赋予它属性和方法    
# 我们画在屏幕上的surface 现在是player的一个属性
class  Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

def update(self,pressed_keys):
    if pressed_keys[K_UP]:
        self.rect.move_ip(0,-5)
    if pressed_keys[K_DOWN]:
        self.rect.move_ip(0,5)
    if pressed_keys[K_LEFT]:
        self.rect.move_ip(-5,0)
    if pressed_keys[K_RIGHT]:
        self.rect.move_ip(5,0)

    # 限定player在屏幕中
    if self.rect.left < 0:
        self.rect.left = 0
    elif self.rect.right > 800:
        self.rect.right = 800
    if self.rect.top <= 0:
        self.rect.top = 0
    elif self.rect.bottom >= 600:
        self.rect.bottom = 600

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=(820, random.randint(0, 600)))
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# 初始化 pygame
pygame.init()

# 创建屏幕对象
# 设定尺寸为 800x600
screen = pygame.display.set_mode((800,600))

#为添加敌人创建自定义事件
ADDENEMY = pygame.USEREVENT +1 
pygame.time.set_timer(ADDENEMY,250)

# 初始化Player， 现在他仅仅是一个矩形
player = Player()

background = pygame.Surface(screen.get_size())
background.fill((0,0,0))

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# 控制主循环的进行的变量
running = True

# 主循环
while running:
     # 事件队列中的循环
     for event in pygame.event.get():
        # 检测 KEYDOWN: KEYDOWN 是我们定义好的pygame.locals中的一个常量
            if event.type == KEYDOWN:
                # 按下 Esc 键则退出主程序
                if event.key == K_ESCAPE:
                    running = False
                # 检测 QUIT 到则终止
             elif event.type == QUIT:
                  running = False
            elif(event.type == ADDENEMY):
                        new_enemy = Enemy()
                        enemies.add(new_enemy)
                        all_sprites.add(new_enemy)

    pressed_keys = pygame.event.get_presssed()
 
    player.update(pressed_keys)   

    # 这一行表示：将surf画到屏幕 x：400.y:300的坐标上
    screen.blit(player.surf,(400,300))
    # 更新
    pygame.display.flip()
```

测试一下！

![Pygame 游戏测试结果](https://realpython.com/images/blog_images/pygame/pygame-part2.png)

## 图片

现在游戏可以玩了，但是长得挺丑的。接下来，我们将白色方块变成有意思的图片，让游戏看上去有游戏的样子。

前面的代码示例中，我们使用了涂色的 Surface 对象表示游戏里的所有事物。虽然这样有助于理解什么是 Surface 和它如何工作，但是却让游戏变得很丑！现在我们要给 player 和 enemy 添加一些图片。我喜欢自己画图，我把 player 画成小飞机，enemy 是导弹，这些可以从[我的代码库](https://github.com/realpython/pygame-primer)中下载。欢迎你使用我的作品，自己画或者者下载一些[免费游戏素材](http://www.gameart2d.com/)。

### 修改对象的构造函数

下面是我们现在的 player 构造函数：

```python
class  Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()
```

新的构造函数将会是这个样子的：

```python
class  Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.image = pygame.image.load('jet.png').convert()
        self.image.set_colorkey((255,255,255),RLEACCEL)
        self.rect = self.image.get_rect()
```

我们想用一张图片替代 Surface 对象。我们将使用 `pygame.image.load()` 导入图片的路径。`load()` 方法将会返回一个 Surface 对象。我们然后在这个 Surface 对象上调用 `convert()` 创建副本，这样可以更快地将它画在屏幕上。

接下来，我们在图片上调用 `set_colorkey()` 方法。`set_colorkey`用于设置图片的颜色，如果不设置 Pygame 会将图片设置为透明。这里我选用白色，因为和飞机的背景色一致。[RLEACCEL](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.set_colorkey) 是一个可选参数，它有助于 PyGame 在非加速显示器上更快地渲染。

最后，我们和之前一样调用 `rect()` 对象：在图片上调用 `get_rect()`。

> 谨记：图片仍然是一个 surface 对象，只不过它上面画了一张图。

对 enemy 构造函数做同样的操作：

```python
class Enemy(pygame.sprite.Sprite):

   def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load('missile.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(random.randint(820, 900), random.randint(0, 600))
        )
        self.speed = random.randint(5,20)
```

现在的游戏虽然和以前一样，但是比之前漂亮多啦！但是我仍然觉得它少了点什么东西。让我们加点不断漂浮的白云，这样会有飞机划过蓝天的感觉。为此，我们需要遵循之前用过的一些原则。首先，我们创建 `cloud` 对象，画上白云的照片，其 `update()` 方法让它不停地向着屏幕左边移动。然后，我们需要添加一个自定义事件，每隔一段时间就生成白云（我们还要将添加白云到 `all_sprites` group）。白云对象的实现如下：

```python
class Cloud (pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('cloud.png').convet()
        self.image.set_colorkey((0,0,0),RLEACCEL)
        self.rect = self.image.get_rect(
            center = (random.randint(820,900),random.randint(0,600))
        )
        
    def update(self):
        self.rect.move_ip(-5,0)
        if self.rect.right < 0:
            self.kill()
```

上面的代码看起来都很熟悉，下面这个事件创建代码也一样，我们将它放在 enemy 事件代码下面：

```python
ADDCLOUD = pygame.USEREVENT+2
pygame.time.set_timer(ADDCLOUD,1000)
```

现在为它们创建一个新的 Sprite.Group：

```python
clouds = pygame.sprite.Group()
```

现在，在主循环中，我们需要开始监听`ADDCLOUD`事件。

下面的代码：

```python
for event in pygame.event.get():
    if event.type == KEYDOWN:
        if event.kay == K_ESCAPE:
            running = False
    elif event.type == QUIT:
        running = False
    elif event.type == ADDENEMY:
        new_enemy = Enemy()
        enemies.add(new_enemy)
        all_sprites.add(new_enemy)
```

将会变成这样：

```python
for event in pygame.event.get():
    if event.type == KEYDOWN:
        if event.kay == K_ESCAPE:
            running = False
    elif event.type == QUIT:
        running = False
    elif event.type == ADDENEMY:
        new_enemy = Enemy()
        enemies.add(new_enemy)
        all_sprites.add(new_enemy)  
    elif event.type == ADDCLOUD:
        new_cloud = Cloud()
        all_sprites.add(new_cloud)
        clouds.add(new_cloud)
```

我们还要把 clouds 添加到 `all_sprites` Group 和新的 clouds Group 中。我们这么做，是因为我们使用 `all_sprites` 来渲染，使用 `clouds` 调用它们的 update 函数。也许你很好奇，为什么我们将它不添加到 `enemies` Group中；毕竟我们调用的是一样的 update 函数。原因在于，我们不想检测白云和飞机之间的冲突。我们的飞机要顺畅地通过所有的云层。现在剩下的就是调用 clouds Group 的 `update()` 方法了！

## 结语

大功告成！让我们测试一下，效果应该是这样的：

![Pygame小游戏最终画面](https://realpython.com/images/blog_images/pygame/pygame-part3.png)

完整代码可以在[ GitHub 上的代码库](https://github.com/realpython/pygame-primer)获取！希望本教程对你有用！

***

[点此查看原文](https://realpython.com/blog/python/pygame-a-primer/#collision)

[Python 翻译组](https://github.com/PythonTG)是EarlGrey@编程派发起成立的一个专注于 Python 技术内容翻译的小组，目前已有近 30 名 Python 技术爱好者加入。

翻译组出品的内容（包括教程、文档、书籍、视频）将在编程派微信公众号首发，欢迎各位 Python 爱好者推荐相关线索。

推荐线索，直接在编程派微信公众号推文下留言即可。

本文译者简介：haiyuqiao，华中科技大学（在读研究生），正在使用 Python 做数据分析。Fighting from now！
