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

- based on Flask
- based on python3.5 and it's prefer to use virtualenv
    1. install pip3
        1. `wget https://bootstrap.pypa.io/get-pip.py`
        2. `python3 get-pip.py`
    2. `pip3 install virtualenv`
    3. `virtualenv py3.5env -p python3`
    4. `source py3.5env/bin/activate`
    5. `pip3 install -r requirements.txt`
- 暂时不用docker，省去构建docker的麻烦
- 前后端分离

### 本机运行：
`python3 app.py`

### Todo list
- [ ] 新闻前端展示
- [ ] 新闻发布管理界面
- [ ] 新增华尔街见闻爬虫
- [ ] 新增wind爬虫
- [ ] 新增新智元爬虫
- [ ] 运行和讯网爬虫 
- [ ] 定时爬取功能
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

