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

class UsuarioStatus (BaseModel):
  status: str
  data: Optional[Usuario]

class UsuarioListStatus (BaseModel):
  status: str
  data: Optional[list[Usuario]]

class UsuarioLogin (BaseModel):
  username: Optional[str]
  email: Optional[str]
  clave: str

class ChangeClave (BaseModel):
  token: str
  clave: str
  newClave: str