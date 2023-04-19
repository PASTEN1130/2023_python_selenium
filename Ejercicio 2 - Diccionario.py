# Crear una lista vacía para almacenar las personas
personas = []

# Utilizar un bucle while para permitir al usuario ingresar la información de cada persona
while True:
    # Pedir al usuario que ingrese el nombre, la edad y la ciudad de residencia de la persona
    nombre = input("Ingrese el nombre de la persona: ")
    edad = input("Ingrese la edad de la persona: ")
    ciudad = input("Ingrese la ciudad de residencia de la persona: ")

    # Crear un diccionario con la información de la persona
    persona = {"nombre": nombre, "edad": edad, "ciudad": ciudad}

    # Agregar el diccionario de la persona a la lista de personas
    personas.append(persona)

    # Preguntar al usuario si desea ingresar la información de otra persona
    respuesta = input("¿Desea ingresar la información de otra persona? (s/n)")
    if respuesta.lower() != "s":
        break

# Mostrar la información completa de todas las personas ingresadas
for persona in personas:
    print()
    print("Nombre:", persona["nombre"])
    print("Edad:", persona["edad"])
    print("Ciudad de residencia:", persona["ciudad"])