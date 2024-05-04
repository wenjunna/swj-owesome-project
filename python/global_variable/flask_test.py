
from global_test import t1, t2, t3
import flask, json
from flask import request

app = flask.Flask(__name__)
# g_b = {"num1": 1, "num2": 2}
# print("t0",id(g_b),g_b)
# global g_b

@app.route('/')
def index():
    return 'hello'

@app.route('/s1/', methods=['GET', 'POST'])
def s1():
    print("s1")
    num = request.values.get('num')
    print(num)
    num=int(num)
    res = t1(num)
    return res

# http://127.0.0.1:8888/s1/?num=3


@app.route('/s2/', methods=['GET', 'POST'])
def s2():
    print("s2")
    num = request.values.get('num')
    num = int(num)
    res = t2(num)
    return res


@app.route('/s3/', methods=['GET', 'POST'])
def s3():
    print("s3")
    num = request.values.get('num')
    num = int(num)
    res = t3(num)
    return res


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8888,debug=True)
    # 8087
    # app.run(debug=True, port=8889, host='127.0.0.1')
