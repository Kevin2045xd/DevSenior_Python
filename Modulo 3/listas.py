frutas = ["papaya", "naranja", "pera", "fresa", 5, True, ["hoy", "ayer", "mañana"]] # lista de frutas
print(len(frutas)) # imprime la cantidad de elementos en la lista
print(frutas[0]) # imprime el primer elemento de la lista
print("mandarina" in frutas) # verifica si "mandarina" está en la lista de frutas e imprime el resultado (True o False)
frutas.append("mandarina") # agrega "mandarina" al final de la lista de frutas
print(frutas)
frutas.insert(2, "kiwi") # inserta "kiwi" en la posición 2 de la lista de frutas (desplazando los elementos posteriores hacia la derecha)
print(frutas)
frutas[2] = "aguacate" # reemplaza el elemento en la posición 2 de la lista de frutas con "aguacate"
print(frutas)
print(frutas[2]) # imprime el elemento en la posición 2 de la lista de frutas (que ahora es "aguacate")
frutas.reverse() # invierte el orden de los elementos en la lista de frutas
print(frutas)
# del frutas # elimina la lista de frutas completamente
# print(frutas) # esto generará un error porque la lista de frutas ha sido eliminada

copia = frutas.copy() # crea una copia de la lista de frutas y la asigna a la variable "copia"
print(copia) # imprime la copia de la lista de frutas
#copia = frutas # asigna la lista de frutas a la variable "copia" (esto no crea una copia, sino que ambas variables apuntan a la misma lista)
#frutas.clear() # borra todos los elementos de la lista "frutas"
#print(copia) # imprime la lista "copia" después de haber borrado los elementos de "frutas" (debería mostrar una lista vacía [] si se usó clear() en "frutas", pero si se usó la asignación directa, "copia" también se vaciará porque ambas variables apuntan a la misma lista)
copia.clear() # borra todos los elementos de la lista "copia"
print(copia) # imprime la lista "copia" después de haber sido vaciada (debería mostrar una lista vacía [])

frutas.count("pera") # cuenta cuántas veces aparece "pera" en la lista de frutas
print(frutas.count("pera")) # imprime el resultado de contar cuántas veces aparece "pera" en la lista de frutas
frutas.append("pera") # agrega "pera" al final de la lista de frutas
print(frutas.count("pera")) # imprime el resultado de contar cuántas veces aparece "pera" en la lista de frutas después de agregar otra "pera"
#frutas.extend(("platano", "banano")) # extiende la lista de frutas agregando los elementos de la tupla (platano, banano)
verduras = ["lechuga", "tomate", "pepino"] # lista de verduras
#frutas.extend(verduras) # extiende la lista de frutas agregando los elementos de la lista de verduras
#print(frutas) 
#frutas.append(verduras) # agrega la lista de verduras como un solo elemento al final de la lista de frutas
print(frutas)
frutas.index("pera") # devuelve el índice de la primera aparición de "pera" en la lista de frutas
print(frutas.index("pera")) # imprime el índice de la primera aparición de "pera"
frutas.insert(1, "manzana") # inserta "manzana" en la posición 1 de la lista de frutas
a = frutas.pop() # elimina y devuelve el último elemento de la lista de frutas, asignándolo a la variable "a"
print(a) # imprime el elemento que fue eliminado de la lista de frutas (que es el
b = frutas.pop(1) # elimina y devuelve el elemento en la posición 1 de la lista de frutas, asignándolo a la variable "b"
print(b) # imprime el elemento que fue eliminado de la lista de frutas (que es "
print(frutas) # imprime la lista de frutas después de eliminar el último elemento
frutas.remove("naranja") # elimina la primera aparición de "naranja" en la lista de frutas
print(frutas) # imprime la lista de frutas después de eliminar "naranja"
frutas.pop(2)
frutas.pop(3)
frutas.reverse() # invierte el orden de los elementos en la lista de frutas
print(frutas) # imprime la lista de frutas después de invertir su orden

#frutas.sort() # ordena los elementos de la lista de frutas en orden alfabético (esto puede generar un error si hay elementos de diferentes tipos en la lista, como números o booleanos)