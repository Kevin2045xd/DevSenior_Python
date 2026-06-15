"""
Enunciado del ejercicio

Desarrolla un programa llamado Sistema de Registro de Tareas.

El programa debe permitir al usuario:

Agregar una nueva tarea.
Ver todas las tareas guardadas.
Buscar una tarea por palabra clave.
Contar cuántas tareas hay registradas.
Salir del programa.

Las tareas deben guardarse en un archivo llamado:

tareas.txt

Cada tarea debe almacenarse en una línea diferente.

Requisitos técnicos

El programa debe usar:

open()

Bloque seguro:

with open(...)

Funciones:

agregar_tarea()
mostrar_tareas()
buscar_tarea()
contar_tareas()

Un ciclo while para mantener activo el menú.

Condicionales if, elif, else para controlar las opciones.

Una lista para almacenar temporalmente las tareas leídas desde el archivo.

Ejemplo de ejecución esperada
===== SISTEMA DE REGISTRO DE TAREAS =====
1. Agregar tarea
2. Ver tareas
3. Buscar tarea
4. Contar tareas
5. Salir

Seleccione una opción: 1
Ingrese la nueva tarea: Estudiar manejo de archivos en Python
Tarea guardada correctamente.

Seleccione una opción: 2

--- LISTADO DE TAREAS ---
1. Estudiar manejo de archivos en Python
2. Comprar materiales para clase
3. Revisar ejercicios pendientes
"""

def agregar_tarea():
        
        tarea = input("Ingrese la tarea: ")

        with open("tareas.txt", "w", encoding= 'utf-8') as archivo:
            archivo.write(tarea + '\n')

def ver_tareas():
      with open("tareas.txt", "r", encoding= 'utf-8') as archivo:
           lineas = archivo.readlines()
           for linea in lineas:
                print(linea.rstrip())

    