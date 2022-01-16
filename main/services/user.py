from model.user import User
from db import db
import logging

def add_test_user():
    user = User()
    user.name = 'teste'

    db.session().add(user)
    db.session().commit()
    logging.info("added user " + user)