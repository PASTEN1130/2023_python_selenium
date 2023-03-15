"""
Construye un script que permita guardar los registros de un contacto en un archivo json de la siguiente cuyos datos son:
 nombre, apellido, email y numero de telefono.
"""
import json

CONTACTS = {
    "contacts": [
        {"nombre": "Roberto", "apellido": "Juarez", "telefono": "55447896", "mail": "r.juarez@gmail.com"}
    ]
}
# Guardar informacion con json

with open("directory.json", "w") as file:
    json.dump(CONTACTS, file)

with open("directory.json") as file:
    data = json.load(file)
    print(type(data))
    for contact in data["contacts"]:
        print(CONTACTS)