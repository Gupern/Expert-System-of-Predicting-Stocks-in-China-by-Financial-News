
# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#######################################
# 本文件为爬取股票分类，并输出股票代码#
#######################################

import re
import urllib2
from bs4 import BeautifulSoup as bs 
#output = open("./class/baoxian.txt","w")
#url = 'http://quote.yztz.com/quote/sector_10612'
output = open("./class/DianLi.txt","a")
url = 'http://quote.yztz.com/quote/sector.jsp?sid=sector_10613&p=2'
response = urllib2.urlopen(url)
content = response.read()
soup = bs(content,'html.parser')
#print soup.find("a",_class="ty f14").encode("gbk")

classes = set()
for i in soup.find_all("a",href=re.compile("../\d+")):
    if i.has_key("class"):
        if "ty" in i["class"]:  # “ty f14”被分为“ty”和“f14”的字典,空格
            print 'good'
            print i.string.encode("gbk")
            classes.add(i.string.encode("gbk"))

print classes
for i in classes:
    output.write(i)
    output.write("\n")
output.close()

# print soup.prettify()  # 格式化输出
