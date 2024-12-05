from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.middlewares.middlewares import LoggingMiddleware
from .routers import items, users
from app.services.cors_services import get_allowed_origins  

app = FastAPI(
    title="API de Gestión de Ítems",
    description="Una API para gestionar ítems en un inventario.",
    version="1.0.0",
    contact={
        "name": "Soporte",
        "url": "https://example.com/contact",
        "email": "soporte@example.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)

# Obtener configuración de orígenes permitidos desde un servicio
origins = get_allowed_origins()

# Agregar el middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Lista de orígenes permitidos obtenidos dinámicamente
    allow_credentials=True,  # Permitir envío de cookies/credenciales
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)

app.add_middleware(LoggingMiddleware)

app.include_router(items.router)
app.include_router(users.router)