print("- CONJUNTOS -")
#los conjuntos se crean con {}
frutas = {"manzana", "banana", "naranja", "pera", "uva", "banana"}
frutas2 = {"fresa", "melon", "kiwi"}
print(frutas)
print(" ")

print("se muestra el numero de elementos del conjunto, no se cuentan los repetidos")
#no pueden existir elementos repetidos
print(len(frutas))
print(" ")

## Metodos

print("Metodos de conjuntos")
frutas.add("kiwi") # añadir elemento
print(frutas)
print(" ")
print(frutas.intersection_update(frutas2)) # actualiza frutas con la interseccion de frutas y frutas2


frutas.remove("pera") # remover elemento
print(frutas)
print(" ")

 # elimina elemento y lo ingresa en una variable
#si no se especifica toma uno al azar
#si no se mete en un lugar, se elimina el elemento
basura = frutas.pop()
print(frutas)
print(basura)
print(" ")

copia_frutas = frutas.copy() # crea una copia
print(copia_frutas)
print(" ")



#Diferencia entre conjuntos
print(" ")
print(frutas.difference(frutas2)) # elementos que estan en frutas pero no en frutas2
print(frutas2.difference(frutas)) # elementos que estan en frutas2 pero no en frutas

#Interseccion entre conjuntos
print(frutas.intersection(frutas2)) # elementos que estan en ambos conjuntos
print(" ")

#Union entre conjuntos
print(frutas.union(frutas2)) # elementos que estan en cualquiera de los dos conjuntos
print(" ")

frutas.discard("banana") # elimina un elemento, si no existe no da error
print(frutas)
print(" ")

"""
frutas.clear() # elimina todos los elementos del conjunto
print(" ")
"""
print("- SUBCONJUNTOS -")
print(frutas.issubset(frutas2)) # verifica si frutas es un subconjunto de frutas2
print(frutas2.issubset(frutas)) # verifica si frutas2 es un subconjunto de frutas
print(" ")

print("- SUPERCONJUNTOS -")
print(frutas.issuperset(frutas2)) # verifica si frutas es un superconjunto de frutas2
print(frutas2.issuperset(frutas)) # verifica si frutas2 es un superconjunto de frutas
print(" ")

#Diferencia simetrica entre conjuntos
print(frutas.symmetric_difference(frutas2)) # elementos que estan en frutas o en frutas2 pero no en ambos
print(" ")


