from flask_restx import Resource, fields
from api import api 
from services.auth import token_encode, token_decode
ns = api.namespace('token', description= 'JWT Token validation. Must be used just for tests and QA.')


@ns.route('/encode')
class TokenEncode(Resource):

    def post(self):
        try:
            return token_encode(api.payload), 200
        except BaseException as e:
            return '{} - {} - {}'.format(type(e), e.args,e), 400


@ns.route('/decode')
class TokenDecode(Resource):

    def post(self):
        try:
            return token_decode(api.payload), 200
        except BaseException as e:
            return '{} - {} - {}'.format(type(e), e.args,e), 400