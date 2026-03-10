numero  = int(input("ingrese un numero de el 1 a el 7: "))

if numero == 1:
    print("lunes")
elif numero == 2:
    print("martes")
elif numero == 3:
    print("miercoles")
elif numero == 4:
    print("jueves")
elif numero == 5:
    print("viernes")
elif numero == 6:
    print("sabado ")
elif numero == 7:
    print("Domingo")
else :
    print("numero invalido")


match numero:
    case 1:
        print("lunes")
    case 2:
        print("martes")
    case 3:
        print("miercoles")
    case 4:
        print("jueves")
    case 5:
        print("viernes")
    case 6:
        print("sabado")
    case 7:
        print("domingo")
    case _:
        print("numero invalido")