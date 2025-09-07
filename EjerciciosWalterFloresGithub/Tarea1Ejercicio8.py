"""
Ejercicio 8. 
Solicita un número y determina si es positivo, negativo o cero. Luego indica si es par o impar.
"""

def clasificar_numero():
    # Solicitar el número al usuario y convertirlo a entero
    try:
        num_str = input("Ingrese un número entero: ")
        numero = int(num_str)

        # Determinar si es positivo, negativo o cero
        if numero > 0:
            print(f"El número {numero} es positivo.")
        elif numero < 0:
            print(f"El número {numero} es negativo.")
        else:
            print(f"El número {numero} es cero.")

        # Determinar si es par o impar
        if numero % 2 == 0:
            print(f"El número {numero} es par.")
        else:
            print(f"El número {numero} es impar.")

    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")

# Llamar a la función para ejecutar el programa
clasificar_numero()