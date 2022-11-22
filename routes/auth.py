from fastapi import APIRouter, HTTPException, status, Depends
from utils.jwt import generate_jwt, verify_jwt
from schemas.usuario import UsuarioLogin, UsuarioChangeClave, UsuarioResetClave
from schemas.status import Status
from schemas.token import Token
from controller.usuario import getUsuarioById, changeClave, resetClave
from utils.usuario import verify_user_exists, getAllAccionesOfUsuario
from middleware.permission import hasPermission
from middleware.verifyTokenRoute import verify_token_header

from schemas.email import EmailSchema
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from os import environ

auth = APIRouter(
  tags=["Auth"]
)

@auth.post('/login')
def login(user: UsuarioLogin):
  user_id = verify_user_exists(user)
  jwt = generate_jwt(user_id)
  user = getUsuarioById(user_id)
  user_data = {
    'id': user['id'],
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

  return [user_data, token, acciones]

@auth.post('/autoLogin')
def autoLogin(token: Token):
  user_id = verify_jwt(token.token, True)
  user = getUsuarioById(user_id)
  user_data = {
    'id': user['id'],
    'nombre': user['nombre'],
    'apellido': user['apellido'],
    'username': user['username'],
  }
  acciones = {
    'acciones': getAllAccionesOfUsuario(user_id)
  }
  return [user_data, acciones]


@auth.post('/verificarToken')
def verify_token(token: Token):
  return verify_jwt(token.token)

@auth.put("/changeClave", response_model=Status)
def change_clave(user: UsuarioChangeClave):
  return changeClave(user.id, user.clave, user.newClave)

@auth.put("/resetClave", response_model=Status, dependencies=[Depends(hasPermission)])
def reset_clave(user: UsuarioResetClave):
  return resetClave(user.id, user.clave)

@auth.post("/email", response_model=Status, dependencies=[Depends(hasPermission)])
async def send_email(email: EmailSchema):
  conf = ConnectionConfig(
    MAIL_USERNAME = environ.get('MAIL_USER'),
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD'),
    MAIL_FROM = environ.get('MAIL_USER'),
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_FROM_NAME="Modulo Seguridad",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
  )

  html = """
    <h4>Hola {0}!</h4><br/>
    <p>Tu clave de acceso es: <b>{1}</b></p>""".format(email.username, email.new_clave)

  message = MessageSchema(
    subject="no-reply",
    recipients=[email.email],
    body=html,
    subtype=MessageType.html,
  )

  fm = FastMail(conf)
  try:
    await fm.send_message(message)
    return {"detail": "Email enviado"}
  except Exception as e:
    print(e)
    return {"detail": "Email no enviado"}