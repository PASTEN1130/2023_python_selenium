"""
Construye un script que permita guardar los registros de un contacto telefónico en un archivo de texto de la siguiente forma:
nombre, apellido,numero

"""

CONTACTS = [
    {"name": "contact 1", "apellido": "apellido 1", "numero": "1", "empresa": "empresa1"},
    {"name": "contact 2", "apellido": "apellido 2", "numero": "2", "empresa": "empresa2"},
    {"name": "contact 3", "apellido": "apellido 3", "numero": "3", "empresa": "empresa3"}
]

# Guardar informacion de contactos en archivo de texto
DELIMITER = "###"
with open("contacts.txt", "w") as file:
    for contact in CONTACTS:
        file.write(f"{DELIMITER.join(contact.values())}\n")