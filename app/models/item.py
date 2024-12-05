# Importación de la clase BaseModel desde Pydantic.
# BaseModel es utilizada para crear modelos de datos que incluyen validación automática y serialización.
from pydantic import BaseModel

# Definición del modelo de datos para un ítem utilizando Pydantic.
class Item(BaseModel):
    """
    Representa un ítem con sus atributos principales.
    
    Atributos:
        id (int): Identificador único del ítem.
        name (str): Nombre del ítem.
        description (str): Descripción detallada del ítem.
    """
    id: int  # Identificador único del ítem, utilizado para diferenciarlo de otros ítems.
    name: str  # Nombre del ítem, puede ser utilizado para su identificación o en listados.
    description: str  # Descripción detallada que proporciona información adicional sobre el ítem.
