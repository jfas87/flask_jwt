import jwt
import logging
from functools import wraps
from flask import request
from services.user import authenticate

secret_key = "secretkey"
algorithm = "HS256"

def token_encode(payload):
    return jwt.encode(payload, secret_key, algorithm=algorithm)

def token_decode(token):
    return jwt.decode(token, secret_key, algorithms=[algorithm])

def create_token(data):
    if(authenticate(data)):
        return token_encode(data)

def validate_token(data):
    logging.info('jwt {}'.format(data))
    user = token_decode(data)
    logging.info('jwt user {}'.format(user))
    return authenticate(user)