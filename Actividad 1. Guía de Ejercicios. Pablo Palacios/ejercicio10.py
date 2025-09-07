# Ejercicio 10: Mejor día de la semana
# Pregunta días hasta que el usuario ingrese "viernes"

# Definir el mejor día
mejor_dia = "viernes"

# Bucle principal
while True:
    # Solicitar día de la semana
    dia = input("Ingrese un día de la semana: ")
    
    # Convertir a minúsculas para comparar
    dia = dia.lower()
    
    # Verificar si es el mejor día
    if dia == mejor_dia:
        print(f"¡Correcto! {mejor_dia.capitalize()} es el mejor día. ¡Programa finalizado!")
        break
    else:
        print(f"{dia.capitalize()} no es el mejor día. Intenta de nuevo.")