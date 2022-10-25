from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from routes.usuario import usuario
from routes.grupo import grupo
from routes.estado_usuario import estadoUsuario
from routes.accion import accion
from routes.auth import auth

app = FastAPI(
    title="API Seguridad",
    description="API for security management",
    openapi_tags=[
        {"name": "Usuarios", "description": "Operaciones de usuarios"},
        {"name": "Grupos", "description": "Operaciones de grupos"},
        {"name": "EstadosUsuario", "description": "Operaciones de estados de usuario"},
        {"name": "Acciones", "description": "Operaciones sobre acciones"},
        {"name": "Login", "description": "Iniciar sesión"},
    ]
)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuario)
app.include_router(grupo)
app.include_router(estadoUsuario)
app.include_router(accion)
app.include_router(auth)