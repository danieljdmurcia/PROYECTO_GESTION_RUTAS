# Proyecto de Gestión de Rutas

Sistema desarrollado con **FastAPI** y **SQLModel** para la administración de empleados, proyectos y asignaciones dentro de una empresa de transporte.  
Permite registrar empleados, crear proyectos, asignar tareas y aplicar validaciones automáticas de datos.

---

##  Descripción del Proyecto

El proyecto **Gestión de Rutas** tiene como objetivo crear una API REST que gestione la información de empleados y proyectos, aplicando buenas prácticas de arquitectura, validaciones con Pydantic y relaciones entre tablas usando SQLModel.

###  Funcionalidades principales

-  CRUD completo de empleados  
-  CRUD completo de proyectos  
-  Relación **N:M** entre empleados y proyectos  
-  Validaciones de datos con Pydantic  
-  Lógica de negocio integrada:
  - No se puede eliminar un gerente activo
  - No se pueden crear proyectos duplicados
  - Un empleado no puede ser asignado dos veces al mismo proyecto  
-  Filtros en endpoints GET
- Documentación automática con Swagger (`/docs`)

---

## Estructura del Proyecto

│
├── app/
│ ├──    main.py # Punto de entrada del servidor
│ ├──    database.py # Conexión y sesión con la base de datos
│ ├──    models.py # Modelos SQLModel (Empleado, Proyecto, Relación)
│ ├──    schemas.py # Esquemas Pydantic para validaciones
│ ├──    crud.py # Lógica CRUD y reglas de negocio
│ ├──     routers/
│ │ ├──     empleados.py # Rutas para empleados
│ │ ├──     proyectos.py # Rutas para proyectos
│ │ └──     asignaciones.py # Rutas para relaciones
│ └──    init.py
│
├──    requirements.txt # Dependencias del proyecto
├──    .gitignore # Archivos y carpetas a ignorar en Git
├──    README.md # Este archivo
└──    venv/ # (opcional) entorno virtual

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
