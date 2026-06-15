

# r se usa para leer un archivo
# w se usa para escribir un archivo, si el archivo no existe lo crea, si existe lo sobreescribe
# a se usa para agregar contenido a un archivo, si el archivo no existe lo crea, si existe agrega el contenido al final del archivo
# r+ se usa para leer y escribir un archivo, si el archivo no existe lo crea, si existe lo sobreescribe
# x se usa para crear un archivo, si el archivo ya existe lanza un error
"""
archivo = open("saludo.txt", "w") # se abre el archivo en modo escritura
archivo.write("Hola, este es un archivo de texto.") # se escribe en el archivo
archivo.close() # se cierra el archivo
"""
"""
archivo = open("Tareas.txt", "r") # se abre el archivo en modo lectura
linea = archivo.readline() # se lee una línea del archivo
print(linea) # se imprime la línea leída
archivo.close() # se cierra el archivo
"""
"""
archivo = open("Tareas.txt", "r") # se abre el archivo en modo lectura
lineas = archivo.readlines() # se leen todas las líneas del archivo y se guardan en una lista
print(lineas) # se imprime la lista de líneas
for linea in lineas: # se recorre la lista de líneas
    print(linea.rstrip()) # se imprime cada línea sin el salto de línea al final
archivo.close() # se cierra el archivo
"""
