"""
la función lambda es una función anónima, es decir, no tiene un nombre específico.
 Se utiliza para crear funciones pequeñas y de una sola línea de código. 
 En este caso, la función lambda toma dos argumentos (n1 y n2) y devuelve su suma.

La función lambda se asigna a la variable suma_lambda, lo que permite utilizarla como cualquier otra función.

estructura de una función lambda:
lambda argumentos: expresión
suma_lambda = lambda n1, n2: n1 + n2 
 """

def suma(n1, n2):
    return n1 + n2

# Función lambda para sumar dos números


suma_lambda = lambda n1, n2: n1 + n2

print(suma(3, 5))  # Salida: 8
print(suma_lambda(3, 5))  # Salida: 8

a = 10
b = 20

# Usando la función lambda para sumar a y b
resultado = suma_lambda(a, b)   
print(resultado)  # Salida: 30
print(suma_lambda(15, 25))  # Salida: 40


es_mayor = lambda edad: "Mayor de edad" if edad >= 18 else "Menor de edad"
print(es_mayor(20))  # Salida: Mayor de edad
print(es_mayor(15))  # Salida: Menor de edad

saludar = lambda nombre: f"Hola, {nombre}!"
print(saludar("Juan"))  # Salida: Hola, Juan!

print("-----------------------------")
print("Ejemplo con map y lambda")

"""
map es una función incorporada en Python que se utiliza para aplicar una función a cada elemento 
de un iterable (como una lista) y devolver un nuevo iterable con los resultados.
"""

numeros = [1, 2, 3, 4, 5]

dobles = list(map(lambda x: x * 2, numeros))
print(dobles)  # Salida: [2, 4, 6, 8, 10]

nombres = ["Alice", "Bob", "Charlie"]  

nombres_mayusculas = list(map(lambda nombre: nombre.upper(), nombres))
print(nombres_mayusculas)  # Salida: ['ALICE', 'BOB', 'CHARLIE']

print("-----------------------------")

print("Ejemplo con filter y lambda")

"""
filter es otra función incorporada en Python que se utiliza para filtrar elementos de un iterable
basándose en una función que devuelve True o False.
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)  # Salida: [2, 4, 6, 8, 10]