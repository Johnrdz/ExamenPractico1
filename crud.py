# Importamos la collection de connection parameters
from connection_parameters import collection

#creamos el crud
def read_books(title= ""):
    if title != "":
        query = {"Titulo": title}
        document = collection.find_one(query)
        print(document)
    else:
        documents = collection.find()
        for document in documents:
            print(document)


def create_books(json_books):
    result = collection.insert_one(json_books)
    print(result.inserted_id)


def update_books(title, json_book_update):
    query = {"Titulo": title}
    new_values = {"$set": json_book_update}
    result = collection.update_one(query, new_values)
    print(result.modified_count)


def delete_books_by_name(title):
    result = collection.delete_one({"Titulo": title})
    print(result.deleted_count)