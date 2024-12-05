# Importación de la clase BaseModel desde Pydantic.
# BaseModel se usa para crear modelos de datos que incluyen validación automática y serialización.
from pydantic import BaseModel

# Definición del esquema de datos para la creación de un usuario utilizando Pydantic.
class UserCreate(BaseModel):
    """
    Esquema utilizado para la creación de un nuevo usuario.
    
    Atributos:
        username (str): Nombre de usuario del nuevo usuario a crear.
        email (str): Dirección de correo electrónico del nuevo usuario a crear.
    """
    username: str  # Nombre de usuario que será utilizado para identificar al nuevo usuario.
    email: str  # Dirección de correo electrónico del nuevo usuario, utilizado para la autenticación y notificaciones.
