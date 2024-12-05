# Importación de APIRouter desde FastAPI para definir rutas específicas en un módulo separado.
from fastapi import APIRouter
# Importación del modelo User desde el módulo de modelos. Este modelo representa la estructura de un usuario en la base de datos.
from ..models.user import User
# Importación del esquema UserCreate desde el módulo de esquemas. Este esquema define los datos necesarios para crear un usuario.
from ..schemas.user import UserCreate

# Crear una instancia de APIRouter que agrupa rutas relacionadas con usuarios.
# Se define un prefijo "/users" para todas las rutas y se etiquetan con "Users." para organizarlas en la documentación.
router = APIRouter(prefix="/users", tags=["Users."])

# Definición de un endpoint para crear un usuario.
@router.post("/", response_model=User)
async def create_user(user: UserCreate):
    """
    Crea un nuevo usuario.

    Args:
        user (UserCreate): Datos necesarios para crear un usuario. Este esquema valida 
        la entrada proporcionada por el cliente.

    Returns:
        User: Devuelve el usuario recién creado en formato JSON con un ID, nombre de usuario 
        y correo electrónico.
    """
    # Simulación de creación de usuario, devolviendo un objeto de tipo User.
    return User(id=1, username=user.username, email=user.email)

# Definición de un endpoint para obtener información de un usuario específico por su ID.
@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    """
    Obtiene información de un usuario específico.

    Args:
        user_id (int): ID del usuario que se desea consultar.

    Returns:
        User: Devuelve un objeto User con los detalles del usuario solicitado.
    """
    # Simulación de recuperación de usuario, devolviendo un objeto de tipo User con un nombre 
    # de usuario y correo electrónico de ejemplo.
    return User(id=user_id, username="sample_user", email="sample@example.com")
