import jwt
import logging
from functools import wraps
from flask import request
from services.user import authenticate

secret_key = "secretkey"
algorithm = "HS256"

def token_encode(payload):
    return jwt.encode(payload, secret_key, algorithm=algorithm)

def token_decode(payload):
    token = payload['token']
    logging.info(token)
    return jwt.decode(token, secret_key, algorithms=[algorithm])

def create_token(data):
    if(authenticate(data)):
        return token_encode(data)

def token_valdation(f):
    @wraps(f)
    def wrapper(*args, **kwargs):

        token = request.headers.get('token')
        if(token):
            user = token_decode(token)
            if(authenticate(user)):
                 return f(*args, **kwargs)
            else:
                raise Exception('Invalid Token')
        else:
            raise Exception('No token found!')
       
    return wrapper