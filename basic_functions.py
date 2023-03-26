# Creamos las basic functions para el crud
def create_json_books():
    title = input("Titulo: ")
    book_autor = input("Autor: ")
    language = input("Idioma: ")
    gender = input("Genero: ")
    publisher = input("Editorial: ")
    year_publish = input("Fecha: ")
    country = input("Pais: ")

    books = {
        "Titulo": title,
        "Autor": book_autor,
        "Idioma": language,
        "Genero": gender,
        "Editorial": publisher,
        "Fecha": year_publish,
        "Pais": country
    }
    return books


def create_json_update():
    print("Menu de opciones")
    print("1. Modificar todos los datos del libro")
    print("2. Modificar un dato del elemento del libro")
    option = input("Ingrese una opcion: ")
    if option == "1":
        title = input("Titulo: ")
        book_autor = input("Autor: ")
        language = input("Idioma: ")
        gender = input("Genero: ")
        publisher = input("Editorial: ")
        year_publish = input("Fecha: ")
        country = input("Pais: ")

        book = {
            "Titulo": title,
            "Autor": book_autor,
            "Idioma": language,
            "Genero": gender,
            "Editorial": publisher,
            "Fecha": year_publish,
            "Pais": country
        }
        return book

    elif option == "2":
        indice = input("Ingrese el indice: ")
        valor = input("Ingrese el valor a modificar: ")
        book = {indice: valor}
        return book