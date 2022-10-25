from pydantic import BaseModel
from typing import Optional

class Accion (BaseModel):
  id: Optional[int]
  nombre: str
  tag: str

class AccionIn (BaseModel):
  nombre: str
  tag: str

class AccionStatus (BaseModel):
  status: str
  data: Optional[Accion]

class AccionListStatus (BaseModel):
  status: str
  data: Optional[list[Accion]]