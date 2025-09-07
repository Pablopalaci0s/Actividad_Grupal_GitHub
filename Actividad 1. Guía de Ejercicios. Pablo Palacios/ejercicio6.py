# Ejercicio 6: Juego de adivinanza
# Generar número aleatorio y dar pistas

import random

# Generar número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)
intentos = 0

print("¡Adivina el número entre 1 y 100!")

# Bucle del juego
while True:
    # Solicitar número al usuario
    numero_usuario = int(input("Ingresa tu número: "))
    intentos = intentos + 1
    
    # Comparar números
    if numero_usuario == numero_secreto:
        print(f"¡Felicidades! Adivinaste el número {numero_secreto}")
        print(f"Lo lograste en {intentos} intentos")
        break
    elif numero_usuario < numero_secreto:
        print("Mayor")
    else:
        print("Menor")