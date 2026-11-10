from libros_crud import consultar_libros, crear_libro, actualizar_libro, buscar_libro_por_id, eliminar_libro 
from usuarios_crud import listar_usuarios, registrar_usuarios
from prestamos_crud import registrar_prestamo
from crear_tablas import crear_tablas


def menu():
    while True:
        print("\nMenu de registro y consultas")
        print("1. Registrar libro")
        print("2. Consultar libros")
        print("3. Consultar libros por id")
        print("4. Actualizar libros")
        print("5. Eliminar libros")
        print("6. Listar usuarios")
        print("7. Registrar usuarios")
        print("8. Registrar prestamo")
        print("0. Salir")

        try:
            opcion = int(input("Ingrese una opcion del menu: "))
        except ValueError:
            print("La opcion ingresada no es valida.")
            continue

        if opcion == 1:
            try:
                titulo = input("Ingrese el titulo del libro: ")
                autor = input("Ingrese el autor del libro: ")
                ejemplares_disponibles = input("Ingrese los ejemplares disponibles: ")
                crear_libro(titulo, autor, ejemplares_disponibles)
            except ValueError as error:
                print(error)


        elif opcion == 0:
            print("Saliendo del sistema.")
            break

        else:
            print("Opcion no valida. Intente otra vez.")


if __name__ == "__main__":
    crear_tablas()
    menu()