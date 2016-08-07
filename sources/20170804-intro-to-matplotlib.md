# 十分钟入门Matplotlib

title: 使用Python进行科学计算：Matplotlib入门
author: Jamal Moir
translator: linkmyth
reviewer: EarlGrey
date: 20160804
permalink: a-quick-intro-to-matplotlib
keywords: matplotlib入门, python绘图库, python绘图基础, matplotlib科学计算, python科学计算, python数据可视化


***

> 本文的原作者是 Jamal Moir，是 Python 科学计算系列的第一篇文章，或许有人已经翻译过了，但我觉得我们 Python 翻译组的译文质量还是不错的。希望对喜欢 Python 的各位朋友有帮助。
>
> 本文译者 linkmyth，校对 EarlGrey@编程派。linkmyth 是同济大学的在读硕士，主攻web开发、机器学习等方向。

以下是原文正文：

***

数据的处理、分析和可视化已经成为 Python 近年来最重要的应用之一。这种现象又进一步引出“大数据”分析等类似的话题，而大数据分析在人们所能预见的诸多领域内都有广泛应用，这其中就包含笔者个人感兴趣的机器学习。

Python 在处理数据、分析数据以及数据可视化方面拥有很多功能强大的工具，这也是 Python 在科学领域中能够迅速发展的一个主要原因。

在接下来的一系列文章中，我们将介绍 Python 科学计算中涉及的主要的库，并且学习如何使用它们处理数据以满足我们的需求。但是我们并非只是停留在快速写出模板代码来使用这些库的层面上，我们还会了解这些库背后的数学知识，以帮助我们更好地理解库的运行原理。

首先，我们将从一个功能非常强大的库 Matplotlib 开始介绍，在后面的文章中也会一直用到这个库。 

## 什么是 Matplotlib?

简单来说，Matplotlib 是 Python 的一个绘图库。它包含了大量的工具，你可以使用这些工具创建各种图形，包括简单的散点图，正弦曲线，甚至是三维图形。Python 科学计算社区经常使用它完成数据可视化的工作。

你可以在他们的[网站](http://matplotlib.org/)上了解到更多 Matplotlib 背后的设计思想，但是我强烈建议你先浏览一下他们的[图库](http://matplotlib.org/gallery.html)，体会一下这个库的各种神奇功能。

## 画一个简单的图形

首先我们要画一条在 [0, 2pi] 上的正弦曲线。读者应该会注意到我们在这里使用了 Numpy 库，但是即便你没有使用过这个库也不用担心，在后面的文章中我们也会介绍到 Numpy 库。

```python
import matplotlib.pyplot as plt
import numpy as np
```

以上这些就是我们将要用到的导入模块。在我的上一篇[文章](http://www.datadependence.com/2016/02/pythonic-idioms-others/)(以及[另一篇文章](http://www.datadependence.com/2016/04/how-to-build-gui-in-python-3/))中都提到过 ```from x import *``` 是一种糟糕的导入方式。我们不想在程序里重复书写 ```matplotlib.pyplot``` 和 ```numpy```，这种书写方式过于冗长，因此我们采用了上面的折中写法。

```python
# 简单的绘图
x = np.linspace(0, 2 * np.pi, 50)
plt.plot(x, np.sin(x)) # 如果没有第一个参数 x，图形的 x 坐标默认为数组的索引
plt.show() # 显示图形
```

上面的代码将画出一个简单的正弦曲线。```np.linspace(0, 2 * np.pi, 50)``` 这段代码将会生成一个包含 50 个元素的数组，这 50 个元素均匀的分布在 [0, 2pi] 的区间上。

```plot``` 命令以一种简洁优雅的方式创建了图形。提醒一下，如果没有第一个参数 x，图形的 x 轴坐标将不再是 0 到 2pi，而应该是数组的索引范围。

最后一行代码 ```plt.show()`` 将图形显示出来，如果没有这行代码图像就不会显示。

运行代码后应该会类似得到下面的图形：

![正弦曲线](http://i0.wp.com/www.datadependence.com/wp-content/uploads/2016/04/basic_plotting-1.png)

## 在一张图上绘制两个数据集

大多数时候读者可能更想在一张图上绘制多个数据集。用 Matplotlib 也可以轻松实现这一点。

```python
x = np.linspace(0, 2 * np.pi, 50)
plt.plot(x, np.sin(x),
        x, np.sin(2 * x))
plt.show()
```

上面的代码同时绘制了表示函数 sin(x) 和 sin(2x) 的图形。这段代码和前面绘制一个数据集的代码几乎完全相同，只有一点例外，这段代码在调用 ```plt.plot()``` 的时候多传入了一个数据集，并用逗号与第一个数据集分隔开。

最后你会得到类似于下面包含两条曲线的图形：

![两条正弦曲线](http://i0.wp.com/www.datadependence.com/wp-content/uploads/2016/04/plotting_two_datasets-1.png)

## 自定义图形的外观

当在同一个图形上展示多个数据集时，通过改变线条的外观来区分不同的数据集变得非常必要。

```python
# 自定义曲线的外观
x = np.linspace(0, 2 * np.pi, 50)
plt.plot(x, np.sin(x), 'r-o',
        x, np.cos(x), 'g--')
plt.show()
```

上述代码展示了两种不同的曲线样式：```'r-o'``` 和 ```'g--'```。字母 'r' 和 'g' 代表线条的颜色，后面的符号代表线和点标记的类型。例如 ```'-o'``` 代表包含实心点标记的实线，```'--'``` 代表虚线。其他的参数需要读者自己去尝试，这也是学习 Matplotlib 最好的方式。

> 颜色：
> 蓝色 - 'b'
> 绿色 - 'g'
> 红色 - 'r'
> 青色 - 'c'
> 品红 - 'm'
> 黄色 - 'y'
> 黑色 - 'k'（'b'代表蓝色，所以这里用黑色的最后一个字母）
> 白色 - 'w'




> 线：
> 直线 - '-'
> 虚线 - '--'
> 点线 - ':'
> 点划线 - '-.'




> 常用点标记
> 点 - '.'
> 像素 - ','
> 圆 - 'o'
> 方形 - 's'
> 三角形 - '^'
> 更多点标记样式点击[这里](http://matplotlib.org/api/markers_api.html)

最后你会得到类似下面的图形：

![图形](http://i1.wp.com/www.datadependence.com/wp-content/uploads/2016/04/line_customisation-1.png)

## 使用子图

使用子图可以在一个窗口绘制多张图。

```python
# 使用子图
x = np.linspace(0, 2 * np.pi, 50)
plt.subplot(2, 1, 1) # （行，列，活跃区）
plt.plot(x, np.sin(x), 'r')
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x), 'g')
plt.show()
```

使用子图只需要一个额外的步骤，就可以像前面的例子一样绘制数据集。即在调用 ```plot()``` 函数之前需要先调用 ```subplot()``` 函数。该函数的第一个参数代表子图的总行数，第二个参数代表子图的总列数，第三个参数代表活跃区域。

活跃区域代表当前子图所在绘图区域，绘图区域是按从左至右，从上至下的顺序编号。例如在 4×4 的方格上，活跃区域 6 在方格上的坐标为 (2, 2)。

最终你会得到类似下面的图形：

![子图](http://i1.wp.com/www.datadependence.com/wp-content/uploads/2016/04/subplot-1.png)

## 简单的散点图

散点图是一堆离散点的集合。用 Matplotlib 画散点图也同样非常简单。

```python
# 简单的散点图
x = np.linspace(0, 2 * np.pi, 50)
y = np.sin(x)
plt.scatter(x,y)
plt.show()
```

正如上面代码所示，你只需要调用 ```scatter()``` 函数并传入两个分别代表 x 坐标和 y 坐标的数组。注意，我们通过 ```plot``` 命令并将线的样式设置为 ```'bo'``` 也可以实现同样的效果。

最后你会得到类似下面的无线图形：

![散点图](http://i2.wp.com/www.datadependence.com/wp-content/uploads/2016/04/scatter_plot-1.png)

## 彩色映射散点图

另一种你可能用到的图形是彩色映射散点图。这里我们会根据数据的大小给每个点赋予不同的颜色和大小，并在图中添加一个颜色栏。

```python
# 彩色映射散点图
x = np.random.rand(1000)
y = np.random.rand(1000)
size = np.random.rand(1000) * 50
colour = np.random.rand(1000)
plt.scatter(x, y, size, colour)
plt.colorbar()
plt.show()
```

上面的代码大量的用到了 ```np.random.rand(1000)```，原因是我们绘图的数据都是随机产生的。

同前面一样我们用到了 ```scatter()``` 函数，但是这次我们传入了另外的两个参数，分别为所绘点的大小和颜色。通过这种方式使得图上点的大小和颜色根据数据的大小产生变化。

然后我们用 ```colorbar()``` 函数添加了一个颜色栏。

最后你会得到类似于下面的彩色散点图：

![彩色散点图](http://i0.wp.com/www.datadependence.com/wp-content/uploads/2016/04/colormap_scatter-1.png)

## 直方图

直方图是另一种常见的图形，也可以通过几行代码创建出来。

```python
# 直方图
x = np.random.randn(1000)
plt.hist(x, 50)
plt.show()
```

直方图是 Matplotlib 中最简单的图形之一。你只需要给 ```hist()``` 函数传入一个包含数据的数组。第二个参数代表数据容器的个数。数据容器代表不同的值的间隔，并用来包含我们的数据。数据容器越多，图形上的数据条就越多。

最终你会得到类似下面的直方图：

![直方图](http://i1.wp.com/www.datadependence.com/wp-content/uploads/2016/04/histogram-1.png)

## 标题，标签和图例

当需要快速创建图形时，你可能不需要为图形添加标签。但是当构建需要展示的图形时，你就需要添加标题，标签和图例。

```python
# 添加标题，坐标轴标记和图例
x = np.linspace(0, 2 * np.pi, 50)
plt.plot(x, np.sin(x), 'r-x', label='Sin(x)')
plt.plot(x, np.cos(x), 'g-^', label='Cos(x)')
plt.legend() # 展示图例
plt.xlabel('Rads') # 给 x 轴添加标签
plt.ylabel('Amplitude') # 给 y 轴添加标签
plt.title('Sin and Cos Waves') # 添加图形标题
plt.show()
```

为了给图形添加图例，我们需要在 ```plot()``` 函数中添加命名参数 ```'label'``` 并赋予该参数相应的标签。然后调用 ```legend()``` 函数就会在我们的图形中添加图例。

接下来我们只需要调用函数 ```title()```，```xlabel()``` 和 ```ylabel()``` 就可以为图形添加标题和标签。

你会得到类似于下面这张拥有标题、标签和图例的图形：

![标题](http://i2.wp.com/www.datadependence.com/wp-content/uploads/2016/04/labeling-1.png)

以上内容应该足够帮助读者开始使用 Matplotlib 和 Python 实现数据可视化，但是这些内容并不全面。我强烈建议读者亲自尝试使用这个工具，笔者也是通过这种方式掌握了这个工具。画一些图形，改变样式并使用子图功能，然后你就会很快掌握 Matplotlib 的使用方式。

这是一篇是关于如何使用 Matplotlib 和 Python 完成数据可视化的文章，也是 Python 科学计算系列文章中的第一篇。我希望读者能从中有所收获，并且对 Matplotlib 库更加熟悉。

### 不要忘记分享和关注

请记得分享这篇文章让更多的人看到它！另外，记得[订阅这个博客的邮件列表](http://eepurl.com/b7iuF5)，关注我的[Twitter](https://twitter.com/jamal_moir)并在[Google+](https://plus.google.com/101283112845335349608)上添加我，这样你就不会错过任何有价值的文章！

我会阅读所有的评论，所以无论你有什么想要说的，或者是想要分享的，甚至是问题之类的，都可以在下面留言。

***

[点此查看原文链接](http://www.datadependence.com/2016/04/scientific-python-matplotlib/)。

[Python 翻译组](https://github.com/PythonTG)是EarlGrey@编程派发起成立的一个专注于 Python 技术内容翻译的小组，目前已有近 30 名 Python 技术爱好者加入。翻译组出品的内容（包括教程、文档、书籍、视频）将在编程派微信公众号首发，欢迎各位 Python 爱好者推荐相关线索。推荐线索，可直接在编程派微信公众号推文下留言即可。
