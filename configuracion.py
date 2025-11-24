# configuracion.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Archivo local SQLite (se creará en la carpeta del proyecto)
DATABASE_URL = "sqlite:///investigacion.db"

# Engine (con echo=True si quieres ver SQL en consola)
engine = create_engine(DATABASE_URL, echo=False, future=True)

# Base declarativa
class Base(DeclarativeBase):
    pass

# Session factory
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
