# __ creamos listas para estudiantes ___

estudiantes = []

# ___ Creamos las funciones para usar en el programa___

# Funcion promedio de notas

def promedio(a,b,c):
    return (a+b+c)/3

# Funcion para evaluar estado

def evaluar_estado(promedio):
    if promedio >= 4.0:
        return "Aprobado"
    elif promedio >= 3.0:
        return "En recuperación"
    else:
        return "Reprobado"
    
    

# Funcion para registrar a un estudiante

def registrar_estudiante (lista_estudiantes):

    nombre = input("Ingrese el nombre de el estudiante: ")
    while True:
       
        try:
            edad = int(input("Ingrese la edad de el estudiante: "))
            if edad > 0:
                break
            else:
                print("Edad invalida")
        except:
            print("Ingrese un numero valido")




    while True:
        try:
            nota1 = float(input("Ingrese nota 1: "))
            if not (0 <= nota1 <= 5):
                print("dato invalido")
            else:
                break
        except:
            print("dato invalido")
   
    while True:
        try:
            nota2 = float(input("Ingrese nota 2: "))
            if not (0 <= nota2 <= 5):
                print("dato invalido")
            else:
                break
        except:
            print("dato invalido")
        
    while True:
        try:
            nota3 = float(input("Ingrese nota 3: "))
            if not (0 <= nota3 <= 5):
                print("dato invalido")
            else:
                break
        except:
            print("dato invalido")
    promedio_notas = promedio(nota1,nota2,nota3)

    estado = evaluar_estado(promedio_notas)

    lista_estudiantes.append({
        "nombre"  : nombre,
        "edad"    : edad,
        "promedio": promedio_notas,
        "estado"  : estado
    })

# ___ Menu principal ___

menu = """
====== Sistema de estudiantes ======

1. Registrar estudiantes
2. Mostrar estudiantes registrados
3. salir

"""

 
opcion = 0
while True:
    print(menu)
    try:
        opcion = int(input("Ingrese la opcion del menu: "))
    
        if opcion == 1:
            registrar_estudiante(estudiantes)
        elif opcion == 2:
            if len(estudiantes) == 0:
                print("No hay estudiantes registrados")
            print(estudiantes)
        elif opcion == 3:
            if  len(estudiantes) == 0:
                print("No hay estudiantes registrados")
                break
            else:
                print(f"cantidad de estudiantes: {len(estudiantes)}")

                promedio_grupo = sum(prom["promedio"] for prom in estudiantes) / len(estudiantes)



                print(f"promedio de el grupo: {promedio_grupo:.2f}")

                print("saliendo de el programa")
                break
        else:
            print("¡No se ingreso un numero de la lista!")
    except:
        print("¡ingrese un numero valido!")

   

        
    

