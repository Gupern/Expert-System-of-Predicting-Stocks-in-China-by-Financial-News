## Introduction

2017-10-25：持续交付，小进步，多迭代，从现在开始

我本科的毕业设计做的是《面向财经新闻的文本挖掘系统设计与实现》，可惜只完成了前两部分。
虽然差一点拿到优秀论文，但是最后还是不要了，毕竟自己没完成，没整合成一个系统。因此放到github上来，慢慢改进，希望做成一个专家系统。

兴趣是最好的老师，没有毕业、没有学分的束缚，相信会更好！


- based on Flask-Admin

    1. git clone https://github.com/flask-admin/flask-admin.git
    2. cd ./flask-admin/examples/auth

- based on python3.5 and it's prefer to use virtualenv
    
    1. install pip3
        1. `wget https://bootstrap.pypa.io/get-pip.py`
        2. `python3 get-pip.py`
    2. `pip3 install virtualenv`
    3. `virtualenv py3.5env -p python3`
    4. `source py3.5env/bin/activate`
    5. `pip3 install -r requirements.txt`

- based on docker 

    1. `cd Expert-System-of-Predicting-Stocks-in-China-by-Financial-News`
    2. `sudo docker build -t esps .`
    3. `sudo docker run --restart=always -d -v /etc/localtime:/etc/localtime:ro -v /root/Desktop/Expert-System-of-Predicting-Stocks-in-China-by-Financial-News/:/mnt --net host --name esps_engine esps /mnt/engine/run.sh`

### docker启动说明

`-v /etc/localtime:/etc/localtime:ro`参数是把宿主机（host）的`/etc/localtime`（冒号前）
映射到docker内部虚拟机的`/etc/localtime`目录（两个冒号中间），后面`ro`代表这是一次只读（readonly）映射

`--net host`是把虚拟机直接绑定到本地的网络环境上，例如虚拟机可以直接在宿主机开端口

`-ti`参数实际上是`-t`和`-i`，其中`-t`是把虚拟机模拟为一个tty终端，就好像ssh终端一样可以访问。
`-i`参数是接受用户输入信息（input），其中docker作为服务运行在后台时应该去掉`-t`参数

命令中间的`bot`是docker image的名字，必须已经加载了这个image

`--rm` 用完即删，不留container

`-v /var/tmp:/var/tmp`我把tmp目录映射过去是想之间通信日志方便

`--name`是给每个container起一个名字，同一个名字的container只能运行一次，
所以是为了避免重复运行，外加也可以代替container id方便一些操作

### 本机运行：

> 假设在root用户下，本机运行

`sudo docker run -ti -v /etc/localtime:/etc/localtime:ro -v /root/Desktop/Expert-System-of-Predicting-Stocks-in-China-by-Financial-News/:/mnt --net host --name esps_engine --rm esps /mnt/engine/run.sh`

> 服务器运行，加了`-d`的参数作为服务器启动，加了`--restart=always`防止服务器关闭

`sudo docker run --restart=always -d -v /etc/localtime:/etc/localtime:ro -v /root/Desktop/Expert-System-of-Predicting-Stocks-in-China-by-Financial-News/:/mnt --net host --name esps_engine esps /mnt/engine/run.sh`


### Coding

---

- [ ] 写爬取wind万德新闻

- [ ] 开发爬虫界面，一键运行爬虫并返回最新更新时间

- [ ] 做伪数据（从csv文件中读取），开发可视化界面，用d3.js or echarts.js 将数据展示出来

- [ ] 使用结巴进行分词获取积极消极词汇


### To Do

---

- [ ] 高级消息队列apsheduler

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

- [x] 用docker运行，并写docker运行文档

- [x] 整合到docker一键部署，写好dockerfile，在虚拟机中开发

- [x] 将scrapy的爬取和讯网stocknews.hexun.com的爬虫重写，用requests和lxml。

- [x] 集成到Flask Web中(1): 增加5个视图: 爬虫、数据库、清洗、分析(各股票次数、各板块次数、预测次数)、可视化


- [x] 集成到Flask Web中(1): 做成一个后台系统，用flask-admin框架

- [x] 爬虫用scrapy框架，争取爬到更多数据。

> 用scrapy爬虫爬取和讯网的股票新闻 http://stock.hexun.com/stocknews/, 注：已遵守该网站的robots.txt说明（All robots will spider the domain)
> 已爬106507条新闻，有body、date、title、source_url四个字段，代码祥见文件夹scrapyLearning
> 初步掌握scrapy框架，不过仍未精通，已知还欠缺代理ip、图像识别验证码、解密等高级知识


- [x] 建立pipeline将数据存入到MongoDB，Pipeline详情见另一项目Data_Clean_Pipeline_System

- [x] 数据库选用NoSQL，MongoDB，如果有必要，存数字数据到MySQL中当做学习   

> 已经存入MongoDB，MongoDB的下载看官网https://www.mongodb.com/
