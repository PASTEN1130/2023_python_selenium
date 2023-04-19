"""
Escribe un programa en Python que pida al usuario una lista de números enteros
separados por comas y que muestre por pantalla la suma, el máximo y el mínimo de
los números ingresados.
"""
#Pídele al usuario que ingrese una lista de números enteros separados por
#comas y almacena los valores en una lista. Para esto, puedes utilizar la
#función input() y luego la función split() para separar los valores por comas

# Pedir al usuario que ingrese una lista de números enteros
numeros = input("Ingrese una lista de números enteros separados por comas: ")
lista_numeros = numeros.split(",")
lista_numeros = [int(num) for num in lista_numeros]

# Calcular la suma, el máximo y el mínimo
suma = 0
maximo = lista_numeros[0]
minimo = lista_numeros[0]
for num in lista_numeros:
    suma += num
    if num > maximo:
        maximo = num
    if num < minimo:
        minimo = num

# Mostrar los resultados por pantalla
print(f"La suma de los números es: {suma}")
print("El número máximo es:", maximo)
print("El número mínimo es:", minimo)