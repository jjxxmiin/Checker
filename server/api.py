import os
from flask import render_template, url_for
from flask_restful import reqparse
from flask_restful import Api
from app import app, db, DB_PATH
from app.models import User


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/read')
def read():
    data = User.query.all()

    return render_template('read.html', data=data)


@app.route('/map')
def map():
    data = User.query.all()

    return render_template('map.html', data=data)


@app.route('/info', methods=['GET'])
def Info():
    parser = reqparse.RequestParser()
    parser.add_argument('timestamp', required=True, type=float)
    parser.add_argument('code', required=True, type=str)
    parser.add_argument('location', required=True, type=int)
    args = parser.parse_args()

    timestamp = args['timestamp']
    student_code = args['code']
    location = args['location']

    user = User(student_code=student_code, timestamp=timestamp, location=location)
    db.session.add(user)
    db.session.commit()

    return {'ok': 1}

if __name__ == "__main__":
    if not os.path.exists(DB_PATH):
        os.mkdir(DB_PATH)
        db.create_all()

    api = Api(app)

    app.run(host='0.0.0.0', port=5170, debug=True)
