from com import app
from flask import Flask, render_template, request, redirect
import redis
import json
import time


#@app.route('/', methods=['get'])
#@app.route('/index', methods=['get'])
def index2():
    return render_template('index.html')


def getTime():
    return str(int(time.time()))


#@app.route('/data', methods=['get','post'])
def getData2():
    try:
        arr = []
        i = 0
        for num in range(1, 20):
            arr.append([int(time.time())*1000, num])
        print  json.dumps(arr)
        return json.dumps(arr)
    except Exception, exception:
        print exception


if __name__ == '__main__':
    getData2()
    mm=getTime()
    print mm
