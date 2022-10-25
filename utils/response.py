messages = {
  "SUCCESS": "success",
  "SIN_REGISTROS": "No se encontraron registros",
  "NO_ENCONTRADO": "Registro no encontrado",
  "NO_CREADO": "No se pudo crear el registro",
  "NO_ACTUALIZADO": "No se pudo actualizar el registro",
  "NO_ELIMINADO": "No se pudo eliminar el registro",
  "LOGIN_INCORRECTO": "Usuario o contraseña incorrectos",
  "SIN_AUTORIZACION": "Autorización no proporcionada",
  "SIN_TOKEN": "Token no proporcionado",
  "TOKEN_INVALIDO": "Token invalido",
  "TOKEN_EXPIRADO": "Token expirado",
  "SIN_PERMISOS": "No tiene permisos para realizar esta acción",
  "ERROR": "Error al procesar la solicitud"
}

def succes_response(data=None):
  if data:
    return {"status": messages["SUCCESS"], "data": data}
  else:
    return {"status": messages["SUCCESS"]}

def error_response(option):
  if option == "SIN_REGISTROS": return {"status": messages["SIN_REGISTROS"]}

  elif option == "NO_ENCONTRADO": return {"status": messages["NO_ENCONTRADO"]}

  elif option == "NO_CREADO": return {"status": messages["NO_CREADO"]}

  elif option == "NO_ACTUALIZADO": return {"status": messages["NO_ACTUALIZADO"]}

  elif option == "NO_ELIMINADO": return {"status": messages["NO_ELIMINADO"]}

  elif option == "LOGIN_INCORRECTO": return messages["LOGIN_INCORRECTO"]

  elif option == "SIN_AUTORIZACION": return messages["SIN_AUTORIZACION"]

  elif option == "SIN_TOKEN": return messages["SIN_TOKEN"]

  elif option == "TOKEN_INVALIDO": return messages["TOKEN_INVALIDO"]

  elif option == "TOKEN_EXPIRADO": return messages["TOKEN_EXPIRADO"]

  elif option == "SIN_PERMISOS": return messages["SIN_PERMISOS"]

  else: return {"status": messages["ERROR"]}