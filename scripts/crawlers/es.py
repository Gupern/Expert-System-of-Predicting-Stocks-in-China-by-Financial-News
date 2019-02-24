import os
import sys
import traceback

from elasticsearch import Elasticsearch
from config import config

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, CURRENT_DIR)


settings = {
    "settings": {
        "analysis": {
            "analyzer": {
                "han_bigrams": {
                    "tokenizer": "standard",
                    "filter": ["han_bigrams_filter"]
                }
            },
            "filter": {
                "han_bigrams_filter": {
                    "type": "cjk_bigram",
                    "ignored_scripts": [
                        "hiragana",
                        "katakana",
                        "hangul"
                    ],
                    "output_unigrams": True
                }
            }
        }
    },
    "mappings": {
        "_default_": {
            "dynamic_templates": [
                {
                    "string_fields": {
                        "match": "*",
                        "match_mapping_type": "text",
                        "mapping": {
                            "type": "text",
                            "index": "analyzed",
                            "analyzer": "han_bigrams",
                            "fielddata": {
                                "format": "disabled"
                            },
                            "fields": {
                                "keyword": {
                                    "type": "keyword",
                                    "index": "not_analyzed",
                                    "ignore_above": 256
                                },
                                "raw": {
                                    "type": "keyword",
                                    "index": "not_analyzed",
                                    "ignore_above": 256
                                }
                            }
                        }
                    }
                }
            ]
        }
    }
}

INIT_CACHE = {}


def get_es(section):
    global INIT_CACHE
    host = config.get(section, 'host')
    port = config.getint(section, 'port')
    index = config.get(section, 'index')
    doc_type = config.get(section, 'doc_type')

    es = Elasticsearch(host=host, port=port, timeout=300)

    try:
        if section not in INIT_CACHE:
            es.indices.create(
                index=index,
                body=settings,
                ignore=[400]
            )
            INIT_CACHE[section] = True
    except:
        traceback.print_exc()

    return es, index, doc_type
