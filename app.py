from flask import Flask
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from flask import request
from flask import json
from  flask import jsonify
from flask import Flask, render_template

app = Flask(__name__)

es = Elasticsearch()

@app.route('/searchInfo', methods=['POST'])
def searchInfo():
    if request.method == 'POST':
        inputInfo = request.form.get('info')
        body = {
            "query": {
                "multi_match": {
                    "query": inputInfo,
                    "fields": ["title", "content"]
                }
            },
            "highlight": {
                "fields": {
                    "title": {}
                }
            }
        }
        params = {
            'size': 30
        }
        searchRes = []
        resEng = es.search(index=['eng', 'ch'], body=body, _source=['title', 'url', 'content'], params=params)
        resEng = resEng['hits']['hits']
        for i in range(0, len(resEng)):
            res = resEng[i]
            searchRes.append(res['_source'])
        # resCh = es.search(index="ch",body=body)
        size = str(len(searchRes))
        print(len(resEng))
        return {'code': 200, 'message': searchRes, 'size': size}
    else:
        return {'code': 400, 'message': '不是post请求'}

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

