from model.user import User, UserTypeEnum
from db import db
from schema.schemas import user_schema, user_schema_list
from sqlalchemy import or_
# import logging

def getAll():
    return User.query.all()

def getBy(args):
    return User.query.where(User.id == args['id']).first()

def create_user(data):

    user_db = db.session.query(User).filter(or_(User.name == data['name'], User.email == data['email'])).first()
    
    if user_db : raise Exception('A user with the same login and\or email already exists!')
    
    user = user_schema.load(data)
    if user.user_type == UserTypeEnum.TEST:
        test_user = db.session.query(User).filter(User.user_type == UserTypeEnum.TEST).first()
        if test_user : raise Exception('A TEST type user already exists!')
    db.session.add(user)
    db.session.commit()
    
    return user_schema.dump(user)

def validate_user(user):
    # db.session. verificar dados de usuário.
    return True