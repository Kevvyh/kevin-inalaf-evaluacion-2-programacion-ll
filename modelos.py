from sqlalchemy import String, CheckConstraint, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship

class Base(DeclarativeBase):
    pass

# entidades

class Libro(Base):

    __tablename__ = "libro" 
    __table_args__ = (
        CheckConstraint("ejemplares_disponibles >= 0", name="ejemplares_positivos")
    )

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    titulo: Mapped[str] = mapped_column(nullable=False)
    autor: Mapped[str] = mapped_column(nullable=False)
    ejemplares_disponibles: Mapped[int] = mapped_column(nullable=False)

class Usuario(Base):

    __tablename__ = "usuario"
    __table_args__ = (
        
    )

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    nombre: Mapped[int] = mapped_column(nullable=False)
    correo: Mapped[int] = mapped_column(nullable=False, unique=True)


class Prestamo(Base):

    __tablename__ = "prestamo"
    __table_args__ = (
        CheckConstraint("cantidad > 0", name="cantidad_mayor_a_cero")
    )

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    libro_id: Mapped[int] = mapped_column(ForeignKey("libro.id"), nullable=False)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False)
    fecha: Mapped[str] = mapped_column(String(10), nullable=False)
    cantidad: Mapped[int] = mapped_column (nullable=False)
    estado: Mapped[int] = mapped_column(nullable=False)
