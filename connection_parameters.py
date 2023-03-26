# Importamos la base de datos con Pymongo
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["library"]
collection = db["books"]

print(collection)