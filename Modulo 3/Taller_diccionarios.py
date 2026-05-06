"""
Ejercicio: Sistema de Gestión de Estudiantes
Crea un programa que gestione las calificaciones de estudiantes usando diccionarios. El programa debe permitir:

Requisitos:
Estructura de datos: Usa un diccionario donde las claves sean los nombres de los estudiantes y los valores sean listas de calificaciones.

Funcionalidades a implementar:

Agregar un nuevo estudiante (con una lista vacía de calificaciones)

Agregar calificaciones a un estudiante existente

Calcular el promedio de un estudiante

Mostrar todos los estudiantes con sus promedios

Encontrar el estudiante con el promedio más alto

Eliminar un estudiante
"""

# Creamos diccionario de estudiantes
estudiantes = {}
opcion = 0

menu = """
---SISTEMA DE GESTION DE ESTUDIANTES---
1. Agregar estudiante
2. Agregar calficacion
3. Calcular promedio de estudiante
4. Mostrar promedios de estudiantes
5. Promedio mas alto
6. Eliminar estudiante
7. Salir
----------------------------------------
"""
print(menu)

while opcion != 7:
    print(menu)
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        nombre = input("Ingrese el nombre del estudiante: ")
        if nombre in estudiantes:
            print(f"El estudiante {nombre} ya existe.")
        else:
            estudiantes[nombre] = []
            print(f"Estudiante {nombre} agregado exitosamente.")

    elif opcion == 2:
        nombre = input("Ingrese el nombre de el estudiante: ")
        if nombre in estudiantes:
            calificacion = float(input("Ingrese la nota: "))
            if calificacion < 0 or calificacion > 5:
                print(f"{calificacion} no es una nota valida")
            else:
                estudiantes[nombre].append(calificacion)
                print(f"Nota {calificacion} agregada")
        else:
            print("El estudiante no existe")

    elif opcion == 3:
        nombre = input("Ingrese el nombre de el estudiante: ")
        if nombre in estudiantes:
            promedio = sum(estudiantes[nombre]) / len(estudiantes[nombre])
            print(f"El promedio de {nombre} es {promedio:.2f}.")
        else:
            print("El estudiante no existe")

    elif opcion == 4:
        for estudiante in estudiantes:
            promedio = sum(estudiantes[estudiante]) / len(estudiantes[estudiante])
            print(f"El promedio de {estudiante} es {promedio:.2f}.")
            



print(estudiantes)




