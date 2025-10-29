from fastapi import HTTPException, status
from sqlmodel import Session, select
from .models import Empleado, Proyecto, Asignacion

def get_empleado(session: Session, empleado_id: int):
    empleado = session.get(Empleado, empleado_id)
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return empleado

def create_empleado(session: Session, empleado: Empleado):
    # prevent duplicate email
    if empleado.email:
        q = select(Empleado).where(Empleado.email == empleado.email)
        if session.exec(q).first():
            raise HTTPException(status_code=409, detail="Email ya registrado")
    session.add(empleado)
    session.commit()
    session.refresh(empleado)
    return empleado

def update_empleado(session: Session, empleado_id: int, data: dict):
    empleado = get_empleado(session, empleado_id)
    for key, value in data.items():
        setattr(empleado, key, value)
    session.add(empleado)
    session.commit()
    session.refresh(empleado)
    return empleado

def delete_empleado(session: Session, empleado_id: int):
    empleado = get_empleado(session, empleado_id)
    session.delete(empleado)
    session.commit()
    return {"ok": True}

# proyectos
def get_proyecto(session: Session, proyecto_id: int):
    proyecto = session.get(Proyecto, proyecto_id)
    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return proyecto

def create_proyecto(session: Session, proyecto: Proyecto):
    q = select(Proyecto).where(Proyecto.nombre == proyecto.nombre)
    if session.exec(q).first():
        raise HTTPException(status_code=409, detail="Proyecto con ese nombre ya existe")
    session.add(proyecto)
    session.commit()
    session.refresh(proyecto)
    return proyecto

def update_proyecto(session: Session, proyecto_id: int, data: dict):
    proyecto = get_proyecto(session, proyecto_id)
    for key, value in data.items():
        setattr(proyecto, key, value)
    session.add(proyecto)
    session.commit()
    session.refresh(proyecto)
    return proyecto

def delete_proyecto(session: Session, proyecto_id: int):
    proyecto = get_proyecto(session, proyecto_id)
    session.delete(proyecto)
    session.commit()
    return {"ok": True}

# asignaciones
def create_asignacion(session: Session, asignacion: Asignacion):
    # business rules: no duplicate assignment for same empleado-project
    q = select(Asignacion).where(Asignacion.empleado_id == asignacion.empleado_id, Asignacion.proyecto_id == asignacion.proyecto_id)
    if session.exec(q).first():
        raise HTTPException(status_code=409, detail="Asignación duplicada")
    # check empleado and proyecto exist
    if not session.get(Empleado, asignacion.empleado_id):
        raise HTTPException(status_code=404, detail="Empleado no existe")
    if not session.get(Proyecto, asignacion.proyecto_id):
        raise HTTPException(status_code=404, detail="Proyecto no existe")
    session.add(asignacion)
    session.commit()
    session.refresh(asignacion)
    return asignacion

def get_asignacion(session: Session, asignacion_id: int):
    asignacion = session.get(Asignacion, asignacion_id)
    if not asignacion:
        raise HTTPException(status_code=404, detail="Asignación no encontrada")
    return asignacion

def delete_asignacion(session: Session, asignacion_id: int):
    asignacion = get_asignacion(session, asignacion_id)
    session.delete(asignacion)
    session.commit()
    return {"ok": True}