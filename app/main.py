from fastapi import FastAPI
from .database import init_db
from .routers import empleados, proyectos, asignaciones

def create_app():
    app = FastAPI(title="PROYECTO_GESTION_RUTAS")
    app.include_router(empleados.router)
    app.include_router(proyectos.router)
    app.include_router(asignaciones.router)
    @app.on_event("startup")
    def on_start():
        init_db()
    return app

app = create_app()