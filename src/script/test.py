import traceback
from bs4 import BeautifulSoup
import csv
import time
import datetime
import requests
import json
import configparser
import os
import pymongo
import sys 
root_dir = os.path.abspath('.')
crawler_dir = root_dir + "/src/engine"
print(crawler_dir)
sys.path.append(crawler_dir)
import crawler

# 获取项目所在目录，配置文件在/src/resource/config.ini下
root_dir = os.path.abspath('.')
cf = configparser.ConfigParser()
cf.read(root_dir + "/src/resource/config.ini")
# mongodb connecting string
conn_str = cf.get('mongodb', 'conn_str')

if __name__=="__main__":
    # get_links()
    # crawl_detail_from_links()
    print("hello world")