from com import app
from flask import Flask, render_template, request, redirect
import redis
import json
import time

#@app.route('/', methods=['get'])
#@app.route('/index', methods=['get'])
def index():
    return render_template('index.html')

def getTime():
        return str(int(time.time()) + 8 * 3600)
@app.route('/data1' ,methods = ['get'])
def getData1():
    hashkey = "pc::key"
    try:
        r = redis.StrictRedis(host='10.10.10.122', port='6379', db=1);
        values = r.hgetall(hashkey)
        arr = []
        i =0
        for key in values:
            i +=1
            arr.append([key, values[key]])
            if i>10:
                break
        return json.dumps(arr)
    except Exception, exception:
        print exception