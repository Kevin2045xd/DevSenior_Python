animal = input("elije perro, gato o pez: ")
 
match animal:
    case "perro":
        print("Guau")
    case "gato":
        print("Miau")
    case "pez":
        print("Blub")
    case _:
        print("ingresaste un dato invalido")
