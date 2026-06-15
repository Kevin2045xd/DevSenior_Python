import csv 

with open("productos.csv", "r", encoding="utf-8") as archivo:
    
    lector_csv = csv.reader(archivo)
    next(lector_csv) # salta la primera fila ( encabezado)

    for fila in lector_csv:
        print(fila)

    

