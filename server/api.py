from flask_restful import Api 
from app import app, db
from app.resource import Info

api = Api(app)
api.add_resource(Info, '/info')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5170, debug=True)
