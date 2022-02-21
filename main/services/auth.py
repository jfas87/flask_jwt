import jwt
import logging

secret_key = "secretkey"
algorithm = "HS256"

def token_encode(payload):
    return jwt.encode(payload, secret_key, algorithm=algorithm)

def token_decode(payload):
    token = payload['token']
    logging.info(token)
    return jwt.decode(token, secret_key, algorithms=[algorithm])