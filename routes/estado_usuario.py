from fastapi import APIRouter
from schemas.estado_usuario import EstadoUsuario, EstadoUsuarioIn
from schemas.status import Status
from controller.estado_usuario import getAllEstadosUsuario, getEstadoUsuario, createEstadoUsuario, updateEstadoUsuario, deleteEstadoUsuario

estadoUsuario = APIRouter(
  prefix="/estadosUsuario",
  tags=["EstadosUsuario"]
)

@estadoUsuario.get("", response_model=list[EstadoUsuario])
def get_estados():
  return getAllEstadosUsuario()

@estadoUsuario.post("", response_model=Status)
def create_estado(estado: EstadoUsuarioIn):
  return createEstadoUsuario(estado)

@estadoUsuario.get("/{id}", response_model=EstadoUsuario)
def get_estado(id: int):
  return getEstadoUsuario(id)

@estadoUsuario.delete("/{id}", response_model=Status)
def delete_estado(id: int):
  return deleteEstadoUsuario(id)

@estadoUsuario.put("/{id}", response_model=Status)
def update_grupo(id: int, estado: EstadoUsuarioIn):
  return updateEstadoUsuario(id, estado)