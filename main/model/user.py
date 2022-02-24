from db import db
import enum
from sqlalchemy import Column, Integer, String, Enum

class UserTypeEnum(enum.Enum):
    DEFAULT=1
    ADMIN=2
    TEST=3

class User(db.Model):
    __tablename__ = 'user_'
    id = Column(Integer, primary_key = True)
    user_type = Column(Enum(UserTypeEnum))
    name = Column(String)
    email = Column(String)
    pswd = Column(String)