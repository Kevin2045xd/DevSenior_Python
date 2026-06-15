import csv

with open('productos.csv', 'r', encoding='utf-8') as archivo:
    lector_csv = csv.reader(archivo)

    next(lector_csv)  # Salta la primera fila (encabezados)

    for fila in lector_csv:
        nombre = fila [0]
        precio = fila [1]
        cantidad = fila [2]
        
        print(nombre, precio, cantidad)
       






