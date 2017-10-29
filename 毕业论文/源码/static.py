# coding:utf-8
# 设置系统默认编码，从ascii改为utf8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

######################################
##  统计数据仓库中的股票频数        ##
######################################

dicFile = open('stockList.txt','r') # 读取字典
sourceText = open('output.html','r') # 读取新闻
result = open('result.txt','w')  # 输出文件
# 读取文件所有内容
b = sourceText.read()
# 替换所有不合法的字符
b = b.replace(u'\ufeff',u' ')
b = b.replace(u'\xa0',u' ')
b = b.replace(u'\u200b',u' ')
b = b.encode("gbk") # 编码为gbk
# 建立字典
dic = dict()
for word in dicFile.readlines():
    word = word[:-1].encode("gbk") # 去除换行符并编码
    # print word
    dic[str(word)] = 0
for word in dic:
    count = b.count(str(word))
    dic[str(word)] = count
    if count:
        print "%s = %s"% (word,count)
        result.write(str(word))
        result.write("\t")
        result.write(str(count))
        result.write("\n")

## 关闭文件
dicFile.close()
sourceText.close()
result.close()
