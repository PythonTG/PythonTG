# Python 程序员都该用的一个库

title: Python 程序员都该用的一个库
author: Hynek Schlawack@TwistedMatrix
translator: linkcheng
reviewer: EarlGrey
date: 20161016
permalink: attrs-one-library-everyone-needs
keywords: python 第三方库, python attrs, 必备的第三方库, Python 设计对象

***

你写 Python 程序吗？那你应该使用 [attrs](https://attrs.readthedocs.io/)。

你问为什么？我只能说，不要问，直接用就好了。

好吧，我还是解释一下。

我热爱 Python，这十多年来一直是我的主力编程语言。尽管期间也出现过一些有意思的语言（指的是 Haskell 和 Rust），但我还不打算换到其他语言。

这不是说 Python 没有本身没有任何问题。在某些情况下，Python 会让你更容易犯错。尤其是一些库大量使用类继承，以及 [God-object](https://en.wikipedia.org/wiki/God_object) 反面模式。

导致该情况的一个原因可能是 Python 是一种非常方便的语言，所以经验欠缺的程序员犯错误后，他们就得继续[忍受下去](https://twistedmatrix.com/documents/current/core/development/policy/compatibility-policy.html)。

但我想，更重要的原因也许是，有时你努力做正确的事，但 Python 却会因此惩罚你。

在对象设计的大背景下，“正确的事“是指设计体量小并且独立的类，只做[一件事](https://en.wikipedia.org/wiki/Single_responsibility_principle)，并且把这件事做[好](https://www.destroyallsoftware.com/talks/boundaries)。例如，如果你的对象开始累积大量的私有方法，也许你应该将它们变成私有属性的公有方法。但是，这种事处理起来非常乏味，你可能就不会理会这些。

如果你有一些相关的数据，而且数据之间的关系和行为是需要进行解释的，那么应该定义为对象。在 Python 中定义元组和列表非常方便。刚开始把 `address = ...` 写成 `host, port = ...` ，可能觉得没什么关系，但很快你就会到处写 `[(family, socktype, proto, canonname, sockaddr)] = ... ` 这样的语句，这时就该后悔了。这还是算你走运的情况。如果倒霉的话，你可能得维护 `values[0][7][4][HOSTNAME][“canonical”]` 这样的代码，这时你的心情是痛苦，而不仅仅是后悔了。

***

这就提出了一个问题：在 Python 中使用类是否是麻烦？我们来看一个简单的数据结构：一个三维直角坐标。从最简单的开始：

```python
class Point3D(object):
```

到现在为止还挺好。我们已经有了一个三维点。 接下来呢？

```python
class Point3D(object):
    def __init__(self, x, y, z):
```

其实，这是有点可惜。我只想对数据的打包，但却不得不覆盖一个 Python 运行时中的特殊方法，而且命名还是约定俗成的。但还不算太坏；毕竟所有的编程语言都是按照某种形式组成的怪异符号而已。

至少可以看到属性名了，还能说得通。

```python
class Point3D(object):
    def __init__(self, x, y, z):
        self.x
```

我已经说过，我想一个 `x`，但现在必须把它指定为一个属性...

```python
class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
```

绑定到 `x` ？呃，很明显...

```python
class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
```

每个属性都得这么做一次，所以这相当糟糕？每个属性名都得敲 3 次？！？

好吧。至少定义完了。

```python
class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
```

什么，难道还没结束吗？

```python
class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return (self.__class__.__name__ +
                ("(x={}, y={}, z={})".format(self.x, self.y, self.z)))
```

拜托。现在我得每个属性名敲 5 次了，如果我想在调试时知道属性到底指的是什么的话。如果定义元组的话，就不用这一步了？！？！？

```python
class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return (self.__class__.__name__ +
                ("(x={}, y={}, z={})".format(self.x, self.y, self.z)))
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)
```

敲 7 次？！？！？！？

```python
class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return (self.__class__.__name__ +
                ("(x={}, y={}, z={})".format(self.x, self.y, self.z)))
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)
    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (self.x, self.y, self.z) < (other.x, other.y, other.z)
```

敲 9 次？！？！？！？！？

```python
from functools import total_ordering
@total_ordering
class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return (self.__class__.__name__ +
                ("(x={}, y={}, z={})".format(self.x, self.y, self.z)))
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)
    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (self.x, self.y, self.z) < (other.x, other.y, other.z)
```

好了，擦汗 - 尽管多了 2 行代码不是很好，但至少现在我们不用定义其他比较方法了。现在一切搞定了，对吧？

```python
from unittest import TestCase
class Point3DTests(TestCase):
```

你知道吗？ 我受够了。一个类码了 20 行，却还什么事都没做；我们这样做是想解四元方程，而不是定义“可以打印和比较的数据结构”。我陷入了大量无用的垃圾元组、列表和字典中；**用 Python 定义合适的数据结构是非常麻烦的**。

### 命名元组 `namedtuple` 

为解决这个难题，标准库给出的解决方案是使用 [namedtuple](https://docs.python.org/2.7/library/collections.html#collections.namedtuple) 。然而不幸的是初稿（在许多方面与[我自己](https://github.com/twisted/epsilon/blob/master/epsilon/structlike.py)的处理方式有相似的尴尬的和过时之处）`namedtuple` 仍然无法挽救这个现象。它引入了大量没有必要的公共函数，这对于兼容性维护来说简直就是一场噩梦，并且它连问题的一半都没有解决。这种做法的缺陷太多了，这里只列一些重点：

* 不管你是否希望如此，它的字段都可以通过数字索引的方式访问。这意味你不能有私有属性，因为所有属性通过公开的 `__getitem__` 接口暴露出来。
* 它等同于有相同值的原始元组，因此很容易发生类型混乱，特别是如果你想避免使用元组和列表。
* 这是一个元组，所以它总是不可变的。 

至于最后一点，你可以像这样使用：

```python
Point3D = namedtuple('Point3D', ['x', 'y', 'z'])
```

在这种情况下它看起来并不像一种类；无特殊情况下，简单的语法分析工具将不能识别它为类。但是这样你不能给它添加任何其他方法，因为没有地方放任何的方法。更别提你必须输入类的名字两次。

或者你可以使用继承：

```python
class Point3D(namedtuple('_Point3DBase', 'x y z'.split())):
    pass
```

尽管这样可以添加方法和文档字符串，看起来也像一个类，但是内部名称（在 `repr` 中显示的内容，并不是类的真实名称）变的很怪了。同时，你还不知不觉中把没列出的属性变成了可变的，这是添加 `class` 声明的一个奇怪的副作用；除非你在类主体中添加 `__slots__='X Y z'.split()`，但这样又回到了每个属性名必须敲两次的情况。

而且，我们还没提科学已经证明[不应该使用继承](https://www.youtube.com/watch?v=3MNVP9-hglc)呢。

因此，如果你只能选命名元组，那就选命名元组吧，也算是改进，虽然只是在部分情况下如此。

## 使用 `attrs`

这时该我最喜欢的 Python 库出场了。

> pip install attrs

我们重新审视一下上述问题。如何使用 `attrs` 库编写 `Point3D` ？

```python
import attr
@attr.s
```

由于它还没有内置到 Python 中，所以必须用以上 2 行开始：导入包然后使用类装饰器。

```python
import attr
@attr.s
class Point3D(object):
```

你看，没有继承！通过使用类装饰器，`Point3D` 仍然是一个普通的 Python 类（尽管我们一会会看到一些双下划线方法）。

```python
import attr
@attr.s
class Point3D(object):
    x = attr.ib()
```

添加属性 `x`。

```python
import attr
@attr.s
class Point3D(object):
    x = attr.ib()
    y = attr.ib()
    z = attr.ib()
```

再分别添加属性 `y` 和 `z`。这样就完成了。

这就 OK 了？ 等等。不用定义字符串表示吗？

```
>>> Point3D(1, 2, 3)
Point3D(x=1, y=2, z=3)
```

怎么进行比较？

```
>>> Point3D(1, 2, 3) == Point3D(1, 2, 3)
True
>>> Point3D(3, 2, 1) == Point3D(1, 2, 3)
False
>>> Point3D(3, 2, 3) > Point3D(1, 2, 3)
True
```

好的。但如果我想将有明确属性定义的数据提取为适合 JSON 序列化的格式呢？

```python
>>> attr.asdict(Point3D(1, 2, 3))
{'y': 2, 'x': 1, 'z': 3}
```

也许上边有一点点准确。即使如此，因为使用了 `attrs` 后，很多事情都变得更简单了，它允许你在类上声明字段，以及相关的元数据。

```
>>> import pprint
>>> pprint.pprint(attr.fields(Point3D))
(Attribute(name='x', default=NOTHING, validator=None, repr=True, cmp=True, hash=True, init=True, convert=None),
 Attribute(name='y', default=NOTHING, validator=None, repr=True, cmp=True, hash=True, init=True, convert=None),
 Attribute(name='z', default=NOTHING, validator=None, repr=True, cmp=True, hash=True, init=True, convert=None))
```

我不打算在这里深入介绍 `attrs` 的每一个有趣的功能；你可以[阅读它的文档](https://attrs.readthedocs.io/)。另外，项目会经常更新，每隔一段时间都会有新的东西出现，因此我也可能会漏掉一些重要的功能。但是用上 `attrs` 之后 ，你会发现它所做的正式此前 Python 所缺乏的：

1. 它让你简洁地定义类型，而不是通过手动键入 `def __init __` 的方式来定义。
2. 它让你直接地说出你声明的意思，而不是拐弯抹角的表达它。与其这样说：“我有一个类型，它被称为 MyType ，它有一个构造函数，在构造函数中用参数 'A' 给属性 'A' 赋值”，而是应该这样说：“我有一个类型，它被称为 MyType ，它有一个属性叫做 `a`，以及跟它相关的方法“，而不必通过逆向工程猜测它的方法（例如，在一个实例中运行 `dir` ，或查看 `self.__ class__. __dict__`）。
3. 它提供了有用的默认方法，而不像 Python 中的默认行为有时有用，大部分时候没用。
4. 它从简单的开始，但是提供了后续添加更严谨实现的空间。

我们详细说明最后一点。

### 逐步改善

虽然我不打算谈及每一个功能，但如果我没有提到以下几个特点，那我就太不负责任了。你可以从上面这些特别长的 `Attribute` 的 `repr()` 中看到一些有趣的东西。

例如：你通过用 `@attr.s` 修饰类来验证属性。比如：Point3D 这个类，应该包含数字。为简单起见，我们可以说这些数字为 `float` 类型，像这样：

```python
import attr
from attr.validators import instance_of
@attr.s
class Point3D(object):
    x = attr.ib(validator=instance_of(float))
    y = attr.ib(validator=instance_of(float))
    z = attr.ib(validator=instance_of(float))
```

因为我们使用了 `attrs` ，这意味着之后有机会进行验证：可以只给每个需要的属性添加类型信息。其中的一些功能，可以让我们避免常见的错误。例如，这是一个很常见的“找 Bug” 面试题：

```python
class Bag:
    def __init__(self, contents=[]):
        self._contents = contents
    def add(self, something):
        self._contents.append(something)
    def get(self):
        return self._contents[:]
```

修正它，正确的代码应该是这个样子：

```python
class Bag:
    def __init__(self, contents=None):
        if contents is None:
            contents = []
        self._contents = contents
```

额外添加了 2 行代码。

这样，`contents` 无意间就成了全局变量，这使得所有没有提供列表的 `Bag` 对象都共享一个列表。使用 `attrs` 的话，就变成这样：

```python
@attr.s
class Bag:
    _contents = attr.ib(default=attr.Factory(list))
    def add(self, something):
        self._contents.append(something)
    def get(self):
        return self._contents[:]
```

`attrs` 还提供一些其他的特性，让你在构建类时更方便更正确。另一个很好的例子？如果你严格的管控对象的属性（或在内存使用上更有效率的 CPython ），你可以在类层级上使用 `slots=True`  - 例如 `@attr.s(slots=True)` - 自动与 `attrs` 声明的 [`__slots__ `属性](https://docs.python.org/3.5/reference/datamodel.html#object.__slots__)匹配。所有这些功能会让通过 `attr.ib()` 声明的属性更好更强大。

## 未来的 Python

有人为以后能普遍使用 Python 3 编程而感到高兴。而我期待的是，能够在 Python 编程时一直用`attrs`。就我所知，它对每个使用了的代码库都产生了积极、微妙的影响。

试试看：你可能会惊讶地发现，以前用不方便写文档的元组、列表或字典的地方，现在可以使用具备清晰解释的类了。既然编写结构清晰的类型如此简单方便，以后应该会经常使用 `attrs` 的。这对你的代码来说是件好事；我就是一个好例子。

[点此查看原文。](https://glyph.twistedmatrix.com/2016/08/attrs.html)