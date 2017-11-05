#encoding:utf-8 
'''
    Author:             Gupern
    CreateTime:         2017-11-04
    Introduction:       Crawl stock news from http://stock.hexun.com
                        and store it into MongoDB
    
'''

import requests 
import gzip 
import json 
import os 
import sys 
from lxml import etree
from pymongo import MongoClient

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, CURRENT_DIR)

# 设置编码
coding = ['utf8', 'gb2312', 'gb18030', 'gbk']
timeout = 30 
retry_timeout = 5
retry_times = 5


# 从url中获取数据 

def fetch(url, retry=0):
    sess = requests.session()

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/48.0.2564.116 Chrome/48.0.2564.116 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Cache-Control': 'max-age=0',
        'Referer': url,
        'Cookie': 'JSESSIONID=DF3824F65843F5861386DA8F48A6F69D; UM_distinctid=15cc37d608a3a8-0cbd87321debff-3063750b-13c680-15cc37d608b45b; CNZZDATA1000522253=992972820-1497923791-%7C1497923791; Hm_lvt_bdeeaac5f88d7c5e2442e0665b4ff88e=1497928393; Hm_lpvt_bdeeaac5f88d7c5e2442e0665b4ff88e=1497928393'
    }
    
    sess.headers.update(headers)

    try:
        res = requests.get(url=url).content 
    except:
        if retry< retry_times:
            return fetch(url, retry+1)
        else:
            return None 
    # 解析编码
    for code in coding:
        try:
            content = res.decode(code)
            return content 
        except:
            pass 
        # 解压编码
        try:
            content = gzip.decompress(res).decode(code)
            return content 
        except:
            pass
    return None

# 解析详情页数据
def parse_detail(db_name, detail_urls_col_name, target_col_name, floor, celling):
    detail_urls_col = get_col(db_name, detail_urls_col_name)
    # 接收从floor到celling的参数，便于多进程爬取
    cursor = detail_urls_col.find().skip(floor).limit(celling)

    for i in cursor:
        try:
            detail_url = i['detail_url']
            print('parsing: ' + detail_url)
            source_html = fetch(detail_url)
            selector = etree.HTML(source_html)
            # ''.join将list转为str
            title = ''.join(selector.xpath('//div[@class="layout mg articleName"]/h1/text()'))
            if not title:
                title = ''.join(selector.xpath('//div[@class="art_title"]/h1/text()'))
            body = ''.join(selector.xpath('//div[@class="art_contextBox"]/p/descendant::text()'))
            if not body:
                body = ''.join(selector.xpath('//div[@class="art_context"]/p/descendant::text()'))
            date = ''.join(selector.xpath('//span[@class="pr20"]/text()'))
            if not date:
                date = ''.join(selector.xpath('//span[@id="artibodyDesc"]/span[1]/text()'))
            
            res = {'title':title.strip(), 
                   'body':body.strip(),
                   'date':date.strip(),
                   'source_url':detail_url.strip()
                   }
            store(db_name, target_col_name, res)
        except:
            pass



# 解析列表页数据
def parse_list(db_name, detail_urls_col_name):
    print('parsing')
    pages = list(range(1,2057))
    urls = ['http://stock.hexun.com/stocknews/index-{}.html'.format(page) \
            for page in pages]
    urls.append('http://stock.hexun.com/stocknews/index.html')

    for url in urls:
        source_html = fetch(url)
        selector = etree.HTML(source_html)
        detail_url = selector.xpath('//div[@class="temp01"]/ul/ul/li/a/@href')
        for tmp in detail_url:
            print(tmp)
            res = {'detail_url': tmp}
            print(res)
            print(type(res))
            store(db_name, detail_urls_col_name, res) # 可以用bulk 和 yield优化
    #        break # 正式跑的时候注释掉

# 连接mongodb的col
def get_col(db_name, col_name, ip='0.0.0.0',port=27017):
    client = MongoClient() # 以后慢慢优化
    db = client[db_name]
    col = db[col_name]
    return col

# 存储数据
def store(db_name, col_name, item):
    print('storing')
    col = get_col(db_name, col_name)
    # 去重,直接find item即可，_id无关
    if not col.find_one(item):
        col.insert(item)

# 主函数
def main():
    db_name = 'stock_news' 
    detail_urls_col_name = 'detail_urls'
    target_col_name = 'stock.hexun.com'

##############################################
# 这里可以优化成一个输入界面，让用户选择
# 1. 爬取详情页链接
# 2. 爬取详情页内容 
# 3. 全部爬取 
##############################################
    print('请选择您想要进行的操作:\n')
    print('1. 爬取详情页链接\n')
    print('2. 爬取详情页内容\n')
    print('3. 全部爬取\n')
    print('0. 退出\n')
    choice = int(input())

    if choice==0:
        pass
    elif choice==1:
        # 爬取详情页链接
        parse_list(db_name, detail_urls_col_name)
    elif choice==2:
        # 爬取详情页内容 
        floor = int(input('请输入从第几个开始爬'))
        celling = int(input('请输入到第几个结束'))
        parse_detail(db_name, detail_urls_col_name, target_col_name, floor, celling)
    elif choice==3:
        # 爬取详情页链接
        parse_list(db_name, detail_urls_col_name)

        # 爬取详情页内容 
        floor = int(input('请输入从第几个开始爬'))
        celling = int(input('请输入到第几个结束'))
        parse_detail(db_name, detail_urls_col_name, target_col_name, floor, celling)






if __name__ == '__main__':
    main()
