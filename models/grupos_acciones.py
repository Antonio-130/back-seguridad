from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime
from config.db import meta, engine
from models.accion import acciones
from models.grupo import grupos

grupos_acciones = Table("grupos_acciones", meta,
  Column("id_grupo", Integer,
    ForeignKey(grupos.c.id, onupdate="CASCADE", ondelete="CASCADE"),
    primary_key=True),
  Column("id_accion", Integer,
    ForeignKey(acciones.c.id, onupdate="CASCADE", ondelete="CASCADE"),
    primary_key=True)
)

meta.create_all(engine)