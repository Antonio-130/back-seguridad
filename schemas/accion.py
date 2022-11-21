from pydantic import BaseModel
from typing import Optional

class Accion (BaseModel):
  id: Optional[int]
  nombre: str
  tag: str
  descripcion: str

class AccionIn (BaseModel):
  nombre: str
  tag: str
  descripcion: str