import os
from flask import Flask, render_template, send_from_directory
from src.dao import *


app = Flask(__name__)


# 渲染主页
@app.route('/')
def index():
    return render_template('index.html')


# 获取所有视频信息
@app.route('/units', methods=['GET'])
def get_all_unit():
    return select_all()


# 提供静态文件
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory(os.path.join(app.root_path, 'static', 'js'), path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory(os.path.join(app.root_path, 'static', 'css'), path)


@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory(os.path.join(app.root_path, 'static', 'img'), path)


@app.route('/icon/<path:path>')
def send_icon(path):
    return send_from_directory(os.path.join(app.root_path, 'static', 'icon'), path)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
