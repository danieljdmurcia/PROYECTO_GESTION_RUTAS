from sqlmodel import create_engine, SQLModel, Session
from typing import Generator
import os

DB_URL = os.getenv("DATABASE_URL", "sqlite:///./db.sqlite3")
engine = create_engine(DB_URL, echo=False)

def init_db():
    from .models import Empleado, Proyecto, Asignacion
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session