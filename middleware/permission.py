from fastapi import HTTPException, status, Request
from controller.usuario import usuarioHasAccion
from utils.jwt import decode_jwt
from utils.response import error_response

async def hasPermission(request: Request):
  token = request.headers.get("Authorization")
  if token == None:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=error_response("SIN_AUTORIZACION"))
  else:
    token = token[7:]
    idUsuario = decode_jwt(token)["sub"]
    accionRequest = str(request.get("endpoint")).split(" ")[1]
    if usuarioHasAccion(accionRequest, idUsuario):
      return True
    else:
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=error_response("SIN_PERMISOS"))