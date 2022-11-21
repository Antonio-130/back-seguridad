from pydantic import BaseModel
from typing import Optional

class AccionGrupo (BaseModel):
  id_accion: int
  nombre: str
  tag: str
  descripcion: str

class Grupo (BaseModel):
  id: Optional[int]
  nombre: str
  descripcion: str
  acciones: list[AccionGrupo]

class GrupoIn (BaseModel):
  nombre: str
  descripcion: str
  acciones: list[int]