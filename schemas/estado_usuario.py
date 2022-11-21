from pydantic import BaseModel
from typing import Optional

class EstadoUsuario (BaseModel):
  id: Optional[int]
  nombre: str

class EstadoUsuarioIn (BaseModel):
  nombre: str