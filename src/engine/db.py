# encoding: utf-8
import pymongo
import traceback

class MongoDBSteward(object):
    def __init__(self, cf):
        print("init %s" % self.__class__)
        if not cf:
            pass # TODO 重新读取cf
        self.cf = cf
        # mongodb connecting string
        conn_str = self.cf.get('mongodb', 'conn_str')

        # init mongodb client
        self.mongo_client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

    def __new__(cls, cf):
        print("new %s" % cls)
        return object.__new__(cls)

    def get_collection(self, db, collection):
        try:
            mongodb = self.mongo_client[db]
            collection = mongodb[collection]
        except Exception:
            print("Unable to connect to the server. %s" %Exception)
            traceback.print_exc()
        return collection

if __name__=="__main__":
    a = MongoDBSteward("aaa")