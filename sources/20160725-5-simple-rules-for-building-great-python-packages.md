# 践行这五条原则，构建优秀的Python包

title: 践行这5条原则，即可构建优秀的Python包
author: mssaxm
translator: liubj2016
reviewer: EarlGrey
date: 20160725
permalink: 5-simple-rules-for-building-great-python-packages
keywords: 构建Python包, init.py, 设计模式, 循环依赖, 五条原则, 导入顺序, 

***

构建一个[包](http://docs.python.org/2/tutorial/modules.html#packages)貌似很简单，只要把一堆[模块](http://docs.python.org/2/tutorial/modules.html)都放进一个有 `__init__.py` 文件的目录里面就行了，对吧？可能看上去简单粗暴，但是随着对包的修改越来越多，设计不好的包就会产生循环依赖问题，而且会变得臃肿、脆弱。

![image](https://axialcorps.files.wordpress.com/2013/08/ryanlerch_roundabout_sign.png?w=200&h=178)

遵循这五个简单的原则，有助于避免这些常见的坑，让你的包能够使用的更久，变得更强大。

## 1. `__init__.py` 只是用来导入包

如果是一个简单的包，你可能会很想把辅助方法、工厂和异常，一股脑都丢进 `__init__.py` 中。千万不要这样做。

格式良好的`__init__.py`有一个重要作用：导入子模块。你的 `__init__.py` 应该像这样：


```python
# 导入顺序很重要 —— 有些模块依赖于其他模块
from exceptions import FSQError, FSQEnvError, FSQEncodeError,\
                       FSQTimeFmtError, FSQMalformedEntryError,\
                       FSQCoerceError, FSQEnqueueError, FSQConfigError,\
                       FSQPathError, FSQInstallError, FSQCannotLockError,\
                       FSQWorkItemError, FSQTTLExpiredError,\
                       FSQMaxTriesError, FSQScanError, FSQDownError,\
                       FSQDoneError, FSQFailError, FSQTriggerPullError,\
                       FSQHostsError, FSQReenqueueError, FSQPushError 

# constants 依赖于：exceptions，internal
import constants

# const 依赖于：constants，exceptions，internal
from const import const, set_const # has tests

# path 依赖于：exceptions，constants，internal
import path # has tests

# lists 依赖于：path
from lists import hosts, queues

#...
```

## 2. 用 `__init__.py` 限制导入的顺序

在上面的[例子](https://github.com/axialmarket/fsq/blob/master/fsq/__init__.py)中，`__init.py` 解决了两个问题：  

1. 在包的作用域中暴露方法和类，用户不必深入到包的内部结构，即可轻松使用包。  
2. 协调导入顺序的唯一位置。

运用得好的话，`__init.py` 可以让你灵活地再组织包的内部结构，而不需要担心内部子模块导入或每个模块的导入顺序带来的副作用。由于你按照某种特定的顺序导入子模块，你的`__init__.py`可以很容易被其他程序员理解，并且可以说明该包所提供的功能。

在包这一级，一个文档字符串以及 `__all__` 属性赋值，就是你的`__init__.py`中唯一的非导入代码：


```python
__all__ = [ 'FSQError', 'FSQEnvError', 'FSQEncodeError', 'FSQTimeFmtError',
            'FSQMalformedEntryError', 'FSQCoerceError', 'FSQEnqueueError',
            'FSQConfigError', 'FSQCannotLock', 'FSQWorkItemError',
            'FSQTTLExpiredError', 'FSQMaxTriesError', 'FSQScanError',
            'FSQDownError', 'FSQDoneError', 'FSQFailError', 'FSQInstallError',
            'FSQTriggerPullError', 'FSQCannotLockError', 'FSQPathError',
            'path', 'constants', 'const', 'set_const', 'down', 'up',
            # ...
          ]
```

## 3. 用一个模块定义所有的异常

你可能已经注意到了，在`__init__.py`的开头，通过一个单一的子模块 `exceptions.py` 导入了所有的异常。这与在大多数包中看到的不同，大多数的包会在抛出异常的代码附近来定义异常。虽然这可以使得模块更加紧密，但是当包足够复杂的时候，则会出现问题，有下面两种情况：

1. 通常，模块/程序需要导入一个子模块来获取一个函数，这个函数可以导入并且使用抛出异常的代码。为了捕获更高粒度的异常，你需要同时导入你需要的模块以及定义了异常的模块（或者更糟，需要链式导入异常）。这种衍生出来的导入要求，只是将你的包中的导入关系变复杂的第一步。你使用这种模式的次数越多，包的相互依赖性就越强，更容易出错。  
2. 随着异常越来越多，找到所有包能够抛出的错误会越来越难。在一个模块中定义所有的异常，可以让程序员轻易地检查确定你的包抛出所有潜在错误情况。

你应该在包中定义一个基类异常：

```python
class APackageException(Exception):
    '''root for APackage Exceptions, only used to except any APackage error, never raised'''
    pass
```

然后，确保在所有错误情况下，你的包抛出的异常都是这个基类异常的子类，这样如果你需要的话，就可以禁止所有的异常：

```python
try:
    '''bunch of code from your package'''
except APackageException:
    '''blanked condition to handle all errors from your package'''
```

对于一些通用的错误情况，已经在标准库中包含了想要的异常（比如 `TypeError`、`ValueError`等）。

定义足够多的异常，并且要有充足的颗粒度：

```python
# from fsq
class FSQEnvError(FSQError):
    '''An error if something cannot be loaded from env, or env has an invalid
       value'''
    pass

class FSQEncodeError(FSQError):
    '''An error occured while encoding or decoding an argument'''
    pass
# ... and 20 or so more
```

异常的[粒度](https://github.com/axialmarket/fsq/blob/master/fsq/exceptions.py)越高，程序员就可以使用 `try / except`，包裹住越大的代码块：

```python
# 像这样
try:
   item = fsq.senqueue('queue', 'str', 'arg', 'arg')
   scanner = fsq.scan('queue')
except FSQScanError:
   '''do something'''
except FSQEnqueueError:
   '''do something else'''

# 而不是这样
try:
    item = fsq.senqueue('queue', 'str', 'arg', 'arg')
except FSQEnqueueError:
    '''do something else'''
try:
    scanner = fsq.scan('queue')
except FSQScanError:
    '''do something'''

# 千万不要这样
try:
    item = fsq.senqueue('queue', 'str', 'arg', 'arg')
    try:
        scanner = fsq.scan('queue')
    except FSQScanError:
        '''do something'''
except FSQEnqueueError:
    '''do something else'''
```

异常定义中的高粒度，使得错误处理更简单易懂，并且可以将常规指令和错误操作指令分组归类，使代码变得容易理解和维护。

## 4. 在包中只进行相对导入

在子模块中最容易犯的错误就是，使用包自身的名字来导入包：

```python
# within a sub-module
from a_package import APackageError
```

这一语句会导致如下两种不好的结果：

1. 只有当这个包安装在 `python` 环境变量路径 PYTHONPATH 中的时候，这个子模块才会正常运行。  
2. 只有当包的名字是 `a_package` 的时候，这个子模块才会正常运行。

第一条好像不是什么大问题，但是如果你的环境变量路径中不同的目录下安装了两个同名的包，你的子模块可能会导入另一个包，你无意间的失误将会让程序员（或者就是你自己）调试很久。与其使用你自己的包的名字，不如在包中采用相对导入：

```python
# within a sub-module 
from . import FSQEnqueueError, FSQCoerceError, FSQError, FSQReenqueueError,\
              constants as _c, path as fsq_path, construct,\
              hosts as fsq_hosts, FSQWorkItem
from . internal import rationalize_file, wrap_io_os_err, fmt_time,\
                      coerce_unicode, uid_gid
# you can also use ../... etc. in sub-packages.
```

## 5. 保持模块小巧

模块应该尽量小巧。记住，程序员在使用你的包时，将会从包的作用域中导入，而你可以使用 `__init__.py` 作为一个管理工具，连贯地暴露接口。

一个很好的经验是，在每个模块中只定义一个类，以及所需要的任何辅助方法和工厂方法：

```python
class APackageClass(object):
    '''One class'''

def apackage_builder(how_many):
    for i in range(how_many):
        yield APackageClass()
```

如果模块中有要暴露出来的方法，那么就将相互依赖的方法放到一个模块中，将不相互关联的方法移到其他模块：


```python
####### EXPOSED METHODS #######
def enqueue(trg_queue, item_f, *args, **kwargs):
    '''Enqueue the contents of a file, or file-like object, file-descriptor or
       the contents of a file at an address (e.g. '/my/file') queue with
       arbitrary arguments, enqueue is to venqueue what printf is to vprintf
    '''
    return venqueue(trg_queue, item_f, args, **kwargs)

def senqueue(trg_queue, item_s, *args, **kwargs):
    '''Enqueue a string, or string-like object to queue with arbitrary
       arguments, senqueue is to enqueue what sprintf is to printf, senqueue
       is to vsenqueue what sprintf is to vsprintf.
    '''
    return vsenqueue(trg_queue, item_s, args, **kwargs)

def venqueue(trg_queue, item_f, args, user=None, group=None, mode=None):
    '''Enqueue the contents of a file, or file-like object, file-descriptor or
       the contents of a file at an address (e.g. '/my/file') queue with
       an argument list, venqueue is to enqueue what vprintf is to printf
       if entropy is passed in, failure on duplicates is raised to the caller,
       if entropy is not passed in, venqueue will increment entropy until it
       can create the queue item.
    '''
    # setup defaults
    trg_fd = name = None
    # ...
```

上面的例子 [`fsq/enqueue.py`](https://github.com/axialmarket/fsq/blob/master/fsq/enqueue.py)，暴露了一组函数，它们提供了同一功能的不同接口（类似于 `simplejson` 中的 `load/loads`）。虽然这个例子很简单直白，但是要做到保持模块小巧，需要一定的判断力，不过一个很少的做法是：  

如不确定，则新建模块。

***

[点此查看原文链接](https://axialcorps.com/2013/08/29/5-simple-rules-for-building-great-python-packages/)。

[Python 翻译组](https://github.com/PythonTG)是EarlGrey@编程派发起成立的一个专注于 Python 技术内容翻译的小组，目前已有近 30 名 Python 技术爱好者加入。

翻译组出品的内容（包括教程、文档、书籍、视频）将在编程派微信公众号首发，欢迎各位 Python 爱好者推荐相关线索。

推荐线索，可直接在编程派微信公众号推文下留言即可。
