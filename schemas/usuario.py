from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class GrupoUsuario (BaseModel):
  id: int
  nombre: str

class EstadoUsuario (BaseModel):
  id: int
  nombre: str

class Usuario (BaseModel):
  id: int
  nombre: str
  apellido: str
  username: str
  email: str
  estado: EstadoUsuario
  fecha_creacion: datetime
  grupos: list[GrupoUsuario]

class UsuarioIn (BaseModel):
  nombre: str
  apellido: str
  username: str
  email: str
  clave: str
  estado: int
  grupos: list[int]

class UsuarioUpdate (BaseModel):
  nombre: Optional[str]
  apellido: Optional[str]
  username: Optional[str]
  email: Optional[str]
  estado: Optional[int]
  grupos: Optional[list[int]]

class UsuarioLogin (BaseModel):
  username: Optional[str]
  email: Optional[str]
  clave: str

class UsuarioChangeClave (BaseModel):
  id: int
  clave: str
  newClave: str