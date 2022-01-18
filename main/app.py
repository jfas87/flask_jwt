from flask import Flask
from flask_restx import Api
from db import init_db
from ma import init_ma
from controller.user import UserList
import logging

api = Api()

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

api.init_app(app)

if __name__ == '__main__':
    logging.basicConfig(filename='app.log', level = logging.INFO)
    init_db(app)
    init_ma(app)
    api.add_resource(UserList, '/user')
    app.run()