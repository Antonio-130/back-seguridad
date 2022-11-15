from config.db import session
from models.grupo import grupos
from models.grupos_acciones import grupos_acciones
from models.usuarios_grupos import usuarios_grupos
from models.accion import acciones
from sqlalchemy import select, join
from fastapi import HTTPException, status

def getAllGrupos():
  session.begin()
  try:
    result = session.execute(grupos.select()).fetchall()
    lista_grupos = []
    for grupo in result:
      lista_grupos.append({
        "id": grupo[0],
        "nombre": grupo[1],
        "descripcion": grupo[2],
        "acciones": session.execute(select([grupos_acciones.c.id_accion, acciones.c.nombre, acciones.c.tag, acciones.c.descripcion])
        .join(acciones, grupos_acciones.c.id_accion == acciones.c.id)
        .where(grupos_acciones.c.id_grupo == grupo[0])).fetchall()
      })
    return lista_grupos
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener los grupos")
  finally:
    session.close()

def getGrupoById(id):
  session.begin()
  try:
    result = session.execute(grupos.select().where(grupos.c.id == id)).fetchone()
    grupo = {
      "id": result[0],
      "nombre": result[1],
      "descripcion": result[2],
      "acciones": session.execute(
        select([grupos_acciones.c.id_accion, acciones.c.nombre, acciones.c.tag, acciones.c.descripcion])
        .join(acciones, grupos_acciones.c.id_accion == acciones.c.id)
        .where(grupos_acciones.c.id_grupo == result[0])
      ).fetchall()
    }
    return grupo
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener el grupo")
  finally:
    session.close()

def createGrupo(grupo):
  session.begin()
  try:
    result = session.execute(grupos.insert().values({"nombre": grupo.nombre, "descripcion": grupo.descripcion}))
    if grupo.acciones:
      for accion in grupo.acciones:
        session.execute(grupos_acciones.insert().values({"id_grupo": result.inserted_primary_key[0], "id_accion": accion}))
    session.commit()
    return True
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear el grupo")
    session.rollback()
  finally:
    session.close()

def updateGrupo(id, grupo):
  session.begin()
  try:
    session.execute(grupos.update().where(grupos.c.id == id).values(nombre=grupo.nombre, descripcion=grupo.descripcion))
    session.execute(grupos_acciones.delete().where(grupos_acciones.c.id_grupo == id))
    for accion in grupo.acciones:
      session.execute(grupos_acciones.insert().values({"id_grupo": id, "id_accion": accion}))
    session.commit()
    return True
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al actualizar el grupo")
    session.rollback()
  finally:
    session.close()

def deleteGrupo(id):
  session.begin()
  try:
    session.execute(grupos.delete().where(grupos.c.id == id))
    session.execute(grupos_acciones.delete().where(grupos_acciones.c.id_grupo == id))
    session.execute(usuarios_grupos.delete().where(usuarios_grupos.c.id_grupo == id))
    session.commit()
    return True
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al eliminar el grupo")
    session.rollback()
  finally:
    session.close()

def getAccionesByGrupo(id):
  session.begin()
  try:
    result = session.execute(
      select([grupos_acciones.c.id_accion, acciones.c.nombre])
      .join(acciones, grupos_acciones.c.id_accion == acciones.c.id)
      .where(grupos_acciones.c.id_grupo == id)
    ).fetchall()
    return result
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener las acciones del grupo")
  finally:
    session.close()