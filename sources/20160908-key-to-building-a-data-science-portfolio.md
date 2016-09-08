# 创建数据科学简历的关键，工作在等你哦

title: 创建数据科学简历的关键，工作在等你哦
author: Vik Paruchuri
translator: 赵喧典
reviewer: EarlGrey
date: 20160908
permalink: should-engineering-managers-code
keywords:build-a-data-science-portfolio-4

***

在本系列之前的文章中，我们讨论了[如何创建数据呈现项目](https://www.dataquest.io/blog/data-science-portfolio-project/)，[如何创建端到端的机器学习项目](https://www.dataquest.io/blog/data-science-portfolio-machine-learning/)，以及[如何搭建一个数据科学博客](https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/)。而本文，我们将回过头来，集中讨论如何创建高大上的数据科学简历。我们将讨论什么技能是雇主希望看到的，以及如何创建一份简历以有效地展示所有的技能。我们将举例说明在简历中应该写哪些项目以及如何写，并给你一些起步的建议。

读完这篇文章之后，应该能够理解为什么要创建数据科学简历，以及具体的创建方法。

## 雇主想要什么

当雇主招人时，他们想要那些能为企业创造价值的人。这通常意味着，应聘者需要掌握能为企业带来收入和机遇的技能。而作为数据科学家，可以通过以下 4 种主要方式中的一种来为企业创造价值:

- 对原始数据的敏锐洞察，能从数据中提取出洞见并向他人展示。
 - 例子：分析广告点击率，会发现面向 18 到 21 周岁人群的广告比面向 21 到 25 周岁人群的广告带来的成本收益高得多——企业据此调整它的广告投入，这就创造了商业价值。
- 构建能为客户带去直接价值的系统。
 - 例子：Facebook 的一位数据科学家通过优化新闻推送为用户展现更好的结果——更多的新闻推送订阅，意味着更多的广告订阅，这就为 Facebook 带来直接收入。
- 构建能为组中其他人带去直接价值的系统
 - 例子：编写脚本以自动地从 3 个数据库提取数据并聚合，为其他人的分析提供清理后的数据集——通过提高他人的工作效率，这也创造了价值。
- 与组中的其他人分享专业知识
 - 例子：与产品经理讨论如何实现用到机器学习算法的功能——通过防止不切实际的时间表和半成品，这也创造了价值。

毋庸置疑的是，当雇主考核应聘者时，他们在考核应聘者是否具备上述四项技能的一项或多项（根据公司和岗位不同，可能需要应聘者同时具备多项技能）。为了向企业证明你能在上述所列 4 个领域为帮到企业，你需要展示自身具备以下技能的综合能力：

- 沟通能力
- 与他人合作的能力
- 技术能力
- 数据推理的能力
- 积极性与主动性

一个面面俱到的简历应该足以展示你在上述各方面的技能，并且对他人而言是易审视的——简历的每一项都应该有理有据，清晰明了，这样，HR 才能快速地对简历进行评估。

## 为什么需要简历

如果你拥有顶尖学府的机器学习或相关领域的学位，获得数据科学相关的工作会**相对**容易。因为顶尖学府的声誉以及专业对口的事实，雇主相信你能为企业创造价值。但如果你没有来自顶尖学府的相关学位，你就不得不为自己建立这份信任。

这样说吧：对于雇主而言，需求的岗位有多达 200 份的申请。假设 HR 总共花 10 小时过滤申请以确定电话面试哪些人。这意味着平均每个申请只有 3 分钟的评估时间。开始时，HR 不相信你能为企业创造价值，而你有 3 分钟的时间来建立他们对你的这份信任，进而为自己创造电话面试的机会。

数据科学的一大特征是，你在自己的项目中所做的工作，和你被录用之后所做的工作几乎一样。作为数据科学家，在 [Lending Club](https://www.lendingclub.com/) 分析信贷数据，可能与分析[他们发布的](https://www.lendingclub.com/info/download-data.action)匿名贷款数据有很大的相似之处。

![Lending Club](lending_club.png)

<small>Lending Club 匿名数据的前几行</small>

建立 HR 对你的信任，最重要的就是证明你能做他们需要你做的工作。对于数据科学而言，这归结为创建项目简历。项目越“真实”，HR 越相信你将是企业的有用之人，你获得电话面试的机会就越大。

## 你的数据科学简历需要包含哪些内容

既然我们知道了需要一份简历，我们就需要弄清楚它需要包含哪些内容。至少，你应该在 [GitHub](https://www.github.com/) 或你的博客上有一些项目，代码是可见的，并配有良好的文档。HR 越是容易找到这些项目，他们就越容易对你的技能进行评估。每个项目都应该尽可能配有良好的文档，用 `README` 文件说明如何进行设置，并介绍数据的特点。

![GitHub Project](github_project.png)

<small>GitHub 上一个组织良好的项目</small>

我们将讨论一些应该写入你的简历的项目类型。建议每种类型都有多个项目，尤其是与你希望从事的岗位相关的项目类型。比方说，如果你申请的岗位需要大量机器学习的知识技能，那么多创建一些用到机器学习的端到端项目会很有帮助。另一方面，如果你申请的是分析师的岗位，那么数据清理和数据呈现项目就更关键了。

## 数据清理项目

数据清理项目向 HR 展示了你能够提取不同的数据集并加以利用。数据清理是数据科学家做的最多的工作，因此，它是需要展示的关键技能。这类项目涉及提取杂乱数据，然后清理，并做分析。数据清理项目证明了你的数据推理能力，以及你将多个数据源的数据提取整合为单个数据集的能力。数据清理是所有数据科学家工作的重要部分，它展示了，在成为公司的助力之前，你就已经具备了这份能力。

你将需要把原始数据清理成易于分析的形式。要做到这一点，你需要：

- 找一个杂乱的数据集
 - 可以在 [data.gev](https://www.data.gov/)，[/r/datasets](https://www.reddit.com/r/datasets/)，或 [Kaggle DataSets](https://www.kaggle.com/datasets) 上找找看
 - 不要挑清理后的数据——挑选有多个数据文件，并且数据有细微差别的那种。
 - 如果可以，找一些附加数据集——比如说，如果你下载了一个航班的数据集，那么通过[谷歌](https://www.google.com/)是否可以找到一些相关的，可与之结合的数据集？
 - 尝试去挑一些你个人感兴趣的——这样，你将完成一个更好的最终项目。
- 选一个可用数据作答的问题
 - 探索数据
 - 从一个有趣的角度进行探索
- 清理数据
 - 如果有多个数据文件，将它们整合到一起
 - 确保你希望进行探索的，在数据层面是可实现的
- 做一些基础分析
 - 尝试着回答你起初选择的问题
- 展示结果
 - 建议用 [Jupyter Notebook](http://jupyter.org/) 或 [R Markdown](http://rmarkdown.rstudio.com/) 进行数据清理和分析
 - 确保代码和逻辑是可理解的，尽可能多地使用注释和 Markdown 单元阐明过程
 - 将项目上传到 GitHub
 - 由于许可的问题，不是总能将原始数据一并提交到 Git 仓库，因此你至少要描述一下原始数据，并说明出处。


本系列之前的文章 `Analyzing NYC School Data` 的第一部分，已经介绍了如何一步步创建一个完整的数据清理项目。你可以在[这里](https://www.dataquest.io/blog/data-science-portfolio-project/)查看。

![A data dictionary of some of the NYC school data.](xj5ud4r.png)

<small>部分纽约市学校数据的数据字典</small>

如果你在寻找一个好的数据集上有困难，以下是一些例子：

- [美国航班数据](http://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time)
- [纽约市地铁旋转门数据](http://web.mta.info/developers/turnstile.html)
- [足球数据](http://www.jokecamp.com/blog/guide-to-football-and-soccer-data-and-apis/)

![The NYC subway](subway.jpg)

<small>纽约市地铁，人来人往</small>

如果你想要一些灵感，以下是一些优秀的数据清理项目的例子：

- [Twitter 数据分析](https://marcobonzanini.com/2015/03/09/mining-twitter-data-with-python-part-2/)
- [Airbnb 数据清理](http://brettromero.com/wordpress/data-science-kaggle-walkthrough-cleaning-data/)

## 数据呈现项目

数据呈现项目展现了你对数据的洞察力，从数据中提取洞见并用数据说话的能力。数据呈现对商业价值有巨大影响，因此，这将是你简历的重要组成部分。这个项目涉及提取一组数据，并用数据呈现一个令人信服的结论。例如，你可以利用航班数据说明某些机场存在显著的航班延迟现象，而这也许可以通过改变航线改善。

一个优秀的数据呈现项目会用到大量的可视化，并能一步步地引导读者了解分析结果。以下是创建一个优秀的数据呈现项目的参考步骤：

- 找一个有趣的数据集
 - 可以在 [data.gev](https://www.data.gov/)，[r/datasets](https://www.reddit.com/r/datasets/)，或 [Kaggle DataSets](https://www.kaggle.com/datasets) 上找找看
 - 挑一个与近期发生的事件有关的内容，以引起读者的兴趣
 - 尝试去挑一些你个人感兴趣的——这样，你将完成一个更好的最终项目。
- 从不同方向探索数据
 - 探索数据
 - 从数据中找出有趣的相关性
 - 创建图表并一步步展示你的发现
- 详细记录这个引人注目的过程
 - 从所有的探索中挑选一个最有趣的角度
 - 记录从原始数据到最终发现的探索过程
 - 创建令人信服的图表
 - 就探索过程中每一步的思考，写一些扩展阐述，也可以对代码进行解释
 - 就每一步的结果，写一些扩展分析，以清晰地告诉读者
 - 告诉读者你在分析数据过程中的所思所想
- 展示结果
 - 建议用 [Jupyter Notebook](http://jupyter.org/) 或 [R Markdown](http://rmarkdown.rstudio.com/) 进行数据分析
 - 确保代码和逻辑是可理解的，尽可能多地使用注释和 Markdown 单元阐明过程
 - 将项目上传到 GitHub

本系列之前的文章 `Analyzing NYC School Data` 的第二部分，已经介绍了如何一步一步让数据发声。你可以在[这里](https://www.dataquest.io/blog/data-science-portfolio-project/)查看。

![A map of SAT scores by district in NYC](district_sat.png)

<small>按街区 SAT 成绩划分的纽约市地图</small>

如果你在寻找一个好的数据集上有困难，这里有一些例子：

- [Lending club 的贷款数据](https://www.lendingclub.com/info/download-data.action)
- [FiveThirtyEight 的数据集](https://github.com/fivethirtyeight/data)
- [Hacker new 的数据](https://github.com/sytelus/HackerNewsData)

如果你想要一些灵感，以下是一些优秀的数据呈现项目的例子：

- [Hip-hop 与美国总统候选人特朗普](http://projects.fivethirtyeight.com/clinton-trump-hip-hop-lyrics/)
- [纽约市出租车与优步数据分析 ](http://toddwschneider.com/posts/analyzing-1-1-billion-nyc-taxi-and-uber-trips-with-a-vengeance/)
- [跟踪研究 NBA 球员的运动](http://savvastjortjoglou.com/nba-play-by-play-movements.html)

![Candidate tweets](candidate_tweets.png)

<small>提及 2016 年美国总统大选候选人的歌词（图片来自以上第一个项目）</small>

## 端到端项目

到目前为止，我们已经介绍了涉及探索性数据清理和分析的项目。这些项目能让 HR 更好地认识到你对数据的洞察力以及呈现数据的能力。然而，它们并不足以展示你的创建面向客户的系统的能力。面向客户的系统涉及高性能的代码，这意味着系统可以使用不同数据，运行多次，产生不同输出。举个例子，一个可以对股市进行预测的系统——每天早上，它会自动下载最新的股市数据，然后据此预测当天哪些股票会走红。

为了展现我们能够创建业务系统，我们需要创建一个端到端的项目。端到端的项目可以接收并处理数据，然后产生输出。通常，这些输出都是机器学习算法的结果，但也可以是其他输出，比如符合某一标准的行总数。

这里的关键是，要让系统能灵活地处理新的数据（比如股市数据），并具有高性能。此外，使代码易于安装设置与运行也很重要。以下是创建一个优秀的端到端项目的参考步骤：

- 找一个有趣的专题
 - 我们不会仅处理一个单一的静态数据集，因此，你需要定一个专题
 - 该专题应该使用公开的、经常更新的数据
 - 以下是一些例子：
    - [天气](https://www.wunderground.com/weather/api/d/pricing.html)
    - [NBA 游戏](http://www.gregreda.com/2015/02/15/web-scraping-finding-the-api/)
    - [航班](http://www.faa.gov/nextgen/programs/swim/products/)
    - [电价](http://www.eia.gov/electricity/data.cfm)
- 导入并解析多个数据集
 - 在你的能力范围内，下载尽可能多的数据
 - 阅读理解数据
 - 找出你所期望的预测内容
- 创建预测
 - 估计任何需要实现的功能
 - 训练并测试数据
 - 做出预测
- 整理代码并配上文档
 - 将代码分解为多个文件
 - 在项目中添加一个 `REAME` 文件，以阐述如何安装和运行该项目
 - 添加内联文档
 - 使代码能轻松地从命令行运行
- 上传项目到 GitHub

本系列之前的文章 `Analyzing Fannie Mae loan data` 中，已经介绍了如何一步一步创建端到端的机器学期项目。你可以在[这里](https://www.dataquest.io/blog/data-science-portfolio-machine-learning)查看。

如果你在定一个好的专题上有困难，以下是一些例子：

- [历史的 S&P 500 数据](http://finance.yahoo.com/quote/%5EGSPC/history?p=%5EGSPC)
- [流式 Twitter 数据](https://dev.twitter.com/streaming/overview)

![sp500](sp500.png)

<small>S&P 500 数据</small>

如果你想要一些灵感，以下是一些优秀的端到端项目例子：

- [股票价格预测](https://github.com/wzchen/stock_market_prediction)
- [自动音乐生成器](https://github.com/MattVitelli/GRUV)

## 说明性文章

理解并解释复杂的数据科学项目很重要，比如机器学习的算法。这可以让 HR 认识到，你善于向组内的其他人或客户解释复杂的概念。这也是数据科学简历的关键点，因为它涵盖了现实世界中数据科学工作的重要部分。这同时还展示了你对概念及其工作原理有深入的理解，而不是仅仅停留在语法层面。深入的理解有助于你更好地判断并做出更好的选择，以及向他人介绍你的工作。

为了写一篇说明性的文章，我们首先需要挑一个数据科学的专题，然后撰写博客。这篇文章需要带领读者从一无所知到对概念有一个清晰的了解。而写文章的关键是，使用朴实的、简单的的语言——你写得越专业，HR 就越难知道你是真懂还是装懂。

写说明性文章的几个重要的步骤是：挑一个你熟悉的专题，带领读者理解概念，然后利用最终的概念做一些有趣的事。以下是一些的参考步骤：

- 找一个你熟悉的或想要去学习的概念
 - 机器学习的算法，比如 [k-nearest neighbors (最近邻居法) ](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) 就是一个可选的例子
 - 统计学的概念，也是不错的选择
 - 确保这个概念有一些精妙之处值得挖掘
 - 确保你真的理解了这个概念，并且解释起来并不复杂
- 挑一个数据集辅助解释
 - 比方说，如果你选择对 k-nearest nerghbors 进行阐述，你可以借助 NBA 的数据（寻找球路相似的球员）
- 列一个文章的大纲
 - 假设读者完全不了解你将阐述的概念
 - 将概念分解成几个部分
    - 比如，k-nearest neighbors，可以分解为：
      - 利用相似性进行预测
      - 相似度量
      - 欧式距离
      - 利用 k = 1 进行匹配
      - 利用 k > 1 进行匹配
- 撰写文章
 - 用直白的语言进行清晰的描述
 - 围绕一个中心点写
 - 试着找一个非技术人员读一读这篇文章，看看他们的反应
- 分享文章
 - 最好推送到你自己的博客
 - 如果没有博客，就上传到 GitHub

如果你在找一个好的概念上有困难，以下是一些例子：

- [k-平均算法](https://en.wikipedia.org/wiki/K-means_clustering)
- [矩阵乘法](https://en.wikipedia.org/wiki/Matrix_multiplication)
- [卡方检验](https://en.wikipedia.org/wiki/Chi-squared_test)

![k-means clustering](kmeans.svg)

<small>k-平均算法的可视化</small>

如果你想要一些灵感，下面是一些比较好的说明性文章的例子：

- [线性回归](http://eli.thegreenplace.net/2016/linear-regression/)
- [自然语言处理](https://www.dataquest.io/blog/natural-language-processing-with-python/)
- [朴素贝叶斯](https://alexn.org/blog/2012/02/09/howto-build-naive-bayes-classifier.html)
- [k-nearest neighbors](https://www.dataquest.io/blog/k-nearest-neighbors-in-python)

## 可选的简历部分

虽然写一份优秀的简历，关键在于你在 GitHub 和博客上的项目，但是添加一些其他的组件也会很有帮助，比如 Quora 上的回答，演讲以及数据科学竞赛的结果。这些通常是 HR 第二关心的，但它们也是突出和证明你能力的一种很好的方式。

### 演讲

演讲是一种帮助教导他人的很有效的方式，它还能够向 HR 证明你对某个专题已经熟悉到足以为人师的地步。它可以帮助 HR 认识你的沟通与演说能力。这些技能与简历上的其他部分在一定程度上会有重叠，但仍然是很好的证明。

最常见的演讲地点是当地的 [Meetup](https://www.meetup.com/)。Meetup 上的演讲都是围绕具体的主题展开的，比如 “Python”，或者“利用 D3 进行数据可视化”。

为给出一个好的演讲，以下是几个值得参考的步骤：

- 找一个你从事过的项目或知道的概念
 - 最好先看一看你写在简历上的项目和博客文章
 - 无论你最终挑了什么，它应该与聚会的主题是一致的
- 分解项目，并用幻灯片演示
 - 你需要将项目进行分解，并用一系列幻灯片进行演示
 - 每张幻灯片都应该尽可能地有文字说明
- 多练几次演讲
- 正式演讲
- 将幻灯片上传到 GitHub 或 你的博客

如果你需要一些灵感，以下是一些优秀的演讲例子：

- [计算统计学](https://www.youtube.com/watch?v=VR52vSbHBAk将)
- [Scikit-learn vs Spark for ML pipelines](https://www.youtube.com/watch?v=v7EX5aYE0xM)
- [NHL(国家冰球联盟) 点球分析](https://www.youtube.com/watch?v=uW02_GnQKeM)

### 数据科学竞赛

数据科学竞赛涉及用大量数据训练最精确的机器学习模型。因此参加竞赛是很好的学习方式。从 HR 的视角来看，数据科学竞赛可以证明你的技术能力（如果你做得够好的话），你的主动性（如果你确实付出了很多努力）以及你的合作能力（如果你是与他人合作参赛的）。这同样与简历上的其他项目有重叠，但它也是突出你能力的第二种方式。

大多数数据科学竞赛都由 [Kaggle](https://www.kaggle.com/) 和 [DrivenData](https://www.drivendata.org/)举办。

要参加（以上的）的数据科学竞赛，你只需要在相应的网站上注册，然后就可以开始了！你可以从[这里](https://www.kaggle.com/c/titanic)开始一项竞赛，你也可以在[这里](https://www.dataquest.io/course/kaggle-competitions)找到一些教程。

![Kaggle](kaggle.png)

<small>Kaggle 上一项赛事的排行榜</small>

## 小结

现在，你对于要在简历上展示哪些内容，以及如何创建简历，应该有了一个清晰的概念。现在就可以行动起来创建简历了！

如果你已经有一份简历，想秀一下，请在评论区告诉我们！

如果你喜欢本文，你也许会喜欢“创建一份数据科学简历”系列的其他文章：

- [让数据发声](https://www.dataquest.io/blog/data-science-portfolio-project/)
- [要写数据科学博客，如何进行设置](https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/)
- [如何创建一个端到端的机器学习项目](https://www.dataquest.io/blog/data-science-portfolio-machine-learning)

***

[点此查看原文链接](https://www.dataquest.io/blog/build-a-data-science-portfolio/)
