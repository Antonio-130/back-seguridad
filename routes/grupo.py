from fastapi import APIRouter, Depends
from schemas.grupo import GrupoIn, GrupoStatus, GrupoListStatus
from schemas.status import Status
from controller.grupo import getAllGrupos, getGrupoById, createGrupo, updateGrupo, deleteGrupo
from utils.response import succes_response, error_response
from middleware.verifyTokenRoute import verify_token_header
from middleware.permission import hasPermission

grupo = APIRouter(
  prefix="/grupos",
  tags=["Grupos"],
  dependencies=[Depends(verify_token_header), Depends(hasPermission)]
)

@grupo.get("", response_model=GrupoListStatus)
def get_grupos():
  result = getAllGrupos()
  if result:
    return succes_response(result)
  else:
    return error_response("SIN_REGISTROS")

@grupo.post("", response_model=Status)
def create_grupo(grupo: GrupoIn):
  result = createGrupo(grupo)
  if result:
    return succes_response()
  else:
    return error_response("NO_CREADO")

@grupo.get("/{id}", response_model=GrupoStatus)
def get_grupo(id: int):
  result = getGrupoById(id)
  if result:
    return succes_response(result)
  else:
    return error_response("NO_ENCONTRADO")

@grupo.delete("/{id}", response_model=Status)
def delete_grupo(id: int):
  result = deleteGrupo(id)
  if result:
    return succes_response()
  else:
    return error_response("NO_ELIMINADO")

@grupo.put("/{id}", response_model=Status)
def update_grupo(id: int, grupo: GrupoIn):
  result = updateGrupo(id, grupo)
  if result:
    return succes_response()
  else:
    return error_response("NO_ACTUALIZADO")