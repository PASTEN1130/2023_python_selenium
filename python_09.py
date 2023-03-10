"""
Imprime todos los números del 0 al 99, de dos en dos y que no sean múltiplos del 3
"""
for num in range (0,99):
    if num % 2 ==0:
        print (f"numero no es multiplo de 3:{num}")
