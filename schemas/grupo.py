from pydantic import BaseModel
from typing import Optional

class AccionGrupo (BaseModel):
  id_accion: int
  nombre: str

class Grupo (BaseModel):
  id: Optional[int]
  nombre: str
  descripcion: str
  acciones: list[AccionGrupo]

class GrupoIn (BaseModel):
  nombre: str
  descripcion: str
  acciones: list[int]

class GrupoStatus (BaseModel):
  status: str
  data: Optional[Grupo]

class GrupoListStatus (BaseModel):
  status: str
  data: Optional[list[Grupo]]