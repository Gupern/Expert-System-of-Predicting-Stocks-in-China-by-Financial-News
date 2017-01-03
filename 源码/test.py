import os,sys
reload(sys)
sys.setdefaultencoding('utf-8')
dir_path='.\class\\'
count = 0
output = open("allStocks.txt","w")
for files in os.listdir(dir_path):
    fileName = open(".\class\\"+files,"r")
    for i in fileName.readlines():
        count += 1
        print i[:-1] + ' ' + str(count)
        output.write(i)
output.close
