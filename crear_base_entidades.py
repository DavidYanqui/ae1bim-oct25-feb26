# crear_base_entidades.py
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from configuracion import Base, engine

class Institucion(Base):
    __tablename__ = "instituciones"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(120), nullable=False, unique=True)
    ciudad: Mapped[str] = mapped_column(String(80), nullable=False)
    pais: Mapped[str] = mapped_column(String(80), nullable=False)

    departamentos: Mapped[list["Departamento"]] = relationship(
        back_populates="institucion", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Institucion id={self.id} nombre={self.nombre!r}>"

class Departamento(Base):
    __tablename__ = "departamentos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    codigo: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    institucion_id: Mapped[int] = mapped_column(
        ForeignKey("instituciones.id", ondelete="CASCADE"), nullable=False
    )

    institucion: Mapped["Institucion"] = relationship(back_populates="departamentos")
    investigadores: Mapped[list["Investigador"]] = relationship(
        back_populates="departamento", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Departamento id={self.id} nombre={self.nombre!r} codigo={self.codigo!r}>"

class Investigador(Base):
    __tablename__ = "investigadores"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(80), nullable=False)
    apellido: Mapped[str] = mapped_column(String(80), nullable=False)
    email: Mapped[str] = mapped_column(String(120), nullable=False, unique=True)
    area_investigacion: Mapped[str] = mapped_column(String(120), nullable=False)
    departamento_id: Mapped[int] = mapped_column(
        ForeignKey("departamentos.id", ondelete="CASCADE"), nullable=False
    )

    departamento: Mapped["Departamento"] = relationship(back_populates="investigadores")
    publicaciones: Mapped[list["Publicacion"]] = relationship(
        back_populates="investigador", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Investigador id={self.id} {self.nombre} {self.apellido} email={self.email}>"

class Publicacion(Base):
    __tablename__ = "publicaciones"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(String(200), nullable=False)
    fecha_publicacion: Mapped[str] = mapped_column(String(10), nullable=False)
    doi: Mapped[str] = mapped_column(String(120), nullable=True, unique=True)
    tipo_publicacion: Mapped[str] = mapped_column(String(40), nullable=False)
    investigador_id: Mapped[int] = mapped_column(
        ForeignKey("investigadores.id", ondelete="CASCADE"), nullable=False
    )

    investigador: Mapped["Investigador"] = relationship(back_populates="publicaciones")

    def __repr__(self) -> str:
        return f"<Publicacion id={self.id} titulo={self.titulo!r} tipo={self.tipo_publicacion!r}>"

if __name__ == "__main__":
    # Crear las tablas
    Base.metadata.create_all(bind=engine)
    print("✅ Tablas creadas en investigacion.db")
