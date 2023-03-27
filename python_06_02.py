"""
Escribe un script que dado el día,mes y año de nacimiento de una persona determine lo siguiente:
•	Cuántos años tiene.
•	Si en lo que va del año ya cumplio o no.
•	Determinar a qué generación pertenece:
•	La generación silenciosa. Nacidos entre 1920 y 1939.
•	Los baby boomers. Nacidos entre 1940 y 1959.
•	Generación X. Nacidos entre 1960 y 1979.
•	Generación Y o millennials. Nacidos entre 1980 y 1989.
•	Generación Z. Nacidos entre 1990 en adelante.

"""
from datetime import datetime
from birthday import delta


PARSER_FMT = "%Y-%m-%d"
CURRENT_DATE = datetime.now()
SILENT_GEN_END = 1939
BOOMERS_GEN_END = 1959
GEN_X_END = 1979
GEN_Y_END = 1989


birthday_str = input(f"Fecha de nacimiento ({PARSER_FMT})?")


birthday = datetime.strptime(birthday_str, PARSER_FMT)
delta = delta.relativedelta(CURRENT_DATE, birthday)
print(f"Edad: {delta.years} años, {delta.months} meses, {delta.days} dias, {delta.minutes} minutes, {delta.seconds} segundos")

birthday_celebrated = (birthday.month >= CURRENT_DATE.month) and (birthday.day >= CURRENT_DATE.day)
print(f"Cumplio años: {birthday_celebrated}")

if birthday.year <= SILENT_GEN_END:
    print("Generacion silencionasa")
elif birthday.year <= BOOMERS_GEN_END:
    print("Baby boomers")
elif birthday.year <= GEN_X_END:
    print("Generacion X")
elif birthday.year <= GEN_Y_END:
    print("Generacion Y o millennials")
else:
    print("Generacion Z")