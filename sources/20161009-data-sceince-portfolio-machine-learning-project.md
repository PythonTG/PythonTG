# 打造数据科学作品集：从机器学习项目开始

title: 打造数据科学作品集：从机器学习项目开始
author: Vik Paruchuri
translator: 唐晓霆
reviewer: EarlGrey
date: 20161009
permalink: data-science-portfolio-machine-learning
keywords: python, matplotlib, pandas, 数据科学, 机器学习, scikit-learn, python 教程, 

***

> 本文是「打造数据科学的作品集」的第三篇，全文大约 25000 字，读完大约需要 37 分钟。如果你喜欢并希望及时获取本系列的最新文章，可以订阅我们。
> 作者：Vik Paruchuri，译者：唐晓霆，校对：EarlGrey，出品：[PythonTG 翻译组](https://github.com/PythonTG/PythonTG)/[编程派](http://codingpy.com)

数据科学公司在招聘时越来越看重个人作品集，原因在于作品集是衡量实际能力最好的方式之一。好消息是，你完全掌控着自己的作品集。如果付出一些努力，你就可以打造出令用人单位印象深刻的高质量作品集。

想要打造高质量作品集，第一步需要搞清楚应该在作品中展现什么能力。公司希望数据科学家具备的能力（也就是他们希望作品集能够展示的能力）包括：

- 沟通能力
- 与他人协作能力
- 技术能力
- 数据推断能力
- 主观能动性

一个好的作品集一般由多个项目构成，每一个项目展示以上 1-2 个能力点。本文是讲述如何建立一个丰满的数据科学作品集的第三篇。本文将介绍如何打造作品集中的第二个项目，以及如何创建一个完整的机器学习项目。最后，你会拥有一个可以展示合理解释数据能力和技术能力的项目。如果你想一窥项目全貌的话，[这里](https://github.com/dataquestio/loan-prediction)是完整的项目文件。

## 一个完整的项目

作为一个数据科学家，有时候你会被叫去分析一个数据集，然后设法[用数据讲故事](http://codingpy.com/article/data-science-portfolio-storytelling-with-data/)。这时，良好的沟通和清晰的思路是非常重要的。像我们在之前用到的 Jupyter notebook 这样的工具，就能很好地帮助你做到这点。客户的预期是总结你发现的演示报告或文档。

然而，有时候你也会被叫去做有业务价值的项目。一个有业务价值的项目会直接影响公司的日常业务，而且会被大家频繁使用。类似这样的任务可能会是“设计一个可以预测用户变动率的算法”， 或者是“创建一个自动给文章打标签的模型”。在这类情况下，讲故事的能力就没有技术能力重要了。你需要能够分析数据集，理解它，然后编写可以处理这些数据的脚本。这些脚本还要跑的快，耗费最少的资源，如内存，这些都是很常见的要求。通常这些脚本需要频繁运行，所以最终的交付品就变成了这些脚本自身，而不是报告。这些成果经常集成到业务流程中，甚至可能会直接面对用户。

创建一个完整项目，要求你：

- 理解整个项目环境
- 探索数据并找到其中的细微差别
- 建立一个结构良好的项目，使其容易集成至业务流程中
- 写出既运行快又占用最少系统资源的高性能代码
- 为代码的安装和使用写出良好的文档，方便他人使用

为了高效地创建这样的项目，我们需要和许多文件打交道。我们非常推荐使用像 [Atom](https://atom.io/) 的文档编辑器，或者像 [PyCharm](https://www.jetbrains.com/pycharm/) 这样的IDE。这些工具允许你在不同文件间跳转，并且可以编辑不同类型的文件，比如 markdown 文件，Python 文件和 csv 文件。给你的代码建立良好的结构，方便进行版本管理，并上传到像[Github](https://github.com/)这样的代码协作工具。

![完整项目](http://ww4.sinaimg.cn/large/801b780agw1f8njpstu2nj20ty0hyjvf.jpg)

在本文中，我们会使用 [Pandas](http://pandas.pydata.org/) 和 [scikit-learn](http://scikit-learn.org/) 等库。我们会大量用到 Pandas 的[DataFrame](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html)，这使得在 Python 中读取和处理表格数据变得非常简单。

## 寻找优质数据集

寻找优质数据集进行完整的项目分析很困难。数据集需要足够大，大到出现内存和性能的限制。还需要具备业务价值。举个例子，[这个数据集](https://collegescorecard.ed.gov/data/)中包含了美国大学的招生条件、毕业率和毕业生未来收入的数据。这就是一个可以用来讲故事的优质数据集。然而，如果你仔细想想，就会发现这里面没有足够的细节来建立一个完整的项目。

举例说，你可以告诉别人如果他们去某些（好）大学，他们未来的潜在收入就会更高，但是这只需要一个很快的查找比较就可以完成，没有足够的空间去展示你的技术能力。你也可以发现如果大学有更高的入学条件，它们的毕业生就更有可能获得高薪，但这些就更偏向于讲故事，而非业务价值了。

当你有 GB 以上的数据量时，或者当你想要预测一些数据细节，内存和性能限制就会逐渐凸现出来，因为得对数据集运行算法运算。

一个优质数据集允许你编写一系列脚本对数据做变形，从而回答一些动态问题。股票价格就是一个很好的数据集。你可以根据这些数据预测第二天的股价走势，并且在闭市的时候把新数据提供给算法。这可以帮助你执行交易，甚至是获取利润。这就不是在讲故事了 -- 而是直接产生价值。

下面是一些能够找到优质数据集的地方：

- [/r/datasets](https://reddit.com/r/datasets) -- 一个有着上百有趣的数据集的 subreddit
- [Google Public Datasets](https://cloud.google.com/bigquery/public-data/#usa-names) -- 一些在 Google BigQuery 上的公共数据集
- [Awesome datasets](https://github.com/caesar0301/awesome-public-datasets) -- 一个托管在 Github 上的数据集清单

浏览这些数据集时，想一想如果有这些数据集，人们可能会问什么问题，然后再想想这些问题是否是一次性的（“S&P 500 和房价的相关性是怎样的？”），或是持续性的（“你能预测股票价格吗？”）。这里的关键在于找到那些持续性的问题，这些问题需要多次运行，并输入不同的数据才能回答。

本文中，我们选择[房利美（Fannie Mae）的贷款数据](http://www.fanniemae.com/portal/funding-the-market/data/loan-performance-data.html)。房利美是一个由美国政府资助的从贷方手里购买房贷的企业。购买房贷之后，它会把这些房贷打包为一些由房贷支撑的证券（MBS）里，再卖出去。这样就帮助了贷方贷出更多的房贷，并给市场创造了更大的流动性。这从理论上说就会产生更多的房屋业主，进而产生更好的房贷政策。然而从借方的角度来看，情况并没有什么不同。

房利美公开了两种数据 -- 收购到的房贷数据，和房贷表现情况数据。在最理想的情况下，一个人从贷方贷了款，然后一直还钱，直到贷款还清。然而，借方有几次没有还款，就可能会导致失去抵押品赎回权。这时，银行就会获得房屋的所有权，因为没还清房贷。房利美记录了哪些房贷没有还，哪些房贷需要取消抵押品赎回权。这个数据每个季度发布一次，而且会滞后一年。撰写本文时，最近的数据集是 2015 年第一季度。

房利美购买房贷时会发布收购信息，其中含有许多关于借方的信息，包括信用评分、房贷和房屋的信息。之后，每个季度发布房贷表现数据，涵盖了借方的支付信息，和抵押权的状态。房贷表现信息里可能有很多行。你可以这么想这个事，收购信息表示房利美现在控制了房贷，表现信息则包括了一系列房贷的状态更新。有的状态可能会说这笔贷款在某个季度借方抵押权被取消了。

![一个借方失去了抵押品赎回权（止赎）的房子正在被卖](http://ww2.sinaimg.cn/large/801b780agw1f8njqpunodj20nm0fp40k.jpg)

*一个借方失去了抵押品赎回权（止赎）的房子正在被卖*

## 选择分析角度

对于房利美数据集，我们可以有多个分析角度。我们可以：

- 尝试预测一个止赎了的房屋的售价
- 预测一个借方的还款历史
- 计算出一个被收购时房贷的评分

重要的事是要坚持一个角度。一次专注于太多事情会很难做成一个优秀的项目。选择一个有足够细节的角度这点也很重要。以下是一些没有多少细节的角度：

- 哪家银行卖给房利美最多止赎的房贷
- 借方信用评分的趋势
- 哪些房屋类型最经常止赎
- 房贷金额和止赎售价的关系

上述的这些角度都很有趣，如果我们关注讲故事的话是很棒的话题，但对于一个业务性的项目来说就没那么好了。

有了房利美数据集，我们将尝试仅仅使用收购房贷时的数据，预测房贷是否会被止赎。实际上，我们会为每一份房贷“打分”，这个分数表示房利美是否应该购买这份房贷。这将是一个良好的基础，也是一个很棒的作品。

## 理解数据

我们首先快速查看原始数据文件。下面是 2012 年第一季度收购数据的前几行：

```
100000853384|R|OTHER|4.625|280000|360|02/2012|04/2012|31|31|1|23|801|N|C|SF|1|I|CA|945||FRM|
100003735682|R|SUNTRUST MORTGAGE INC.|3.99|466000|360|01/2012|03/2012|80|80|2|30|794|N|P|SF|1|P|MD|208||FRM|788
100006367485|C|PHH MORTGAGE CORPORATION|4|229000|360|02/2012|04/2012|67|67|2|36|802|N|R|SF|1|P|CA|959||FRM|794
```

下面是 2012 年第一季度的表现数据的前几行：

```
100000853384|03/01/2012|OTHER|4.625||0|360|359|03/2042|41860|0|N||||||||||||||||
100000853384|04/01/2012||4.625||1|359|358|03/2042|41860|0|N||||||||||||||||
100000853384|05/01/2012||4.625||2|358|357|03/2042|41860|0|N||||||||||||||||
```

在编写代码之前，花点时间去理解数据是很有用的。尤其对于业务型项目而言，因为我们没有互动式地去探索数据，很难发现某些细节，除非一开始就找到它们。这种情况下，第一步就是去房利美的网站上读一读有关数据集的材料：

- [简介](http://www.fanniemae.com/portal/funding-the-market/data/loan-performance-data.html)
- [词汇表](https://loanperformancedata.fanniemae.com/lppub-docs/lppub_glossary.pdf)
- [常见问题](https://loanperformancedata.fanniemae.com/lppub-docs/lppub_faq.pdf)
- [收购和表现文件里的列](https://loanperformancedata.fanniemae.com/lppub-docs/lppub_file_layout.pdf)
- [收购数据样本文件](https://loanperformancedata.fanniemae.com/lppub-docs/acquisition-sample-file.txt)
- [表现数据样本文件](https://loanperformancedata.fanniemae.com/lppub-docs/performance-sample-file.txt)

读完这些材料之后，我们知道了一些有用的关键信息：

- 从 2000 年到现在，每个季度都有一个收购文件和表现文件。数据滞后一年，所以最近的数据是 2015 年的
- 这些文件是文本形式，用 `|` 作为分隔符
- 这些文件没有头文档，但是我们有所有列名称的列表
- 全部加起来，这些文件共包含 2.2 千万个房贷的数据
- 因为表现文件涵盖了之前的房贷信息，所以早些时候的房贷会有更多的表现数据（举个例子，2014 年收购的房贷不会有太多表现信息）

在设计项目结构和处理数据时，这些信息能帮助我们节省一大笔时间。

## 设计项目结构

在开始下载和探索数据之前，设计好项目结构是非常重要的。在打造一个完整的项目时，我们的主要目标是：

- 输出一个可行的解决方案
- 解决方案运行快且消耗最少资源
- 让他人可以很容易地扩展项目
- 让他人可以容易地理解代码
- 写的代码越少越好

为了达到这些目标，我们要设计好项目的结构。一个结构良好的项目遵从以下规范：

- 数据文件和源代码分开
- 原始数据和生成数据分开
- 有一个 `README.md` 文件，介绍如何安装并使用这个项目
- 有一个 `requirements.txt` 文件，包含项目所需的所有模块
- 有一个 `settings.py` 文件，包含所有其他文件所需的设置
	- 例如，如果有很多Python脚本都读取同一个文件，就不如让它们都导入`settings`并从这一个地方来得到文件
- 有一个 `.gitignore` 文件，来防止一些特别大的或者私密的文件被提交到 Git
- 把任务分成几步，并分别放在可以单独执行的文件里
	- 例如， 用一个文件读取数据，一个文件建立特征，一个文件执行预测
- 储存中间值。例如，一个脚本可能会输出一个文件，这个文件又会被另外一个脚本读取
	- 这使得我们可以在数据处理的流程中做一些改动，而又不需要重新计算

该项目的文件结构如下：

```
loan-prediction
├── data
├── processed
├── .gitignore
├── README.md
├── requirements.txt
├── settings.py
```

## 创建初始文件

首先，创建 `loan-prediction` 文件夹。在这个文件夹里，创建 `data` 文件夹和 `processed` 文件夹。第一个用来储存原始数据，第二个用来储存所有中间值。

接着，创建 `.gitignore` 文件。`.gitignore` 文件会确保一些文件会被 git 忽略，并不会被推送到 Github 上。OS X 在每个文件夹里创建的 `.DS_Store` 文件就是这类需要忽略的文件。要入门 `.gitignore` 文件，可以参考[这里](https://github.com/github/gitignore/blob/master/Python.gitignore)。还要忽略一些体积太大的文件，而且房利美的条款并不允许二次发布这些文件，所以我们应该在 `.gitignore` 文件最后加上这两行：

```
data
processed
```

[这里](https://github.com/dataquestio/loan-prediction/blob/master/.gitignore)是本项目的示例 `.gitignore` 文件。

接着，创建 `README.md` ，这有助于人们理解项目。`.md` 代表这个文件是 markdown 格式。Markdown 能让你直接用纯文本写作，但是如果想的话，也可以添加一些好看的排版格式。[这里](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)是一个 markdown 指南。如果你往 Github 上传了一个叫 `README.md` 的文件，Github 会自动处理该文件，把它作为主页展示给浏览者。[这里](https://github.com/dataquestio/loan-prediction)有一个例子。

目前，只需要在`README.md`里面放一段简短的描述：

```md
Loan Prediction
-----------------------

Predict whether or not loans acquired by Fannie Mae will go into foreclosure.  Fannie Mae acquires loans from other lenders as a way of inducing them to lend more.  Fannie Mae releases data on the loans it has acquired and their performance afterwards [here](http://www.fanniemae.com/portal/funding-the-market/data/loan-performance-data.html).
```

现在，创建 `requirements.txt` 文件。这可以帮助其他人安装我们的项目。目前还不知道具体需要哪些库，但下面这些是一个好的起点：

```
pandas
matplotlib
scikit-learn
numpy
ipython
scipy
```

以上是用 Python 作数据分析最常用的几个库，在这个项目中应该会用到它们。[这里是](https://github.com/dataquestio/loan-prediction/blob/master/requirements.txt)本项目的示例 requirements 文件。

创建 `requirements.txt` 之后，你应该安装这些模块。在本文中，我们使用 `Python 3` 。如果你还没有安装 Python，建议使用 [Anaconda](https://www.continuum.io/downloads)，这是一个可以安装上述所有模块的 Python 安装器。

最后，创建一个空白的 `settings.py` 文件，因为项目还没有任何设置。

## 获得数据

创建好整个项目的框架之后，就可以获取原始数据了。

房利美对数据下载有一些限制，所以你得先注册一个账号。下载页面在[这里](https://loanperformancedata.fanniemae.com/lppub/index.html)。注册完账户后，就可以随意下载贷款数据了。文件是 zip 格式，解压之后也挺大的。

本文中，我们会把 2012 年第一季度到 2015 年第一季度之间的所有数据都下载下来。然后解压文件，解压之后，删除原始的 `.zip` 文件。最后，`loan-prediction` 文件夹的结构应该类似这样：

```
loan-prediction
├── data
│   ├── Acquisition_2012Q1.txt
│   ├── Acquisition_2012Q2.txt
│   ├── Performance_2012Q1.txt
│   ├── Performance_2012Q2.txt
│   └── ...
├── processed
├── .gitignore
├── README.md
├── requirements.txt
├── settings.py
```

下载完数据之后，可以用 `head` 和 `tail` 等 shell 命令去观察文件的前几行和后几行。有没有不需要的列？查看数据时可以参考一下[介绍列名称的 PDF 文件](https://loanperformancedata.fanniemae.com/lppub-docs/lppub_file_layout.pdf)

## 读取数据

有两个问题，使得直接处理数据比较困难：

- 收购和表现数据集被分散在了许多文件里
- 所有文件都缺少头文档

在开始处理这些数据之前，需要把所有的收购数据集中到一个文件，所有的表现数据集中到一个文件。每个文件只需要包含我们关心的列，和正常的头文档。这里有一个小问题，即表现数据特别大，所以可能的话我们得删减一些列。

第一步是在 `settings.py` 里面增添一些变量，包含到原始数据和中间数据的路径。我们也会加上一些之后会有用的设置：

```
DATA_DIR = "data"
PROCESSED_DIR = "processed"
MINIMUM_TRACKING_QUARTERS = 4
TARGET = "foreclosure_status"
NON_PREDICTORS = [TARGET, "id"]
CV_FOLDS = 3
```

把路径放在 `settings.py` 里面，会使得它们统一在一个地方，使得今后改动变得简单。当许多文件都用了同一些变量的时候，把它们放在一起会比分别在每个文件里做改动要简单得多。[这里](https://github.com/dataquestio/loan-prediction/blob/master/settings.py)是该项目的示例 `settings.py` 文件。

第二步是创建一个叫做 `assemble.py` 的文件，这个文件会把分散的数据组合成 2 个文件。运行 `python assemble.py` 后，会在 `processed` 文件夹里面得到 2 个数据文件。

然后再 `assemble.py` 中写代码。首先，给每个文件定义头文档，所以我们需要查看[解释列名称的 PDF 文档](https://loanperformancedata.fanniemae.com/lppub-docs/lppub_file_layout.pdf)，然后为收购数据和表现数据文件分别创建一个列表，表示其中的行。

```python
HEADERS = {
    "Acquisition": [
        "id",
        "channel",
        "seller",
        "interest_rate",
        "balance",
        "loan_term",
        "origination_date",
        "first_payment_date",
        "ltv",
        "cltv",
        "borrower_count",
        "dti",
        "borrower_credit_score",
        "first_time_homebuyer",
        "loan_purpose",
        "property_type",
        "unit_count",
        "occupancy_status",
        "property_state",
        "zip",
        "insurance_percentage",
        "product_type",
        "co_borrower_credit_score"
    ],
    "Performance": [
        "id",
        "reporting_period",
        "servicer_name",
        "interest_rate",
        "balance",
        "loan_age",
        "months_to_maturity",
        "maturity_date",
        "msa",
        "delinquency_status",
        "modification_flag",
        "zero_balance_code",
        "zero_balance_date",
        "last_paid_installment_date",
        "foreclosure_date",
        "disposition_date",
        "foreclosure_costs",
        "property_repair_costs",
        "recovery_costs",
        "misc_costs",
        "tax_costs",
        "sale_proceeds",
        "credit_enhancement_proceeds",
        "repurchase_proceeds",
        "other_foreclosure_proceeds",
        "non_interest_bearing_balance",
        "principal_forgiveness_balance"
    ]
}
```

下一步是定义需要保留哪些列。因为我们关心的房贷只是关于它有没有被止赎，所以可以从表现数据里面丢弃很多列（不影响是否止赎的数据）。但是我们需要保留所有收购数据，因为我们想要尽可能多的房贷信息（毕竟我们要在收购房贷时预测是否会被止赎）。丢弃一些列可以省下一些磁盘空间和内存，同时也会加速代码的运行速度。

```python
SELECT = {
    "Acquisition": HEADERS["Acquisition"],
    "Performance": [
        "id",
        "foreclosure_date"
    ]
}
```

接下来，写一个函数来拼接所有的数据集。下面的代码会：

- 导入一些需要的库，包括`settings`
- 定义函数 `concatenate`，它可以：
	- 拿到 `data` 目录里面所有文件的名字
	- 遍历每个文件
		- 如果文件的格式不对（并不是以预期的前缀开始），就忽略它
		- 用 Pandas 的[read_csv](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html)函数，把文件读取到一个 [DataFrame](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html) 里
			- 把分隔符设置为 `|` ，正确读取数据
			- 数据现在没有头文档，所以把 `header` 设置成 `None` 
			- 把 `HEADERS` 字典里的值设置为列的名称，这些会成为 DataFrame 里面的列名称
			- 只把加在 `SELECT` 里面的列从 DataFrame 里面选出来
		- 把所有的 DataFrame 拼接在一起
		- 把拼接好的 DataFrame 输出成一个文件

```python
import os
import settings
import pandas as pd

def concatenate(prefix="Acquisition"):
    files = os.listdir(settings.DATA_DIR)
    full = []
    for f in files:
        if not f.startswith(prefix):
            continue

        data = pd.read_csv(os.path.join(settings.DATA_DIR, f), sep="|", header=None, names=HEADERS[prefix], index_col=False)
        data = data[SELECT[prefix]]
        full.append(data)

    full = pd.concat(full, axis=0)

    full.to_csv(os.path.join(settings.PROCESSED_DIR, "{}.txt".format(prefix)), sep="|", header=SELECT[prefix], index=False)

```

可以用参数 `Acquisition` 和 `Performance` 分别调用上面的函数，把所有的收购和表现文件拼接在一起。下面的代码会：

- 只当脚本是在命令行用 `python assemble.py` 执行时运行
- 拼接所有文件，并输出成两个文件：
    - `processed/Acquisition.txt`
    - `processed/Performance.txt`

```python
if __name__ == "__main__":
    concatenate("Acquisition")
    concatenate("Performance")
```

我们现在有了一个模块化的 `assemble.py` 文件，既容易运行，又易扩展。像这样把大问题划分成小问题，我们将项目变得更简单。我们把不同文件分离开，定义它们之间的数据，而不是用一个脚本做所有的事情。当你在做一个大项目的时候，这样做通常很好，因为更改一些文件后不会产生不可预期的结果。

完成 `assemble.py` 脚本后，运行 `python assemble.py` 。你可以在[这里](https://github.com/dataquestio/loan-prediction/blob/master/assemble.py)找到完整的脚本。

这会在 `processed` 目录里面输出两个文件：

```
loan-prediction
├── data
│   ├── Acquisition_2012Q1.txt
│   ├── Acquisition_2012Q2.txt
│   ├── Performance_2012Q1.txt
│   ├── Performance_2012Q2.txt
│   └── ...
├── processed
│   ├── Acquisition.txt
│   ├── Performance.txt
├── .gitignore
├── assemble.py
├── README.md
├── requirements.txt
├── settings.py
```

## 表现数据计算

下一步就是从 `processed/Performance.txt` 数据中计算一些值。我们想做的就是预测一间房产以后会不会被止赎。为了弄明白这一点，我们只需要看看表现数据里面的房贷是否有一个 `foreclosure_date` 。如果 `foreclosure_date` 是 `None` ，那么这间房产就没有被止赎。我们也需要规避那些在表现数据里没有多少历史数据的房贷，要做到这一点，通过计算它们在表现数据里面累计有多少行就可以。

可以用下面的方法来思考收购数据和表现数据的关系：

![](http://ww4.sinaimg.cn/large/801b780agw1f8njvy5hupj20j607twey.jpg)

我们发现，收购数据里每一行都对应了表现数据中的多行。在表现数据中，当止赎发生的时候，当季度的 `foreclosure_date` 就会出现日期，在这之前都应该是空白的。一些贷款从未被止赎，所以与之相关的表现数据里的 `foreclosure_date` 都是空白的。

我们需要计算 `foreclorsure_status` ，这是一个布尔值，代表一个贷款 `id`是否有被止赎过。我们也要计算 `performance_count` ，也就是每个 `id` 在表现数据里有多少行。

有几种方法可以计算 `performance_count`：

  - 读取所有的表现数据，然后用 Pandas 的 [groupby](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.groupby.html) 方法求每个贷款 `id` 相关联的行数，同时 `id` 对应的 `foreclosure_date` 有没有不是 `None` 过。
    - 这样做的好处是实现的语法很简单
    - 这样做的坏处是读取 `129236094` 行数据会花很多内存，而且极其慢
  - 我们可以读取所有的表现数据，然后在收购数据 DataFrame 上使用 [apply](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.apply.html) ，从而求得每个 `id` 的计数
    - 好处是概念上很简单
    - 坏处仍然是读取 `129236094` 行数据会花很多内存，而且极其慢
  - 我们可以遍历表现数据里的每一行，然后保存一个单独的包含计数的字典
    - 好处是不需要把所有数据一起读取进内存，所以这样做会很快，也会优化内存
    - 坏处是得花长一点时间来理清概念和实现，而且需要手工地解析每一行

把所有数据一并加载会花很多内存，所以我们采用第三种方法。我们所要的就是遍历表现数据里面的每一行，并且保存一个包含每个 `id` 的计数字典。在字典里面，我们记录下表现数据里面每个 `id` 出现了多少次，并且 `foreclosure_date` 是否为非 `None` 过。这样就能求出 `foreclosure_status` 和 `performance_count` 。

新建一个文件 `annotate.py` ，并加入用来计算的代码。在下面的代码中，我们会：

  - 导入需要的库
  - 定义一个叫做 `count_performance_rows` 的函数
      - 打开 `precessed/Performance.txt` 。这不会把文件读取进内存，而仅仅是打开一个文件句柄，一行一行地读取文件内容
      - 遍历文件里的每一行
          - 根据分隔符 `|` 分割字符串
          - 检查 `loan_id` 是否在 `counts` 字典里
              - 如果不在，把它加入 `counts` 
          - 给 `load_id` 对应的 `performance_count` 加1
          - 如果 `date` 不是 `None`，那么我们就知道这笔贷款止赎了，所以设置相应的 `foreclosure_status` 

```python
import os
import settings
import pandas as pd

def count_performance_rows():
    counts = {}
    with open(os.path.join(settings.PROCESSED_DIR, "Performance.txt"), 'r') as f:
        for i, line in enumerate(f):
            if i == 0:
                # Skip header row
                continue
            loan_id, date = line.split("|")
            loan_id = int(loan_id)
            if loan_id not in counts:
                counts[loan_id] = {
                    "foreclosure_status": False,
                    "performance_count": 0
                }
            counts[loan_id]["performance_count"] += 1
            if len(date.strip()) > 0:
                counts[loan_id]["foreclosure_status"] = True
    return counts
```

## 得到计算结果

创建建了 counts 字典后，我们可以用一个函数抽取出和传入的 `load_id` 和 `key` 相应的值了：

```python
def get_performance_summary_value(loan_id, key, counts):
    value = counts.get(loan_id, {
        "foreclosure_status": False,
        "performance_count": 0
    })
    return value[key]
```

上面这个函数会从 `counts` 字典里返回相应的值，并且可以让我们为收购数据里每一行添加 `foreclosure_status` 和 `performance_count` 值。字典的 [get](https://docs.python.org/3/library/stdtypes.html#dict.get) 方法在没有找到 key 的情况下就会返回一个默认值，所以就算没有找到也能返回合理的默认值。

## 给数据做标记

我们已经在 `annotate.py` 中添加上一些函数，现在可以开始处理最有价值的部分了。我们需要把收购数据转换成一个机器学习算法可以使用的训练集。需要做以下几件事：

- 把所有数据变成数字
- 补足空白的值
- 给每一行添加一个 `performance_count` 和一个 `foreclosure_status` 
- 删除那些没有多少表现历史数据的行（那些 `performance_count` 很低的行）

有几列的数据都是文字，这在机器学习里没有什么用。然而它们其实是类别变量，比如说 `R`、`S` 这样的类别编号。我们分别赋予它们数字，从而把它们变成数字：

![](http://ww1.sinaimg.cn/large/801b780agw1f8njwy2xq9j20nj0940tb.jpg)

这样转化了之后，就能把它们用于机器学习。

一些列也包含了时间（ `first_payment_date` 和 `origination_date` ）。可以把它们各自分割成两列：

![](http://ww4.sinaimg.cn/large/801b780agw1f8njxkbk57j20ny09qt9d.jpg)

下面的代码中，我们会转换收购数据。定义一个函数，这个函数会：

- 从 `counts` 字典里获取数据，在 `acquisition` 里建立一个 `foreclosure_status` 列
- 从 `counts` 字典里获取数据，在 `acquisition` 里建立一个 `performance_count` 列
- 把下面的列从文字转成数字：
    - `channel` 
    - `seller`
    - `first_time_homebuyer`
    - `loan_purpose`
    - `property_type`
    - `occupancy_status`
    - `property_state`
    - `product_type`
- 分别把 `first_payment_date` 和 `origination_date` 转换成两列：
    - 以 `/` 为分隔符进行分割
    - 把第一部分赋予 `month` 列
    - 把第二部分赋予 `year` 列
    - 删除原本列
    - 最后，我们就会有 `first_payment_month`、`first_payment_year`、`origination_month` 和 `origination_year` 
- 将 `acquisition`里的所有缺失值都替换成 `-1`

```python
def annotate(acquisition, counts):
    acquisition["foreclosure_status"] = acquisition["id"].apply(lambda x: get_performance_summary_value(x, "foreclosure_status", counts))
    acquisition["performance_count"] = acquisition["id"].apply(lambda x: get_performance_summary_value(x, "performance_count", counts))
    for column in [
        "channel",
        "seller",
        "first_time_homebuyer",
        "loan_purpose",
        "property_type",
        "occupancy_status",
        "property_state",
        "product_type"
    ]:
        acquisition[column] = acquisition[column].astype('category').cat.codes

    for start in ["first_payment", "origination"]:
        column = "{}_date".format(start)
        acquisition["{}_year".format(start)] = pd.to_numeric(acquisition[column].str.split('/').str.get(1))
        acquisition["{}_month".format(start)] = pd.to_numeric(acquisition[column].str.split('/').str.get(0))
        del acquisition[column]

    acquisition = acquisition.fillna(-1)
    acquisition = acquisition[acquisition["performance_count"] > settings.MINIMUM_TRACKING_QUARTERS]
    return acquisition
```

## 拼接所有数据

很快就可以将所有数据拼接在一起了，在这之前我们只要再加一些代码到 `annotate.py` 里。在下面的代码中，我们：

- 定义一个函数来读取收购数据
- 定义一个函数把处理过的数据写入 `processed/train.csv`
- 如果文件是从命令行传入的，比如 `python annotate.py`，则:
    - 读取收购数据
    - 计算表现数据的累计数目，并赋值给 `counts`
    - 给 `acquisition` DataFrame 做标记
    - 把 `acquisition` DataFrame 写入 `train.csv`

```python
def read():
    acquisition = pd.read_csv(os.path.join(settings.PROCESSED_DIR, "Acquisition.txt"), sep="|")
    return acquisition
    
def write(acquisition):
    acquisition.to_csv(os.path.join(settings.PROCESSED_DIR, "train.csv"), index=False)

if __name__ == "__main__":
    acquisition = read()
    counts = count_performance_rows()
    acquisition = annotate(acquisition, counts)
    write(acquisition)
```

写好文件后，记得用 `python annotate.py` 来运行它，这会生成一个 `train.csv` 文件。完整的 `annotate.py` 文件在[这里](https://github.com/dataquestio/loan-prediction/blob/master/annotate.py)。

文件夹现在应该长这样：

```
loan-prediction
├── data
│   ├── Acquisition_2012Q1.txt
│   ├── Acquisition_2012Q2.txt
│   ├── Performance_2012Q1.txt
│   ├── Performance_2012Q2.txt
│   └── ...
├── processed
│   ├── Acquisition.txt
│   ├── Performance.txt
│   ├── train.csv
├── .gitignore
├── annotate.py
├── assemble.py
├── README.md
├── requirements.txt
├── settings.py
```

## 寻找误差衡量指标

我们生成好了训练数据，现在只需要完成最后一步，生成预测。我们需要找到一个误差的衡量指标，以及如何评估数据。就本文而言，没有被止赎的贷款比止赎的贷款多得多，所以典型的准确度衡量并不适用。

如果我们看一看训练数据，并查看 `foreclosure_status` 列的计数，会发现：

```python
import pandas as pd
import settings

train = pd.read_csv(os.path.join(settings.PROCESSED_DIR, "train.csv"))
train["foreclosure_status"].value_counts()
```

```
False    4635982
True        1585
Name: foreclosure_status, dtype: int64
```

因为只有这么一点点贷款是止赎了，所以如果我们只看有多少百分比的标签被正确预测了，那我们即使建立了一个只预测 `False` 的模型，一样可以得到很高的准确度。所以我们采用的衡量指标要把这种不平衡考虑进去，确保准确预测。我们不想要太多假正（False Positive），即预测一个贷款会止赎，但其实不会，或者太多假负（False Negative），即预测一个贷款不会被止赎，但其实会。在这两者之间，假负对房利美来说成本更高，因为他们买的这些房贷没法收回投资。

我们定义假负率为预测不会止赎但其实会的预测数量，除以总的止赎贷款数量。这就是模型没有体现的实际止赎百分比。下面是一个图表：

![](http://ww1.sinaimg.cn/large/801b780agw1f8njy7aeu9j20lp090aab.jpg)

在上图中，状态为 1 的贷款被预测为非止赎，但它其实被止赎了。如果把它除以实际止赎贷款数量 2，错误的负预测率为 50% 。我们用它作为误差衡量指标，这样就能够有效地评估模型的表现。

## 为机器学习设置好分类器

我们使用交叉验证来做预测。为了进行交叉验证，我们把数据分成 3 组，然后：

- 在 1 组和 2 组上训练模型，然后在 3 组上预测
- 在 1 组和 3 组上训练模型，然后在 2 组上预测
- 在 2 组和 3 组上训练模型，然后在 1 组上预测

把数据分成几组意味着我们不会用同样的数据来训练模型，然后又用同样的数据来做预测。这就避免了过拟合。如果过拟合了，就会得到一个错的低假负率，也就是说我们的模型很难应用于真实情况或进行后续改进。

[Scikit-learn](http://scikit-learn.org/) 中有一个叫做 [cross_val_predict](http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.cross_val_predict.html) 的函数，使得交叉验证变得很容易。

我们还需要挑选一个算法来做预测。我们需要一个分类器来做[二元分类](https://en.wikipedia.org/wiki/Binary_classification)。因为目标变量 `foreclosure_status` 只有两个值，`True`和`Flase`。

我们使用 [逻辑回归算法](https://en.wikipedia.org/wiki/Logistic_regression)。因为它在二元分类下表现很好，运行得极快，而且消耗很少内存。这是因为这个算法的工作方式 -- 它不会像随机森林算法那样建立一堆决策树，或像支持向量机那样做很耗资源的变换，其设计的矩阵操作相对来说少得多。

我们可以用 scikit-learn 里自带的[逻辑递归分类器](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)算法。唯一需要注意的就是每个类的权重。 如果给每个类同样的权重,，算法就会对每一行预测 `False` ，因为它要最小化误差.。然而，我们更关心止赎的贷款而不是不会止赎的贷款。因此，我们给 [Logistic Regression 类](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)传入 `balanced` 参数到 `class_weight` 关键字中，从而得到一个考虑样本数量而给于平衡的比重的算法。这样就能确保算法不会对每一行都预测 `False`。

## 进行预测

现在已经完成了前期准备工作，可以开始做预测了。创建一个叫 `predict.py` 的新文件，使用我们之前创建的 `train.csv`。下面的代码会：

- 导入需要的库
- 创建一个 `cross_validate` 函数，它会：
    - 用正确的关键词参数创建一个逻辑递归分类器
    - 创建用来训练模型的数据列列表，同时删除 `id` 和 `foreclosure_status` 列
    - 在 `train` DataFrame 上运行交叉验证
    - 返回预测

```python
import os
import settings
import pandas as pd
from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

def cross_validate(train):
    clf = LogisticRegression(random_state=1, class_weight="balanced")

    predictors = train.columns.tolist()
    predictors = [p for p in predictors if p not in settings.NON_PREDICTORS]

    predictions = cross_validation.cross_val_predict(clf, train[predictors], train[settings.TARGET], cv=settings.CV_FOLDS)
    return predictions
```

## 预测误差

现在只需要写一些函数来计算误差。下面的代码会：

- 创建 `computer_error` 函数，它会：
    - 用 scikit-learn 计算一个简单准确度评分（符合真实 `foreclosure_status` 值的预测的百分比）
- 创建 `computer_false_negatives` 函数，它会:
    - 把目标和预测写进一个 DataFrame
    - 计算假负率
- 创建 `computer_false_positives` 函数，它会:
    - 把目标和预测写进一个DataFrame
    - 计算假正率
        - 找到模型预测为止赎但并未止赎的贷款数量
        - 用这个数量除以不是止赎的贷款数量

```python
def compute_error(target, predictions):
    return metrics.accuracy_score(target, predictions)

def compute_false_negatives(target, predictions):
    df = pd.DataFrame({"target": target, "predictions": predictions})
    return df[(df["target"] == 1) & (df["predictions"] == 0)].shape[0] / (df[(df["target"] == 1)].shape[0] + 1)

def compute_false_positives(target, predictions):
    df = pd.DataFrame({"target": target, "predictions": predictions})
    return df[(df["target"] == 0) & (df["predictions"] == 1)].shape[0] / (df[(df["target"] == 0)].shape[0] + 1)
```

## 整合所有函数

现在，把上面的函数都放在 `predict.py` 里面。下面的代码会：

- 读取数据集
- 计算交叉验证预测
- 计算上面提到的 3 个误差值
- 打印出误差值

```python
def read():
    train = pd.read_csv(os.path.join(settings.PROCESSED_DIR, "train.csv"))
    return train
    
if __name__ == "__main__":
    train = read()
    predictions = cross_validate(train)
    error = compute_error(train[settings.TARGET], predictions)
    fn = compute_false_negatives(train[settings.TARGET], predictions)
    fp = compute_false_positives(train[settings.TARGET], predictions)
    print("Accuracy Score: {}".format(error))
    print("False Negatives: {}".format(fn))
    print("False Positives: {}".format(fp))
```

添加完这些代码后，可以运行 `python predict.py` 来生成预测。结果显示，假负率为 .26 ，也就是说对于止赎贷款来说，我们错误地预测了其中的 26% 。这是个好的开始，但还有很大的提升空间。

完整的 `predict.py` 文件在[这里](https://github.com/dataquestio/loan-prediction/blob/master/predict.py)。

文件树现在应该长这样：

```
loan-prediction
├── data
│   ├── Acquisition_2012Q1.txt
│   ├── Acquisition_2012Q2.txt
│   ├── Performance_2012Q1.txt
│   ├── Performance_2012Q2.txt
│   └── ...
├── processed
│   ├── Acquisition.txt
│   ├── Performance.txt
│   ├── train.csv
├── .gitignore
├── annotate.py
├── assemble.py
├── predict.py
├── README.md
├── requirements.txt
├── settings.py
```

## 撰写 README

现在我们完成了这个完整的项目, 接下来只需要写 `README.md` 文件进行总结，向他人说明我们做了什么，以及如何复制它。一个典型的 `README.md` 应该包括以下内容：

- 项目概览及目标
- 如何下载所需数据或材料
- 安装教程
    - 如何安装需要的模块
- 使用教程
    - 如何运行项目
    - 每一步应该看到哪些结果
- 如何贡献
    - 扩展这个项目的要怎么做

[这里](https://github.com/dataquestio/loan-prediction/blob/master/README.md)是本项目的示例 `README.md`。

## 下一步

恭喜，你已经完成了一个完整的机器学习项目！你可在[这里](https://github.com/dataquestio/loan-prediction)找到完整的示例项目。完成项目之后，记得上传到 Github 上，这样其他人就会看到这是你作品集的一部分。

这些数据尚有一些地方待你挖掘。大致来说，我们可以把它们分成 3 类 -- 扩展项目提高准确率，利用其它数据列进行预测，进一步探索数据。以下想法仅供参考：

- 用 `annotate.py` 生成更多特征
- 在 `predict.py` 里换个算法
- 使用更多来自房利美的数据
- 加上一个预测未来数据的方法。如果添加更多的数据，目前的代码都是可以运行的，所以我们可以加上更多过去的或者未来的数据
- 尝试能不能预测银行一开始该不该放出贷款(以及房利美应不应该收购贷款)
    - 删除那些银行在发放贷款时不能获得的信息列
        - 有些在房利美收购的时候有，但之前没有
    - 做预测
- 探索一下能不能预测除了 `foreclosure_status` 以外的数据
    - 能不能预测房产在出售时能卖多少钱？
- 探索一下表现数据更新时的细节
    - 能不能预测借方迟付贷款的次数？
    - 能不能画出典型的贷款周期?
- 按州或邮编对数据进行绘图
    - 有看到一些有趣的模式吗?

如果你创建了一些有趣的项目, 请在留言区告知我们！

***

本系列其他译文：

1. [打造数据科学作品集：用数据讲故事](http://codingpy.com/article/data-science-portfolio-storytelling-with-data/)
2. [打造数据科学作品集：搭建一个数据科学博客](http://codingpy.com/article/making-data-science-blog/)

