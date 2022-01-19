from flask_restx import Api
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

api = Api(app, title = 'Auth Api', description = 'Implementation of Authentication using Flask and JWT')