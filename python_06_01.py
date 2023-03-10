"""""
Entregar siguientes ejercicios como python_06_01.py:
Escribe un script que dado la edad de una persona y su altura pueda determinar
si la misma puede o no subirse en la montaña rusa “Push-Pull”,
dado que se debe ser mayor a 14 años y tener una altura no menor de 1,62.
 El script debe ser capaz de informar si puede o no subirse y en el caso de que no,
 porque razon (Si por edad, por tamaño u ambas)
 """

edad = input ("Cual es tu edad")
altura = input ("Cual es tu algura")
edad = "int"
altura = "float"

if edad > 14 and altura > 1.60:
    print (f"Puedes subir a la montaña Push Pull {edad} ,{altura}")
"""""
else:
    print(f"no puedes subir")
    
"""""