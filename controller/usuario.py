from config.db import session
from models.usuario import usuarios
from models.estado_usuario import estados_usuario
from models.grupo import grupos
from models.usuarios_grupos import usuarios_grupos
from models.grupos_acciones import grupos_acciones
from models.accion import acciones
from sqlalchemy import select, join
from utils.password import encrypt_password, compare_password
from datetime import datetime
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

def getAllUsuarios():
  session.begin()
  try:
    result = session.execute(usuarios.select()).fetchall()
    lista_usuarios = []
    for usuario in result:
      lista_usuarios.append({
        "id": usuario[0],
        "nombre": usuario[1],
        "apellido": usuario[2],
        "username": usuario[3],
        "email": usuario[4],
        "estado": session.execute(estados_usuario.select().where(estados_usuario.c.id == usuario[6])).fetchone(),
        "fecha_creacion": usuario[7],
        "grupos": session.execute(select([grupos.c.id, grupos.c.nombre])
          .join(usuarios_grupos, usuarios_grupos.c.id_grupo == grupos.c.id)
          .where(usuarios_grupos.c.id_usuario == usuario[0])).fetchall()
      })
    return lista_usuarios
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener los usuarios")
  finally:
    session.close()

def getUsuarioById(id):
  session.begin()
  try:
    result = session.execute(usuarios.select().where(usuarios.c.id == id)).fetchone()
    usuario = {
      "id": result[0],
      "nombre": result[1],
      "apellido": result[2],
      "username": result[3],
      "email": result[4],
      "estado": session.execute(estados_usuario.select().where(estados_usuario.c.id == result[6])).fetchone(),
      "fecha_creacion": result[7],
      "grupos": session.execute(select([grupos.c.id, grupos.c.nombre])
      .join(usuarios_grupos, usuarios_grupos.c.id_grupo == grupos.c.id)
      .where(usuarios_grupos.c.id_usuario == result[0])).fetchall()
    }
    return usuario
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener el usuario")
  finally:
    session.close()

def getUsuarioByUsername(username):
  session.begin()
  try:
    usuario = session.execute(usuarios.select().where(usuarios.c.username == username)).fetchone()
    return usuario
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener el usuario")
  finally:
    session.close()

def getUsuarioByEmail(email):
  session.begin()
  try:
    usuario = session.execute(usuarios.select().where(usuarios.c.email == email)).fetchone()
    return usuario
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener el usuario")
  finally:
    session.close()

def createUsuario(usuario):
  session.begin()
  try:
    new_usuario = {
      "nombre": usuario.nombre,
      "apellido": usuario.apellido,
      "username": usuario.username,
      "email": usuario.email,
      "clave": encrypt_password(usuario.clave),
      "estado": usuario.estado,
      "fecha_creacion": datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    }
    result = session.execute(usuarios.insert().values(new_usuario))
    if usuario.grupos:
      for grupo in usuario.grupos:
        session.execute(usuarios_grupos.insert().values({"id_usuario": result.inserted_primary_key[0], "id_grupo": grupo}))
    session.commit()
    return {'detail': 'Usuario creado correctamente'}
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear el usuario")
    session.rollback()
  finally:
    session.close()

def updateUsuario(id, usuario):
  session.begin()
  usuario_to_update = {
    "nombre": usuario.nombre,
    "apellido": usuario.apellido,
    "username": usuario.username,
    "email": usuario.email,
    "estado": usuario.estado,
  }
  try:
    session.execute(usuarios.update().where(usuarios.c.id == id).values(usuario_to_update))
    session.execute(usuarios_grupos.delete().where(usuarios_grupos.c.id_usuario == id))
    if usuario.grupos:
      for grupo in usuario.grupos:
        session.execute(usuarios_grupos.insert().values({"id_usuario": id, "id_grupo": grupo}))
    session.commit()
    return {'detail': 'Usuario actualizado correctamente'}
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al actualizar el usuario")
    session.rollback()
  finally:
    session.close()

def deleteUsuario(id):
  session.begin()
  try:
    session.execute(usuarios.delete().where(usuarios.c.id == id))
    session.execute(usuarios_grupos.delete().where(usuarios_grupos.c.id_usuario == id))
    session.commit()
    return {'detail': 'Usuario eliminado correctamente'}
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al eliminar el usuario")
    session.rollback()
  finally:
    session.close()

def getAllAccionesOfUsuario(id):
  session.begin()
  try:
    acciones_usuario = session.execute(select([acciones.c.nombre, acciones.c.tag])
    .join(grupos_acciones, grupos_acciones.c.id_accion == acciones.c.id)
    .join(usuarios_grupos, usuarios_grupos.c.id_grupo == grupos_acciones.c.id_grupo)
    .where(usuarios_grupos.c.id_usuario == id)).fetchall()
    lista_acciones = []
    for accion in acciones_usuario:
      lista_acciones.append({
        "nombre": accion[0],
        "tag": accion[1]
      })
    return lista_acciones
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener las acciones del usuario")
  finally:
    session.close()

def usuarioHasAccion(nombre_accion, id_usuario):
  session.begin()
  try:
    accion = session.execute(select([acciones.c.id])
    .join(grupos_acciones, grupos_acciones.c.id_accion == acciones.c.id)
    .join(usuarios_grupos, usuarios_grupos.c.id_grupo == grupos_acciones.c.id_grupo)
    .where(usuarios_grupos.c.id_usuario == id_usuario)
    .where(acciones.c.nombre == nombre_accion)).fetchone()
    if accion:
      return True
    else:
      return False
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="EL usuario no tiene la accion")
  finally:
    session.close()

def changeClave(id, clave, newClave):
  session.begin()
  try:
    usuario = session.execute(usuarios.select().where(usuarios.c.id == id)).fetchone()
    if not usuario:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    validate = bool(compare_password(clave, usuario["clave"]))
    if validate:
      session.execute(usuarios.update().where(usuarios.c.id == id).values({"clave": encrypt_password(newClave)}))
      session.commit()
      return {'detail': 'Clave actualizada correctamente'}
    else:
      return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={'detail': 'Clave incorrecta'})
  except:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al cambiar la clave")
    session.rollback()
  finally:
    session.close()