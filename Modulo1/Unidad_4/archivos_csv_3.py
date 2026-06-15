import csv 

datos = [
    ["portatil", 2500000],
    ["celular", 1500000],
    ["tablet", 1000000]
]

with open("inventario.csv", "w", encoding="utf-8", newline="") as archivo:
    
    escritor_csv = csv.writer(archivo)
    escritor_csv.writerow(["Producto", "Precio"])
    escritor_csv.writerows(datos)