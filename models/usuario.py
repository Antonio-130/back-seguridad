from sqlalchemy import Table, Column, UniqueConstraint, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime
from config.db import meta, engine
from models.estado_usuario import estados_usuario

usuarios = Table("usuarios", meta,
  Column("id", Integer, primary_key=True, autoincrement=True),
  Column("nombre", String(50), nullable=False),
  Column("apellido", String(50), nullable=False),
  Column("username", String(20), nullable=False),
  Column("email", String(255), nullable=False),
  Column("clave", String(255), nullable=False),
  Column("estado", Integer, ForeignKey(estados_usuario.c.id, onupdate="CASCADE", ondelete="CASCADE")),
  Column("fecha_creacion", DateTime, nullable=False),
  UniqueConstraint("username", name="username_unique"),
  UniqueConstraint("email", name="email_unique")
)

meta.create_all(engine)