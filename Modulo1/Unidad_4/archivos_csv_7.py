import csv
with open("malo.csv", "r", encoding="utf-8") as archivo:

    lector_csv = csv.DictReader(archivo)

    for fila in lector_csv:
        try:
            nombre = fila["nombre"]
            precio = float(fila["precio"])
            cantidad = int(fila["cantidad"])
            
            if precio < 0 or cantidad < 0:
                print(f"Error en el producto {nombre}: precio o cantidad negativa")
                continue
            print(f"Producto: {nombre}, Precio: {precio}, Cantidad: {cantidad}")
        except (ValueError, TypeError):
            print(f"Error en el producto {fila['nombre']}: precio o cantidad no es un número")
        except KeyError:
            print(f"Error en el producto {fila.get('nombre', 'desconocido')}: falta el campo precio o cantidad")