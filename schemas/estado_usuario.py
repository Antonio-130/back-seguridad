from pydantic import BaseModel
from typing import Optional

class EstadoUsuario (BaseModel):
  id: Optional[int]
  nombre: str

class EstadoUsuarioIn (BaseModel):
  nombre: str

class EsatadoUsuarioStatus (BaseModel):
  status: str
  data: Optional[EstadoUsuario]

class EsatadoUsuarioListStatus (BaseModel):
  status: str
  data: Optional[list[EstadoUsuario]]