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
output = open("./class/allClasses.txt","w")
url = 'http://quote.yztz.com/quote/sector_industry.jsp'
response = urllib2.urlopen(url)
content = response.read()
soup = bs(content,'html.parser')
#print soup.find("a",_class="ty f14").encode("gbk")

classes = set()
for i in soup.find_all("a",href=re.compile("sector_")):
    print i.string.encode("gbk")
    classes.add(i.string.encode("gbk"))


print classes
for i in classes:
    output.write(i)
    output.write("\n")
output.close()
#
# print soup.prettify()  # 格式化输出
