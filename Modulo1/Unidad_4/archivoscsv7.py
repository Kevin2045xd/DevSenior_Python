import csv

with open("ensayis.csv", "r", encoding="utf-8") as archivo:

    lector_csv = csv.reader(archivo, delimiter=";")

    for fila in lector_csv:
        print(fila)