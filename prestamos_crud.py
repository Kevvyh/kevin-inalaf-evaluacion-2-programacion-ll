from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select

from conexion import engine
from modelos import Libro, Usuario, Prestamo

def registrar_prestamo(libro_id, usuario_id, fecha, cantidad):
    if not fecha:
        print("La fecha no puede estar vacia.")
    if cantidad < 0:
        print("La cantidad debe ser mayor a 0.")

    with Session(engine) as session:
        libro = session.get(Libro, libro_id)
        usuario = session.get(Usuario, usuario_id)

        if not libro:
            raise ValueError(f"No se ha encontrado un libro con el id: {libro_id}")
        if libro.ejemplares_disponibles < 0:
            raise ValueError("No hay ejemplares disponibles para este libro.")

        if not usuario:
            raise ValueError(f"No se ha encontrado un usuario con el id: {usuario_id}")

        nuevo_prestamo = Prestamo(libro_id=libro_id, usuario_id=usuario_id, fecha=fecha, cantidad=cantidad)
        session.add(nuevo_prestamo)
        session.commit()
        print(f"El prestamo para el usuario: {usuario.nombre} para el libro {libro.titulo} ha sido registrado correctamente.")
        print(f"El id del prestamo es: {nuevo_prestamo.id}")
        return nuevo_prestamo.id


