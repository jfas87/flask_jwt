from flask_restx import Resource, fields
from api import api 
from services.auth import token_encode
ns = api.namespace('token', description= 'JWT Token validation. Must be used just for tests and QA.')


@ns.route('')
class Token(Resource):

    def post(self):
        return token_encode(api.payload)