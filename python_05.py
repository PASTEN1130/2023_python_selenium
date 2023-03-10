def sumar (num_a: int, num_b: int):
    """

    :param num_a:
    :param num_b:
    :return:
    """
    print (f"La suma es: {num_a} + {num_b}")
    return num_a + num_b

numero_1 = input("Numero A:")
numero_2 = input ("Numero B:")
numero_1 = int(numero_1)
numero_2 = int(numero_2)

print(f"Resultado suma: {sumar (numero_1, numero_2)}")

print(80 * "-")

def restar (num_b: int, num_c: int):
    print (f"La resta es: {num_b} - {num_c}")
    return num_b - num_c

numero_3= input("Numero A:")
numero_4 = input ("Numero B:")
numero_3 = int(numero_3)
numero_4 = int(numero_4)

print(f"Resultado resta: {restar (numero_3, numero_4)}")

print(80 * "-")

def multiplicar (num_a: int, num_b: int):
    print (f"La multiplicación es: {num_a} * {num_b}")
    return num_a * num_b

numero_5= input("Numero A:")
numero_6 = input ("Numero B:")
numero_5 = int(numero_5)
numero_6 = int(numero_6)

print(f"Resultado multimplicación: {multiplicar (numero_5, numero_6)}")

print(80 * "-")

def dividir (num_a: int, num_b: int):
    print (f"La división es: {num_a} / {num_b}")
    return num_a / num_b

numero_7= input("Numero A:")
numero_8 = input ("Numero B:")
numero_7 = int(numero_7)
numero_8 = int(numero_8)

print(f"Resultado división: {dividir (numero_7, numero_8)}")

print(80 * "-")

def dividir (num_a: int, num_b: int):
    print (f"La división es: {num_a} % {num_b}")
    return num_a % num_b

numero_7= input("Numero A:")
numero_8 = input ("Numero B:")
numero_7 = int(numero_7)
numero_8 = int(numero_8)

print(f"Resultado Modulo: {dividir (numero_7, numero_8)}")

print(80 * "-")

num_a = input ("Ingrese un numero:")
num_b = input ("Ingrese otro numero:")

print(float(num_a))
print(float(num_b))

print(80 * "-")

num_a = input ("Ingrese un numero:")

num_b = input ("Ingrese otro numero:")

print(int(num_a))
print(int(num_b))

print(80 * "-")
'''convierte temperatura en grados celsius a fahrenheit'''

f = float(input("Ingresa los grados Fahrenheit: "))
c = (f-32) /1.8
print(f"Los {f} grados Fahrenheit son {c} grados celsius")

c = float(input("Ingresa los grados Celsius: "))
f = (c * 1.8) + 32
print(f"Los {c} grados Celsius son {f} grados Fahrenheit")

print(80 * "-")







