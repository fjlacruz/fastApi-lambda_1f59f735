# Importación de la clase BaseModel desde Pydantic.
# BaseModel es utilizada para crear modelos de datos con validación automática y serialización.
from pydantic import BaseModel

# Definición del esquema de datos para la creación de un ítem utilizando Pydantic.
class ItemCreate(BaseModel):
    """
    Esquema utilizado para la creación de un nuevo ítem.
    
    Atributos:
        name (str): Nombre del ítem a crear.
        description (str): Descripción detallada del ítem a crear.
    """
    name: str  # Nombre del ítem que se va a crear. Es un campo requerido para la creación del ítem.
    description: str  # Descripción detallada del ítem que se va a crear. Es un campo requerido.

