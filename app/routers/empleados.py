from fastapi import APIRouter, Depends, status
from sqlmodel import select
from typing import List
from ..database import get_session
from ..schemas import EmpleadoCreate, EmpleadoRead
from ..models import Empleado
from ..crud import get_empleado, create_empleado, update_empleado, delete_empleado

router = APIRouter(prefix="/empleados", tags=["empleados"])

@router.post("/", response_model=EmpleadoRead, status_code=status.HTTP_201_CREATED)
def create(data: EmpleadoCreate, session=Depends(get_session)):
    empleado = Empleado(**data.dict())
    return create_empleado(session, empleado)

@router.get("/", response_model=List[EmpleadoRead])
def list_empleados(q: str = None, session=Depends(get_session)):
    stmt = select(Empleado)
    if q:
        stmt = stmt.where(Empleado.nombre.contains(q))
    return session.exec(stmt).all()

@router.get("/{empleado_id}", response_model=EmpleadoRead)
def get_one(empleado_id: int, session=Depends(get_session)):
    return get_empleado(session, empleado_id)

@router.put("/{empleado_id}", response_model=EmpleadoRead)
def update(empleado_id: int, data: EmpleadoCreate, session=Depends(get_session)):
    return update_empleado(session, empleado_id, data.dict())

@router.delete("/{empleado_id}")
def delete(empleado_id: int, session=Depends(get_session)):
    return delete_empleado(session, empleado_id)