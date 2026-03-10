
# Creamos la funcion para saludar
def saludar (a):
    return print("¡Hola! ", a)

# Se pregunta el nombre
nombre = input("¿Como te llamas? ")

# Se crea el saludo llamando la funcion
# y se guarda en una variable

saludo = saludar(nombre)

# Se imprime el saludo
print(saludo)