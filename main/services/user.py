from model.user import User
from db import db
from schema.schemas import user_schema, user_schema_list
import logging

def save(user):
    user = user_schema.load(user)
    if(user.id != 0):
        db.session.merge(user)
    else:
        db.session.add(user)
    db.session.commit()
    return user_schema.dump(user)

def getAll():
    return user_schema_list.dump(User.query.all())