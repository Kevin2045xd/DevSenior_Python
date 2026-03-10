nombre = input(" ¿como te llamas?")
print(f"Hola {nombre}")
print("vamos a calcular el pago de tus trabajadores esta semana")


horas1 = float(input("Cuantas horas trabajo el primer empleado? "))
pago_por_hora1 = int(input("Cuanto gana por hora? "))
sueldo1 = horas1 * pago_por_hora1

horas2 = float(input("Cuantas horas trabajo el segundo empleado? "))
pago_por_hora2 = int(input("Cuanto gana por hora? "))
sueldo2 = horas2 * pago_por_hora2

horas3 = float(input("Cuantas horas trabajo el tercer empleado? "))
pago_por_hora3 = int(input("Cuanto gana por hora? "))
sueldo3 = horas3 * pago_por_hora3

nomina = sueldo1 + sueldo2 + sueldo3
print("El valor a pagar a los empleados por su trabajo de la semana es: ", nomina)