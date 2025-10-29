from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr, validator
from datetime import date

class EmpleadoCreate(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=100)
    cargo: str = Field(..., min_length=2, max_length=50)
    email: Optional[EmailStr] = None

class EmpleadoRead(EmpleadoCreate):
    id: int

class ProyectoCreate(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=100)
    descripcion: Optional[str] = Field(None, max_length=300)

class ProyectoRead(ProyectoCreate):
    id: int

class AsignacionCreate(BaseModel):
    empleado_id: int
    proyecto_id: int
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    rol: Optional[str] = Field("colaborador", min_length=3, max_length=50)

    @validator('fecha_fin')
    def check_dates(cls, v, values):
        if v and values.get('fecha_inicio') and v < values['fecha_inicio']:
            raise ValueError('fecha_fin no puede ser anterior a fecha_inicio')
        return v

class AsignacionRead(AsignacionCreate):
    id: int