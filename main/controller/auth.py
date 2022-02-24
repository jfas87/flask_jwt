from flask_restx import Resource
from api import api
from controller.model import user_model
from services.user import validate_user

ns = api.namespace('auth', description= 'Manage JWT Token')

@ns.route('/user')
class AuthUser(Resource):

    @api.marshal_with(user_model)
    def post(self):
        try:
            return validate_user(api.payload), 200
        except BaseException as e:
            err_s = '{} - {} - {}'.format(type(e), e.args,e)
            return { 'error' : err_s }, 400
