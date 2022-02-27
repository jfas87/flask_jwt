from flask_restx import Resource
from api import api
from controller.model import user_model
from services.user import authenticate
import logging

ns = api.namespace('auth', description= 'Manage JWT Token')

@ns.route('/user')
class AuthUser(Resource):

    def post(self):
        try:
            return authenticate(api.payload), 200
        except BaseException as e:
            err_s = '{} - {} - {}'.format(type(e), e.args,e)
            logging.info(err_s)
            return { 'error' : err_s }, 400
