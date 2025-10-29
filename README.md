# PROYECTO_GESTION_RUTAS

Proyecto de ejemplo para la asignación de empleados a proyectos usando FastAPI y SQLModel.

## Requisitos
- Python 3.10+ recommended

## Instalación rápida (desde la carpeta del proyecto)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoints principales
- `POST /empleados/` crear empleado
- `GET /empleados/` listar empleados (filtro: ?q=nombre)
- `GET /empleados/{id}` obtener empleado
- `PUT /empleados/{id}` actualizar empleado
- `DELETE /empleados/{id}` eliminar empleado

- `POST /proyectos/` crear proyecto
- `GET /proyectos/` listar proyectos (filtro: ?q=nombre)
- `GET /proyectos/{id}` obtener proyecto
- `PUT /proyectos/{id}` actualizar proyecto
- `DELETE /proyectos/{id}` eliminar proyecto

- `POST /asignaciones/` crear asignación (valida duplicados)
- `GET /asignaciones/` listar asignaciones (filtros: empleado_id, proyecto_id)
- `GET /asignaciones/{id}` obtener asignación
- `DELETE /asignaciones/{id}` eliminar asignación

## Notas
- Swagger UI disponible en `/docs`
- Variables de entorno: `DATABASE_URL` (por defecto usa sqlite `sqlite:///./db.sqlite3`)