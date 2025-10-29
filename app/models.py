from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from datetime import date

class Empleado(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True, max_length=100)
    cargo: str = Field(max_length=50)
    email: Optional[str] = Field(default=None, index=True)

    asignaciones: list["Asignacion"] = Relationship(back_populates="empleado")

class Proyecto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True, max_length=100)
    descripcion: Optional[str] = Field(default=None, max_length=300)

    asignaciones: list["Asignacion"] = Relationship(back_populates="proyecto")

class Asignacion(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    empleado_id: int = Field(foreign_key="empleado.id")
    proyecto_id: int = Field(foreign_key="proyecto.id")
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    rol: Optional[str] = Field(default="colaborador", max_length=50)

    empleado: Optional[Empleado] = Relationship(back_populates="asignaciones")
    proyecto: Optional[Proyecto] = Relationship(back_populates="asignaciones")