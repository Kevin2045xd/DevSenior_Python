"""
archivo = open("datos1.txt", "w") # se abre el archivo en modo escritura
archivo.write("saludos kevin") # se escribe en el archivo
archivo.close() # se cierra el archivo
"""
with open("datos2.txt", "w", encoding="utf-8") as archivo: # se abre el archivo en modo escritura, se cierra automáticamente al salir del bloque
    # el encoding se usa para especificar la codificación del archivo, en este caso utf-8 es una codificación que soporta caracteres especiales como acentos y eñes
    archivo.write("saludos kevin") # se escribe en el archivo

with open("datos2.txt", "r", encoding="utf-8") as archivo: # se abre el archivo en modo lectura, se cierra automáticamente al salir del bloque
    linea = archivo.readline() # se lee una línea del archivo
    print(linea) # se imprime la línea leída

with open("datos2.txt", "a", encoding="utf-8") as archivo: # se abre el archivo en modo agregar, se cierra automáticamente al salir del bloque
    archivo.write("\nAdiós kevin") # se agrega una línea al final del archivo
    
with open("datos2.txt", "r", encoding="utf-8") as archivo: # se abre el archivo en modo lectura, se cierra automáticamente al salir del bloque
    lineas = archivo.readlines() # se leen todas las líneas del archivo
    print(lineas) # se imprime la lista de líneas
    for linea in lineas: # se recorre la lista de líneas
        print(linea.rstrip()) # se imprime cada línea sin el salto de línea al final