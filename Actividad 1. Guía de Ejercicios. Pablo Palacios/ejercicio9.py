# Ejercicio 9: Tabla de multiplicar
# Solicita un número y muestra su tabla del 1 al 10

# Solicitar número
numero = int(input("Ingrese un número: "))

# Mostrar tabla de multiplicar
print(f"\nTabla de multiplicar del {numero}:")

# Bucle para generar la tabla
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")