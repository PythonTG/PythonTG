
title: 打造数据科学作品集: 去哪儿找优质数据集？
author: Vik Paruchuri
translator: EarlGrey
reviewer: EarlGrey
date: 20161012
permalink: 
keywords: 

***

如果你做过业余数据科学项目，很可能花过很多时间浏览互联网，寻找可以分析的有趣数据。从几十个数据集中筛选出合适的数据集，本身就充满了乐趣。但是下载并导入了许多 csv 文件之后，如果发现这些数据其实没什么意义的话，将会是十分令人郁闷的。幸运的是，有许多在线仓库会整理好数据集，大部分会移除那些没什么价值的。

在本文中，我们将介绍数据科学项目的类型，包括数据可视化项目、数据清洗项目和机器学习项目，并指出每种类型应该去哪里找数据集。不管你是想加强自身的数据科学作品集（如展示数据可视化能力），还是就想花几个小时练习一下机器学习技巧，都能在本文中找到答案。

## 数据可视化项目的数据集



## Datasets for Data Visualization Projects

A typical data visualization project might be something along the lines of "I
want to make an infographic about how income varies across the different
states in the US". There are a few considerations to keep in mind when looking
for a good dataset for a data visualization project:

  * It shouldn't be messy, because you don't want to spend a lot of time cleaning data.
  * It should be nuanced and interesting enough to make charts about.
  * Ideally, each column should be well-explained, so the visualization is accurate.
  * The dataset shouldn't have too many rows or columns, so it's easy to work with.

A good place to find good datasets for data visualization projects are news
sites that release their data publicly. They typically clean the data for you,
and also already have charts they've made that you can replicate or improve.

### 1\. FiveThirtyEight

![](/blog/images/datasets/fivethirtyeight.jpg)

[FiveThirtyEight](http://fivethirtyeight.com/) is an incredibly popular
interactive news and sports site started by [Nate Silver](http://fivethirtyeight.com/contributors/nate-silver/). They write interesting data-driven articles, like ["Don't blame a skills gap for lack of hiring in manufacturing"](http://fivethirtyeight.com/features/dont-blame-a-skills-gap-for-lack-of-hiring-in-manufacturing/) and ["2016 NFL Predictions"](http://projects.fivethirtyeight.com/2016-nfl-predictions/).

FiveThirtyEight makes the datasets used in its articles available online on
[Github](https://www.github.com).

[View the FiveThirtyEight Datasets](https://github.com/fivethirtyeight/data)

Here are some examples:

  * [Airline Safety](https://github.com/fivethirtyeight/data/tree/master/airline-safety) - contains information on accidents from each airline.
  * [US Weather History](https://github.com/fivethirtyeight/data/tree/master/us-weather-history) - historical weather data for the US.
  * [Study Drugs](https://github.com/fivethirtyeight/data/tree/master/study-drugs) - data on who's taking Adderall in the US.

### 2\. BuzzFeed

![](/blog/images/datasets/buzzfeed.png)

[BuzzFeed](https://www.buzzfeed.com) started as a purveyor of low-quality
articles, but has since evolved and now writes some investigative pieces, like
["The court that rules the world"](https://www.buzzfeed.com/chrishamby/super-
court?utm_term=.wbp4OyzN6#.qoYY4v0N1) and ["The short life of Deonte
Hoard"](https://www.buzzfeed.com/albertsamaha/the-short-life-of-deonte-hoard-
the-53rd-person-murdered-in-c?utm_term=.kr5wlo05R#.wa2WmQvMN).

BuzzFeed makes the datasets used in its articles available on Github.

[View the BuzzFeed Datasets](https://github.com/BuzzFeedNews)

Here are some examples:

  * [Federal Surveillance Planes](https://github.com/BuzzFeedNews/2016-04-federal-surveillance-planes) - contains data on planes used for domestic surveillance.
  * [Zika Virus](https://github.com/BuzzFeedNews/zika-data) - data about the geography of the Zika virus outbreak.
  * [Firearm background checks](https://github.com/BuzzFeedNews/nics-firearm-background-checks) - data on background checks of people attempting to buy firearms.

### 3\. Socrata OpenData

![](/blog/images/datasets/socrata.jpeg)

[Socrata OpenData](https://opendata.socrata.com/) is a portal that contains
multiple clean datasets that can be explored in the browser or downloaded to
visualize. A significant portion of the data is from US government sources,
and many are outdated.

You can explore and download data from OpenData without registering. You can
also use visualization and exploration tools to explore the data in the
browser.

[View Socrata OpenData](https://opendata.socrata.com/)

Here are some examples:

  * [White House staff salaries](https://opendata.socrata.com/Government/2010-Report-to-Congress-on-White-House-Staff/vedg-c5sb0) - data on what each White House staffer made in 2010.
  * [Radiation Analysis](https://opendata.socrata.com/Government/Milk-RadNet-Laboratory-Analysis/pkfj-5jsd) - data on what milk products in what locations in the US were radioactive.
  * [Workplace fatalities by US state](https://opendata.socrata.com/Government/2012-Workplace-Fatalities-by-State/vcx3-xxtb) - the number of workplace deaths across the US.

## Datasets for Data Processing Projects

Sometimes you just want to work with a large dataset. The end result doesn't
matter as much as the process of reading in and analyzing the data. You might
use tools like [Spark](http://spark.apache.org/) or
[Hadoop](http://hadoop.apache.org/) to distribute the processing across
multiple nodes. Things to keep in mind when looking for a good data processing
dataset:

  * The cleaner the data, the better - cleaning a large dataset can be very time consuming.
  * The dataset should be interesting.
  * There should be an interesting question that can be answered with the data.

A good place to find large public datasets are cloud hosting providers like
[Amazon](https://www.amazon.com) and [Google](https://www.google.com). They
have an incentive to host the datasets, because they make you analyze them
using their infrastructure \(and pay them\).

### 4\. AWS Public Datasets

![](/blog/images/datasets/aws.jpg)

Amazon makes large datasets available on its [Amazon Web
Services](https://www.amazon.com/aws) platform. You can download the data and
work with it on your own computer, or analyze the data in the cloud using
[EC2](https://aws.amazon.com/ec2/) and Hadoop via
[EMR](https://aws.amazon.com/emr/). You can read more about how the program
works [here](https://aws.amazon.com/public-data-sets/).

Amazon has a page that lists all of the datasets for you to browse. You'll
need an AWS account, although Amazon gives you a
[free](https://aws.amazon.com/free/) access tier for new accounts that will
enable you to explore the data without being charged.

[View AWS Public
Datasets](https://aws.amazon.com/datasets/?_encoding=UTF8&jiveRedirect=1)

Here are some examples:

  * [Lists of n-grams from Google Books](https://aws.amazon.com/datasets/google-books-ngrams/) - common words and groups of words from a huge set of books.
  * [Common Crawl Corpus](https://aws.amazon.com/public-data-sets/common-crawl/) - data from a crawl of over 5 billion web pages.
  * [Landsat images](https://aws.amazon.com/public-data-sets/landsat/) - moderate resolution satellite images of the surface of the Earth.

### 5\. Google Public Datasets

![](/blog/images/datasets/google.jpg)

Much like Amazon, Google also has a cloud hosting service, called [Google
Cloud Platform](https://cloud.google.com/). With GCP, you can use a tool
called [BigQuery](https://cloud.google.com/bigquery/) to explore large
datasets.

Google lists all of the datasets on a page. You'll need to sign up for a GCP
account, but the first 1TB of queries you make are
[free](https://cloud.google.com/bigquery/pricing#query-pricing-details).

[View Google Public Datasets](https://cloud.google.com/bigquery/public-data/)

Here are some examples:

  * [USA Names](https://cloud.google.com/bigquery/public-data/usa-names) - contains all Social Security name applications in the US, from 1879 to 2015.
  * [Github Activity](https://cloud.google.com/bigquery/public-data/github) - contains all public activity on over 2.8 million public Github repositories.
  * [Historical Weather](https://cloud.google.com/bigquery/public-data/noaa-gsod) - data from 9000 NOAA weather stations from 1929 to 2016.

### 6\. Wikipedia

![](/blog/images/datasets/wikipedia.jpg)

[Wikipedia](https://www.wikipedia.org) is a free, online, community-edited
encyclopedia. Wikipedia contains an astonishing breadth of knowledge,
containing pages on everything from the [Ottoman-Habsburg
Wars](https://en.wikipedia.org/wiki/Ottoman%E2%80%93Habsburg_wars) to [Leonard
Nimoy](https://en.wikipedia.org/wiki/Leonard_Nimoy). As part of Wikipedia's
commitment to advancing knowledge, they offer all of their content for free,
and regularly generate dumps of all the articles on the site. Additionally,
Wikipedia offers edit history and activity, so you can track how a page on a
topic evolves over time, and who contributes to it.

You can find the various ways to download the data on the Wikipedia site.
You'll also find scripts to reformat the data in various ways.

[View Wikipedia
Datasets](https://en.wikipedia.org/wiki/Wikipedia:Database_download)

Here are some examples:

  * [All images and other media from Wikipedia](https://meta.wikimedia.org/wiki/Mirroring_Wikimedia_project_XML_dumps#Media0) - all the images and other media files on Wikipedia.
  * [Full site dumps](https://dumps.wikimedia.org/) - of the content on Wikipedia, in various formats.

### Enjoying this post? Learn data science with Dataquest\!

#####

  * Learn from the comfort of your browser.
  * Work with real-life data sets.
  * Build a portfolio of projects.

[Start for Free](https://www.dataquest.io/)

## Datasets for Machine Learning Projects

When you're working on a machine learning project, you want to be able to
predict a column from the other columns in a dataset. In order to be able to
do this, we need to make sure that:

  * The dataset isn't too messy - if it is, we'll spend all of our time cleaning the data.
  * There's an interesting target column to make predictions for.
  * The other variables have some explanatory power for the target column.

There are a few online repositories of datasets that are specifically for
machine learning. These datasets are typically cleaned up beforehand, and
allow for testing of algorithms very quickly.

### 7\. Kaggle

![](/blog/images/datasets/kaggle.jpg)

[Kaggle](https://www.kaggle.com) is a data science community that hosts
machine learning competitions. There are a variety of externally-contributed
interesting datasets on the site. Kaggle has both live and historical
competitions. You can download data for either, but you have to sign up for
Kaggle and accept the terms of service for the competition.

You can download data from Kaggle by entering a
[competition](https://www.kaggle.com/competitions). Each competition has its
own associated dataset. There are also user-contributed datasets found in the
new [Kaggle Datasets](https://www.kaggle.com/datasets) offering.

[View Kaggle Datasets](https://www.kaggle.com/datasets)  
[View Kaggle Competitions](https://www.kaggle.com/competitions)

Here are some examples:

  * [Satellite Photograph Order](https://www.kaggle.com/c/draper-satellite-image-chronology) - a dataset of satellite photos of Earth - the goal is to predict which photos were taken earlier than others.
  * [Manufacturing Process Failures](https://www.kaggle.com/c/bosch-production-line-performance) - a dataset of variables that were measured during the manufacturing process. The goal is to predict faults with the manufacturing.
  * [Multiple Choice Questions](https://www.kaggle.com/c/the-allen-ai-science-challenge) - a dataset of multiple choice questions and the corresponding correct answers. The goal is to predict the answer for any given question.

### 8\. UCI Machine Learning Repository

![](/blog/images/datasets/uci.gif)

The [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/) is one
of the oldest sources of datasets on the web. Although the datasets are user-
contributed, and thus have varying levels of documentation and cleanliness,
the vast majority are clean and ready for machine learning to be applied. UCI
is a great first stop when looking for interesting datasets.

You can download data directly from the UCI Machine Learning repository,
without registration. These datasets tend to be fairly small, and don't have a
lot of nuance, but are good for machine learning.

[View UCI Machine Learning
Repository](http://archive.ics.uci.edu/ml/datasets.html)

Here are some examples:

  * [Email spam](http://archive.ics.uci.edu/ml/datasets/Spambase) - contains emails, along with a label of whether or not they're spam.
  * [Wine classification](http://archive.ics.uci.edu/ml/datasets/Wine) - contains various attributes of 178 different wines.
  * [Solar flares](http://archive.ics.uci.edu/ml/datasets/Solar+Flare) - attributes of solar flares, useful for predicting characteristics of flares.

### 9\. Quandl

![](/blog/images/datasets/quandl.png)

[Quandl](https://www.quandl.com) is a repository of economic and financial
data. Some of this information is free, but many datasets require purchase.
Quandl is useful for building models to predict economic indicators or stock
prices. Due to the large amount of available datasets, it's possible to build
a complex model that uses many datasets to predict values in another.

[View Quandl Datasets](https://www.quandl.com/browse).

Here are some examples:

  * [Entrepreneurial activity by race and other factors](https://www.quandl.com/data/KAUFFMAN?keyword=) - contains data from the Kauffman foundation on entrepreneurs in the US.
  * [Chinese macroeconomic data](https://www.quandl.com/data/NBSC?keyword=) -- indicators of Chinese economic health.
  * [US Federal Reserve data](https://www.quandl.com/data/FRED?keyword=) - US economic indicators, from the Federal Reserve.

## Datasets for Data Cleaning Projects

Sometimes, it can be very satisfying to take a dataset spread across multiple
files, clean them up, condense them into one, and then do some analysis. In
data cleaning projects, sometimes it takes hours of research to figure out
what each column in the dataset means. It may sometimes turn out that the
dataset you're analyzing isn't really suitable for what you're trying to do,
and you'll need to start over.

When looking for a good dataset for a data cleaning project, you want it to:

  * Be spread over multiple files.
  * Have a lot of nuance, and many possible angles to take.
  * Require a good amount of research to understand.
  * Be as "real-world" as possible.

These types of datasets are typically found on aggregators of datasets. These
aggregators tend to have datasets from multiple sources, without much
curation. Too much curation gives us overly neat datasets that are hard to do
extensive cleaning on.

### 10\. Data.gov

![](/blog/images/datasets/datagov.jpg)

[Data.gov](https://www.data.gov) is a relatively new site that's part of a US
effort towards open government. Data.gov makes it possible to download data
from multiple US government agencies. Data can range from government budgets
to school performance scores. Much of the data requires additional research,
and it can sometimes be hard to figure out which dataset is the "correct"
version. Anyone can download the data, although some datasets require
additional hoops to be jumped through, like agreeing to licensing agreements.

You can browse the datasets on Data.gov directly, without registering. You can
browse by topic area, or search for a specific dataset.

[View Data.gov Datasets](https://www.data.gov/)

Here are some examples:

  * [Food Environment Atlas](https://catalog.data.gov/dataset/food-environment-atlas-f4a22) - contains data on how local food choices affect diet in the US.
  * [School system finances](https://catalog.data.gov/dataset/annual-survey-of-school-system-finances) - a survey of the finances of school systems in the US.
  * [Chronic disease data](https://catalog.data.gov/dataset/u-s-chronic-disease-indicators-cdi-e50c9) - data on chronic disease indicators in areas across the US.

### 11\. The World Bank

![](/blog/images/datasets/worldbank.jpg)

[The World Bank](http://www.worldbank.org/) is a global development
organization that offers loans and advice to developing countries. The World
Bank regularly funds programs in developing countries, then gathers data to
monitor the success of these programs.

You can browse World Bank datasets directly, without registering. The datasets
have many missing values, and sometimes take several clicks to actually get to
data.

[View World Bank Datasets](http://data.worldbank.org/)

Here are some examples:

  * [World Development Indicators](http://data.worldbank.org/data-catalog/world-development-indicators) - contains country level information on development.
  * [Educational Statistics](http://data.worldbank.org/data-catalog/ed-stats) - data on education by country.
  * [World Bank project costs](http://www.worldbank.org/projects) - data on World Bank projects and their corresponding costs.

### 12\. /r/datasets

![](/blog/images/datasets/reddit.jpg)

[Reddit](https://www.reddit.com), a popular community discussion site, has a
section devoted to sharing interesting datasets. It's called the [datasets
subreddit](https://www.reddit.com/r/datasets), or /r/datasets. The scope of
these datasets varies a lot, since they're all user-submitted, but they tend
to be very interesting and nuanced.

You can browse the subreddit [here](https://www.reddit.com/r/datasets). You
can also see the most highly upvoted datasets
[here](https://www.reddit.com/r/datasets/top/?sort=top&t=all).

[View Top /r/datasets
Posts](https://www.reddit.com/r/datasets/top/?sort=top&t=all)

Here are some examples:

  * [All Reddit submissions](https://www.reddit.com/r/datasets/comments/3mg812/full_reddit_submission_corpus_now_available_2006/) - contains reddit submissions through 2015.
  * [Jeopardy questions](https://www.reddit.com/r/datasets/comments/1uyd0t/200000_jeopardy_questions_in_a_json_file/) - questions and point values from the gameshow Jeopardy.
  * [New York City property tax data](https://www.reddit.com/r/datasets/comments/4jjcdx/we_scraped_11_million_property_tax_bills_to/) - data about properties and assessed value in New York City.

### 13\. Academic Torrents

![](/blog/images/datasets/at-logo.png)

[Academic Torrents](http://academictorrents.com/) is a new site that is geared
around sharing the datasets from scientific papers. It's a newer site, so it's
hard to tell what the most common types of datasets will look like. For now,
it has tons of interesting datasets that lack context.

You can browse the datasets directly on the site. Since it's a torrent site,
all of the datasets can be immediately downloaded, but you'll need a
[Bittorrent](http://www.bittorrent.com/) client. [Deluge](http://deluge-
torrent.org/) is a good free option.

[View Academic Torrents
Datasets](http://academictorrents.com/browse.php?cat=6)

Here are some examples:

  * [Enron emails](http://academictorrents.com/details/4697a6e1e7841602651b087d84f904d43590d4ff) - a set of many emails from executives at Enron, a company that famously went bankrupt.
  * [Student learning factors](http://academictorrents.com/details/e24e083cc337695bb84a2b68707695579c0ab4d8) - a set of factors that measure and influence student learning.
  * [News articles](http://academictorrents.com/details/95d3b03397a0bafd74a662fe13ba3550c13b7ce1) - contains news article attributes and a target variable.

## Bonus: Streaming data

It's very common when you're building a data science project to download a
dataset and then process it. However, as online services generate more and
more data, an increasing amount is generated in real-time, and not available
in dataset form. Some examples of this include data on tweets from
[Twitter](https://www.twitter.com), and stock price data. There aren't many
good sources to acquire this kind of data, but we'll list a few in case you
want to try your hand at a streaming data project.

### 14\. Twitter

![](/blog/images/datasets/twitter.png)

[Twitter](https://www.twitter.com) has a good streaming API, and makes it
relatively straightforward to filter and stream tweets. You can get started
[here](https://dev.twitter.com/streaming/overview). There are tons of options
here - you could figure out what states are the happiest, or which countries
use the most complex language. We also recently wrote an article to get you
started with the Twitter API [here](https://www.dataquest.io/blog/streaming-
data-python/).

[Get started with the Twitter API](https://dev.twitter.com/streaming/overview)

### 15\. Github

![](/blog/images/datasets/github.png)

[Github](https://github.com/) has an API that allows you to access repository
activity and code. You can get started with the API
[here](https://developer.github.com/v3/). The options are endless - you could
build a system to automatically score code quality, or figure out how code
evolves over time in large projects.

[Get started with the Github API](https://developer.github.com/v3/)

### 16\. Quantopian

![](/blog/images/datasets/quantopian.jpg)

[Quantopian](https://www.quantopian.com/) is a site where you can develop,
test, and operationalize stock trading algorithms. In order to help you do
that, they give you access to free minute by minute stock price data. You
could build a stock price prediction algorithm.

[Get started with Quantopian](https://www.quantopian.com/)

### 17\. Wunderground

![](/blog/images/datasets/wunderground.jpg)

[Wunderground](http://www.wunderground.com/) has an API for weather forecasts
that free up to 500 API calls per day. You could use these calls to build up a
set of historical weather data, and make predictions about the weather
tomorrow.

[Get started with the Wunderground
API](https://www.wunderground.com/weather/api/)

## Next steps

In this post, we covered good places to find datasets for any type of data
science project. We hope that you find something interesting that you want to
sink your teeth into\!

If you do end up building a project, we'd love to hear about it. Please tell
us about it in the comments below\!

_If you liked this, you might like to read the other posts in our 'Build a
Data Science Portfolio' series:_

  * _[Storytelling with data](https://www.dataquest.io/blog/data-science-portfolio-project/)._
  * _[How to setup up a data science blog](https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/)._
  * _[Building a machine learning project](https://www.dataquest.io/blog/data-science-portfolio-machine-learning/)._
  * _[The key to building a data science portfolio that will get you a job](https://www.dataquest.io/blog/build-a-data-science-portfolio/)._

