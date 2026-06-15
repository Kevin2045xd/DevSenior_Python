import csv

with open("usuarios.csv", "w", encoding="utf-8", newline="") as archivo:
    campos = ["Nombre", "Edad",]

    escritor_csv = csv.DictWriter(archivo, fieldnames=campos)

    escritor_csv.writeheader()
    escritor_csv.writerow({"Nombre": "Carlos", "Edad": 30})
    escritor_csv.writerow({"Nombre": "María", "Edad": 25})