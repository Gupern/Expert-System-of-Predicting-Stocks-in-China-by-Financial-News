#encoding: utf-8
import os
from flask import Flask, url_for, redirect, render_template, request, abort

@app.route('/api/get_news/<day>')
def get_news(day):
    """ 获取单独某一天的新闻 """
    from push_news import get_news_obj, get_extra_news_obj

    edit_version = False
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
        if res['hits']['hits']:
            tmp = res['hits']['hits'][0]['_source']['content']
            package = {
                "yihangsanhui_data": tmp.get('高层表态'),
                "gaocengdongtai_data": tmp.get('部委举措'),
                "wallstreetcn_data": tmp.get('市场要闻'),
                "dichan_data": tmp.get('科技动态'),
            }
            edit_version = True
            return jsonify(
                success=True,
                data=package
            )
    except:
        traceback.print_exc()

    if not edit_version:
        try:
            news_obj = get_news_obj(day)
            extra_news_obj = get_extra_news_obj(day)

            package = {
                "yihangsanhui_data": [{'title': item[0], 'abstract': item[1]} for item in
                                      news_obj['femorning'][0]['高层表态']],
                "gaocengdongtai_data": [{'title': item[0], 'abstract': item[1]} for item in
                                        news_obj['femorning'][1]['部委举措']],
                "wallstreetcn_data": extra_news_obj['wallstreetcn'][:5],
                "hujin_data": [],
                "dichan_data": [{'title': item[0], 'abstract': item[1]} for item in news_obj['dichan']],
            }

            return jsonify(
                success=True,
                data=package
            )
        except:
            return jsonify(
                success=False,
                data=[]
            )


if __name__ == '__main__':

    app_dir = os.path.realpath(os.path.dirname(__file__))
    database_path = os.path.join(app_dir, app.config['DATABASE_FILE'])

    # Start app
    app.run(host='0.0.0.0', port=8888, debug=True)
