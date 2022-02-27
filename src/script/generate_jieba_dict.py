# encoding: utf-8
"""
    Author: Gupern
    Description: generate jieba dict, such as A stocks name, code and industry
    Using: python src/main.py --collection=stock_basic --script=generate_jieba_dict
"""
import os

root_dir = os.path.abspath('.')

def func(mongo_collection, crawler):
    # 创建文件
    f_a_stock_name_dict = open(root_dir + "/src/resource/dict_a_stock_name_jieba.txt", "w", encoding="utf-8")
    f_a_stock_code_dict = open(root_dir + "/src/resource/dict_a_stock_code_jieba.txt", "w", encoding="utf-8")
    f_a_stock_industry_dict = open(root_dir + "/src/resource/dict_a_stock_industry_jieba.txt", "w", encoding="utf-8")

    # 建立集合 去重
    name_set = set()
    code_set = set()
    industry_set = set()

    # 从库中读取集合
    for i in mongo_collection.find():
        name = i['name']
        code = i['symbol']
        industry = i['industry']
        name_set.add(name)
        code_set.add(code)
        industry_set.add(industry)

    # 写入数据，如果为空，则跳过
    for name in name_set:
        if name is None:
            continue
        f_a_stock_name_dict.write(name + "\n")
    for code in code_set:
        if code is None:
            continue
        f_a_stock_code_dict.write(code + "\n")
    for industry in industry_set:
        if industry is None:
            continue
        f_a_stock_industry_dict.write(industry + "\n")
    
    # 关闭文件
    f_a_stock_code_dict.close()
    f_a_stock_industry_dict.close()
    f_a_stock_name_dict.close()

if __name__ == "__main__":
    print("hello world")