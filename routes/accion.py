from fastapi import APIRouter
from schemas.accion import AccionIn, AccionStatus, AccionListStatus
from schemas.status import Status
from controller.accion import getAllAcciones, getAccionById, createAccion, updateAccion, deleteAccion
from utils.response import succes_response, error_response

accion = APIRouter(
  prefix="/acciones",
  tags=["Acciones"]
)

@accion.get("", response_model=AccionListStatus)
def get_acciones():
  result = getAllAcciones()
  if result:
    return succes_response(result)
  else:
    return error_response("SIN_REGISTROS")

@accion.post("", response_model=Status)
def create_accion(accion: AccionIn):
  result = createAccion(accion)
  if result:
    return succes_response()
  else:
    return error_response("NO_CREADO")

@accion.get("/{id}", response_model=AccionStatus)
def get_accion(id: int):
  result = getAccionById(id)
  if result:
    return succes_response(result)
  else:
    return error_response("NO_ENCONTRADO")

@accion.delete("/{id}", response_model=Status)
def delete_accion(id: int):
  result = deleteAccion(id)
  if result:
    return succes_response()
  else:
    return error_response("NO_ELIMINADO")

@accion.put("/{id}", response_model=Status)
def update_accion(id: int, accion: AccionIn):
  result = updateAccion(id, accion)
  if result:
    return succes_response()
  else:
    return error_response("NO_ACTUALIZADO")