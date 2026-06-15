import csv

datos = [
    ["Portatil", 2500000],
    ["Tablet", 1500000],
    ["Smartphone", 1000000]
]

with open("inventario.csv", "w", newline = "", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Producto", "Precio"]) 
    
    for fila in datos:
        escritor.writerow(fila)
        