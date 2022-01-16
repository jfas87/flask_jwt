from distutils.log import debug
from flask import Flask
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from db import init_db
from services.user import add_test_user
import logging
api = Api()

app = Flask(__name__)



app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

api.init_app(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        add_test_user()
        return {'hello': 'world'}

if __name__ == '__main__':
    logging.basicConfig(filename='app.log', level = logging.INFO)
    init_db(app)
    app.run()
    
    # print("done")

