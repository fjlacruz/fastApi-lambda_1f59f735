# Importación de APIRouter desde FastAPI para definir un conjunto de rutas específicas relacionadas con ítems.
from fastapi import APIRouter
# Importación del modelo Item desde el módulo de modelos. Este modelo representa la estructura de un ítem en la base de datos.
from ..models.item import Item
# Importación del esquema ItemCreate desde el módulo de esquemas. Este esquema define los datos necesarios para crear un ítem.
from ..schemas.item import ItemCreate
# Crear una instancia de APIRouter para agrupar rutas relacionadas con ítems.
# Se define un prefijo "/items" para todas las rutas y se utiliza la etiqueta "items" para organizarlas en la documentación.
router = APIRouter(prefix="/items", tags=["items"])

# Definición de un endpoint para crear un nuevo ítem.
@router.post("/", response_model=Item)
async def create_item(item: ItemCreate):
    """
    Crea un nuevo ítem.

    Args:
        item (ItemCreate): Datos necesarios para crear un ítem. Este esquema valida la entrada proporcionada por el cliente.

    Returns:
        Item: Devuelve el ítem recién creado en formato JSON con un ID, nombre y descripción.
    """
    # Simulación de creación de un ítem, devolviendo un objeto de tipo Item con los datos proporcionados.
    return Item(id=1, name=item.name, description=item.description)

# Definición de un endpoint para obtener información de un ítem específico por su ID.
@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """
    Obtiene información de un ítem específico.

    Args:
        item_id (int): ID del ítem que se desea consultar.

    Returns:
        Item: Devuelve un objeto Item con los detalles del ítem solicitado.
    """
    # Simulación de recuperación de un ítem, devolviendo un objeto de tipo Item con datos de ejemplo.
    return Item(id=item_id, name="Sample Item", description="This is a sample item.")

