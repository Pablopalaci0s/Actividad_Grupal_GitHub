# Ejercicio 2: Equilibrio de género en un grupo
# Calcula porcentajes y determina si está equilibrado

# Solicitar cantidad de personas
hombres = int(input("Ingrese la cantidad de hombres: "))
mujeres = int(input("Ingrese la cantidad de mujeres: "))

# Calcular total y porcentajes
total = hombres + mujeres
porcentaje_hombres = (hombres / total) * 100
porcentaje_mujeres = (mujeres / total) * 100

# Determinar si está equilibrado (diferencia ≤10%)
diferencia = abs(porcentaje_hombres - porcentaje_mujeres)

if diferencia <= 10:
    equilibrio = "SÍ está equilibrado"
else:
    equilibrio = "NO está equilibrado"

# Mostrar resultados
print(f"\nTotal de personas: {total}")
print(f"Hombres: {hombres} ({porcentaje_hombres:.1f}%)")
print(f"Mujeres: {mujeres} ({porcentaje_mujeres:.1f}%)")
print(f"Diferencia: {diferencia:.1f}%")
print(f"El grupo {equilibrio}")