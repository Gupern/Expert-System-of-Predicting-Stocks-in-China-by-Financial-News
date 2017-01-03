# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import re
import urllib2
from bs4 import BeautifulSoup as bs 

# 打开文件
output = open("./class/allClasses.txt","w")
url = 'http://quote.yztz.com/quote/sector_industry.jsp'

response = urllib2.urlopen(url)
content = response.read()
soup = bs(content,'lxml')

for i in soup.find_all('a',href=re.compile("sector_")):
    if i.has_key('class'):  # 找出不含有class的a
        print 'not this'
    else:
        output.write(str(i.string))
        output.write("\n")
output.close()
