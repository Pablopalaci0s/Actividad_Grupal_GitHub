"""
Ejercicio 6. 
Genera un número aleatorio entre 1 y 100. 
El usuario debe adivinarlo. El programa da pistas ("Mayor" o "Menor") y cuenta los intentos. 
"""
import random

numero_secreto = random.randint(1, 100)

intentos = 0

print("¡¡¡ Juguemos a adivinar el número !!!")
print("El número secreto está entre 1 y 100...")

while True:
    try:
        adivinanza = int(input("Adivina el número: "))
        intentos += 1

        if adivinanza < numero_secreto:
            print("Mayor")
        elif adivinanza > numero_secreto:
            print("Menor")
        else:
            print(f"¡Sos un crack! ¡Adivinaste el número en {intentos} intentos!")
            break
    except ValueError:
        print("Por favor, ingresa un número válido, es entre 1 y 100 brother.")
