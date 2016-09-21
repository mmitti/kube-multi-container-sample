from flask import Flask, render_template, request, redirect, url_for
import sys
import requests as req
import json
import os
from socket import gethostname

app = Flask(__name__)
api = "http://localhost:8000"
path = "/db/dat.json"
@app.route('/')
def index():
    f = open(path, "r")
    data = json.loads(f.read())
    f.close()
    return render_template('index.html', view_host=gethostname(), data=data["data"],
        info=data["info"], url=url_for("post", _external=True))

@app.route('/post', methods=['POST'])
def post():
    if request.method == 'POST':
        text = request.form['text']
        req.post(api+"/add", data=json.dumps({"text":text, "host":gethostname()}))
    return redirect(url_for('index', _external=True))
if __name__ == '__main__':
    app.run(host='0.0.0.0')
