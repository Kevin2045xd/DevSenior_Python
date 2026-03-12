"""escribir un programa que pida a el usuario dos numeros y muestre un menu de opciones
suma, resta, multiplicacion y division
"""

def suma(a,b):
    resultado = a+b
    print(f"el resultado de la suma es: {resultado}")

def resta (a,b):
    resultado = a-b
    print(f"el resltado de la resta es: {resultado}")

def multiplicacion (a,b):
    resultado = a*b
    print(f"el resultado de la multiplicacion es: {resultado}")

def division (a,b):
    if b == 0:
        print("no se puede dividir entre cero")
    else:
        resultado = a/b
        print(f"el resultado de la division es: {resultado}")

def division_entera (a,b):
    if b == 0:
        print("no se puede dividir entre cero")

    else:
        resultado = a//b
        print(f"el resultado de la division entera es: {resultado}")

def potencia (a,b):
    resultado = a**b
    print(f"el resultado de la potencia es: {resultado}")

def modulo (a,b):
    if b == 0:
        print("no se puede dividir entre cero")
    else:
        resultado = a%b
        print(f"el modulo es: {resultado}")

print("Calculadora\n")
numero1 = int(input("ingrese numero 1: "))
numero2 = int(input("ingrese numero 2: "))





while True :
    opcion = int(input("""
1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Division entera
6. Potencia
7. Modulo
8. Salir

Seleccione una opcion: """))
    if opcion == 1:
        suma(numero1,numero2)
    elif opcion == 2:
        resta(numero1,numero2)
    elif opcion == 3:
        multiplicacion(numero1,numero2)
    elif opcion == 4:
        division(numero1,numero2)
    elif opcion == 5:
        division_entera(numero1,numero2)
    elif opcion == 6:
        potencia(numero1,numero2)
    elif opcion == 7: 
        modulo(numero1,numero2)
    elif opcion == 8:
        print("Sesion terminada")
        break
    else :
        print("Dato invalido")
