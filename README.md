Sistema de Gestión de Proyectos:

API REST desarrollada con FastAPI y SQLModel para la gestión integral de empleados, proyectos y asignaciones dentro de una empresa consultora.
El sistema permite registrar empleados, crear proyectos, asignar roles y mantener un control eficiente de los recursos humanos y técnicos.

Descripción:

Una empresa consultora necesita gestionar sus proyectos y empleados.
Este sistema fue diseñado para ofrecer una solución ágil que permita:

Registrar empleados (nombre, especialidad, salario, estado).

Registrar proyectos (nombre, descripción, presupuesto, estado).

Asignar empleados a proyectos (relación N:M).

Definir un gerente responsable por cada proyecto (relación 1:N).

Consultar los proyectos de un empleado y los empleados de un proyecto.

Aplicar reglas de negocio automáticas que mantienen la integridad del sistema.

Características Principales

CRUD completo de Empleados, Proyectos y Asignaciones.

Relación 1:N → Un gerente puede dirigir varios proyectos.

Relación N:M → Un empleado puede trabajar en muchos proyectos.

Validaciones automáticas con Pydantic.

Lógica de negocio integrada:

No se puede eliminar un gerente activo con proyectos asignados.

No se pueden crear proyectos duplicados (nombre único).

Un empleado no puede ser asignado dos veces al mismo proyecto.

Filtros personalizados en endpoints (por nombre, estado o especialidad).

Documentación automática con Swagger UI (/docs).

Lógica de Negocio:

Un empleado gerente no puede eliminarse si tiene proyectos asignados.

Los proyectos no pueden tener nombres repetidos.

Un empleado no puede estar asignado dos veces al mismo proyecto.

Tecnologías Utilizadas:

Python 3.12+

FastAPI

SQLModel / SQLAlchemy

SQLite

Uvicorn

Pydantic

Instalación y Ejecución
1. Clonar el repositorio
git clone https://github.com/danieljdmurcia/PROYECTO_GESTION_RUTAS.git
cd PROYECTO_GESTION_RUTAS

3. Crear y activar entorno virtual

En Windows:

python -m venv venv
venv\Scripts\activate


En Linux / macOS:

python3 -m venv venv
source venv/bin/activate

3. Instalar dependencias
pip install -r requirements.txt

4. Ejecutar el servidor
uvicorn app.main:app --reload

5. Acceder a la documentación

Swagger UI → http://127.0.0.1:8000/docs

Redoc → http://127.0.0.1:8000/redoc

Estructura del Proyecto:
PROYECTO_GESTION_RUTAS/
│
├── app/
│   ├── main.py                # Punto de entrada de la aplicación
│   ├── database.py            # Conexión y creación de tablas
│   ├── models.py              # Modelos SQLModel (Empleado, Proyecto, Asignación)
│   ├── schemas.py             # Esquemas Pydantic
│   ├── crud.py                # Funciones CRUD y reglas de negocio
│   ├── routers/
│   │   ├── empleados.py       # Endpoints de empleados
│   │   ├── proyectos.py       # Endpoints de proyectos
│   │   └── asignaciones.py    # Endpoints de asignaciones
│   └── __init__.py
│
├── requirements.txt           # Dependencias del proyecto
├── README.md                  # Documentación
└── venv/                      # Entorno virtual (opcional)

Mapa de Endpoints
Empleados
Método	Endpoint	Descripción
POST	/empleados/	Crear un nuevo empleado
GET	/empleados/	Listar empleados (filtros: nombre, especialidad, estado)
GET	/empleados/{id}	Obtener información de un empleado
PUT	/empleados/{id}	Actualizar información de un empleado
DELETE	/empleados/{id}	Eliminar un empleado (si no es gerente activo)
Proyectos
Método	Endpoint	Descripción
POST	/proyectos/	Crear un nuevo proyecto
GET	/proyectos/	Listar proyectos (filtros: nombre, estado, presupuesto)
GET	/proyectos/{id}	Obtener información de un proyecto
PUT	/proyectos/{id}	Actualizar datos de un proyecto
DELETE	/proyectos/{id}	Eliminar un proyecto (validando dependencias)
Asignaciones
Método	Endpoint	Descripción
POST	/asignaciones/	Asignar un empleado a un proyecto
GET	/asignaciones/	Listar todas las asignaciones (filtros: empleado, proyecto)
GET	/asignaciones/{id}	Consultar una asignación
DELETE	/asignaciones/{id}	Eliminar una asignación
Ejemplos de Cuerpos JSON
Crear Empleado
{
  "nombre": "Laura Gómez",
  "especialidad": "Backend",
  "salario": 3500000,
  "estado": "Activo"
}

Crear Proyecto
{
  "nombre": "Sistema de Control Vehicular",
  "descripcion": "Proyecto para monitorear rutas y conductores",
  "presupuesto": 12000000,
  "estado": "Activo",
  "id_gerente": 1
}

Crear Asignación
{
  "id_proyecto": 1,
  "id_empleado": 3,
  "rol": "Desarrollador",
  "fecha_asignacion": "2025-10-30"
}

Estado del Proyecto

CRUD completo y funcional

Reglas de negocio operativas

Validaciones de datos activas

Documentación automática lista

Base de datos SQLite en funcionamiento

Autor

Daniel Murcia
Proyecto académico desarrollado para la asignatura Desarrollo de Software
Repositorio GitHub: PROYECTO_GESTION_RUTAS
