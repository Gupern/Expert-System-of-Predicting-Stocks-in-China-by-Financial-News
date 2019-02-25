## Introduction

- 一个金融领域的专家系统
    - 财经新闻采集
    - 股票新闻采集
    - 自然语言处理
    - 数据统计分析
    - 日常报表生成
    
## Purposes
- 兴趣爱好，愉悦自己
- 盲人摸象，了解经济
- 如有可能，发家致富


## Stacks

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

    0. `mv Expert-System-of-Predicting-Stocks-in-China-by-Financial-News esps`
    1. `cd esps` 
    2. `sudo docker build -t esps .`
    3. `sudo docker run --restart=always -d -v /etc/localtime:/etc/localtime:ro -v /root/Desktop/esps/:/mnt --net host --name esps_engine esps /mnt/engine/run.sh`

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

`sudo docker run -ti -v /etc/localtime:/etc/localtime:ro -v /root/Desktop/esps/:/mnt --net host --name esps_engine --rm esps /mnt/engine/run.sh`

> 服务器运行，加了`-d`的参数作为服务器启动，加了`--restart=always`防止服务器关闭

`sudo docker run --restart=always -d -v /etc/localtime:/etc/localtime:ro -v /root/Desktop/esps/:/mnt --net host --name esps_engine esps /mnt/engine/run.sh`


### Coding

---
- [ ] 新闻发布管理界面
- [ ] 新闻前端展示
- [ ] 新增华尔街见闻爬虫
- [ ] 新增wind爬虫
- [ ] 新增新智元爬虫
- [ ] 运行和讯网爬虫 
- [ ] 定时爬取功能

### Todo list

---

- [ ] 获得所有最新的股票名称和相应股票代码

- [ ] 情感分析:使用结巴进行分词获取积极消极词汇

- [ ] 开发可视化界面，用d3.js or echarts.js 将数据展示出来

- [ ] 开发爬虫界面，一键运行爬虫并返回最新更新时间

- [ ] 使用消息队列MQ或者Redis

- [ ] 进修机器学习、博弈论、和时间序列知识，等建设好数据仓库，则进行预测

- [ ] 查询每条新闻中出现的股票名称或代码，打上标签nameTaps、codeTaps

- [ ] 根据热度值画图

- [ ] 搭建大数据集群，存储数据到elasticsearch/spark中

- [ ] 自动爬取最新新闻

- [ ] 爬取股票数据

- [ ] 做实时对比图

