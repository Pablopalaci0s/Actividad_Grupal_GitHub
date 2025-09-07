"""
Ejercicio 2. 
Solicita la cantidad de hombres y mujeres en un grupo. 
Calcula el porcentaje de cada uno y determina si el grupo está equilibrado (diferencia ≤10%). 

"""

Cantidad_Hombres = int (input("Ingresar el número de Mujeres en el grupo:"))
Cantidad_Mujeres = int (input("Ingresar el número de Hombres en el grupo:"))

Total_Grupo = Cantidad_Mujeres + Cantidad_Hombres

Porcentaje_Mujeres = (Cantidad_Mujeres / Total_Grupo)*100

Porcentaje_Hombres = (Cantidad_Hombres / Total_Grupo)*100

print ("El numero Total del grupo es ",Total_Grupo)
print ("Porcentaje de Hombres en el grupo:",Porcentaje_Mujeres) 
print ("Porcentaje de Mujeres en el grupo:",Porcentaje_Hombres)

Proporcion_mujeres = Cantidad_Mujeres / Total_Grupo
Proporcion_Hombres = Cantidad_Hombres / Total_Grupo

Diferencia_Proporcion = abs(Proporcion_mujeres - Proporcion_Hombres)

print ("Diferncia de propocion",Diferencia_Proporcion)

if Diferencia_Proporcion <= 1:
    print ("El grupo esta balanceado y todo en orden")
else:
    print ("El grupo no esta balanceado")
