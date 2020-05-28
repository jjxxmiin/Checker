import datetime
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


class User(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('timestamp', required=True, type=float)
        parser.add_argument('code', required=True, type=str)
        parser.add_argument('location', required=True, type=int)
        args = parser.parse_args()

        time = datetime.datetime.fromtimestamp(int(args['timestamp'])).strftime('%Y-%m-%d %H:%M:%S')
        user_code = args['code']
        user_location = args['location']

        print(f"Time : {time} \n"
              f"Code : {user_code} \n"
              f"Location : {user_location}")

        return {'ok': 1}


api.add_resource(User, '/user')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5170, debug=True)
