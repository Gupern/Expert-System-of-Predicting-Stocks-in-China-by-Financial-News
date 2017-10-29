## Introduction

2017-10-25：持续交付，小进步，多迭代，从现在开始

我本科的毕业设计做的是《面向财经新闻的文本挖掘系统设计与实现》，可惜只完成了前两部分。
虽然差一点拿到优秀论文，但是最后还是不要了，毕竟自己没完成，没整合成一个系统。因此放到github上来，慢慢改进，希望做成一个专家系统。

兴趣是最好的老师，没有毕业、没有学分的束缚，相信会更好！



### Coding

---

- [x] 集成到Flask Web中(1): 做成一个后台系统，用flask-admin框架

- [ ] 集成到Flask Web中(1): 增加视图

- [ ] 高级消息队列apsheduler



### To Do

---

- [ ] 整合到docker一键部署，在虚拟机中开发

- [ ] 学习d3.js进行可视化

- [ ] 进修机器学习、博弈论、和时间序列知识，等建设好数据仓库，则进行预测

- [ ] 获得所有最新的股票名称和相应股票代码

- [ ] 查询每条新闻中出现的股票名称或代码，打上标签nameTaps、codeTaps

- [ ] 情感分析

- [ ] 根据热度值画图

- [ ] 搭建大数据集群，存储数据到elasticsearch/spark中

- [ ] 自动爬取最新新闻

- [ ] 爬取股票数据

- [ ] 做实时对比图

- [ ] 未完待续...

### Done list

---

- [x] 爬虫用scrapy框架，争取爬到更多数据。

> 用scrapy爬虫爬取和讯网的股票新闻 http://stock.hexun.com/stocknews/, 注：已遵守该网站的robots.txt说明（All robots will spider the domain)
> 已爬106507条新闻，有body、date、title、source_url四个字段，代码祥见文件夹scrapyLearning
> 初步掌握scrapy框架，不过仍未精通，已知还欠缺代理ip、图像识别验证码、解密等高级知识


- [x] 建立pipeline将数据存入到MongoDB，Pipeline详情见另一项目Data_Clean_Pipeline_System

- [x] 数据库选用NoSQL，MongoDB，如果有必要，存数字数据到MySQL中当做学习   

> 已经存入MongoDB，MongoDB的下载看官网https://www.mongodb.com/
