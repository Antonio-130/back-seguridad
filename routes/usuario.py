from fastapi import APIRouter, Depends
from schemas.usuario import Usuario, UsuarioIn, UsuarioUpdate
from schemas.status import Status
from controller.usuario import getAllUsuarios, getUsuarioById, createUsuario, updateUsuario, deleteUsuario
from middleware.verifyTokenRoute import verify_token_header
from middleware.permission import hasPermission

usuario = APIRouter(
  prefix="/usuarios",
  tags=["Usuarios"],
  dependencies=[Depends(verify_token_header), Depends(hasPermission)]
)

@usuario.get("", response_model=list[Usuario])
def get_usuarios():
  return getAllUsuarios()

@usuario.post("", response_model=Status)
def create_usuario(usuario: UsuarioIn):
  return createUsuario(usuario)

@usuario.get("/{id}", response_model=Usuario)
def get_usuario(id: int):
  return getUsuarioById(id)

@usuario.delete("/{id}", response_model=Status)
def delete_usuario(id: int):
  return deleteUsuario(id)

@usuario.put("/{id}", response_model=Status)
def update_usuario(id: int, usuario: UsuarioUpdate):
  return updateUsuario(id, usuario)