from ma import ma
from model.user import User
# from marshmallow import post_load
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True

    id = ma.auto_field()
    name = ma.auto_field()
    email = ma.auto_field()
    pswd = ma.auto_field()

