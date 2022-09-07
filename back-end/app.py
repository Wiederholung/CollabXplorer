import json

from flask import Flask

import getJSON

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/getjson/<name_ch>')
def get_json(name_ch):
    return json.dumps(getJSON.get_data(name_ch=name_ch), ensure_ascii=False)


if __name__ == '__main__':
    app.run(host='::')