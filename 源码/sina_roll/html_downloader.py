# coding:utf8 

import urllib2
import StringIO
import gzip

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        req_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                  'Accept':'text/html;q=0.9,*/*;q=0.8',
                  'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                  'Accept-Encoding':'gzip',
                  'Connection':'close',
                  'Referer':None
        }
        req_timeout = 5
        req = urllib2.Request(url,None,req_header)
        response = urllib2.urlopen(req,None,req_timeout)
        if response.getcode() != 200:
            return None
        data = response.read()
        data = StringIO.StringIO(data)
        gzipper = gzip.GzipFile(fileobj=data)
        html = gzipper.read()
        #print("success")
        return html
