import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
DB_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)) , 'db')
dbfile = os.path.join(DB_PATH, 'db.sqlite') # 데이터베이스 이름과 경로

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SECRET_KEY'] = '8427'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app import models