'''
@Author: alphapenng
@Date: 2020-06-04 16:11:13
@LastEditors: alphapenng
@LastEditTime: 2020-06-05 09:41:48
@Description: 
'''
from flask import Flask, render_template

name = 'alphapenng'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'}
]

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)
