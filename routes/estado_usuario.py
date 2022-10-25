from fastapi import APIRouter
from schemas.estado_usuario import EstadoUsuarioIn, EsatadoUsuarioStatus, EsatadoUsuarioListStatus
from schemas.status import Status
from controller.estado_usuario import getAllEstadosUsuario, getEstadoUsuario, createEstadoUsuario, updateEstadoUsuario, deleteEstadoUsuario
from utils.response import succes_response, error_response

estadoUsuario = APIRouter(
  prefix="/estadosUsuario",
  tags=["EstadosUsuario"]
)

@estadoUsuario.get("", response_model=EsatadoUsuarioListStatus)
def get_estados():
  result = getAllEstadosUsuario()
  if result:
    return succes_response(result)
  else:
    return error_response("SIN_REGISTROS")

@estadoUsuario.post("", response_model=Status)
def create_estado(estado: EstadoUsuarioIn):
  result = createEstadoUsuario(estado)
  if result:
    return succes_response()
  else:
    return error_response("NO_CREADO")

@estadoUsuario.get("/{id}", response_model=EsatadoUsuarioStatus)
def get_estado(id: int):
  result = getEstadoUsuario(id)
  if result:
    return succes_response(result)
  else:
    return error_response("NO_ENCONTRADO")

@estadoUsuario.delete("/{id}", response_model=Status)
def delete_estado(id: int):
  result = deleteEstadoUsuario(id)
  if result:
    return succes_response()
  else:
    return error_response("NO_ELIMINADO")

@estadoUsuario.put("/{id}", response_model=Status)
def update_grupo(id: int, estado: EstadoUsuarioIn):
  result = updateEstadoUsuario(id, estado)
  if result.rowcount:
    return succes_response()
  else:
    return error_response("NO_ACTUALIZADO")