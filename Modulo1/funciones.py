#FUNCIONES
"""
LAS FUNCIONES SON LLAMADOS A METODOS PARA EJECUTARLOS

1. hay funciones que no reciben nada y no retornan nada
2. hay funciones que reciben algo y no retornan nada
3. hay funciones que no reciben nada y retornan algo
4: hay funciones que reciben algo y retornan algo



"""

#---

"""
# def"nombre de la funcion"(parametros que recibe): 
# esta funcion, no recibe nada y no retorna nada 
def suma():
    a = int(input("ingrese el primer numero: "))
    b = int(input("ingrese el segundo numero: "))
    print(f"{a} + {b} = {str(a+b)}")
        

#si no se llama la funcion no se ejecuta
print("hola mundo")
# para que se ejecute se llama la funcion
suma()
"""


"""
#esta funcion recibe dos parametros "a" y "b" y no retorna nada
#se llama parametro, a los datos que recibe la funcion
def suma2(a,b):
    a = int(input("ingrese el primer numero: "))
    b = int(input("ingrese el segundo numero: "))
    print(f"{a} + {b} = {str(a+b)}")

#aqui "a" = 6  y  "b" =  8
#aqui se queman los argumento, en el llamado de la funcion se llama argumento 

suma2(6,8)
"""

#--
#para pedir los datos se crea un input y se ponen en el llamado

"""

def suma2(num1,num2):
    print(f"{num1} + {num2} = {str(num1+num2)}")
    1
num1 = int(input("ingrese el primer numero: \n"))
num2 = int(input("ingrese el segundo numero: \n"))

suma2(num1,num2)
"""

#--

"""
#esta funcion no recibe parametros pero retorna algo
def suma3():
    num1 = int(input("ingrese el primer numero: \n"))
    num2 = int(input("ingrese el segundo numero: \n"))
    resultado = num1 +num2
    return resultado

#aqui no aparacera el resultado, porque se hizo la operacion
#pero no se imprime, para que aparezca hay que imprimirlo
#ya sea imprimiendo en la funcion o en el llamado

print(suma3()) 
"""

#--

"""
#esta funcion recibe un los parametros y retorna algo
def suma4(num1,num2):
    
    resultado = num1 +num2
    return resultado

#aqui no aparacera el resultado, porque se hizo la operacion
#pero no se imprime, para que aparezca hay que imprimirlo
#ya sea imprimiendo en la funcion o en el llamado

num1 = int(input("ingrese el primer numero: \n"))
num2 = int(input("ingrese el segundo numero: \n"))
print(suma4(num1,num2)) 
"""


#--- 

print ("calculadora de con funciones \n")


"""
Escriba un programa que pida al ususario 2 numeros y muestre un menu de opciones
1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Division entera
6. Potencia
7. Modulo
8. Salir
"""

    
def Suma():
    num1 = int(input("ingrese el primer numero de la suma: "))
    num2 = int(input("ingrese el segundo numero de la suma: "))
    resultado1 = num1+num2
    return resultado1


def Resta():
    num1 = int(input("ingrese el primer numero de la resta: "))
    num2 = int(input("ingrese el segundo numero de la resta: "))
    resultado2 = num1-num2
    return resultado2


def Multiplicacion():
    num1 = int(input("ingrese el primer numero de la multiplicacion: "))
    num2 = int(input("ingrese el segundo numero de la multiplicacion: "))
    resultado3 = num1*num2
    return resultado3


def Division():
    num1 = int(input("ingrese el primer numero de la division: "))
    num2 = int(input("ingrese el segundo numero de la division: "))
    resultado4 = num1/num2
    return resultado4


def DivisionEntera():
    num1 = int(input("ingrese el primer numero de la diviosion entera: "))
    num2 = int(input("ingrese el segundo numero de la division entera: "))
    resultado5 = num1//num2
    return resultado5


def Potencia():
    num1 = int(input("ingrese el primer numero de la potencia: "))
    num2 = int(input("ingrese el segundo numero de la potencia: "))
    resultado6 = num1**num2
    return resultado6


def Modulo():
    num1 = int(input("ingrese el primer numero de el modulo: "))
    num2 = int(input("ingrese el segundo numero de el modulo: "))
    resultado7 = num1%num2
    return resultado7

operacion = int(input("""A continuacion vamos a hacer operaciones.\n
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Division entera
    6. Potencia
    7. Modulo
    8. Salir \n
    seleccione la operacion que quiere hacer: 
    """))

while operacion != 8:

    if operacion < 1 or operacion > 9:
        print("\n !!!INGRESE UNA OPCION VALIDA.¡¡¡ ")

    if operacion == 1:
        print(f"\n el resultado de la suma es {Suma()}\n")

    if operacion == 2:
        print(f"\n el resultado de la resta es {Resta()}\n")

    if operacion == 3:
        print(f"\n el resultado de la multiplicacion es {Multiplicacion()}\n")

    if operacion == 4:
        print(f"\n el resultado de la division es {Division()}\n")

    if operacion == 5:
        print(f"\n el resultado de la division entera es {DivisionEntera()}\n")

    if operacion == 6:
        print(f"\n el resultado de la potencia es {Potencia()}\n")

    if operacion == 7:
        print(f"\n el resultado de el modulo es {Modulo()}\n")

    #aqui se vuelve a pedir ""operacion" para que pueda elegir otra operacion, y que pregunte hasta que seleccione 8
    operacion = int(input("""A continuacion vamos a hacer operaciones.\n
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Division entera
    6. Potencia
    7. Modulo
    8. Salir \n
    seleccione la operacion que quiere hacer: 
    """))    

#cuando selecciona 8 se sale del while e imprime esto
print("gracias por usar el programa.")