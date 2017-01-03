# coding:utf8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time
from sina_roll import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):

    def __init__(self):                                     # 初始化
        self.urls = url_manager.UrlManager()                # 将url_manager.UrlManager()更名为self.urls方便编程
        self.downloader = html_downloader.HtmlDownloader()  # 以下同上
        self.parser = html_parser.HtmlParser()              
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.set_old_urls()
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print ('craw %d : %s'%(count, new_url))
                html_cont = self.downloader.download(new_url)
                print ('downloader success')
                new_urls, new_data = self.parser.parse(new_url, html_cont, count)  # new_url will become a set of urls 
                print ('parse success')
                self.urls.add_new_urls(new_urls)                            # add all urls to url_list of UrlManager
                print ('add success')
                self.outputer.collect_data(new_data)
                print ('output success')
                self.urls.add_old_url(new_url)
                print ('add_old success')
                #if count == 3:
                #    break
                count = count + 1
            except:
                print ('craw failed')
            if not self.urls.has_new_url():
                print ('all well done')
        self.urls.save_url()
        self.outputer.output_html()

if __name__=="__main__":
    # 个股点评
    root_url = "http://finance.sina.com.cn/column/ggdp.shtml"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
