"""
Ejercicio 3. 
Simula el cálculo de salario para 20 empleados que trabajan 6 días a la semana, 
2 horas extra diarias, a $5.00 por hora. 
Usa un bucle para repetir el cálculo por cada empleado. 
Muestra cuanto es total que se debe pagar por empleado y el total de la nómina. 
"""

for i in range(0,3):
    print(f"--- Empleado {i+1} ---")
    Nombre_Empleado = input("Ingrese Nombre de empleado: ")
    Horas_Trabajadas = float(input("Horas trabajadas: "))
    
    Hora_Semanal = 6 * Horas_Trabajadas
    Salario_Semanal = Hora_Semanal * 5
    
    Nomina = [Nombre_Empleado,Horas_Trabajadas,Salario_Semanal]

    print(Nombre_Empleado,"ha trabajado", Horas_Trabajadas,"horas esta semana y su salario semanal es de $", Salario_Semanal)
    

    
  










