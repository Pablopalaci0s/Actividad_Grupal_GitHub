"""
Ejercicio 5. 
Crea un menú con opciones: Mostrar día de la semana (según número del 1 al 7), 
Recomendar actividad según clima, Salir. El menú se repite hasta que el usuario elija salir
"""
def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Opción 1: Lunes")
    print("2. Opción 2: Martes")
    print("3. Opción 3: Miércoles")
    print("4. Opción 4: Jueves")
    print("5. Opción 5: Viernes")
    print("6. Opción 6: Sábado")
    print("7. Opción 7: Domingo")
    print("X. Salir")

def opcion1():
    print("Mal clima y tráfico los lunes, quedate en casa mejor")
def opcion2():
    print("Wendys al 2x1... visita uno lo antes posible")
def opcion3():
    print("Cine a mitad de precio, apresurate")
def opcion4():
    print("Burgerking al 2x1... apresurate")
def opcion5():
    print("Rock en la zona rosa... buena opción")
def opcion6():
    print("La montaña te espera")
def opcion7():
    print("Visita de familiares")

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ").strip().upper() 

    if opcion == '1':
        opcion1()
    elif opcion == '2':
        opcion2()
    elif opcion == '3':
        opcion3()
    elif opcion == '4':
        opcion4()
    elif opcion == '5':
        opcion5()
    elif opcion == '6':
        opcion6()
    elif opcion == '7':
        opcion7()
    elif opcion == 'X':
        print("Saliendo del programa...")
        break 
    else:
        print("Opción inválida. Por favor, intenta de nuevo.")
