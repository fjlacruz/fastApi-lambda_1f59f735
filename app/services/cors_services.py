from typing import List

def get_allowed_origins() -> List[str]:
    """
    Retorna una lista de orígenes permitidos para configurar CORS.
    Esta lista puede ser obtenida de una base de datos, archivo de configuración, 
    variable de entorno, o incluso un servicio remoto.

    Returns:
        List[str]: Lista de URLs permitidas.
    """
    # Ejemplo: Obtener los orígenes desde variables de entorno
    import os

    origins_env = os.getenv("ALLOWED_ORIGINS", "")  # Orígenes separados por comas
    if origins_env:
        return [origin.strip() for origin in origins_env.split(",")]

    # Lista por defecto en caso de no configurarlo mediante variables de entorno
    return [
        "http://localhost",
        "http://localhost:3000",
        "http://127.0.0.1:5500",
        "https://example.com",
    ]
