# Ejercicio 3: Cálculo de salario para 20 empleados
# 6 días a la semana, 2 horas extra diarias, $5.00 por hora

# Definimos los datos predeterminados
horas_extra_dia = 2
dias_semana = 6
pago_hora = 5
num_empleados = 20

# Variable para acumular el total de la nómina
total_nomina = 0

# Bucle para cada empleado
for i in range(1, num_empleados + 1):
    pago_empleado = horas_extra_dia * dias_semana * pago_hora
    print(f"Empleado {i}: se le debe pagar ${pago_empleado}")
    total_nomina += pago_empleado

# Mostrar total general
print(f"\nEl total de la nómina para {num_empleados} empleados es: ${total_nomina}")
