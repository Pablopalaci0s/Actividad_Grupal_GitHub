# Ejercicio 5: Menú con opciones
# Día de la semana, recomendación de actividad según clima, salir

# Inicializamos la variable de opción
opcion = 0

# Bucle que se repite mientras el usuario no elija salir (opción 3)
while opcion != 3:
    # Mostramos el menú
    print("MENÚ PRINCIPAL")
    print("1. Mostrar día de la semana")
    print("2. Recomendar actividad según clima")
    print("3. Salir")

    # Solicitamos al usuario que elija una opción
    opcion = int(input("Elige una opción: "))

    # Opción 1: Mostrar día de la semana según número
    if opcion == 1:
        numero = int(input("Digite un número del 1 al 7: "))
        if numero == 1:
            print("Lunes")
        elif numero == 2:
            print("Martes")
        elif numero == 3:
            print("Miércoles")
        elif numero == 4:
            print("Jueves")
        elif numero == 5:
            print("Viernes")
        elif numero == 6:
            print("Sábado")
        elif numero == 7:
            print("Domingo")
        else:
            print("Número inválido. Debe ser entre 1 y 7.")

    # Opción 2: Recomendar actividad según el clima
    elif opcion == 2:
        clima = input("¿Cómo está el clima? (soleado/lluvioso/frío): ").lower()  # se convierte en minúsculas para evitar errores
        if clima == "soleado":
            print("Recomendación: ve a caminar al parque:) ")
        elif clima == "lluvioso":
            print("Recomendación: mira una película en casa :O ")
        elif clima == "frío":
            print("Recomendación: toma un chocolate caliente :D")
        else:
            print("No tengo recomendación para ese clima D:")

    # Opción 3: Salir del programa
    elif opcion == 3:
        print("Saliendo del programa... ¡Adiós!")

    # Si el usuario ingresa un número que no corresponde a ninguna opción
    else:
        print("Opción inválida, intenta de nuevo.")
