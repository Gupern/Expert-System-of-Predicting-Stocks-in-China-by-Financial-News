# coding:utf-8
# 本文件为对数据仓库中的Text进行分词，得出所有词的集合与频数
import sys
reload(sys)
sys.setdefaultencoding='utf-8'

import csv
# 写入文件的方程
def writing(fileName,i):
    print 'nothing'

# 读取数据仓库列表
db = open('db.csv','r')
reader = csv.reader(db)
db_list = list()
for i in reader:
    db_list.append(i)

# 建立时间集合
time_set = set()
for i in db_list:
    time_set.add(i[1])

# 按时间输出文件
for i in time_set:
    output = open('sourcesByDay/' + str(i) + '.csv','a')
    for j in db_list:
        # 输出相应文件
        if i==j[1]:
            #print i,j[1],j[0].decode('utf-8','ignore').encode('gbk')
            output.write('"')
            output.write(j[0])
            output.write('"')
            output.write(',')
            output.write('"')
            output.write(j[1])
            output.write('"')
            output.write(',')
            output.write('"')
            output.write(j[2])
            output.write('"')
            output.write('\n')
    output.close()

    
# 关闭文件
db.close()
