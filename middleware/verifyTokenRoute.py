from fastapi import Header, HTTPException, status
from utils.jwt import verify_jwt
from utils.response import error_response

async def verify_token_header(Authorization: str = Header()):
  token = Authorization
  if token == None:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=error_response("SIN_AUTORIZACION"))
  else:
    validation = verify_jwt(token.split(" ")[1], False)
    if validation:
      return True
    else:
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=error_response("TOKEN_INVALIDO"))