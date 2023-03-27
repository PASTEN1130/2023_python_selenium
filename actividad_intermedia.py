
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
    print("AGREGAR CURSO")
    print("=" * 80)
    name = input("NOMBRE DEL CURSO?")
    total_student = input("TOTAL DE ALUMNOS?")
    total_sessions = input("TOTAL DE CLASES?")
    status = input(f"Status? {' | '.join(VALID_STATUS) }")
    if status in VALID_STATUS:
        course = {
            "name": name,
            "totalStudent": total_student,
            "totalSessions": total_sessions,
            "status": status
        }
        lst.append(course)
        print("Curso agregado")
        show_course(course)
    else:
        print(f"Estado no valido: {status}")


def search_course(lst: list):
    print("=" * 80)
    print("BUSCAR CURSO")
    print("=" * 80)
    target = input("Nombre?")
    found = [course for course in lst if course["name"] == target]
    if found and len(found) > 0:
        print(f"HAZ ENCONTRADO EL CURSO!")
        show_course(found[0])
        update = input(f"QUIERES ACTUALIZAR? (YES|NO)")
        if update == "YES":
            update_course(found[0])
    else:
        print("Curso no encontrado")


def show_courses(lst: list):

    names = [course["name"] for course in lst]
    print(f"CURSOS: {names}")
    show_details = input("DESEAS VER LOS DETALLES ? (YES|NO)")
    if show_details == "YES":
        for course in lst:
            show_course(course)


def update_course(course: dict):
    print("=" * 80)
    print("ACTUALIZAR CURSO")
    print("=" * 80)
    status = input(f"Status? {' | '.join(VALID_STATUS) }")
    if status in VALID_STATUS:
        course["status"] = status
        print("CURSO ACTUALIZADO")
        show_course(course)
    else:
        print(f"Estado no valido: {status}")


def show_course(course: dict):

    print(f"\t--->[{course['name']}]: Status = {course['status']}")


def close(lst: list):

    print("CLOSING...")
    print(f"Cursos: {lst}")
    exit(0)


VALID_STATUS = ("No Activo", "Activo", "Suspendido")
COURSES = []
MENU_OPTIONS = {
    "ADD": add_course,
    "UPDATE": search_course,
    "SHOW_ALL": show_courses,
    "CLOSE": close
}

while True:
    for option, method in MENU_OPTIONS.items():
        action = input(f"Que accion deases realizar: {' | '.join(MENU_OPTIONS.keys())}\n")
        if action in MENU_OPTIONS.keys():
            MENU_OPTIONS[action](COURSES)
        else:
            print(f"Action not supported: {action}")