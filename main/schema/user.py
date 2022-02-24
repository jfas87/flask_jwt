import enum
from ma import ma
from model.user import User, UserTypeEnum
# from marshmallow import post_load
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields
from marshmallow import fields
import logging

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True

    id = ma.auto_field()
    name = ma.auto_field()
    email = ma.auto_field()
    pswd = ma.auto_field()
    user_type = fields.Method(deserialize="deserialze_user_type", serialize = "serialize_user_Type")

    def deserialze_user_type(self, value):
        return UserTypeEnum[value]

    def serialize_user_Type(self,  obj):
        return obj.user_type.name
        