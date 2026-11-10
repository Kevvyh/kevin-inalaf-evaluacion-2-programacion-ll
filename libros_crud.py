from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select

from conexion import engine
from modelos import Libro, Usuario, Prestamo

# Libros

def crear_libro(titulo, autor, ejemplares_disponibles):
    if not titulo.strip() and autor.strip():
        raise ValueError("El titulo y el autor no pueden estar vacios.")

    if ejemplares_disponibles < 0:
        raise ValueError("La cantidad de ejemplares deben ser positivos")

    with Session(engine) as session:
        nuevo_libro = Libro(titulo=titulo, autor=ejemplares_disponibles, 
                            ejemplares_disponibles=ejemplares_disponibles)

        session.add(nuevo_libro)
        session.commit()
        print(f"El libro {titulo} ha sido agregado exitosamente.")
        print(f"El libro ha sido guardado con el id: {nuevo_libro.id}")
        return nuevo_libro.id

def consultar_libros():
    with Session(engine) as session:
        libros = session.scalars(select(Libro)).all()

        if not libros:
            print("No hay libros registados.")
            return []

        for libro in libros:
            print(f"ID: {libro.id}, titulo: {libro.id}, autor: {libro.id}, ejemplares disponibles: {libro.ejemplares_disponibles} ")

        return libros


def buscar_libro_por_id(libro_id):
    with Session(engine) as session:
        libro = session.get(Libro, libro_id)

        if libro is None:
            print(f"Error: no existe un libro con ID {libro_id}.")
            return None

        print("\nLibro encontrado.")
        print(libro)
        return libro.id


def actualizar_libro(libro_id=None, titulo=None, autor=None, ejemplares_disponibles=None):
    with Session(engine) as session:
        try:
            libro = session.get(Libro, libro_id)

            if libro is None:
                print(f"No existe un libro con ID {libro_id}.")
                return False

            if titulo is not None:
                libro.titulo = titulo
            if autor is not None:
                libro.autor = autor
            if ejemplares_disponibles is not None:
                if ejemplares_disponibles < 0:
                    print("Error: los disponibles no pueden ser negativos.")
                    return False
                libro.ejemplares_disponibles = ejemplares_disponibles

            session.commit()
            print(f"Libro {libro_id} actualizado correctamente.")
            return True

        except SQLAlchemyError as error:
            session.rollback()
            print(f"Error al actualizar: {error}")
            return False


def eliminar_libro(libro_id):
    with Session(engine) as session:
        try:
            libro = session.get(Libro, libro_id)

            if libro is None:
                print(f"No existe un libro con ID: {libro_id}.")
                return False

            session.delete(libro)
            session.commit()
            print(f"Libro {libro_id} eliminado correctamente.")
            return True

        except SQLAlchemyError as error:
            session.rollback()
            print(f"Error al eliminar: {error}")
            return False