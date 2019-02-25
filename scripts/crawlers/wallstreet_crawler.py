#!/usr/bin/env python3

import gzip
import json
import os
import re
import sys
import time

import requests
from es import get_es
from pyquery import PyQuery as pq

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, CURRENT_DIR)

coding = ['utf8', 'gb2312', 'gb18030', 'gbk']
timeout = 30
retry_timeout = 5
retry_times = 5


def fetch(url, retry=0):
    sess = requests.session()

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/48.0.2564.116 Chrome/48.0.2564.116 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Cache-Control': 'max-age=0',
        'Referer': url
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
    url = 'https://api-prod.wallstreetcn.com/apiv1/search/article?order_type=time&cursor=&limit=20&search_id=&query=%E5%8D%8E%E5%B0%94%E8%A1%97%E8%A7%81%E9%97%BB%E6%97%A9%E9%A4%90'
    text = fetch(url)
    obj = json.loads(text)
    res = {}
    if obj.get('data'):
        for item in obj['data']['items']:
            if 'Radio' in item['title']:
                print (item['uri'])
                res = parse_detail(item['uri'])
                break
    return [res]


def parse_detail(url):
    text = fetch(url)
    content = pq(text).find('.node-article-content').html()
    content = content.replace('\n','')
    keywords = re.findall(r'<h2.*?><strong>(.*?)</strong></h2>', content)
    split_contents = re.split(r'<h2.*?><strong>.*?</strong></h2>', content)
    if not keywords:
        keywords = re.findall(r'</p><h2.*?>(.*?)</h2><p>', content)
        split_contents = re.split(r'</p><h2.*?>.*?</h2><p>', content)
    html_compiler = re.compile(r'<[^>]+>', re.S)
    res = []
    for i in range(0, len(split_contents)):
        if '要闻详情' in keywords[i]:
            titles = re.findall('<a.*?>(.*?)</a>', split_contents[i + 1])
            contents = re.split('<a.*?>.*?</a>', split_contents[i + 1])
            for j in range(0, len(titles)):
                tmp = {}
                title_1 = titles[j].strip()
                # 取出strong标签
                a = re.compile('<strong>')
                title_2 = a.sub('',title_1)
                b = re.compile('</strong>')
                title = b.sub('',title_2)
                tmp['title'] = title
                tmp['abstract'] = html_compiler.sub('', contents[j + 1]).strip()
                if len(tmp['abstract']) < 10:
                    continue
                res.append(tmp)
            break
    news_date = pq(text).find('.article__heading__meta .time').text()[:10]
    crawl_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    res = {'datetime':news_date, 'content':res, 'url':url, 'crawl_time':crawl_time, 'news_date':news_date}
    return res


def main():
    es, index, doc_type = get_es('es_news_wallstreetcn')
    res = parse()
    for item in res:
        es.index(
            index=index,
            doc_type=doc_type,
            body=item,
            id=item['url']
        )


if __name__ == '__main__':
    main()
