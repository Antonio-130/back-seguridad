from sqlalchemy import Table, Column, UniqueConstraint
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

acciones = Table("acciones", meta,
  Column("id", Integer, autoincrement=True, primary_key=True),
  Column("nombre", String(30), nullable=False),
  Column("tag", String(30), nullable=False),
  UniqueConstraint("nombre", name="uq_accion_nombre")
)

meta.create_all(engine)