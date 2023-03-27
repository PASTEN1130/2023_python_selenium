def imprimir_header(header: str):
    print(f"{40 * '='} {header} {40 * '='}")
##########################################################################################
# GENERAR PARTIDAS ALEATORIAS
##########################################################################################
from random import choice

JUGADORES = []
print(jugador)

partida_A = []

jugador = choice(jugador)
print(jugador)
partida_A.append(jugador)
jugadores.remove(jugador)
print("jugadores restantes:",jugador)



def imprimir_header(header: str):
    print(f"{40 * '='} {header} {40 * '='}")
##########################################################################################
# IMPORTAR ARCHIVO
##########################################################################################
import json

JUGADORES = {
    "JUGADORES": [
        {"nombre_jugador", "mail", "estado", "raza"}
    ]
}
with open("directory.json", "w") as file:
    json.dump(JUGADORES, file)

with open("directory.json") as file:
    data = json.load(file)
    print(type(data))
    for contact in data["contacts"]:
        print(JUGADORES)


raza = ["TERRAN", "ZERG", "PROTOSS"]
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
    print(f"Jugador Registrado: {jugador}")

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