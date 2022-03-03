from flask_restx import reqparse
import services.user as user_service
from controller.model import user_model
from api import api
from controller.base import BaseResource

ns = api.namespace("user", title="User",description="CRUD for User")

parser = reqparse.RequestParser()
parser.add_argument('id')

@ns.route('/list')
class UserList(BaseResource):

    @ns.marshal_list_with(user_model)
    def get(self):        
        return super(User, self).get(user_service.getAll())

@ns.route('')
class User(BaseResource):

    @ns.marshal_with(user_model)
    def get(self):
        args = parser.parse_args()
        id = args['id']
        if(id):    
            return super(User, self).get(user_service.getBy(args))

    @ns.marshal_with(user_model)
    def post(self):
        return super(User, self).post(user_service.create_user(api.payload))

        
