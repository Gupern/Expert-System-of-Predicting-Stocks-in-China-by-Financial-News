from bs4 import BeautifulSoup
import csv
import time
import datetime
import requests
import json
import configparser
import os
import pymongo

# 获取项目所在目录，配置文件在/src/resource/config.ini下
root_dir = os.path.abspath('.')
cf = configparser.ConfigParser()
cf.read(root_dir + "/src/resource/config.ini")
# mongodb connecting string
conn_str = cf.get('mongodb', 'conn_str')

# init mongodb client
mongo_client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
try:
    mongodb = mongo_client.esps
    # collection = mongodb.test
    collection = mongodb.info_detail
    print(mongodb)
except Exception:
    print("Unable to connect to the server.")

"""
    create_time: 2022-1-23
    author: Gupern
    description: 爬取同花顺财经 http://news.10jqka.com.cn/today_list/
                    入口页--同花顺财经中转页--源网页
                 存储数据格式
                    资讯内容表	source_link为唯一主键	减少重复内容，且不需要更新
                    _id	mongodb唯一id	
                    source_link	资讯源链接	
                    crawler_entry_link	爬虫入口链接	
                    content_raw	资讯内容-未清洗版	
                    content_clean	资讯内容-清洗版	
                    crawled_time	爬取时间	年月日时分秒
                    created_date	创建时间-入库时间 年月日
                    tag_list	标签列表	任意标签，方便搜索
                    title	标题	
                    updated_time	更新时间	清洗数据时标注更新时间
"""
headers = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b20',
    'Accept-Encoding':
    'gzip, deflate',
    'Accept-Language':
    'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control':
    'max-age=0',
    'Connection':
    'keep-alive',
    'Cookie':
    'spversion=20130314; historystock=300059%7C*%7C300033; userid=502126316; u_name=yufeijason; escapename=yufeijason; user=MDp5dWZlaWphc29uOjpOb25lOjUwMDo1MTIxMjYzMTU6NywxMTExMTExMTExMSw0MDs0NCwxMSw0MDs2LDEsNDA7NSwxLDQwOzEsMSw0MDsyLDEsNDA7MywxLDQwOzUsMSw0MDs4LDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxLDQwOjE6Ojo1MDIxMjYzMTU6MTU3MzQ3MjYyNzo6OjE1NzM0NzI1MjA6NjA0ODAwOjA6MTc0NjVlMTY1NDVlNTMwY2JjYTU2YzgyY2U4NzkwMTAwOmRlZmF1bHRfMzow; ticket=29857a3a991e61c22242191bc7200932; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1572181059,1572196044,1572266592,1573472631; v=AiaG-hXJR3ghIRPcFWzSShOYd5erB2rHPEueJRDPEskkk8hBeJe60Qzb7-fj',
    'Host':
    'news.10jqka.com.cn',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
}

# 获取入口页所有的title和中间跳转页链接
def get_links():
    with open('./codeinfo.csv', 'w', encoding='UTF-8', newline='') as f:
        url_demo = 'http://news.10jqka.com.cn/today_list/index_{}.shtml'
        temp_list = []
        for i in range(1,2931):
            # 获取列表页所有的链接
            url = url_demo.format(i)
            print(i, ':', url)
            html = requests.get(url, headers=headers, timeout=15).content
            soup = BeautifulSoup(html, features='lxml')
            for tr in soup.find_all(name="span", attrs={"class":"arc-title"}):
                item = tr.find_all("a")[0]
                title = item.attrs["title"]
                href = item.attrs["href"]
                temp_list.append([title, href])
        f.write(json.dumps(temp_list))

def crawl_detail_from_links():
    tmp = open('./fail.txt', 'w', encoding='UTF-8')
    with open('./codeinfo.csv', 'r', encoding='UTF-8', newline='') as f:
        temp_list = eval(f.read())
        print(len(temp_list))
        # 对列表页链接进行详情访问
        index = 0
        for i in temp_list:
            index += 1
            title = i[0]
            middle_link = i[1]
            middle = requests.get(middle_link, headers=headers, timeout=15) 
            if middle.status_code!=200:
                tmp.write(json.dumps(i))
                tmp.write('\n')
                print(index, ':fails', middle_link)
                continue
            middle_html = middle.content
            middle_soup = BeautifulSoup(middle_html, features='lxml')

            # 初始化源链接 如果没有中转页，则使用middle_link
            source_html = middle_html
            source_soup = middle_soup
            source_link = middle_link

            # 如果是中转页的情况
            for meta_item in middle_soup.find_all("meta"):
                if meta_item.attrs.get('http-equiv') is not None and meta_item.attrs['http-equiv'] == "Refresh":
                    source_link = meta_item.attrs['content'].split(';')[1].split('=')[1]
                    print("change source_link...")
                    source_html = requests.get(source_link).content
                    source_soup = BeautifulSoup(source_html,features='lxml')

            # 拼装数据，写入mongodb
            content_raw = source_soup.prettify()
            content_clean = source_soup.text
            nowatime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            nowadate = time.strftime("%Y-%m-%d", time.localtime())
            mongo_doc = {
                "source_link": source_link,
                "crawler_entry_link": 'http://news.10jqka.com.cn/today_list/',
                "content_raw": content_raw,
                "content_clean": content_clean,
                "crawler_time": nowatime,
                "created_date": nowadate,
                "updated_time": nowatime,
                "title": title,
                "tag_list": ["ths_today_list"]
            }
            inserted_id = collection.insert_one(mongo_doc).inserted_id
            print(index, ':', inserted_id, source_link)
            time.sleep(3)
    tmp.close()


if __name__=="__main__":
    # get_links()
    crawl_detail_from_links()