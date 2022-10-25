from fastapi import APIRouter, Depends
from schemas.usuario import UsuarioIn, UsuarioUpdate, UsuarioStatus, UsuarioListStatus
from schemas.status import Status
from controller.usuario import getAllUsuarios, getUsuarioById, createUsuario, updateUsuario, deleteUsuario
from utils.response import succes_response, error_response
from middleware.verifyTokenRoute import verify_token_header
from middleware.permission import hasPermission

usuario = APIRouter(
  prefix="/usuarios",
  tags=["Usuarios"],
  dependencies=[Depends(verify_token_header), Depends(hasPermission)]
)

@usuario.get("", response_model=UsuarioListStatus)
def get_usuarios():
  result = getAllUsuarios()
  if result:
    return succes_response(result)
  else:
    return error_response("SIN_REGISTROS")

@usuario.post("", response_model=Status)
def create_usuario(usuario: UsuarioIn):
  result = createUsuario(usuario)
  if result:
    return succes_response()
  else:
    return error_response("NO_CREADO")

@usuario.get("/{id}", response_model=UsuarioStatus)
def get_usuario(id: int):
  result = getUsuarioById(id)
  if result:
    return succes_response(result)
  else:
    return error_response("NO_ENCONTRADO")

@usuario.delete("/{id}", response_model=Status)
def delete_usuario(id: int):
  result = deleteUsuario(id)
  if result:
    return succes_response()
  else:
    return error_response("NO_ELIMINADO")

@usuario.put("/{id}", response_model=Status)
def update_usuario(id: int, usuario: UsuarioUpdate):
  result = updateUsuario(id, usuario)
  if result:
    return succes_response()
  else:
    return error_response("NO_ACTUALIZADO")