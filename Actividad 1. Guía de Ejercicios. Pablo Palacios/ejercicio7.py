# Ejercicio 7: Calculadora simple
# Dos números y una operación básica

# Inicializamos la variable para controlar si seguimos usando la calculadora
seguir = "s"

while seguir.lower() == "s":
    # Pedimos los dos números
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    # Pedimos la operación
    operacion = input("Ingrese la operación (+, -, *, /): ")
    
    # Calculamos según la operación
    if operacion == "+":
        print("El resultado es:", num1 + num2)
    elif operacion == "-":
        print("El resultado es:", num1 - num2)
    elif operacion == "*":
        print("El resultado es:", num1 * num2)
    elif operacion == "/":
        print("El resultado es:", num1 / num2)
    else:
        print("Operación inválida")
    
    # Preguntamos si quiere hacer otra operación
    seguir = input("¿Desea hacer otra operación? (s/n): ")
