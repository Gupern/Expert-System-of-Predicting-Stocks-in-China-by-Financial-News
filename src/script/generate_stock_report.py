# encoding: utf-8
"""
    Author: Gupern
    Description: to segment Chinese word and generate reporting statistics
    Algorithm: 
        1. 导入结巴分词
        2. 读取数据库信息
            2.1 股票名称列表
            2.2 股票代号列表
            2.3 股票行业列表
            2.4 股票资讯for循环
        3. 统计每个股票出现的名称、代号、行业、积极消极词频
        4. 打印数据
    Using: python src/main.py --collection=info_detail --script=generate_stock_report --crawler_component=date:2022-03-01;2022-01-23
    # 每天的数据入库到新collection，行业统计表、个股统计表:
    # 日期，股票名称，出现总频次，积极频次，消极频次
    # 日期，股票代号，出现总频次，积极频次，消极频次
    # 日期，行业，出现总频次，积极频次，消极频次

"""

import jieba
import os

root_dir = os.path.abspath('.')

def func(mongo_collection, crawler):
    print("hello world")

    # 根据时间进行遍历 created_date为新闻爬取时间
    for created_date in crawler.date:
        # 积极词汇及出现频数
        positive_count_dict = {}
        # 消极词汇及出现频数
        negative_count_dict = {}
        # 所有词出现总频数
        word_total_count = 0
        # 股票名称出现频数
        stock_name_count_dict = {}
        # 股票代号出现频数
        stock_code_count_dict = {}
        # 行业名称出现频数
        raw_industry_count_dict = {}
        # 股票所属行业出现频数
        stock_relative_industry_count_dict = {}
        # 总行业名称出现频数
        all_industry_count_dict = {}


        # 读取数据库资讯信息
        for i in mongo_collection.find({"created_date":created_date}):
            print(i["content_clean"])
            print(i['created_date'])
            # TODO 进行分词，匹配词频，每个词:次数字典
                # TODO 进行积极词汇分词及统计
                # TODO 进行消极词汇分词及统计
                # TODO 进行总词汇统计
                # TODO 进行股票名称分词及统计
                # TODO 进行股票代号分词及统计
                # TODO 进行行业分词及统计
            # TODO 进行股票名称关联行业
            # TODO 打印字符串
            # TODO 打印报表
            # TODO 数据入库
            break



if __name__ == "__main__":
    print("hello world")