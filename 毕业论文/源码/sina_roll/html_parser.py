# coding:utf8 
from bs4 import BeautifulSoup
import re
# import urlparse

class HtmlParser(object):
	def _get_new_urls(self, page_url, soup):
		new_urls = set()	# create a set of urls 
		links1 = soup.find_all('a', href=re.compile(r"http://finance.sina.com.cn/stock/\w+\/\d+\/\d+\.shtml"))
		for link in links1:
			new_url = link['href']
			new_urls.add(new_url)
		links2 = soup.find_all('a', href=re.compile(r"http://blog.sina.com.cn/s/\w+\_\w+\.html\?tj=fina"))
		for link in links2:
			new_url = link['href'][:-8]
			new_urls.add(new_url)
		return new_urls
	def _get_new_data(self, page_url, soup):
		res_data = {}
		res_data['url'] = page_url
		blogOrNot = page_url.find('blog')
		if blogOrNot != -1:
			# blog's parser
			title_node = soup.find('div', class_="BNE_title")
			res_data['title'] = title_node.get_text()
			summary_node = soup.find('div', class_="BNE_cont")
			res_data['summary'] = summary_node.get_text()
		else:
			# finace's parser
			title_node = soup.find('div', class_="page-header").find("h1")
			res_data['title'] = title_node.get_text()
			summary_node = soup.find('div', class_="article article_16")
			res_data['summary'] = summary_node.get_text()
		return res_data
	
	def parse(self, page_url, html_cont, count):
		if page_url is None or html_cont is None:
			return
		soup = BeautifulSoup(html_cont,'html.parser',from_encoding='gbk')
		new_urls = self._get_new_urls(page_url, soup)
		if count == 1:
			new_data = {'url':'URL','summary':'Data','title':'Title'}
			# print (new_data)
		else:
			new_data = self._get_new_data(page_url, soup)
		return new_urls, new_data
