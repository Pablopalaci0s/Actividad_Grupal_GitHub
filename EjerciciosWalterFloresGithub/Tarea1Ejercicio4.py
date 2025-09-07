"""
Ejercicio 4. 
Solicita la edad de tres personas y muestra quién es el mayor, el medio y el menor.
"""

Edad1 = int (input("Ingrese la edad de la primer persona a evaluar por favor: "))
Edad2 = int (input("Ingrese la edad de la segunda persona a evaluar por favor: "))
Edad3 = int (input("Ingrese la edad de la tercera persona a evaluar por favor: "))

edades = [Edad1, Edad2, Edad3]

edades.sort()

menor = edades[0]
medio = edades[1]
mayor = edades[2]

print(f"\nLa persona menor tiene: {menor} años")
print(f"La persona de edad intermedia tiene: {medio} años")
print(f"La persona mayor tiene: {mayor} años")
           
