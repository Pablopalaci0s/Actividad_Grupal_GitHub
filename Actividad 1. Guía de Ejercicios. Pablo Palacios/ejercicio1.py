# Ejercicio 1: Promedio de un estudiante
# Solicita nombre y tres notas, calcula promedio y determina aprobación

# Solicitar datos del estudiante
nombre = input("Ingrese el nombre del estudiante: ")

# Solicitar las tres notas
nota1 = float(input("Ingrese la primera nota: "))
if nota1 > 10:
    print("Nota muy alta, se ajustó a 10")
    nota1 = 10

nota2 = float(input("Ingrese la segunda nota: "))
if nota2 > 10:
    print("Nota muy alta, se ajustó a 10")
    nota2 = 10

nota3 = float(input("Ingrese la tercera nota: "))
if nota3 > 10:
    print("Nota muy alta, se ajustó a 10")
    nota3 = 10

# Calcular promedio
promedio = (nota1 + nota2 + nota3) / 3

# Determinar si aprueba
if promedio >= 6.0:
    resultado = "APROBADO"
    mensaje = f"¡Felicidades {nombre}! Has aprobado con un promedio de {promedio:.2f}"
else:
    resultado = "REPROBADO"
    mensaje = f"Lo siento {nombre}, has reprobado con un promedio de {promedio:.2f}"

# Mostrar resultado
print(f"\nEstudiante: {nombre}")
print(f"Promedio: {promedio:.2f}")
print(f"Estado: {resultado}")
print(mensaje)