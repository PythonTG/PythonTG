# 用代码作画

title: 用代码作画
author: 王海磊
translator: 唐晓霆 Jason
reviewer: EarlGrey
date: 20160816
permalink: painting-with-code/
keywords: 生成艺术, generative art, 代码作画, 代码和艺术, 代码油画

***

> 作者王海磊是 IDEO 上海办公室的设计总监。他大部分时间在设计和开发 APP，同时探索在艺术和设计领域利用生成艺术方法的可能，尤其是在 3D 打印领域。

> 译者简介：唐晓霆，在香港的成都人，城市大学研究助理，会写python，兴趣是深度学习。

白天，我给APP写代码，设计用户体验。有空的时候，我搞艺术。最近我开始在代码和艺术上同时探索 ---- 我开始探索[**生成艺术**（generative art）](https://en.wikipedia.org/wiki/Generative_art)，一个电脑编程和视觉艺术的绝佳结合领域。动态**生成艺术**，或者叫做代码生成的艺术，是一种新的艺术形式。懂艺术的程序员用参数和命令来实现他们心中的艺术畅想。但是制作动态**生成艺术**在很大程度上与绘画和其他传统艺术差不多。

当你创作一幅油画的时候，你先要有灵感，并把它简单地画在纸上。然后你才开始调试颜料、笔刷和画板，再不断完善油画里的各种元素直到满意。在制作动态**生成艺术**的时候，我采用相似的方法。当一些事情启发我的时候 ---- 不论它是一幅地理杂志周刊上的等高线图，一个数学公式的图表，还是我老爸工作坊里各种不同的机械工具 ---- 我就会在纸上给它画个草图，然后写下最能描述这个灵感的关键字。接着，我就会坐在我的电脑前，开始敲打出可以“画出”合我心意的“笔刷”的代码（用的是 [Python 这门编程语言](https://en.wikipedia.org/wiki/Python_(programming_language)）。然后在电脑上跑代码，生成图片，修改，这样不断重复，直到这些代码输出能够完美表达我心意的形状、颜色、透明度和阴影。

我用电脑的计算能力来生成艺术品。当传统艺术家掏出颜料和笔刷来表达颜色和形状的时候，我其实做的是相同的事，只不过用了参数的方式。举个例子来说，我为画出波浪，定义了一个[调色板](https://gist.github.com/wanghailei/9ebd5511c9c48ac903c0), 像这样：

``` python
palette_for_wave = [colors.hex("#020034", "dark blue"),
                    colors.hex("#0A5CD6", "aqua blue"),
                    colors.hex("#FEFFFF", "milk white")]
```

我把电脑当做是一只举着画笔的手，通过输入[命令代码](https://gist.github.com/wanghailei/9ebd5511c9c48ac903c0)告诉它如何画画，比如 `draw_wave` ：

```python
def draw_wave(path, palette_for_wave) :
	stroke_width( choice( [random(0.1, 100), random(1, 1000)]))
	stroke( choice(palette_for_wave))
	cornu.draw_path(path, close = False, flat = True)
```

## 欢乐的随机数

虽然我代码里面大多数的参数都是静态的，我也加了一个使得部分参数随机生成的算法，这可以使得图像里的视觉元素在一个指定范围内随机变动。这样的话，最后的图像就是无法预测的了。我永远没有办法精确地知道会生成什么样的图片。

这个函数随机地返回一个 0.1 到 0.7 之间的浮点数：

``` python
random( 0.1, 0.7 )
```

这些随机参数不仅仅不可预测，而且是不可重复的，所以这些图片不能被重复生成 ---- 它们完全是独特的。

## 算法也是艺术

计算机图形是基于数学的，所以当我用代码画画的时候，我其实是在探索和可视化数学的结构、抽象和复杂度之美，而这些在日常生活中是很难观察到的。在我探索新的算法，看看它能生成什么样的图片的时候，我有时会受到启发，进而把这些灵感变为艺术，比如下面的[海啸](https://gist.github.com/wanghailei/9ebd5511c9c48ac903c0)。在探索一个叫做[Cornu Curve](https://www.nodebox.net/code/index.php/Cornu)的算法时，我产生了这个系列画作的灵感。这个算法能用夸张的波浪生成无与伦比的视觉效果。用[同样的代码](https://gist.github.com/wanghailei/9ebd5511c9c48ac903c0)， 我用数百条透明度和蓝色深浅不一的曲线制作了六张不同的图片。

![代码生成的画作](https://labs.ideo.com/wp-content/uploads/2014/06/Tsunami_1.jpg)
![代码生成的画作](https://labs.ideo.com/wp-content/uploads/2014/06/Tsunami_2.jpg)
![代码生成的画作](https://labs.ideo.com/wp-content/uploads/2014/06/Tsunami_3.jpg)
![代码生成的画作](https://labs.ideo.com/wp-content/uploads/2014/06/Tsunami_4.jpg)
![代码生成的画作](https://labs.ideo.com/wp-content/uploads/2014/06/Tsunami_5.jpg)
![代码生成的画作](https://labs.ideo.com/wp-content/uploads/2014/06/Tsunami_6.jpg)

## 无限的复杂度

用代码创作艺术让我可以制作一些用手永远无法描绘出的艺术，比如[All Seeing Eye](https://gist.github.com/wanghailei/ad3b609a85dd5f0fd0b2)。这幅图是由上百万条线和上百个图层组合而成，而且每条线都有它自己的阴影、模糊度和透明度。

![All Seeing Eye](https://labs.ideo.com/wp-content/uploads/2014/06/All-See-Eye-No_post.jpg)

我的目标是用复杂的纹理来创造一种让观众误以为是眼睛的视觉效果。用计算机来做这种重复、复杂的工作，然后变成艺术，实在让我激动。一个由数以百万计的形状组成的艺术品只需要花几分钟就能画出。如果用人手来画的话，同样一件艺术可能要花一个人十年的时间完成。

![All Seeing Eye](https://labs.ideo.com/wp-content/uploads/2014/06/All-Seeing-Eye-No_detail.jpg)

就像一个画家会选择对他来说最好的工具一样，我在[下面的代码](https://gist.github.com/wanghailei/ad3b609a85dd5f0fd0b2)里，定义了一支拥有合适特征的笔刷。有了这支笔刷，我就能创造出我想要的线条。


``` python
def composeimage( x, y, colr, radius, points, diminish ) :
	nofill()
	stroke()
	strokewidth( 0.05 )
	autoclosepath( False )
	count = int( radius * 1.3 )
	colr = colors.color( colr )
	grad = colors.gradient( colr.darken( 1.0 ), colr, colr.lighten( 1.0 ).desaturate( 0.4 ), steps = count )
	for i in range( count ) :
		stroke( grad[ i ] )
		a = 0.75 - 0.25 * float( i ) / count
		colors.shadow( dx = 5, dy = 8, alpha = a, blur = 15 )
		path = oval( x - radius + i * 0.5, y - radius + i * 0.5,
		radius * 2 - i, radius * 2 - i, draw = False )
		drawpath( brushpaint( path, points = int( points - i * 0.2 ), length = radius - i + random( count - i ) / 3, diminish = diminish ) )
```

之后， 就像画家会用特定的技巧去创造视觉艺术一样，我用[下面的代码](https://gist.github.com/wanghailei/ad3b609a85dd5f0fd0b2)告诉计算机如何控制我创造的笔刷：

``` python
def brushpaint( path, points = 100, length = 100, diminish = 700 ) :
	beginpath( 0, 0 )
	for ap in path.points( points ) :
		angle = geo.angle( ap.x, ap.y, ap.ctrl1.x, ap.ctrl1.y )
		dx,dy = geo.coordinates( ap.x, ap.y, length, angle + 90 )
		moveto( ap.x, ap.y )
		curveto( ap.x + random( -diminish, diminish ),  ap.y + random( -diminish, diminish ), dx + random( -diminish, diminish ), dy + random( -diminish, diminish ), dx, dy )
		return endpath( draw = False )
```

## 功能性设计

**生成艺术**激动人心的地方不止在于创作艺术，而且在于它的实用性。我们可以为时尚产业量身定做独特的织物纹理，我们也可以比二维创作更进一步，去创作雕塑、家具甚至建筑设计。

为这篇博客，我开发了一个可以生成独特的 IDEA LABS 图像的[算法](https://gist.github.com/wanghailei/a95ceaa8c662e33cf3e3)：

![IDEA LABS 图像](https://labs.ideo.com/wp-content/uploads/2014/06/IDEO_labs_image_1.jpg)

[这个代码](https://gist.github.com/wanghailei/a95ceaa8c662e33cf3e3)告诉计算机随机地在图像上摆放不同颜色、透明度和线宽的小圆圈，并且让它们按一定的字母路径排列。这个路径还可以表现字体（这里用的是Courier）。

``` python
font( "Courier", 200 )
align( CENTER )
text_path_line_1 = textpath( "IDEO", 0, 200, width = WIDTH)
text_path_line_2 = textpath( "LABS", 0, 350, width = WIDTH)

resx = 200
resy = 80
rx = 2.0
ry = 1.5
dotsize = 5.5
dx = WIDTH  / float( resx )
dy = HEIGHT / float( resy )

def draw_text() :
	nofill()
	strokewidth( random( 0.2, 2.8 ) )
	clr = choice( [ colors.hex( "#FF0000" ), colors.hex( "#FF0033" ), colors.hex( "#000000" ), colors.hex( "#FF0011" ), colors.hex( "#000000" ) ]   )
	clr.a = random( 0.6, 1 )
	stroke( clr )
	oval( pointx + random( -rx, rx ), pointy + random( -ry, ry ), size, size )

for x, y in grid( resx, resy ) :
	size = choice( [ 1, 2, 2, 2, 3, 3, 3, dotsize ] )
	pointx = x * dx - size
	pointy = y * dy - size
	if text_path_line_1.contains( pointx, pointy ) or text_path_line_2.contains( pointx, pointy ) :
		draw_text()
```

![IDEA LABS](https://labs.ideo.com/wp-content/uploads/2014/06/IDEO_labs_image_2.jpg)

通过用代码创作艺术，我一直在努力探索创造视觉艺术的新可能。电脑在许多方面都变革了人类的生活，现在，**生成艺术**也有可能变革艺术表现方式，给创新提供无限的空间。

***

[点此阅读原文链接](https://labs.ideo.com/2014/06/04/painting-with-code/)

[Python 翻译组](https://github.com/PythonTG)是EarlGrey@编程派发起成立的一个专注于 Python 技术内容翻译的小组，目前已有近 30 名 Python 技术爱好者加入。

翻译组出品的内容（包括教程、文档、书籍、视频）将在编程派微信公众号首发，欢迎各位 Python 爱好者推荐相关线索。

推荐线索，可直接在编程派微信公众号推文下留言即可。
