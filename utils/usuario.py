from fastapi import HTTPException, status, Request
from schemas.usuario import UsuarioLogin
from utils.password import compare_password
from utils.response import error_response
from utils.jwt import verify_jwt
from controller.usuario import getUsuarioByEmail, getUsuarioByUsername, getAllAccionesOfUsuario

def verify_user_exists(user: UsuarioLogin):
  login_incorrecto = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=error_response("LOGIN_INCORRECTO"))

  user_finded = getUsuarioByEmail(user.email) if user.email else getUsuarioByUsername(user.username)

  if not user_finded:
    raise login_incorrecto

  if not compare_password(user.clave, user_finded["clave"]):
    raise login_incorrecto

  return user_finded["id"]