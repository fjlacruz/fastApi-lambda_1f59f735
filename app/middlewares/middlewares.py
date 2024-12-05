import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time

        print(f"Request =======>>>> {request.method} {request.url.path} - Time ======>>>> {process_time:.2f}s")
        
        # Agregar un encabezado adicional con el tiempo de procesamiento
        response.headers["X-Process-Time"] = f"{process_time:.2f}s"
        return response
