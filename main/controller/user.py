from flask_restx import Resource, fields, reqparse
import services.user as user_service
from api import api
import logging

ns = api.namespace("user", title="User",description="CRUD for User")

model = api.model('user', {
    'name' : fields.String,
    'email' : fields.String,
    'pswd' : fields.String
})

parser = reqparse.RequestParser()
parser.add_argument('id')

@ns.route('')
class User(Resource):

    def get(self):
        try:
            id = parser.parse_args()['id']
            if(id):
                return user_service.getBy(id)
            else:
                return user_service.getAll()
        except BaseException as e:
            return '{} - {} - {}'.format(type(e), e.args,e), 400

    @api.marshal_with(model)
    def post(self):
        try:
            return user_service.save(api.payload), 200
        except BaseException as e:
            return '{} - {} - {}'.format(type(e), e.args,e), 400
        
