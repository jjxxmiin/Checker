import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))  # database 경로를 절대경로로 설정함
dbfile = os.path.join(os.path.join(basedir, 'db'), 'db.sqlite') # 데이터베이스 이름과 경로

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SECRET_KEY'] = '8427'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)