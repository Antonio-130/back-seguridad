from fastapi import Request, HTTPException, status
from utils.jwt import verify_jwt

async def verify_token_header(request: Request):
  token = request.headers.get("Authorization")
  if token == None:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Autorización no proporcionada")
  else:
    token = token[7:]
    validation = verify_jwt(token)
    if validation:
      return True
    else:
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")