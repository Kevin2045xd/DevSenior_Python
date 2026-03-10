"""
for x in range(1,11):
    print(x)

for x in range(5):
    print(x)

for x in range(1,11,2):
    print(x)

texto = "python"
for letra in texto:
    print(letra)
    """

tabla = int(input("ingresa la tabla de multiplicar que quieres ver"))

multiplicador = 1
for x in range (1,11):
    print(f"{tabla} x {multiplicador} = {tabla*multiplicador}" )
    multiplicador += 1