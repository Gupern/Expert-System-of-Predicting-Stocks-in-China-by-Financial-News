#encoding: utf-8
"""
    author: Gupern
    description: update ip pool list and store it into mongodb esps.ip_pool
    using: `python src/main.py --collection=ip_pool --crawler_component=selenium,agent`
"""
from bs4 import BeautifulSoup as bs
import time

def func(mongo_collection, crawler):
    print("[INFO] starting update_ip_pool_list.py...")
    # 爬取IP池
    # 89ip.cn index % 5
    url_template = "https://www.89ip.cn/index_{}.html"
    # kuaidaili.com index % 7
    # url_template = "https://www.kuaidaili.com/free/inha/{}/"
    fout = open("./src/resource/ip_pool.txt", "w+", encoding="utf-8")
    for i in range(1, 2):
        print(i)
        crawl_ip(url_template.format(i), fout, crawler)
        time.sleep(5)
    
    fout.close()

def crawl_ip(url, fout, crawler):
    res = crawler.get(url)
    soup = bs(res.content, features="lxml")
    td_list = soup.find_all(name="td")
    index = 0
    line = ""
    for i in td_list:
        index += 1
        text = i.getText().strip()
        if index % 5 == 1:
            line += text
            line += ":"
        elif index % 5 == 2:
            line += text
            line += "\n"
    fout.write(line)

if __name__=="__main__":
    print("hello world")