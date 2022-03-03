from flask_restx import Resource
from services.auth import token_valdation
import logging

class BaseResource(Resource):

    def get(self, func):
        try:
            if token_valdation() : 
                return func , 200
        except BaseException as e:
            #need to enhanced so for better troubleshooting
            err_s = '{} - {} - {}'.format(type(e), e.args,e)
            return {'error':err_s}, 400

    def post(self, func):
        try:
            if token_valdation() : return func, 200
        except BaseException as e:
            err_s = '{} - {} - {}'.format(type(e), e.args,e)
            return {'error':err_s}, 400