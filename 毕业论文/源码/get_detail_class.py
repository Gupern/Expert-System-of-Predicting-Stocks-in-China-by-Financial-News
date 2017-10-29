# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import re
import urllib 
import urllib2
from bs4 import BeautifulSoup as bs 

## 本文件为手动爬下行业板块

# 打开文件
url = 'http://quote.yztz.com/quote/sector.jsp'
output = open(".\class\QiTaJinRong.txt","a")
# 参数
values={
        "sid":"11580",
        "p":"1"
        }
# 进行参数封装
data = urllib.urlencode(values)
# 组装url
req = urllib2.Request(url,data)
response = urllib2.urlopen(req)
content = response.read()
soup = bs(content,'lxml')

classes = set()
for i in soup.find_all("a",href=re.compile("../\d+")):
    if i.has_key("class"):
        if "ty" in i["class"]:  # “ty f14”被分为“ty”和“f14”的字典,空格
            print i.string.encode("gbk")
            classes.add(i.string.encode("gbk"))
for i in classes:
    output.write(i)
    output.write("\n")
output.close()
