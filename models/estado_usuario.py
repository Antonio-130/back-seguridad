from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

estados_usuario = Table("estados_usuario", meta,
  Column("id", Integer, autoincrement=True, primary_key=True),
  Column("nombre", String(30), nullable=False)
)

meta.create_all(engine)