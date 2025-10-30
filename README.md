 Sistema de Gestión de Rutas

API REST desarrollada con FastAPI y SQLModel para la administración de empleados, proyectos y asignaciones dentro de una empresa de transporte.

El sistema permite registrar empleados, crear proyectos, asignar tareas y aplicar validaciones automáticas de datos con Pydantic, además de mantener relaciones entre entidades y ofrecer documentación interactiva.

 Descripción del Proyecto

El proyecto Gestión de Rutas tiene como objetivo construir una API REST que gestione la información de empleados y proyectos de forma eficiente, aplicando buenas prácticas de arquitectura, validaciones y relaciones entre tablas con SQLModel.

 Funcionalidades Principales

 CRUD completo de empleados

 CRUD completo de proyectos

 Relación N:M entre empleados y proyectos

Validaciones de datos mediante Pydantic

 Reglas de negocio integradas:

No se puede eliminar un gerente activo.

No se pueden crear proyectos duplicados.

Un empleado no puede ser asignado dos veces al mismo proyecto.

 Filtros en endpoints GET (por nombre o ID)

Documentación automática con Swagger (/docs)

 Tecnologías Utilizadas

Python 3.12+

FastAPI

SQLModel

SQLite

Uvicorn

Pydantic

 Instalación y Ejecución
1️ Clonar el repositorio
git clone https://github.com/danieljdmurcia/PROYECTO_GESTION_RUTAS-3.git
cd PROYECTO_GESTION_RUTAS-3

2️ Crear y activar el entorno virtual

Windows

python -m venv venv
venv\Scripts\activate


Linux / macOS

python3 -m venv venv
source venv/bin/activate

3️ Instalar dependencias
pip install -r requirements.txt

4️ Ejecutar el servidor
uvicorn app.main:app --reload

5️ Acceder a la documentación

Swagger UI: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc

 Estructura del Proyecto
PROYECTO_GESTION_RUTAS/
│
├── app/
│   ├── main.py               # Punto de entrada del servidor
│   ├── database.py           # Conexión y sesión con la base de datos
│   ├── models.py             # Modelos SQLModel (Empleado, Proyecto, Asignación)
│   ├── schemas.py            # Esquemas Pydantic para validaciones
│   ├── crud.py               # Lógica CRUD y reglas de negocio
│   ├── routers/
│   │   ├── empleados.py      # Endpoints de empleados
│   │   ├── proyectos.py      # Endpoints de proyectos
│   │   └── asignaciones.py   # Endpoints de asignaciones
│   └── __init__.py
│
├── requirements.txt          # Dependencias del proyecto
├── .gitignore                # Archivos y carpetas a ignorar en Git
└── README.md                 # Documentación del proyecto

 Mapa de Endpoints
 Empleados
Método	Endpoint	Descripción
POST	/empleados/	Crear empleado
GET	/empleados/	Listar empleados (filtro: ?q=nombre)
GET	/empleados/{id}	Obtener empleado por ID
PUT	/empleados/{id}	Actualizar empleado
DELETE	/empleados/{id}	Eliminar empleado
 Proyectos
Método	Endpoint	Descripción
POST	/proyectos/	Crear proyecto
GET	/proyectos/	Listar proyectos (filtro: ?q=nombre)
GET	/proyectos/{id}	Obtener proyecto por ID
PUT	/proyectos/{id}	Actualizar proyecto
DELETE	/proyectos/{id}	Eliminar proyecto
🔗 Asignaciones
Método	Endpoint	Descripción
POST	/asignaciones/	Crear asignación (valida duplicados)
GET	/asignaciones/	Listar asignaciones (filtros: empleado_id, proyecto_id)
GET	/asignaciones/{id}	Obtener asignación por ID
DELETE	/asignaciones/{id}	Eliminar asignación
🧾 Ejemplos de Cuerpos JSON
Crear Empleado
{
  "nombre": "Juan Pérez",
  "cargo": "Conductor",
  "estado": "Activo"
}

Crear Proyecto
{
  "nombre": "Ruta Norte",
  "descripcion": "Proyecto para la gestión de rutas del norte",
  "fecha_inicio": "2025-11-01",
  "fecha_fin": "2026-02-15",
  "gerente_id": 1
}

Crear Asignación
{
  "empleado_id": 2,
  "proyecto_id": 1,
  "rol": "Coordinador de ruta"
}

 Reglas de Negocio y Validaciones

 No se puede eliminar un gerente activo.

 No se pueden crear proyectos duplicados.

 Un empleado no puede ser asignado dos veces al mismo proyecto.

 Filtros disponibles en endpoints GET para buscar por nombre o ID.

 Validaciones automáticas de datos con Pydantic.

 Notas

Documentación Swagger disponible en /docs

Variable de entorno por defecto:

DATABASE_URL=sqlite:///./db.sqlite3

Autor

Daniel Murcia
Proyecto académico: Sistema de Gestión de Rutas con FastAPI y SQLModel
📦 Repositorio GitHub: https://github.com/danieljdmurcia/PROYECTO_GESTION_RUTAS-3
