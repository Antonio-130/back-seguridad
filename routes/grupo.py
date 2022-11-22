from fastapi import APIRouter, Depends
from schemas.grupo import Grupo, GrupoIn
from schemas.status import Status
from controller.grupo import getAllGrupos, getGrupoById, createGrupo, updateGrupo, deleteGrupo
from middleware.verifyTokenRoute import verify_token_header
from middleware.permission import hasPermission
from middleware.verifyTokenRoute import verify_token_header

grupo = APIRouter(
  prefix="/grupos",
  tags=["Grupos"],
  dependencies=[Depends(verify_token_header), Depends(hasPermission)]
)

@grupo.get("", response_model=list[Grupo])
def get_grupos():
  return getAllGrupos()

@grupo.post("", response_model=Status)
def create_grupo(grupo: GrupoIn):
  return createGrupo(grupo)

@grupo.get("/{id}", response_model=Grupo)
def get_grupo(id: int):
  return getGrupoById(id)

@grupo.delete("/{id}", response_model=Status)
def delete_grupo(id: int):
  return deleteGrupo(id)

@grupo.put("/{id}", response_model=Status)
def update_grupo(id: int, grupo: GrupoIn):
  return updateGrupo(id, grupo)