from model.user import User
from db import db
from schema.schemas import user_schema, user_schema_list
import logging

def save(data):

    user = user_schema.load(data)
    if(user.id):
        db.session.add(user)
    else:
        db.session.merge(user)
    db.session.commit()
    # return user_schema.dump(user)
    return user

def getAll():
    return user_schema_list.dump(User.query.all())

def validate_user(user):
    # db.session. verificar dados de usuário.    
    return True