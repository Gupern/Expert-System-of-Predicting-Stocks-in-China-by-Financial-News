#encoding: utf-8

from datetime import datetime

from es import get_es

一行三会 = ['央行', '证监会', '银监会', '保监会']  # , '深交所', '上交所'

高层动态 = ['中共中央', '国务院', '李克强', '习近平', '部委', '财政部', '商务部', '工信部', '发改委', '住建部', '统计局', '审计署', '海关总署', '税务总局']


def get_news_obj(day=None):
    if day == None:
        day = str(datetime.now())[:10]

    def news_query(source):
        from datetime import datetime

        weekday = datetime.now().weekday()
        if weekday == 0:
            size = 3
        else:
            size = 1
        body = {
            "query": {
                "bool": {
                    "must": [{
                        "query_string": {
                            "fields": [
                                "source"
                            ],
                            "query": "{}".format(source)
                        }
                    },
                        {"range": {
                            "datetime": {
                                "lte": day
                            }
                        }}
                    ]
                }
            },
            "sort": [
                {
                    "datetime": "desc"
                }
            ],
            "size": size
        }

        es, index, doc_type = get_es('es_news')

        ret = es.search(body=body, index=index, doc_type=doc_type)  # fetch all items from es's es_news index
        hits = ret['hits']['hits']
        if len(hits) == 0:
            return []
        else:
            contents = {}
            for hit in hits:
                if hit['_source']['datetime'] == day:
                    for content in hit['_source']['content']:
                        key = list(content.keys())[0]
                        if key not in contents:
                            contents[key] = content[key]
                        else:
                            contents[key] = contents[key] + content[key]
            return {'content': [contents], 'datetime': hits[0]['_source']['datetime']}

    def wrap_result(keyword):
        res1 = news_query(keyword)
        news_obj = res1['content'] if res1 else []
        datetime = res1['datetime'] if res1 else []

        dichan = []
        res = {'一行三会': [], '高层动态': []}

        for section in news_obj:
            for section_key in section.keys():
                if section_key == '地产观察':
                    dichan = section[section_key]

        news_obj = list(filter(lambda x: any(key in x.keys() for key in ['宏观数据', '市场要闻', '债券资讯', '宏观', '行业']),
                               news_obj))

        for section in news_obj:
            for section_key in section.keys():
                list_copy = section[section_key]
                for i in range(0, len(list_copy)):
                    if any([x in list_copy[i][1] or x in list_copy[i][0] for x in 一行三会]):
                        res['一行三会'].append(list_copy[i])
                    elif any([x in list_copy[i][1] or x in list_copy[i][0] for x in 高层动态]):
                        res['高层动态'].append(list_copy[i])

        def sort_in_content(input, keywords):
            for i in range(0, len(keywords)):
                if keywords[i] in input[1] or keywords[i] in input[0]:
                    return i
            return len(keywords)

        res['一行三会'] = sorted(res['一行三会'], key=lambda x: sort_in_content(x, 一行三会))
        res = [{'一行三会': res['一行三会']}, {'高层动态': res['高层动态']}]

        return res, dichan

    res_femorning, dichan = wrap_result("财经早餐")
    if not res_femorning:
        res_shanguotou, dichan = wrap_result("陕国投信托")
    else:
        res_shanguotou = []

    return {'femorning': res_femorning, 'shanguotou': res_shanguotou, 'dichan': dichan}


def get_extra_news_obj(day=None):
    if day == None:
        day = str(datetime.now())[:10]

    def news_query(doc_type):
        body = {
            "query": {
                "range": {
                    "datetime": {
                        "lte": day
                    }
                }
            },
            "sort": [
                {
                    "datetime": "desc"
                }
            ]
        }
        es, index, doc_type = get_es(doc_type)

        ret = es.search(body=body, index=index, doc_type=doc_type)  # fetch all items from es's es_news index
        hits = ret['hits']['hits']
        return hits

    def date_filter(res, date):
        return [x['_source'] for x in res if x['_source']['datetime'] == date]

    caijing01 = date_filter(news_query("es_news_caijing01")[:10], day)
    kr36 = date_filter(news_query("es_news_kr36")[:10], day)

    wallstreetcn_res = news_query("es_news_wallstreetcn")

    wallstreetcn = []
    for item in wallstreetcn_res:  # [:size]:
        if item['_source']['datetime'] == day:
            wallstreetcn += item['_source']['content']
    wallstreetcn = list(
        filter(lambda x: all(key not in x['title'] and key not in x['abstract'] for key in 一行三会 + 高层动态),
               wallstreetcn))

    return {'caijing01': caijing01, 'kr36': kr36, 'wallstreetcn': wallstreetcn}


def packing(date):
    f = lambda a: map(lambda b: a[b: b + 2], range(0, len(a) - 1, 2))
    div_list = list(f(index_data))
    news_obj = get_news_obj(date)
    extra_news_obj = get_extra_news_obj(date)

    package = {
        "femorning_data": news_obj['femorning'],
        "shanguotou_data": news_obj['shanguotou'],
        "wallstreetcn_data": extra_news_obj['wallstreetcn'],
        "hujin_data": extra_news_obj['caijing01'],
        "dichan_data": news_obj['dichan'],
        "ai_data": extra_news_obj['kr36']
    }
    return package


if __name__ == '__main__':
    push_news()
