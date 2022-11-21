import jwt
from datetime import datetime, timedelta
from os import environ
from fastapi import HTTPException

def generate_jwt(payload):
    return jwt.encode({
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow(),
        'sub': payload
    }, environ.get('JWT_SECRET'), algorithm='HS256')

def decode_jwt(token):
    try:
        return jwt.decode(jwt=token, key=environ.get('JWT_SECRET'), algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=419, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token invalido")
    except jwt.DecodeError:
        raise HTTPException(status_code=401, detail="Error al decodificar el token")

def verify_jwt(token, output=False):
    decoded = decode_jwt(token)
    return decoded['sub'] if output else True