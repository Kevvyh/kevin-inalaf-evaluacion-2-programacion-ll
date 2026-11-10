from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select

from conexion import engine
from modelos import Libro, Usuario, Prestamo

def registrar_usuarios(nombre, correo):
    if not nombre.strip() and correo.strip():
        raise ValueError("El nombre y el correo son necesarios.")

    with Session(engine) as session:
        try:
            existente = session.scalars(
                select(Usuario).where(Usuario.correo == correo)
            ).first()

            if existente is not None:
                print(f"Error: el correo '{correo}' ya está registrado.")
                return None

            usuario = Usuario(nombre=nombre, correo=correo)
            session.add(usuario)
            session.commit()
            print(f"El usuario ha sido registrado con el ID: {usuario.id}.")
            return usuario.id

        except SQLAlchemyError:
            session.rollback()
            print(f"El correo: {correo} ya está registrado.")
            return None
        except SQLAlchemyError as error:
            session.rollback()
            print(f"Error al registrar el usuario: {error}")
            return None

def listar_usuarios():
    with Session(engine) as session:
        usuarios = session.scalars(select(Usuario)).all()

        if not usuarios:
            print("No hay usuarios registrados.")
            return []

        for usuario in usuarios:
            print(f"ID: {usuario.id}, nombre: {usuario.nombre}, correo: {usuario.correo}")

        return usuarios