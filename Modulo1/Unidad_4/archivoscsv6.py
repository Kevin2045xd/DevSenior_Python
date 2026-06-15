import csv

with open("usuarios.csv", "w", newline='',encoding="utf-8") as archivo:

    campos = ["Nombre", "Edad"]

    escritor = csv.DictWriter(archivo, fieldnames=campos)

    escritor.writeheader()

    escritor.writerow({
        "Nombre": "Carlos", 
        "Edad": 30
        })
    
    escritor.writerow({
        "Nombre": "Ana",
        "Edad": 25
    })