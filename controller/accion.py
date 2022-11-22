from config.db import session
from models.accion import acciones
from models.grupos_acciones import grupos_acciones
from fastapi import HTTPException, status

def getAllAcciones():
  session.begin()
  try:
    result = session.execute(acciones.select()).fetchall()
    return result
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener las acciones")
  finally:
    session.close()

def getAccionById(id):
  session.begin()
  try:
    result = session.execute(acciones.select().where(acciones.c.id == id)).fetchone()
    return result
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener la accion")
  finally:
    session.close()

def createAccion(accion):
  session.begin()
  try:
    session.execute(acciones.insert().values({"nombre": accion.nombre, "tag": accion.tag, "descripcion": accion.descripcion}))
    session.commit()
    return {'detail': 'Accion creada correctamente'}
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear la accion")
    session.rollback()
  finally:
    session.close()

def updateAccion(id, accion):
  session.begin()
  try:
    session.execute(acciones.update().where(acciones.c.id == id).values({"nombre": accion.nombre, "tag": accion.tag}))
    session.commit()
    return {'detail': 'Accion actualizada correctamente'}
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al actualizar la accion")
    session.rollback()
  finally:
    session.close()

def deleteAccion(id):
  session.begin()
  try:
    session.execute(acciones.delete().where(acciones.c.id == id))
    session.execute(grupos_acciones.delete().where(grupos_acciones.c.id_accion == id))
    session.commit()
    return {'detail': 'Accion eliminada correctamente'}
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al eliminar la accion")
    session.rollback()
  finally:
    session.close()