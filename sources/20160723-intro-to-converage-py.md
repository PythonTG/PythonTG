## 如何测试代码覆盖率：coverage.py 简介

title: 如何测试代码覆盖率：coverage.py 简介
author: Mike Driscoll
translator: linkcheng
reviewer: EarlGrey
date: 20160723
permalink: an-intro-to-coverage-py
keywords: coverage.py, 测试覆盖率, 代码测试, 单体测试

***


**Coverage.py**  是一个用来测试代码覆盖率的 Python 第三方库。它起初是由 Ned  Batchelder 创建。在编程界，术语“覆盖”通常是用来描述测试的有效性，以及测试的实际覆盖率。coverage.py 库支持 Python 2.6 或者更高的版本，还兼容 Python 3 的最新版以及 PyPy 。

```
pip install coverage
```

执行以上指令来安装 coverage.py ，不过我们需要写一些代码才能使用它。创建一个名为 **mymath.py** 的模块，代码如下：

```python
def add(a, b):
	return a + b


def subtract(a, b):
	return a - b


def multiply(a, b):
	return a * b


def divide(numerator, denominator):
	return float(numerator) / denominator
```

现在需要一个测试文件。接下来，我们创建一个测试 **add** 函数的测试文件，并将其命令为 **test_mymath.py** 。然后把它保存在与 mymath.py 的相同目录下。接着在测试文件中写入以下代码：

``` python
# test_mymath.py
import mymath
import unittest

class TestAdd(unittest.TestCase):
	"""
	Test the add function from the mymath library
	"""

	def test_add_integers(self):
		"""
		Test that the addition of two integers returns the correct total
		"""
		result = mymath.add(1, 2)
		self.assertEqual(result, 3)

	def test_add_floats(self):
		"""
		Test that the addition of two floats returns the correct result
		"""
		result = mymath.add(10.5, 2)
		self.assertEqual(result, 12.5)

	def test_add_strings(self):
		"""
		Test the addition of two strings returns the two string as one
		concatenated string
		"""
		result = mymath.add('abc', 'def')
		self.assertEqual(result, 'abcdef')


if __name__ == '__main__':
	unittest.main()
```

一切准备就绪，让我们使用测试文件来运行 coverage.py。打开终端并且进入我们刚才写的那两个文件所在的目录。然后通过以下方式执行 coverage.py：

```
coverage run test_mymath.py
```

注意，我们需要调用 **run** 才能让 coverage.py 运行指定的模块。如果模块接收参数，可以像正常运行这个的模块一样带上参数。当执行以上指令后，你会看到测试模块的输出，就像正常运行该模块一样。在当前目录下，你还会发现一个名字为 **.coverage** 的文件（注意开头的点号）。要想获得文件中的信息，需要执行以下指令：

```
coverage report -m
```

执行这条指令将会在终端打印以下信息：

```
Name             Stmts   Miss  Cover   Missing
----------------------------------------------
mymath.py            9      3    67%   9, 13, 17
test_mymath.py      14      0   100%
----------------------------------------------
TOTAL
```

**-m** 选项告诉 coverage.py 你想在输出信息中显示 **Missing** 列。如果省略 **-m** 选项，就只能看到前四列信息。上面的输出表明，coverage 在执行完测试代码之后，判断我写的单体测试程序对 mymath 模块的覆盖率只有 67% 。 “Missing” 列表明哪些行代码没有被覆盖。如果你看过 coverage.py 指出的那些行代码，很快就会发现测试程序没有运行测试 **subtract**, **multiply** 和 **divide** 函数。

在尝试添加更多的覆盖率测试代码之前，先来学习一下怎么通过 coverage.py 来生成 HTML报告。只需要执行以下命令即可：

```
coverage html
```

以上指令将会生成一个叫 **htmlcov** 的目录，其中包括各种各样的文件。进入这个目录，并通过浏览器打开 **index.html** 文件。在我的电脑上，浏览器加载了这样的页面：

![chp26_coverage_index](http://www.blog.pythonlibrary.org/wp-content/uploads/2016/07/chp26_coverage_index.png)

实际上，你可以通过点击 Module 列中列出的文件名来打开一个新的页面，页面中将会明显标识出代码中没有被单体覆盖的部分。显然 mymath.py 的覆盖率不够高，所以点击 mymath.py ，页面最终显示如下：

![chp26_mymath_coverage](http://www.blog.pythonlibrary.org/wp-content/uploads/2016/07/chp26_mymath_coverage.png)

以上截图清晰地展示了没有被单体测试所覆盖的部分。现在我们清楚地知道测试覆盖有哪些缺失了，接下来就给 **subtract** 函数添加单体测试，并且看一下覆盖率的改变。

打开 **test_mymath.py** 并且添加下边的类：

``` python
class TestSubtract(unittest.TestCase):
	"""
	Test the subtract function from the mymath library
	"""

	def test_subtract_integers(self):
		"""
		Test that subtracting integers returns the correct result
		"""
		result = mymath.subtract(10, 8)
		self.assertEqual(result, 2)
```

现在我们需要重新对更新后的测试文件运行 coverage。你只需要再次运行该命令即可：**coverage run test_mymath.py**。命令输出将指出成功通过了四个测试。接着，重新运行 **coverage html**，再打开 index.html 文件。你应该会看到我们达到了 78% 的覆盖率：

![chp26_subtract_coverage](http://www.blog.pythonlibrary.org/wp-content/uploads/2016/07/chp26_subtract_coverage.png)

这次修改让覆盖率提高了 11% ！接下来，让我们给 multiply 和 divide 函数添加简单的测试，看覆盖率能否达到 100% ！

``` python
class TestMultiply(unittest.TestCase):
	"""
	Test the multiply function from the mymath library
	"""

	def test_subtract_integers(self):
		"""
		Test that multiplying integers returns the correct result
		"""
		result = mymath.multiply(5, 50)
		self.assertEqual(result, 250)


class TestDivide(unittest.TestCase):
	"""
	Test the divide function from the mymath library
	"""

	def test_divide_by_zero(self):
		"""
		Test that multiplying integers returns the correct result
		"""
		with self.assertRaises(ZeroDivisionError):
			result = mymath.divide(8, 0)
```

再次运行之前运行过的命令，然后再重新打开 “index.html”。然后就会看到如下截图：

![测试覆盖率报告](http://www.blog.pythonlibrary.org/wp-content/uploads/2016/07/chp26_full_coverage.png)

正如你看到的那样，这次我们的覆盖率达到了 100%！显然，覆盖率 100% 意味着我们测试程序测试了每一个需要被测试的函数。当然这也有些不尽人意的地方，比如：add 函数的单体测试数量是其他几个函数的三倍，然而 coverage.py 并没有给出关于这些的详细信息。尽管 coverage.py 不能详尽说明我们是否测试了所有可能的参数组合情况，但却可以明确反映关于覆盖率的一些基本信息。

### 额外信息

顺便再简单提及一些 coverage.py 的其他特性。首先，coverage.py 支持配置文件。配置文件格式是传统的“.ini”文件，使用中括号作为节与节的分界（例如：[my_section]）。还可以使用 # 或者 ; （分号）来添加注释。

Coverage.py 也允许在上述提到的配置文件中指定你需要解析的源文件。一旦在配置文件中设置了需要解析的文件，就可以通过运行 coverage.py 来看运行结果。它还支持“-source”命令行选项。最后，还可以使用“-include”和“-omit”选项来包含或者移除一个文件名模式的列表。这些选项也可以通过在配置文件中添加对应的配置项进行设置。

关于 coverage.py 想最后再说明一点，就是它支持插件。你可以自己写插件，也可以从网上下载并安装别人的插件来增强 coverage.py 的功能。

### 总结

现在你已经了解 coverage.py 的基本情况以及它的一些用途。Coverage.py 可以检测单体测试代码并且发现单体测试覆盖中的漏洞。如果不确定你的单体测试程序是否达标，那么使用这个库包将会帮助你找到那些存在的漏洞。即便如此，你仍然需要认真负责地编写高质量的测试程序。如果没有写出有效的测试，而且测试还通过了，那么 coverage.py 也无法帮到你。

***

[点此查看原文链接](http://www.blog.pythonlibrary.org/2016/07/20/an-intro-to-coverage-py/)。

[Python 翻译组](https://github.com/PythonTG)是EarlGrey@编程派发起成立的一个专注于 Python 技术内容翻译的小组，目前已有近 30 名 Python 技术爱好者加入。

翻译组出品的内容（包括教程、文档、书籍、视频）将在编程派微信公众号首发，欢迎各位 Python 爱好者推荐相关线索。

推荐线索，可直接在编程派微信公众号推文下留言即可。


