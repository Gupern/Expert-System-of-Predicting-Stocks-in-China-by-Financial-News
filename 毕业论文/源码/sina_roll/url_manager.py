# coding:utf-8
class UrlManager(object):

    def __init__(self):
        self.new_urls = set()			# initial a set
        self.old_urls = set()

    def set_old_urls(self):
        urlFile = open("url_old.txt","r")
        # print self.old_urls
        try:
            while 1:
                lines = urlFile.readlines(100)
                if not lines:
                    break
                for line in lines:
                    line = line[:-1] # 删除字符串的最后一个字符，即换行符
                    self.old_urls.add(line)
            self.old_urls = self.old_urls - set(['http://finance.sina.com.cn/column/ggdp.shtml'])
            # print self.old_urls
        finally:
            urlFile.close()

    def add_new_url(self, url):
        if url is None:
            return
        #print 'url = ' + url
        #print 'old_urls = ' 
        #print self.old_urls
        if url in self.old_urls:
            print 'This url has been crawled'
        if url not in self.new_urls and url not in self.old_urls:		# add the url which never be used
            #print url + '  here'
            self.new_urls.add(url)

    def save_url(self):
        file = open("url_old.txt","a")
        for i in self.old_urls:
            file.write(i)
            file.write("\n")
        print 'saved successfully'

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()			# pop the element by queue
        return new_url 

    def add_old_url(self, old_url):
        self.old_urls.add(old_url)				# prevent to crawl it again
        # self.old_urls.add(new_url)
	
