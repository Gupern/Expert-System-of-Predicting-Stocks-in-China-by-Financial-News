# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from scrapyLearning.items import ScrapylearningItem
client = MongoClient()
db = client['test']
col = db['hexun']

class ScrapylearningPipeline(object):
    def __init__(self):
        # 连接数据库
        self.db = db
        self.col = col

    def process_item(self, item, spider):
        data = dict(item)
        # isinstance判断a是否是b的一个实例
        if isinstance(item, ScrapylearningItem):
            one = data
            # one['imgage_ali_urls'] = item['imgage_ali_urls']
            # one['image_paths'] = item['image_paths']
            self.col.insert_one(one)
            print 'inserting .........  done'
            # 处理好了最后就返回None
            
            return None
        # 没有处理好久继续返回
        return item