"""
QA Minds Labs estaría necesitando de una agenda que permita guardar a sus alumnos del curso de Python.
En este sentido el sistema debe contar con la posibilidad de crear un  Alumno, las cuales tendrán un nombre, apellido,
un mail y un estado. Los Alumnos pueden tener los estados de: Activo, Mora, Retirado Egresado y  Certificado.
Los Alumnos por defecto se crearán en estado Activo.
El sistema debe poder dar de alta un Alumno.
El sistema debe permitir buscar un alumno y poder modificar su estado (Ejemplo: de Activo a Egresado)
El sistema debe permitir mostrar TODOS los Alumnos existentes, como también la posibilidad de mostrar
todos los alumnos por un estado definido.
"""
def add_alumnos(lst: list):
    """Agrega un nuevo alumno al sistema.

    Ejemplo de lista de cursos:
    [{
        "name": name,
        "totalStudent": students,
        "totalSessions": classes,
        "status": status
    }]

    :param lst: Lista actual de cursos
    :return: None
    """
    print("AGREGAR ALUMNO")
    name = input("Nombre del Alumno?")
    apellido = input("Apellido")
    mail = input("e-mail")
    status = input(f"Status? {' | '.join(VALID_STATUS) }")
    if status in VALID_STATUS:
        alumnos = {
            "name": name,
            "Apellido": apellido,
            "mail": mail,
            "status": status
        }
        lst.append(alumnos)
        print("Alumno agregado")
        show_alumnos(alumnos)
    else:
        print(f"Alumno no válido: {status}")


def search_alumnos(lst: list):
    
    print("BUSCAR ALUMNO")
    target = input("Nombre del Alumno?")
    found = [alumnos for alumnos in lst if alumnos["name"] == target]
    if found and len(found) > 0:
        print(f"Alumno Encontrado!")
        show_alunos(found[0])
        update = input(f"Desea actualizar estatus? (YES|NO)")
        if update == "YES":
            update_course(found[0])
    else:
        print("Estatus no encontrado")


def show_alumnos(lst: list):
    """

    :param lst:
    :return:
    """
    names = [alumnos["name"] for alumnos in lst]
    print(f"Alumnos: {names}")
    show_details = input("Mostrar informacion del Alumno? (YES|NO)")
    if show_details == "YES":
        for alumnos in lst:
            show_alumnos(alumnos)


def update_alumnos(alumnos: dict):
    print("ACTUALIZAR CURSO")
    status = input(f"Status? {' | '.join(VALID_STATUS) }")
    if status in VALID_STATUS:
        alumnos["status"] = alumnos
        print("Estatus actualizado!")
        show_alumnos(Alumnos)
    else:
        print(f"Estado no valido: {status}")


def show_alumnos(course: dict):
    """

    :param course:
    :return:
    """
    print(f"\t--->[{alumnos['name']}]: apellido = {alumnos['apellido']}, mail = {alumnos['mail']}, Status = {alumnos['status']}")


def close(lst: list):
    """Salir del programa

    Ejemplo de lista:
    [{
        "name": name,
        "totalStudent": students,
        "totalSessions": classes,
        "status": status
    }]

    :param lst: Lista cursos, cada curso esta representado por un diccionario.
    :return: None
    """
    print("CLOSING...")
    print(f"Alumnos: {lst}")
    exit(0)


VALID_STATUS = ("Activo", "Mora", "Retirado", "Egresado", "Certificado")
ALUMNOS = []
MENU_OPTIONS = {
    "ADD": add_alumnos,
    "UPDATE": search_alumnos,
    "SHOW_ALL": show_alumnos,
    "CLOSE": close
}

while True:
    for option, method in MENU_OPTIONS.items():
        action = input(f"Que accion deases realizar: {' | '.join(MENU_OPTIONS.keys())}\n")
        if action in MENU_OPTIONS.keys():
            MENU_OPTIONS[action](ALUMNOS)
        else:
            print(f"Action not supported: {action}")
