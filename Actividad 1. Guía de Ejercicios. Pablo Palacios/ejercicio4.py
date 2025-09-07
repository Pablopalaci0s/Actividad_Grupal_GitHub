# Ejercicio 4: Edad de tres personas
# Determina quién es el mayor, medio y menor

# Solicita edades
Edad1 = int(input("Digite la edad de la primera persona: "))
Edad2 = int(input("Digite la edad de la segunda persona: "))
Edad3 = int(input("Digite la edad de la tercera persona: "))
 
# Determinar mayor, medio y menor
if Edad1 >= Edad2 and Edad1 >= Edad3:
    mayor = Edad1
    if Edad2 >= Edad3:
        medio = Edad2
        menor = Edad3
    else:
        medio = Edad3
        menor = Edad2

elif Edad2 >= Edad1 and Edad2 >= Edad3:
    mayor = Edad2
    if Edad1 >= Edad3:
        medio = Edad1
        menor = Edad3
    else:
        medio = Edad3
        menor = Edad1

else:
    mayor = Edad3
    if Edad1 >= Edad2:
        medio = Edad1
        menor = Edad2
    else:
        medio = Edad2
        menor = Edad1

# se imprime el resultado
print(f"El mayor tiene {mayor} años")
print(f"El del medio tiene {medio} años")
print(f"El menor tiene {menor} años")
