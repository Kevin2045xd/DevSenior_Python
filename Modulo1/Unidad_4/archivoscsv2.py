import csv

with open("estudiantes.csv", "w", encoding="utf-8", newline='') as archivo:

    escritor_csv = csv.writer(archivo)

    escritor_csv.writerow(["nombre", "nota"])
    escritor_csv.writerow(["Juan", 8])
    escritor_csv.writerow(["María", 9])