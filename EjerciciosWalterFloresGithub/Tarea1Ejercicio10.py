"""
Ejercicio 10. 
Solicita un día de la semana. 
Si el usuario ingresa el "mejor día" (por ejemplo, "viernes"), el programa finaliza. Si no, sigue preguntando. 
"""

while True:
    dia = input("Introduce un día de la semana por favor: ")
    if dia.lower() == "viernes":
        print("Elegiste el mejor día de la semana !!!")
        break 
    else:
        print("Elige otro, ese día es muy aburrido")
