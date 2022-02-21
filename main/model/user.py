from db import db
from sqlalchemy import Column, Integer, String

class User(db.Model):
    __tablename__ = 'user_'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    email = Column(String)
    pswd = Column(String)