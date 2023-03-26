# Importamos crud
from crud import *
# Importamos basi_functions
from basic_functions import *

# Abrimos un while para crear el menu index
while True:
    try:
        # Creamos el menu
        print("Menu de opciones")
        print("1. Ver todos los libros")
        print("2. Buscar un libro")
        print("3. Agregar un libro")
        print("4. Modificar un libro")
        print("5. Eliminar un libro")
        print("6. Salir del sistema")
        option = input("Ingrese una opcion: ")

        # Creamos un bucle de las opciones del menu
        if option == "1":
            read_books()
        elif option == "2":
            title = str(input("Ingrese el titulo del libro a bucar: "))
            read_books(title)
        elif option == "3":
            book = create_json_books()
            create_books(book)
        elif option == "4":
            title = str(input("Ingrese el libros a modificar: "))
            book = (create_json_update())
            update_books(title, book)
        elif option == "5":
            title = str(input("Ingrese el libro a eliminar: "))
            delete_books_by_name(title)
        elif option == "6":
            print("Gracias por usar el sistema crack")
            break
        else:
            print("Opcion invalida. Ingrese una opcion valida.")
    except Exception as e:
        print("Se ha producido un error:", e)