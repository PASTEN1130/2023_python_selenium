
"""
QA Minds Labs estaría necesitando de un sistema que permita administrar sus cursos.
En este sentido el sistema debe contar con la posibilidad de crear un  Curso, el cual tendrán un nombre,
cantidad de alumnos, un estado y cantidad de clases.
El sistema debe poder dar de alta un Curso.
El sistema debe permitir buscar un curso y poder modificar su estado (Ejemplo: de No Iniciado a Activo)
El sistema debe permitir mostrar TODOS los Cursos existentes, como también la posibilidad de mostrar toda la información del curso.
"""
def add_course(lst: list):
    print("=" * 80)
    print("Agregar nuevo curso:")
    print("=" * 80)
    nombre_cur = input("Ingrese Nombre del curso:")
    can_alumnos = input("Ingrese cantidad de alumnos:")
    estado = input("Ingrese el estado del curso:")
    can_clases = input("Ingrese la cantidad de clases:")

    nueva_entrada = {
        "nombre_cur": nombre_cur,
        "can_alumnos": can_alumnos,
        "estado": estado,
        "can_clases": can_clases,
    }
    lst.append(nueva_entrada)
    print(lst)

def search(lst: list):
    pass

def modify(lst: list):
    pass

libreria = {}

cursos = []

while True:
    action = input("Que accion deseas hacer? (ADD | SEARCH | MODIFY)")
    if action == "ADD":
        add_course(cursos)
    elif action == "SEARCH":
        search(cursos)
     elif action == "MODIFY":
        modify(cursos)
    else:
        print(f"Opcion invalida: {action}")