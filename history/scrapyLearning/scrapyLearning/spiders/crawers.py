#-*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapyLearning.items import ScrapylearningItem
from .. import util

class ToScrapySpider(scrapy.Spider):
    name = 'scrapyLearning'
    urlSet = util.getUrlSet()
    def start_requests(self):
        start_urls = [
            'http://stock.hexun.com/stocknews/',
        ]
        for i in range(0,2007):
            next_link = 'http://stock.hexun.com/stocknews/index-' + str(i) + '.html'
            start_urls.append(next_link)
        for url in start_urls:
            yield scrapy.Request(url = url, callback=self.parse)

    def parse(self,response):
        # 获取相对路径
        url_link = response.xpath('//div[@class="temp01"]/ul/ul/li/a/@href').extract()
        # zip()是什么意思?
        for new_link in url_link:
#             print 'new_link: ' + new_link 
            yield Request(new_link, meta={'new_link':new_link},callback=self.parse_detial)



    def parse_detial(self,response):
        item = ScrapylearningItem()
        new_link = response.meta['new_link']
#         if util.checkUrl(new_link):
#        if new_link in self.urlSet or util.checkUrl(new_link):
        if new_link in self.urlSet:
            yield None
        else:
            self.urlSet.add(new_link)
            # response.text 代表页面源代码
            # if 'art_contextBox' in response.text:
            title = ''.join(response.xpath('//div[@class="layout mg articleName"]/h1/text()').extract())
            if title:
                item['title'] = title
            else:
                item['title'] = ''.join(response.xpath('//div[@class="art_title"]/h1/text()').extract())

            body = ''.join(response.xpath('//div[@class="art_contextBox"]/p/descendant::text()').extract()).replace("\r","").replace("\n","").replace(" ","")
            if body:
                item['body'] = body
            else:
                item['body'] = ''.join(response.xpath('//div[@class="art_context"]/p/descendant::text()').extract()).replace("\r","").replace("\n","").replace(" ","")

            date = ''.join(response.xpath('//span[@class="pr20"]/text()').extract())
            if date:
                item['date'] = date
            else:
                item['date'] = ''.join(response.xpath('//span[@id="artibodyDesc"]/span[1]/text()').extract())


            item['source_url'] = new_link

            #print 'title',item['title'],'body',item['body']
            # 爬取其中所有的文字，包括被<strong>包围的文字 descendant::text()
            yield item
