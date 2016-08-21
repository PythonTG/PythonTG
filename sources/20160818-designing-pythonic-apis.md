# 设计符合 Python 理念的应用编程接口

title: 设计符合 Python 编程理念的应用编程接口
author: noamelf
translator: linkmyth
reviewer: EarlGrey
date: 20160813
permalink: designing-pythonic-apis
keywords: requests库设计, python API设计, 应用编程接口设计, urllib库, python标准库

***


本文参考了 Kenneth Reitz 的 [Requests 库](http://docs.python-requests.org/en/master/) 的 API 设计。

编写软件包（库）时，设计良好的 API 与软件包的功能同样重要（当然，前提是你想让别人使用），那么好的 API 的标准是什么？在本文中，笔者将会比较 Requests 库和 Urllib 库（属于 Python 标准库）在一些典型的 HTTP 使用场景下的差异，并依此发表一些笔者的看法，同时讨论一下 Requests 库为何在 Python 用户群中成为实际上的标准库。

接下来的讨论中我们将会用到 **Python 3.5** 和 **Requests 2.10.0**。

这篇文章改编自上周我在本地的 Python 聚会上的[演讲](http://www.meetup.com/PyWeb-IL/events/232724175/)。读者可以在[这里](http://noamelf.com/designing-pythonic-apis-talk/#/)找到演讲的幻灯片。

## Requests 和 Urllib

### 用例 1：发送 Get 请求

```python
import urllib.request
urllib.request.urlopen('http://python.org/')
```

```
<http.client.HTTPResponse at 0x7fdb08b1bba8>
```

```python
import requests
requests.get('http://python.org/')
```

```
<Response [200]>
```

#### 明确（API 端点）优于隐晦

- Requests 库发送请求的目的更加简明（因此也更加清晰）
- Urllib 库是在省略```data```参数的情况下发送 Get 请求，这种方式要更加隐晦
- Requests 库的函数名清晰地解释了函数的用途

#### 有用的对象表示法

- 读者观察后可以发现，Requests 库返回一个包含请求状态码的字符串（这是通过```__repr()__```方法实现的）
- Urllib 库只返回默认的（模糊的）对象表示

#### 代码片段

[requests/api.py](https://github.com/kennethreitz/requests/blob/v2.10.0/requests/api.py)：

```python
def request(method, url, **kwargs):
    with sessions.Session() as session:
        return session.request(method=method, url=url, **kwargs)

def get(url, params=None, **kwargs):
    kwargs.setdefault('allow_redirects', True)
    return request('get', url, params=params, **kwargs)

def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs)
```

- 所有的 HTTP 动作在发送之前都会有类似的处理流程，因此这里实现一个```request()```函数作为主要的流程控制函数。
- 所有的 HTTP 动作都有一个对应的“辅助函数”，然后在辅助函数中调用```request()```函数，这使得我们的函数调用更加明确。

### 用例 2：获取请求状态码

```python
import urllib.request
r = urllib.request.urlopen('http://python.org/')
r.getcode()
```

```
200
```

```python
import requests
r = requests.get('http://python.org/')
r.status_code
```

```
200
```

#### 不需要 getters 和 setters

- 通过读取属性的方式（而不是调用方法）获取对象的特性能使代码更加清晰。
- 如果读者接触过其他面向对象的语言（比如说 Java），你可能会通过设置 getters 和 setters 来修改对象的属性。在 Python 中则不必如此，读者只需使用 ```@property```装饰器就能完成这一目标。

#### 代码片段

[http/client.py](https://github.com/python/cpython/blob/3.5/Lib/http/client.py#L737):

```python
class HTTPResponse(io.BufferedIOBase):

    # ...

    def getcode(self):
        return self.status
```

- Urllib 库（或者说 http）用一个“getter”方法返回类的属性

### 用例 3：编码、发送和解码 POST 请求

```python
import urllib.parse
import urllib.request
import json

url = 'http://www.httpbin.org/post'
values = {'name' : 'Michael Foord'}

data = urllib.parse.urlencode(values).encode()
response = urllib.request.urlopen(url, data)
body = response.read().decode()
json.loads(body)
```

```python
import requests

url = 'http://www.httpbin.org/post'
data = {'name' : 'Michael Foord'}

response = requests.post(url, data=data)
response.json()
```

#### 常用功能要易于使用

- Requests 库提供了预置的方法来实现编码数据以及解析 JSON 响应，然而读者在使用 Urllib 库时需要自己实现这些方法。
- 在设计 API 时读者需要思考：软件包最主要的用途是什么？可以添加哪些接口能更方便的满足这些用途？

同样地，Requests 库也为发送 JSON 数据提供了一种优雅的方式：

```python
import requests

url = 'http://www.httpbin.org/post'
data = {'name' : 'Michael Foord'}

response = requests.post(url, json=data)
response.json()
```

### 用例 4：发送验证过的请求

下面的代码为 HTTP 请求完成了长期的身份认证，同时发送了一个请求：

```python
import urllib.request

gh_url = 'https://api.github.com/user'

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, gh_url, 'user', 'pswd')
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

opener = urllib.request.build_opener(handler)
opener.open(gh_url)
```

```python
import requests

session = requests.Session()
session.auth = ('user', 'pswd')
session.get('https://api.github.com/user')
```

但是如果我们只需完成一次 HTTP 请求？是否还需要这么多代码？使用 Requests 库只需要下面的代码就可以完成：

```python
import requests

requests.get('https://api.github.com/user', auth=('user', 'pswd'))
```

#### 同时包含简单用法和高级用法

- Requests 库既有发送单个请求的简单用法，也拥有发送多个请求的复杂用法。
- 不要让用户在完成简单任务时也需要经过漫长的过程。

#### 尽量使用 Python 内建的数据结构，而不是创建新的数据结构

- Requests 库使用 Python 内建的数据结构，这使得它非常易于使用。用户不需要了解 Requests 库内部的结构。

#### 库代码

[requests/models.py](https://github.com/kennethreitz/requests/blob/v2.10.0/requests/models.py#L488)

```python
def prepare_auth(self, auth, url=''):
    """Prepares the given HTTP auth data."""

    # ...

    if auth:
        if isinstance(auth, tuple) and len(auth) == 2:
            # special-case basic HTTP auth
            auth = HTTPBasicAuth(*auth)
```

- Requests 库在内部将 ```(user, pass)``` 元组转化为一个身份验证类

### 用例 5：处理错误

```python
from urllib.request import urlopen
response = urlopen('http://www.httpbin.org/geta')
response.getcode()
```

```
---------------------------------------------------------------------------

HTTPError                                 Traceback (most recent call last)

<ipython-input-45-5fba039d189a> in <module>()
      1 from urllib.request import urlopen
----> 2 response = urlopen('http://www.httpbin.org/geta')
      3 response.getcode()


/usr/lib/python3.5/urllib/request.py in urlopen(url, data, timeout, cafile, capath, cadefault, context)
    161     else:
    162         opener = _opener
--> 163     return opener.open(url, data, timeout)
    164
    165 def install_opener(opener):


/usr/lib/python3.5/urllib/request.py in open(self, fullurl, data, timeout)
    470         for processor in self.process_response.get(protocol, []):
    471             meth = getattr(processor, meth_name)
--> 472             response = meth(req, response)
    473
    474         return response


/usr/lib/python3.5/urllib/request.py in http_response(self, request, response)
    580         if not (200 <= code < 300):
    581             response = self.parent.error(
--> 582                 'http', request, response, code, msg, hdrs)
    583
    584         return response


/usr/lib/python3.5/urllib/request.py in error(self, proto, *args)
    508         if http_err:
    509             args = (dict, 'default', 'http_error_default') + orig_args
--> 510             return self._call_chain(*args)
    511
    512 # XXX probably also want an abstract factory that knows when it makes


/usr/lib/python3.5/urllib/request.py in _call_chain(self, chain, kind, meth_name, *args)
    442         for handler in handlers:
    443             func = getattr(handler, meth_name)
--> 444             result = func(*args)
    445             if result is not None:
    446                 return result


/usr/lib/python3.5/urllib/request.py in http_error_default(self, req, fp, code, msg, hdrs)
    588 class HTTPDefaultErrorHandler(BaseHandler):
    589     def http_error_default(self, req, fp, code, msg, hdrs):
--> 590         raise HTTPError(req.full_url, code, msg, hdrs, fp)
    591
    592 class HTTPRedirectHandler(BaseHandler):


HTTPError: HTTP Error 404: NOT FOUND
```

```python
import requests
r = requests.get('http://www.httpbin.org/geta')
r.status_code
```

```
404
```

#### 让用户选择处理错误的方式

- 有些程序员倾向于用异常的方式处理错误，而有些则倾向于用检查的方式处理错误。
- 某些场景下检查的方式更为优雅，而另一些场景下则恰恰相反。
- 合理的做法是让用户可以选择处理错误的方式。
- 默认返回错误代码可以实现上面所述的合理做法，而默认采用异常处理错误则无法实现。


用例：

```python
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
try:
    response = urlopen('http://www.httpbin.org/geta')
except HTTPError as e:
    if e.code == 404:
        print('Page not found')
else:
    print('All good')
```

```
Page not found
```

```python
from requests.exceptions import HTTPError
import requests
r = requests.get('http://www.httpbin.org/posta')
try:
    r.raise_for_status()
except HTTPError as e:
    if e.response.status_code == 404:
        print('Page not found')
```

```
Page not found
```

```python
import requests
r = requests.get('http://www.httpbin.org/geta')
if r.ok:
    print('All good')
elif r.status_code == requests.codes.not_found:
    print('Page not found')
```

```
Page not found
```

以上所述就是这篇文章的全部内容。在准备这次演讲和这篇文章的过程中，笔者收获颇丰，也希望读者在阅读的过程中同样能有所收获。读者可以通过在文章下方评论或者在 Twitter 上留言的方式（@noamelf）向我提供建议，我非常乐于倾听这些建议。

##### 更新（2016年8月8日）

如果读者在阅读完文章后，像包括笔者在内的很多人一样，对 Requests 库和 Urllib 库的可用性之间存在如此大的差异感到惊讶，那么 Nick Coghlan 在[下面的评论](http://noamelf.com/2016/08/05/designing-pythonic-apis/#comment-2823855721)和后来的文章（标题的含义一目了然）[它解决了什么问题](http://www.curiousefficiency.org/posts/2016/08/what-problem-does-it-solve.html)中分享了自己对这个问题的看法。

***

[点此查看原文链接](http://noamelf.com/2016/08/05/designing-pythonic-apis/)。

[Python 翻译组](https://github.com/PythonTG)是EarlGrey@编程派发起成立的一个专注于 Python 技术内容翻译的小组，目前已有近 30 名 Python 技术爱好者加入。

翻译组出品的内容（包括教程、文档、书籍、视频）将在编程派微信公众号首发，欢迎各位 Python 爱好者推荐相关线索。

推荐线索，可直接在编程派微信公众号推文下留言即可。
