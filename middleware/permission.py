from fastapi import HTTPException, status, Request
from controller.usuario import getAllAccionesOfUsuario
from utils.jwt import decode_jwt
from utils.response import error_response

async def hasPermission(request: Request):
  token = request.headers.get("Authorization")
  if token == None:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=error_response("SIN_AUTORIZACION"))
  else:
    idUsuario = decode_jwt(token.split(" ")[1])["sub"]
    accionRequest = str(request.get("endpoint")).split(" ")[1]
    acciones = getAllAccionesOfUsuario(idUsuario)
    for accion in acciones:
      if accion["nombre"] == accionRequest:
        return True
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=error_response("SIN_PERMISOS"))