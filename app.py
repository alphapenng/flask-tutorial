'''
@Author: barca8best
@Date: 2020-06-04 16:11:13
@LastEditors: barca8best
@LastEditTime: 2020-06-04 17:43:17
@Description: 
'''
from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello'

@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' %name

@app.route('/test')
def test_url_for():
    return 'Test page'

