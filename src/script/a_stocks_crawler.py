# encoding:utf-8
"""
    爬取A股信息并入库
"""

import tushare as ts
import configparser
import os
import pymongo
""" configparser用法
# 获取文件中所有的section(一个配置文件中可以有多个配置，如数据库相关的配置，邮箱相关的配置，每个section由[]包裹，即[section])，并以列表的形式返回
# secs = cf.sections()
# options = cf.options("Mysql-Database")  # 获取某个section名为Mysql-Database所对应的键
# print(options)
# items = cf.items("Mysql-Database")  # 获取section名为Mysql-Database所对应的全部键值对
# print(items)
# host = cf.get("Mysql-Database", "host")  # 获取[Mysql-Database]中host对应的值
"""
# 获取配置信息

# 获取项目所在目录，配置文件在/src/resource/config.ini下
root_dir = os.path.abspath('.')
cf = configparser.ConfigParser()
cf.read(root_dir + "/src/resource/config.ini")
# tushare token
tushare_token = cf.get('tushare', 'token')
# mongodb connecting string
conn_str = cf.get('mongodb', 'conn_str')

# init mongodb client
mongo_client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
try:
    mongodb = mongo_client.esps
    collection = mongodb.stock_basic
    print(mongodb)
except Exception:
    print("Unable to connect to the server.")

# get tushare stock basic info
ts.set_token(tushare_token)
pro = ts.pro_api()
data = pro.query(
    'stock_basic',
    exchange='',
    list_status='L',
    fields='ts_code,symbol,name,area,industry,' +
    'list_date,fullname,enname,cnspell,market,exchange,curr_type,is_hs')
for i in range(0, len(data)):
    print(i)
    data_frame = data.loc[i]
    mongo_doc = data_frame.to_dict()
    inserted_id = collection.insert_one(mongo_doc).inserted_id
    print(inserted_id)