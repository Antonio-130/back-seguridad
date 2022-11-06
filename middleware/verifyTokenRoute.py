from fastapi import Request, HTTPException, status
from utils.jwt import verify_jwt
from utils.response import error_response

async def verify_token_header(request: Request):
  token = request.headers.get("Authorization")
  if token == None:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=error_response("SIN_AUTORIZACION"))
  else:
    token = token[7:]
    validation = verify_jwt(token, False)
    if validation:
      return True
    else:
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=error_response("TOKEN_INVALIDO"))