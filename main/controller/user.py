from flask_restx import Namespace, Resource
import services.user as user_service

ns = Namespace("User", path="/user", description="CRUD for User")

class UserList(Resource):
    def get(self):
        return user_service.getAll()
        
