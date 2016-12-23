from flask import Flask, render_template, request, redirect
import time
import json
import redis

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET", "POST"])
def hello():
    return render_template("mon.html")


@app.route("/data", methods=["GET"])
def getData1():
    hashkey = "pc::key"
    try:
        r = redis.StrictRedis(host='10.10.10.122', port='6379', db=1);
        values = r.hgetall(hashkey)
        arr = []
        a="x"
        b="y"
        for key in values:
            arr.append({a:int(key)*1000,b:int(values[key])})
        return json.dumps(arr)
    except Exception, exception:
        print exception


@app.route("/data1", methods=["GET"])
def getdata2():
    arr = []
    for num in range(1, 20):
        arr.append([int(time.time()) * 1000, num])

    return json.dumps(arr)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1011,debug=True)
