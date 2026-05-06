notas = []

while True:
    nota = int(input("ingrese una nota entre 0 y 10 o ingrese -1 para terminar: ")) # se debe convertir a entero para poder comparar con -1 y validar el rango de notas

    if nota == -1:
        for i in notas:
            total = sum(notas)
            promedio = total / len(notas)
        print("el promedio de las notas es: ", promedio)
        break
    elif nota < 0 or nota > 10:
        print("nota no valida, intente de nuevo")
    else:
        notas.append(nota)





