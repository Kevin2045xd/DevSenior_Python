nombre = input(" ¿como te llamas?")
print(f"Hola {nombre}")
print("vamos a calcular cuanto ganaste esta semana")

horas_diarias = float(input("¿Cuantas horas trabajas en el dia?"))
dias_trabajados = int(input("¿Cuantos dias trabajas en la semana?"))
valor_horas = int(input("¿Cuanto te pagan por hora?"))
pago = horas_diarias*dias_trabajados*valor_horas

print(f"{nombre} esta semana ganaste {pago:.0f} pesos")