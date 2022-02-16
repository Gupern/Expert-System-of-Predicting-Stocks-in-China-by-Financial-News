#encoding: utf-8
"""
    author: Gupern
    description: update ip pool list and store it into mongodb esps.ip_pool
    using: `python src/main.py --collection=ip_pool --crawler_component=selenium,agent`
"""
from bs4 import BeautifulSoup as bs

def func(mongo_collection, crawler):
    print("[INFO] starting update_ip_pool_list.py...")
    # 爬取IP池
    url = "https://www.89ip.cn/"
    res = crawler.get(url)
    soup = bs(res.content, features="lxml")
    print(soup)
    td_list = soup.find_all(name="td")
    index = 0
    line = ""
    fout = open("./src/resource/ip_pool.txt", "w+", encoding="utf-8")
    for i in td_list:
        text = i.getText().strip()
        line = line + text
        index += 1
        if index % 5 == 0:
            line += "\n"
        else:
            line += ","
        print(line)
        fout.write(line)
    fout.close()

if __name__=="__main__":
    print("hello world")