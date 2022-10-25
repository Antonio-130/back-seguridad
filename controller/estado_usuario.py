from config.db import session
from models.estado_usuario import estados_usuario
from models.usuario import usuarios
from fastapi import HTTPException, status

def getAllEstadosUsuario():
  session.begin()
  try:
    result = session.execute(estados_usuario.select()).fetchall()
    session.commit()
    return result
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener los estados de usuario")
    session.rollback()
  finally:
    session.close()

def getEstadoUsuario(id):
  session.begin()
  try:
    result = session.execute(estados_usuario.select().where(estados_usuario.c.id == id)).fetchone()
    session.commit()
    return result
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener el estado de usuario")
    session.rollback()
  finally:
    session.close()

def createEstadoUsuario(estado_usuario):
  session.begin()
  try:
    session.execute(estados_usuario.insert().values({"nombre": estado_usuario.nombre}))
    session.commit()
    return True
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear el estado de usuario")
    session.rollback()
  finally:
    session.close()

def updateEstadoUsuario(id, estado_usuario):
  session.begin()
  try:
    session.execute(estados_usuario.update().where(estados_usuario.c.id == id).values({"nombre": estado_usuario.nombre}))
    session.commit()
    return True
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al actualizar el estado de usuario")
    session.rollback()
  finally:
    session.close()

def deleteEstadoUsuario(id):
  session.begin()
  try:
    session.execute(estados_usuario.delete().where(estados_usuario.c.id == id))
    session.excetute(usuarios.update().where(usuarios.c.estado == id).values({"estado": null}))
    session.commit()
    return True
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al eliminar el estado de usuario")
    session.rollback()
  finally:
    session.close()