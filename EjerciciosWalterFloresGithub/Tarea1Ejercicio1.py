"""
Ejercicio 1. 
Solicita el nombre de un estudiante y sus tres notas. 
Calcula el promedio y determina si aprueba (≥6.0). 
Muestra un mensaje personalizado. 

"""

Nombre_Estudiante = str (input("Cuál es el nombre del estudiante? \n "))

Nota1 = float (input("Ingrese la primer nota por favor: \n"))
Nota2 = float (input("Ingrese la segunda nota por favor: \n"))
Nota3 = float (input("Ingrese la tercer nota por favor: \n"))

Nota_final = (Nota1 + Nota2 + Nota3) / 3

if Nota_final >= 6.0:
    print("Afortunadamente la pasaste campeón con ese tu",Nota_final)
else:
    print ("La carlitos compadre con ese tu",Nota_final)
    
if Nota_final >= 6.0:
    print("A seguir adelante con la programación II",Nombre_Estudiante)
else:
    print ("Para la próxima hay que esmerarse más",Nombre_Estudiante)



