"""
Ejercicio 7. 
Solicita dos números y una operación (+, -, *, /). 
Realiza la operación seleccionada y muestra el resultado. Repite hasta que el usuario decida salir.
"""
while True:
    try:
        num1 = float(input("Ingresa el primer número por favor: "))
        operacion = input("Ingresa la operación aritmética a usar (+, -, *, /) o 'salir': ")

        if operacion.lower() == 'salir':
            break

        num2 = float(input("Ingresa el segundo número por favor: "))

        if operacion == '+':
            resultado = num1 + num2
        elif operacion == '-':
            resultado = num1 - num2
        elif operacion == '*':
            resultado = num1 * num2
        elif operacion == '/':
            if num2 == 0:
                print("No se puede dividir por cero.")
                continue  
            resultado = num1 / num2
        else:
            print("Operación no válida. Por favor, ingresa +, -, *, / o 'salir'.")
            continue 

        print(f"El resultado es: {resultado}")

    except ValueError:
        print("Entrada no válida. Por favor, ingresa números.")