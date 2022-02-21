import jwt

secret_key = "definitelynotasecretkey"
algorithm = "HS256"

def token_encode(payload):
    return jwt.encode(payload, secret_key, algorithm=algorithm)

def token_decode(token):
    return jwt.decode(token, secret_key, algorithms=[algorithm])