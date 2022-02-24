from flask_restx import Resource, reqparse
import services.user as user_service
from controller.model import user_model
from api import api
# import logging

ns = api.namespace("user", title="User",description="CRUD for User")

parser = reqparse.RequestParser()
parser.add_argument('id')

@ns.route('')
class User(Resource):

    @api.marshal_list_with(user_model)
    def get(self):        
        try:
            args = parser.parse_args()
            id = args['id']
            if(id):
                return user_service.getBy(args)
            else:
                return user_service.getAll()
                
        except BaseException as e:
            err_s = '{} - {} - {}'.format(type(e), e.args,e)
            return {'error':err_s}, 400

    @api.marshal_with(user_model)
    def post(self):
        try:
            return user_service.create_user(api.payload), 200
        except BaseException as e:
            err_s = '{} - {} - {}'.format(type(e), e.args,e)
            return {'error':err_s}, 400
        
