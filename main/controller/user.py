from gzip import READ
from flask_restx import Resource, fields
import services.user as user_service
from api import api

ns = api.namespace("user", title="User",description="CRUD for User")

model = api.model('User', {
    'name' : fields.String,
    'email' : fields.String
})

@ns.route('')
class User(Resource):
    def get(self):
        return user_service.getAll()

    @api.marshal_with(model)
    def post(self, user):
        return user_service.save(user)
        
