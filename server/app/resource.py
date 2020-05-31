from datetime import datetime
from flask_restful import Resource, reqparse
from app import db, render_template, app
from app.models import User


@app.route('/')
def index():
    return render_template('index.html') 


@app.route('/read')
def read():
    data = User.query.all()
    
    return render_template('read.html', data=data)


class Info(Resource):
    def get(self):
        try:
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

        except Exception as e:
            return {'error': str(e)}

