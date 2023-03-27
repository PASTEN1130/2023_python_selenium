"""""
Entregar siguientes ejercicios como python_06_01.py:
Escribe un script que dado la edad de una persona y su altura pueda determinar
si la misma puede o no subirse en la montaña rusa “Push-Pull”,
dado que se debe ser mayor a 14 años y tener una altura no menor de 1,62.
 El script debe ser capaz de informar si puede o no subirse y en el caso de que no,
 porque razon (Si por edad, por tamaño u ambas)
 """
edad_persona= input ("Cual es tu edad: ")
edad=int(edad_persona)
altura_persona = input ("Cual es tu altura: ")
edad=float(altura_persona)


if edad_persona >= 14 and altura_persona >= 1.62:

    print (f"Puedes subir a la montaña Push Pull {edad} ,{altura}")

else:

    print(f"No puedes subir a la montaña Push pull porque tu {edad} y tu {altura} no esta permitida ")
