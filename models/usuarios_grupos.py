from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime
from config.db import meta, engine
from models.usuario import usuarios
from models.grupo import grupos

usuarios_grupos = Table("usuarios_grupos", meta,
  Column("id_usuario", Integer,
    ForeignKey(usuarios.c.id, onupdate="CASCADE", ondelete="CASCADE"),
    primary_key=True),
  Column("id_grupo", Integer,
    ForeignKey(grupos.c.id, onupdate="CASCADE", ondelete="CASCADE"),
    primary_key=True)
)

meta.create_all(engine)