import json
from flask_cors import CORS
from flask import Flask
from api import graph

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/selectByAcademy/getjson/<name_ch>')
def get_graph(name_ch):
    return json.dumps(graph.get_data_academy(name_ch=name_ch), ensure_ascii=False)


@app.route('/selectByCluster/getjson/<name_ch>')
def get_graph_2(name_ch):
    return json.dumps(graph.get_data_cluster(name_ch=name_ch), ensure_ascii=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
