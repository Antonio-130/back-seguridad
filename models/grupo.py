from sqlalchemy import Table, Column, UniqueConstraint
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

grupos = Table("grupos", meta,
  Column("id", Integer, autoincrement=True, primary_key=True),
  Column("nombre", String(30), nullable=False),
  Column("descripcion", String(255), nullable=False),
  UniqueConstraint("nombre", name="uq_grupo_nombre")
)

meta.create_all(engine)