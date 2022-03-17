from flask_restx import Resource
from api import api
from controller.model import user_model
from services.token_jwt import create_token
import logging

ns = api.namespace('auth', description= 'Manage JWT Token')

@ns.route('/user')
class AuthUser(Resource):

    def post(self):
        try:
            return create_token(api.payload), 200
        except BaseException as e:
            err_s = f'{type(e)} - {e.args} - {e}'
            logging.info(err_s)
            return { 'error' : err_s }, 400
