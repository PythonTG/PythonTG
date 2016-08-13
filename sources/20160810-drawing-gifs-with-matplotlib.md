# 用Matplotlib画GIF动图

title: 用Matplotlib画GIF动图
author: Eli Bendersky
translator: 唐晓霆 Jason
reviewer: EarlGrey
date: 20160810
permalink: drawing-gifs-with-matplotlin
keywords: matplotlib教程, matplotlib技巧, matplotlib画图, Python 动图, matplotlib动图, 

***

> 今天分享的这篇译文中介绍了 matplotlib 绘图库的一个 使用示例，即如何制作 GIF 动图。本文原作者为 Eli Bendersky，译者为 唐晓霆 Jason ，由编程派 EarlGrey 校对。
>
> 译者简介：唐晓霆，在香港的成都人，城市大学研究助理，会写python，兴趣是深度学习。

这篇短文介绍如何用 Python 里的 matplotlib 画出 GIF 动图。下面的代码我在一台安装了 ImagMagick 的 Ubuntu 机器上运行过。 若想要用 matplotlib 的 `save` 方法渲染 GIF 动图的话，就必须安装 ImageMagick 。

下面给一个动画样本：

![matplotlib 绘制的动图](http://eli.thegreenplace.net/images/2016/animline.gif)

有几点需要注意:

1. 图里的散点部分是不变的；变的是直线
2. X 轴的标题每一帧都在变化

下面上制作该图的代码：

```python
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
fig.set_tight_layout(True)

#  询问图形在屏幕上的尺寸和DPI（每英寸点数）。
#  注意当我们把图形储存成一个文件时，我们需要再另外提供一个DPI值
print('fig size: {0} DPI, size in inches {1}'.format(
    fig.get_dpi(), fig.get_size_inches()))

# 画出一个维持不变（不会被重画）的散点图和一开始的那条直线。
x = np.arange(0, 20, 0.1)
ax.scatter(x, x + np.random.normal(0, 3.0, len(x)))
line, = ax.plot(x, x - 5, 'r-', linewidth=2)

def update(i):
    label = 'timestep {0}'.format(i)
    print(label)
    # 更新直线和x轴（用一个新的x轴的标签）。
    # 用元组（Tuple）的形式返回在这一帧要被重新绘图的物体
    line.set_ydata(x - 5 + i)
    ax.set_xlabel(label)
    return line, ax

if __name__ == '__main__':
    # FuncAnimation 会在每一帧都调用“update” 函数。
    # 在这里设置一个10帧的动画，每帧之间间隔200毫秒
    anim = FuncAnimation(fig, update, frames=np.arange(0, 10), interval=200)
    if len(sys.argv) > 1 and sys.argv[1] == 'save':
        anim.save('line.gif', dpi=80, writer='imagemagick')
    else:
        # plt.show() 会一直循环播放动画
        plt.show()
```

如果你想换一个更精美的主题，安装 seaborn 库之后添加一行：

``` python
import seaborn
```

然后你就会得到这个图：

![安装seaborn之后的动图](http://eli.thegreenplace.net/images/2016/animline-seaborn.gif)

提一句关于文件大小的警告：虽然我在这里分享的GIF只有 10 帧，而且图像也很简单，但是它们每一帧都占大约 160K 。就我理解而言，GIF 动图不使用跨帧压缩， 所以这使得长一点的 GIF 占的空间异常大。减少帧数到最最小并且让每一帧的图像小一点（通过在 matplotlib 里调整图形尺寸或者 DPI ），就可以多多少少帮助缓解一下这个问题。

> EarlGrey：我自己测试生成的 line.gif 文件大概 86 KB 左右。

***

[点此查看原文链接](http://eli.thegreenplace.net/2016/drawing-animated-gifs-with-matplotlib/)

[Python 翻译组](https://github.com/PythonTG)是EarlGrey@编程派发起成立的一个专注于 Python 技术内容翻译的小组，目前已有 30 多名 Python 技术爱好者加入。

翻译组出品的内容（包括教程、文档、书籍、视频）将在编程派微信公众号首发，欢迎各位 Python 爱好者推荐相关线索。推荐线索，可直接在编程派微信公众号推文下留言即可。
