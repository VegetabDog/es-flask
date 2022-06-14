import pymysql
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from elasticsearch.helpers import bulk

db = pymysql.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='data_web'
)

es = Elasticsearch()

def set_mapping(es):
    if not es.indices.exists(index='ch'):
        body = {
            "settings": {
                "index": {
                    "analysis.analyzer.default.type": "ik_max_word"
                }
            }
        }
        es.indices.create("ch", body=body)
    if not es.indices.exists(index='eng'):
        body = {
            "settings": {
                "analysis": {
                    "analyzer": {
                        "english": {
                            "tokenizer": "standard",
                            "filter": ["lowercase", "stop", "snowball"]
                        }
                    }
                },
                "index": {
                    "analysis.analyzer.default.type": "english"
                }
            }
        }
        es.indices.create("eng", body=body)

def getData():
    try:
        cursor = db.cursor()
        sql = "SELECT * FROM english"
        cursor.execute(sql)
        data_eng = cursor.fetchall()
        # print(len(data_eng))
        antions = []
        for i in data_eng:
            print('title= '+str(i[1]))
            print('url= ' + str(i[2]))
            print('content= ' + str(i[3]))
            print('tiem= ' + str(i[4]))
            action = {
                '_index': 'eng',
                '_id': i[0],
                '_source': {
                    'title': i[1],
                    'url': i[2],
                    'content': i[3],
                    'time': i[4]
                }
            }
            antions.append(action)
        print(len(antions))
        # helpers.bulk(es, antions)
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (sql, e))

def getChData():
    try:
        cursor = db.cursor()
        sql = "SELECT * FROM chinese"
        cursor.execute(sql)
        data_eng = cursor.fetchall()
        # print(len(data_eng))
        antions = []
        for i in data_eng:
            print('title= '+str(i[1]))
            print('url= ' + str(i[2]))
            print('content= ' + str(i[3]))
            print('tiem= ' + str(i[4]))
            action = {
                '_index': 'ch',
                '_id': i[0],
                '_source': {
                    'title': i[1],
                    'url': i[2],
                    'content': i[3],
                    'time': i[4]
                }
            }
            antions.append(action)
        print(len(antions))
        helpers.bulk(es, antions)
    except Exception as e:
        db.rollback()
        print("执行MySQL: %s 时出错：%s" % (sql, e))

if __name__ == '__main__':
    set_mapping(es)
    # getData()
    getChData()
    # es.delete_by_query(index='eng', doc_type='_doc', body={"query": {"match_all": {}}})
    # delete_by_all = {"query": {"match_all": {}}}
