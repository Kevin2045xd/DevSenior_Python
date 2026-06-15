import csv

with open("inventario.csv", "r", encoding="utf-8") as archivo:
    lector_csv = csv.DictReader(archivo)  # se crea un objeto lector_csv que es un diccionario, cada fila del archivo se convierte en un diccionario con las claves siendo los nombres de las columnas


    for fila in lector_csv:
        print(fila)