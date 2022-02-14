# encoding: utf-8
"""
    author: Gupern
    description: this is the crawler framework which can used by script
"""

class Crawler():
    def __init__(self, crawler_component=None):
        if not crawler_component:
            self.ip_pool = None
            self.selenium = None

    def __new__(cls, crawler_component):
        print("new %s" % cls)
        return object.__new__(cls)


if __name__=="__main__":
    a = Crawler(None)