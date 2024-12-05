# Importación de la clase BaseModel desde Pydantic.
# BaseModel proporciona las herramientas necesarias para la validación y serialización de datos en Python.
from pydantic import BaseModel

# Definición del modelo de datos para un usuario utilizando Pydantic.
class User(BaseModel):
    """
    Representa un usuario con atributos básicos.
    
    Atributos:
        id (int): Identificador único del usuario.
        username (str): Nombre de usuario.
        email (str): Dirección de correo electrónico del usuario.
    """
    id: int  # Identificador único del usuario, normalmente asignado por la base de datos.
    username: str  # Nombre de usuario, utilizado para identificación en la aplicación.
    email: str  # Dirección de correo electrónico, debe cumplir con el formato de correo válido.

