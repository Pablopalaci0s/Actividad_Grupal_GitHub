# Ejercicio 8: Determinar si un número es positivo/negativo/cero y par/impar

# Solicitar número
numero = int(input("Ingrese un número: "))

# Determinar si es positivo, negativo o cero
if numero > 0:
    signo = "positivo"
elif numero < 0:
    signo = "negativo"
else:
    signo = "cero"

# Determinar si es par o impar (solo si no es cero)
if numero != 0:
    if numero % 2 == 0:
        paridad = "par"
    else:
        paridad = "impar"
    
    print(f"El número {numero} es {signo} y {paridad}")
else:
    print(f"El número {numero} es {signo}")