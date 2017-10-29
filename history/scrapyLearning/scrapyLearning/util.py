#encoding:utf-8
from pymongo import MongoClient
client = MongoClient()
db = client['test']
col = db['hexun']
def testUtil():
    print 'yes, I\'m util'
# 如果找到返回document，找不到返回None
def checkUrl(source_url):
    return col.find_one({'source_url':source_url})
def getUrlSet():
    a = set()
    for i in col.find():
        a.add(i['source_url'])
    return a