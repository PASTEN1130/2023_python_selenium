from random import choice

jugadores = ["CHITA", "TARZAN", "JANE", "PATRICIO"]
print(jugadores)

equipoA = []

jugadorA = choice(jugadores)
print(jugadorA)
equipoA.append(jugadorA)
jugadores.remove(jugadorA)
print("jugadores restantes:",jugadores)