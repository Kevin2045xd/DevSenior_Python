import csv

with open("estudiantes.csv", "w", encoding="utf-8", newline="") as archivo:

    escritor_csv = csv.writer(archivo)

    escritor_csv.writerow(["Nombre", "Edad", "Carrera"])
    escritor_csv.writerow(["Ana", 22, "Ingeniería"])
    escritor_csv.writerow(["Luis", 24, "Medicina"])
    escritor_csv.writerow(["Sofía", 21, "Derecho"])