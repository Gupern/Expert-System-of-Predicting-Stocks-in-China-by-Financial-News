#encoding: utf-8
import os
from flask import Flask, url_for, redirect, render_template, request, abort, jsonify
import sys
import traceback

# 引入上层的utils模块，爬虫和引擎共用
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
sys.path.append("../utils")
sys.path.append("../scripts")
sys.path.append("../scripts/crawlers")

from log import bootstrap


app = Flask(__name__)


@app.route('/api/get_news/<day>')
def get_news(day):
    from es import get_es
    """ 获取单独某一天的新闻 """
    try:
        es, index, doc_type = get_es('es_news_pub')
        body = {
            "query": {
                "term": {
                    "datetime": day
                }
            }
        }
        res = es.search(index=index, doc_type=doc_type, body=body)

        # 科技动态板块
        technology_news = []

        for r in res['hits']['hits']:
            tmp = r['_source']
            print(tmp)
            if tmp.get("category") == "technology_news":
                technology_news.append(tmp)

        package = {
            "technology_news": technology_news
        }

        return jsonify(
            success=True,
            data=package
        )
    except:
        traceback.print_exc()


if __name__ == '__main__':
    bootstrap()

    app.run(host='0.0.0.0', port=8888, debug=True)
