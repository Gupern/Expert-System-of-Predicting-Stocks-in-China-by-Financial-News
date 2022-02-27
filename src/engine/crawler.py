# encoding: utf-8
"""
    author: Gupern
    description: this is the crawler framework which can used by script
"""

from fake_useragent import UserAgent
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import os, configparser
from random import choice


class Crawler():

    def __init__(self, crawler_component=None, cf=None):
        if not cf:
            root_dir = os.path.abspath('.')
            cf = configparser.ConfigParser()
            cf.read(root_dir + "/src/resource/config.ini")

        selenium_executable_path = cf.get("selenium", "executable_path")
        selenium_binary_location = cf.get("selenium", "binary_location")

        self.ip_pool = []
        self.requests = requests
        self.browser = None
        self.cap = None
        self.headers = {"User-Agent": ""}

        if crawler_component:
            components = crawler_component.split(",")

            if "agent" in components:
                print("[INFO] setting agent...")
                ua = UserAgent().random
                print("[INFO] ua: %s" % str(ua))
                self.headers["User-Agent"] = str(ua)
            if "ip_pool" in components:
                print("[INFO] setting ip_pool...")
                fin = open("./src/resource/ip_pool.txt", "r", encoding="utf-8")
                # 从txt中读取ip_pool list
                for line in fin.readlines():
                    print(line)
                    if line.strip() == "":
                        continue
                    self.ip_pool.append(line.strip())

            if "selenium" in components:
                print("[INFO] setting selenium...")
                selenium_service = Service(selenium_executable_path)
                chrome_options = webdriver.ChromeOptions()
                # using headless non-UI mode
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--disable-gpu")
                cap = webdriver.DesiredCapabilities.CHROME.copy()
                for k, v in self.headers.items():
                    cap['chrome.page.customHeaders.{}'.format(k)] = v
                self.browser = webdriver.Chrome(service=selenium_service,
                                                desired_capabilities=cap,
                                                chrome_options=chrome_options)

    def __new__(cls, crawler_component):
        print("new %s" % cls)
        return object.__new__(cls)

    def get(self, url, referer=""):
        self.headers["Referer"] = referer
        return self.requests.get(url, headers=self.headers)

    def get(self, url, referer="", use_proxy=False):
        self.headers["Referer"] = referer
        proxies = None
        if use_proxy:
            proxy = choice(self.ip_pool)
            proxies = {"http": "http://" + proxy, "https": "http://" + proxy}
            print("proxies: ", proxies)
        return self.requests.get(url, headers=self.headers, proxies=proxies)

    def post(self, url, referer=""):
        self.headers["Referer"] = referer
        return self.requests.get(url, headers=self.headers)

    def post(self, url, referer="", use_proxy=False):
        self.headers["Referer"] = referer
        proxies = None
        if use_proxy:
            proxy = choice(self.ip_pool)
            proxies = {"http": "http://" + proxy, "https": "http://" + proxy}
            print("proxies: ", proxies)
        return self.requests.get(url, headers=self.headers, proxies=proxies)

    def selenium_open(self, url):
        return self.browser.get(url)


if __name__ == "__main__":
    crawler = Crawler("selenium,agent")
    res = crawler.selenium_open("https://www.89ip.cn/")
    print(crawler.browser.page_source)