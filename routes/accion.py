from fastapi import APIRouter
from schemas.accion import Accion, AccionIn
from schemas.status import Status
from controller.accion import getAllAcciones, getAccionById, createAccion, updateAccion, deleteAccion

accion = APIRouter(
  prefix="/acciones",
  tags=["Acciones"]
)

@accion.get("", response_model=list[Accion])
def get_acciones():
  return getAllAcciones()

@accion.post("", response_model=Status)
def create_accion(accion: AccionIn):
  return createAccion(accion)

@accion.get("/{id}", response_model=Accion)
def get_accion(id: int):
  return getAccionById(id)

@accion.delete("/{id}", response_model=Status)
def delete_accion(id: int):
  return deleteAccion(id)

@accion.put("/{id}", response_model=Status)
def update_accion(id: int, accion: AccionIn):
  return updateAccion(id, accion)