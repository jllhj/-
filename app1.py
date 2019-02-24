from flask import Flask,render_template,request,jsonify


app = Flask(__name__)

import queue
q = queue.Queue()


@app.route('/get/vote')
def get_vote():
    try:
        val = q.get(timeout=20)
    except queue.Empty:
        val = '已超时'

    return val

@app.route('/vote')
def vote():
    q.put('10')
    return '投票成功'

if __name__ == '__main__':
    app.run(threaded=True)