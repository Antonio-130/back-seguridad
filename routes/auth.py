from fastapi import APIRouter, HTTPException, status
from utils.jwt import generate_jwt, verify_jwt
from schemas.usuario import UsuarioLogin, ChangeClave
from schemas.status import Status
from schemas.token import Token
from controller.usuario import getUsuarioById, changeClave
from utils.usuario import verify_user_exists, getAllAccionesOfUsuario
from utils.response import succes_response

auth = APIRouter(
  tags=["Auth"]
)

@auth.post('/login')
def login(user: UsuarioLogin):
  user_id = verify_user_exists(user)
  jwt = generate_jwt(user_id)
  user = getUsuarioById(user_id)
  user_data = {
    'nombre': user['nombre'],
    'apellido': user['apellido'],
    'username': user['username'],
  }
  token = {
    'token': jwt
  }
  acciones = {
    'acciones': getAllAccionesOfUsuario(user_id)
  }

  return succes_response([user_data, token, acciones])

@auth.post('/autoLogin')
def autoLogin(token: Token):
  user_id = verify_jwt(token.token, True)['data']
  user = getUsuarioById(user_id)
  user_data = {
    'nombre': user['nombre'],
    'apellido': user['apellido'],
    'username': user['username'],
  }
  acciones = {
    'acciones': getAllAccionesOfUsuario(user_id)
  }
  return succes_response([user_data, acciones])


@auth.post('/verificarToken')
def verify_token(token: Token):
  return verify_jwt(token.token)

@auth.put("/changeClave", response_model=Status)
def change_clave(claves: ChangeClave):
  user_id = verify_jwt(claves.token, True)['data']
  print(user_id)
  result = changeClave(user_id, claves.clave, claves.newClave)
  if result:
    return succes_response()
  else:
    return error_response("NO_ACTUALIZADO")