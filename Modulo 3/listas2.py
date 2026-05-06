
a = ["fresas", "naranja", "pera", "mandarina", "mora"]
b = list(("fresas", "naranja", "pera", "naranja", "mandarina", "mora", "naranja"))
print(a)
print(b)


numero = 0
for i in a :
    
    numero += len(i)
    print(numero)


numero2 = 0

while numero2 < len(a) :
    print(a[numero2])
    numero2 += 1

c = b.copy()

contador = 0

while contador < len(b):
    if b[contador] == "naranja":
        print("encoontre una naranja e la posicion ",contador)
    contador += 1