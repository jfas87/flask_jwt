from flask_restx import Resource, fields, reqparse
import services.user as user_service
from api import api
# import logging
from model.user import UserTypeEnum

ns = api.namespace("user", title="User",description="CRUD for User")

model = api.model('user', {
    'name' : fields.String,
    'email' : fields.String,
    'pswd' : fields.String,
    'user_type' : fields.String(description="User type", enum=[x.name for x in UserTypeEnum])
})

parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('email')
parser.add_argument('name')

@ns.route('')
class User(Resource):

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
            logging.error(err_s)
            return err_s, 400

    @api.marshal_with(model)
    def post(self):
        try:
            logging.info(api.payload)
            return user_service.save(api.payload), 200
        except BaseException as e:
            err_s = '{} - {} - {}'.format(type(e), e.args,e)
            logging.error(err_s)
            return err_s, 400
        
