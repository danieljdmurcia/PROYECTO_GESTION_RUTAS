from fastapi import APIRouter, Depends, status
from sqlmodel import select
from typing import List
from ..database import get_session
from ..schemas import AsignacionCreate, AsignacionRead
from ..models import Asignacion
from ..crud import create_asignacion, get_asignacion, delete_asignacion

router = APIRouter(prefix="/asignaciones", tags=["asignaciones"])

@router.post("/", response_model=AsignacionRead, status_code=status.HTTP_201_CREATED)
def create(data: AsignacionCreate, session=Depends(get_session)):
    asignacion = Asignacion(**data.dict())
    return create_asignacion(session, asignacion)

@router.get("/", response_model=List[AsignacionRead])
def list_asignaciones(empleado_id: int = None, proyecto_id: int = None, session=Depends(get_session)):
    stmt = select(Asignacion)
    if empleado_id:
        stmt = stmt.where(Asignacion.empleado_id == empleado_id)
    if proyecto_id:
        stmt = stmt.where(Asignacion.proyecto_id == proyecto_id)
    return session.exec(stmt).all()

@router.get("/{asignacion_id}", response_model=AsignacionRead)
def get_one(asignacion_id: int, session=Depends(get_session)):
    return get_asignacion(session, asignacion_id)

@router.delete("/{asignacion_id}")
def delete(asignacion_id: int, session=Depends(get_session)):
    return delete_asignacion(session, asignacion_id)