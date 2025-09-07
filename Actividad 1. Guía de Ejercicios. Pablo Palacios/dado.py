import random

# se le solicita al usuario que adivine un número entre 1 y 6
usuario = int(input("Adivina el número que saldrá (1 - 6): "))

# se genera un número aleatorio entre 1 y 6 (se simula el dado)
dado = random.randint(1, 6)

# Mostrar el resultado
print(f"\nEl dado cayó en: {dado}")

# Verificar si el usuario adivinó
if usuario == dado:
    print("¡Felicidades! Adivinaste correctamente.")
else:
    print("No adivinaste, suerte para la próxima.")
