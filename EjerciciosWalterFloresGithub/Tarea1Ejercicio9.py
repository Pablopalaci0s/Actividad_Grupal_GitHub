"""
Ejercicio 9. 
Solicita un número y muestra su tabla de multiplicar del 1 al 10
"""

num = int(input("Ingresa un número y te mostraré su tabla de multiplicar: "))

print(f"Tabla de multiplicar del {num}:")
for i in range(1, 11):
  print(f"{num} x {i} = {num * i}")