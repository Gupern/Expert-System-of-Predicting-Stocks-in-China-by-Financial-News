#encoding: utf-8
#!/usr/bin/env python3
import gzip
import json
import os
import sys
import time
import requests

# 引入上层的utils模块，爬虫和引擎共用
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
sys.path.append("../../utils")

from es import get_es
from nlp_tools import strip_title


coding = ['utf8', 'gb2312', 'gb18030', 'gbk']
timeout = 30
retry_timeout = 5
retry_times = 5


def fetch(url, retry=0):
    sess = requests.session()

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu\
 Chromium/48.0.2564.116 Chrome/48.0.2564.116 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Cache-Control': 'max-age=0',
        'Referer': url,
        'Cookie': 'JSESSIONID=DF3824F65843F5861386DA8F48A6F69D;\
 UM_distinctid=15cc37d608a3a8-0cbd87321debff-3063750b-13c680-15cc37d608b45b;\
 CNZZDATA1000522253=992972820-1497923791-%7C1497923791;\
 Hm_lvt_bdeeaac5f88d7c5e2442e0665b4ff88e=1497928393;\
 Hm_lpvt_bdeeaac5f88d7c5e2442e0665b4ff88e=1497928393'
    }

    sess.headers.update(headers)

    try:
        res = requests.get(url=url).content
    except:
        if retry < retry_times:
            return fetch(url, retry + 1)
        else:
            return None
    for code in coding:
        try:
            content = res.decode(code)
            return content
        except:
            pass
        try:
            content = gzip.decompress(res).decode(code)
            return content
        except:
            pass
    return None


def parse():
    keywords = ['阿里', '蚂蚁金服', '腾讯', '百度', '京东', '头条',
                '美团', '滴滴', '网易', '华为', '小米', '苹果', '谷歌',
                '微软', 'FACEBOOK', '亚马逊', '特斯拉']
    urls = ['http://36kr.com/api/search/entity-search?page=1&per_page=40&keyword={}&entity_type=newsflash'.format(key)
            for key in keywords]
    res = []
    for url in urls:
        obj = json.loads(fetch(url))
        if obj.get('data') and obj['data'].get('items'):
            for item in obj['data'].get('items'):
                tmp = {
                    'title': strip_title(item['title']),
                    'abstract': item['description_text'],
                    'datetime': item['updated_at'][:10]
                }
                crawl_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                tmp['crawl_time'] = crawl_time
                tmp['category'] = "technology_news"
                res.append(tmp)
    return res


def main():
    res = parse()
    es, index, doc_type = get_es('es_news_kr36')
    es1, index, doc_type = get_es('es_news_pub')
    for item in res:
        try:
            es.index(
                index=index,
                doc_type=doc_type,
                body=item,
                id=item['title']
            )
            # 存入到pub中
            es1.index(
                index=index,
                doc_type=doc_type,
                body=item,
                id=item['title']
            )
        except:
            print(item['title'])


if __name__ == '__main__':
    main()
