# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapylearningItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 标题
    body = scrapy.Field()   # 新闻内容主题
    source_url = scrapy.Field()   # 源链接
    date = scrapy.Field()   # 源链接
    pass
