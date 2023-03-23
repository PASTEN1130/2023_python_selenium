VALID_RAZA = ("TERRAN", "ZERG", "PROTOSS")

def imprimir_header(header: str):
    print(f"{40 * '='} {header} {40 * '='}")

##########################################################################################
# ACCIONES DEL SISTEMA
##########################################################################################
def alta():
    imprimir_header("ALTA")
    nombre_jugador = input("Nombre del Jugador:")
    mail = input("mail:")
    raza = input("Raza:")
    estado=input("Estado del Jugador:")
    jugador = jugador(nombre_jugador, mail, estado, raza[str, str, str])
    JUGADORES.append(jugador)
    print(f"Alumno registrado: {jugador}")

##########################################################################################
# CONTROL PRINCIPAL
##########################################################################################
JUGADORES = []

MENU = {
    "Alta": alta,

}

OPTIONS = ' | '.join(MENU.keys())  # alta

while True:
    action = input(f"Que accion deases realizar? {OPTIONS}\n")
    if action in MENU.keys():
        MENU[action]()
    else:
        print(f"Accion not soportada: {action}")