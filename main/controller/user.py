from flask_restx import Resource, fields
import services.user as user_service
from api import api

ns = api.namespace("user", title="User",description="CRUD for User")

model = api.model('User', {
    'name' : fields.String,
    'email' : fields.String,
    'pswd' : fields.String
})

@ns.route('')
class User(Resource):

    def get(self):
        return user_service.getAll()

    @api.marshal_with(model)
    def post(self):
        try:
            return user_service.save(api.payload), 200
        except BaseException as e:
            return e, 400
        
