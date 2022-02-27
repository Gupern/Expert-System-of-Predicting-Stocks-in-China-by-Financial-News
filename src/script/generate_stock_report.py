# encoding: utf-8
"""
    Author: Gupern
    Description: to segment Chinese word and generate reporting statistics
    Algorithm: 
        TODO 
        1. 导入结巴分词 done
        2. 读取数据库信息
            2.1 股票名称列表
            2.2 股票代号列表
            2.3 股票行业列表
            2.4 股票资讯for循环
        3. 统计每个股票出现的名称、代号、行业、积极消极词频
        4. 打印数据
    Using: python src/main.py --collection=info_detail --script=generate_stock_report
"""

import jieba
import os

root_dir = os.path.abspath('.')

def func(mongo_collection, crawler):
    print("hello world")

if __name__ == "__main__":
    print("hello world")