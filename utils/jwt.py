import jwt
from datetime import datetime, timedelta
from os import environ
from fastapi import HTTPException
from utils.response import succes_response, error_response

def generate_jwt(payload):
    return jwt.encode({
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow(),
        'sub': payload
    }, environ.get('JWT_SECRET'), algorithm='HS256')

def decode_jwt(token):
    return jwt.decode(token, environ.get('JWT_SECRET'), algorithms=['HS256'])

def verify_jwt(token, output=False):
    try:
        decoded = decode_jwt(token)
        if datetime.utcnow() < datetime.fromtimestamp(decoded['exp']):
            return succes_response(decoded['sub']) if output else True
        else:
            raise HTTPException(status_code=401, detail=error_response("TOKEN_EXPIRADO"))
    except:
        raise HTTPException(status_code=401, detail=error_response("TOKEN_INVALIDO"))