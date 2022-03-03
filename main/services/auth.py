import jwt
import logging
from functools import wraps
from flask import request
from services.token_jwt import validate_token

def token_valdation():
    token = request.headers.get('token')
    if(token):
        try:
            return validate_token(token)
        except BaseException as e:
            raise e
    else:
        raise Exception('No token found')