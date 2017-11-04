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
def parse_detail(detail_urls):
    res = []
    for detail_url in detail_urls:
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
        
        tmp = {'title':title.strip(), 
               'body':body.strip(),
               'date':date.strip(),
               'source_url':detail_url.strip()
               }
        res.append(tmp)

#        break

    return(res)

# 解析列表页数据
def parse_list():
    pages = list(range(1,2057))
    urls = ['http://stock.hexun.com/stocknews/index-{}.html'.format(page) \
            for page in pages]
    urls.append('http://stock.hexun.com/stocknews/index.html')

    detail_urls = []
    for url in urls:
        source_html = fetch(url)
        selector = etree.HTML(source_html)
        detail_url = selector.xpath('//div[@class="temp01"]/ul/ul/li/a/@href')
        for tmp in detail_url:
            detail_urls.append(tmp)
#        break # 正式跑的时候注释掉

    return detail_urls

# 存储数据
def store(res):
    client = MongoClient() # default is 127.0.0.1:27017
    db = client['stock_news']
    col = db['hexun']
    for item in res:
        if not col.find_one({'source_url':item['source_url']}):
            col.insert(item)

# 主函数
def main():
    detail_urls = parse_list()
    res = parse_detail(detail_urls)
    for i in res:
        print(i)
    store(res)

if __name__ == '__main__':
    main()
