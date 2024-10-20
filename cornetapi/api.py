
from flask import Flask, jsonify, make_response, request, Response
import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

import urllib.parse
from pymongo import MongoClient

username = urllib.parse.quote_plus("admin")             # Логин админстратора
password = urllib.parse.quote_plus("3gaSc&Bi")          # Пароль администратора

host = "gekukugep.beget.app"  # Адрес сервера / доменное имя

client = MongoClient(f"mongodb://{username}:{password}@{host}")
db = client['test']


app = Flask(__name__)




@app.route('/app')
def hello_world():

    return "This's -- api"




@app.route('/profile', methods=['GET','POST'])
def endp1() -> Response:

    try:
        if request.method == 'POST':
            res = request.json['point']
        else :
            res = request.args['point']

            res = [i for i in res.split(',')][0]

        print(res)

        myquery = {"name": {"$eq": res}}
        res = list(db['sym_eqt_tam'].find(myquery,{'_id':0}))[0]
        print(res)
        res= {k:v for k,v in res.items() if k in ['name', 'email', 'profession',  'date']}
        ds ={'status':'ok', 'results':res}

        return make_response(jsonify(ds))

    except KeyError:
        raise RuntimeError('"X" cannot be be found in JSON payload.')


@app.route('/get_role', methods=['GET','POST'])
def endp2() -> Response:

    try:
        if request.method == 'POST':
            res = request.json['point']
        else :
            res = request.args['point']

            res = [i for i in res.split(',')][0]

        print(res)

        myquery = {"name": {"$eq": res}}
        res = list(db['sym_eqt_tam'].find(myquery,{'_id':0}))[0]['role']
        ds ={'status':'ok', 'results':res}

        return make_response(jsonify(ds))

    except KeyError:
        raise RuntimeError('"X" cannot be be found in JSON payload.')


@app.route('/get_stash', methods=['GET','POST'])
def endp3() -> Response:

    try:
        if request.method == 'POST':
            res = request.json['point']
        else :
            res = request.args['point']

            res = [i for i in res.split(',')][0]

        print(res)

        myquery = {"name": {"$eq": res}}
        res = list(db['sym_eqt_tam'].find(myquery,{'_id':0}))[0]['stash']
        ds ={'status':'ok', 'results':res}

        return make_response(jsonify(ds))

    except KeyError:
        raise RuntimeError('"X" cannot be be found in JSON payload.')



@app.route('/upload_nft', methods=['GET','POST'])
def endp4() -> Response:

    try:
        if request.method == 'POST':
            res = request.json
        else :
            res = request.args

            print(res)

        myquery = {"name": {"$eq": res['point']}}
        res = db['sym_eqt_tam'].update_one(myquery,{'$set':{'nft':res['nft']}})

        ds ={'status':'ok'}

        return make_response(jsonify(ds))

    except KeyError:
        raise RuntimeError('"X" cannot be be found in JSON payload.')


if __name__ == '__main__':
    import platform

    if platform.system() == 'Windows':
        app.run(debug = True, use_reloader=False)
    else:
        app.run(host='0.0.0.0', port=8081 )





