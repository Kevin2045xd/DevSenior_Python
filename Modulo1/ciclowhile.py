menu = """
Restaurante el Buen Sabor
1. Hamburguesa 20.000
2. Pizza 15.000
3. Ensalada 4.500
4. Salchipapa 8.000
5. Perro Caliente 12.000
6. Salir
"""
print(menu)
opcion = 0
cuenta = 0
while opcion != 6 :
    opcion = int(input("Ingrese una opción del menú: "))
    if opcion == 1:
        print("Has elegido Hamburguesa")
        cuenta += 20000
        print(f"La cuenta es de: {cuenta}")
    elif opcion == 2:
        print("Has elegido Pizza")
        cuenta += 15000
        print(f"La cuenta es de: {cuenta}")
    elif opcion == 3:
        print("Has elegido Ensalada")
        cuenta += 4500
        print(f"La cuenta es de: {cuenta}")
    elif opcion == 4:
        print("Has elegido Salchipapa")
        cuenta += 8000
        print(f"La cuenta es de: {cuenta}")
    elif opcion == 5:
        print("Has elegido Perro Caliente")
        cuenta += 12000
        print(f"La cuenta es de: {cuenta}")
    elif opcion == 6:
        print(f"El valor de la cuenta es de: {cuenta}")
        print("Gracias por visitar el Restaurante el Buen Sabor. ¡Hasta luego!")
        cuenta = 0
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")
    print(menu)