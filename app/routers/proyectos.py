from fastapi import APIRouter, Depends, status
from sqlmodel import select
from typing import List
from ..database import get_session
from ..schemas import ProyectoCreate, ProyectoRead
from ..models import Proyecto
from ..crud import get_proyecto, create_proyecto, update_proyecto, delete_proyecto

router = APIRouter(prefix="/proyectos", tags=["proyectos"])

@router.post("/", response_model=ProyectoRead, status_code=status.HTTP_201_CREATED)
def create(data: ProyectoCreate, session=Depends(get_session)):
    proyecto = Proyecto(**data.dict())
    return create_proyecto(session, proyecto)

@router.get("/", response_model=List[ProyectoRead])
def list_proyectos(q: str = None, session=Depends(get_session)):
    stmt = select(Proyecto)
    if q:
        stmt = stmt.where(Proyecto.nombre.contains(q))
    return session.exec(stmt).all()

@router.get("/{proyecto_id}", response_model=ProyectoRead)
def get_one(proyecto_id: int, session=Depends(get_session)):
    return get_proyecto(session, proyecto_id)

@router.put("/{proyecto_id}", response_model=ProyectoRead)
def update(proyecto_id: int, data: ProyectoCreate, session=Depends(get_session)):
    return update_proyecto(session, proyecto_id, data.dict())

@router.delete("/{proyecto_id}")
def delete(proyecto_id: int, session=Depends(get_session)):
    return delete_proyecto(session, proyecto_id)