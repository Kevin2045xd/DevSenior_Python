"""
Desarrollar un programa en Python que permita gestionar clientes y sus mascotas utilizando diccionarios 
anidados, simulando un sistema básico de una veterinaria

Estructura de datos

Debes usar un diccionario con la siguiente estructura:
veterinaria = {
    "cliente1": {
        "telefono": "123456789",
        "mascotas": {
            "Firulais": {
                "especie": "perro",
                "edad": 5,
                "peso": 12.5
            },
            "Misu": {
                "especie": "gato",
                "edad": 3,
                "peso": 4.2
            }
        }
    }
}


1️⃣ Agregar un cliente
Solicitar:
Nombre del cliente
Teléfono
Crear el cliente con un diccionario vacío de mascotas
2️⃣ Agregar una mascota a un cliente
Solicitar:
Nombre del cliente
Nombre de la mascota
Especie
Edad
Peso
Guardar la mascota dentro del cliente
3️⃣ Mostrar todos los clientes y sus mascotas

Debe mostrar algo como:

Cliente: Carlos
 Teléfono: 123456
 Mascotas:
   - Firulais | Perro | 5 años | 12.5 kg
4️⃣ Buscar una mascota
Solicitar el nombre del cliente y la mascota
Mostrar toda la información de la mascota
5️⃣ Calcular el peso promedio de las mascotas de un cliente
Recorrer el diccionario anidado
Calcular el promedio del peso de todas las mascotas del cliente
6️⃣ Encontrar la mascota más pesada de toda la veterinaria
Debes recorrer todos los clientes y todas sus mascotas
7️⃣ Eliminar una mascota
Solicitar cliente y nombre de la mascota
Eliminarla del diccionario
8️⃣ Eliminar un cliente
Eliminar completamente su registro
🧩 Bonus (opcional 🔥)
Mostrar cuántas mascotas tiene cada cliente
Validar que no se repitan nombres de mascotas dentro del mismo cliente
Mostrar el cliente con más mascotas
"""



menu = """
========== SISTEMA DE GESTION DE VETERINARIA ==========
1. Agregar cliente
2. Agregar mascota
3. Mostrar clientes y mascotas
4. Buscar mascota
5. Calcular promedio de peso
6. Encontrar mascota más pesada
7. Eliminar mascota
8. Eliminar cliente
9. Salir
"""
servidor = {

}
while True:
    print(menu)
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        # Agregar cliente
        nombre = input("Ingrese el nombre del cliente: ")
        telefono = input("Ingrese el telefono del cliente: ")
        if nombre in servidor:
            print(f"El cliente {nombre} ya existe.")
        else:
            servidor[nombre] = {
                "telefono": telefono,
                "mascotas": {}
            }
            print(f"Cliente {nombre} agregado exitosamente.")

    elif opcion == 2:
        # Agregar mascota
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        if nombre_cliente in servidor:
            nombre_mascota = input("Ingrese el nombre de la mascota: ")
            if nombre_mascota in servidor[nombre_cliente]["mascotas"]:
                    print(f"La mascota {nombre_mascota} ya existe para el cliente {nombre_cliente}.")
            else:
                especie = input("Ingrese la especie de la mascota: ")
                edad = int(input("Ingrese la edad de la mascota: "))
                peso = float(input("Ingrese el peso de la mascota en Kg: "))
                servidor[nombre_cliente]["mascotas"][nombre_mascota] = {
                    "especie": especie,
                    "edad": edad,
                    "peso": peso
                }
                print(f"Mascoata {nombre_mascota} agregada exitosamente al cliente {nombre_cliente}.")
        else:
            print(f"El cliente {nombre_cliente} no existe.")


    elif opcion == 3:
        # Mostrar clientes y mascotas
        if len(servidor) == 0:
            print("No hay clientes registrados.")
        else:
            for cliente, info in servidor.items():
                print(f"Cliente: {cliente}")
                print(f" Teléfono: {info['telefono']}")
                print(" Mascotas:")
                if len(info["mascotas"]) == 0:
                    print("  No tiene mascotas registradas.")
                else:
                    for mascota, detalles in info["mascotas"].items():
                        print(f"  - {mascota} | {detalles['especie']} | {detalles['edad']} años | {detalles['peso']} kg")

    elif opcion == 4:
        # Buscar mascota
        cliente = input("Ingrese el nombre de el Cliente: ")
        if cliente in servidor:
            mascota = input("Ingrese el nombre de la mascota: ")
            if mascota in servidor[cliente]["mascotas"]:
                detalles = servidor[cliente]["mascotas"][mascota]
                print(f"Se encontro a {mascota}")
                print(f"Especie: {detalles['especie']}")
                print(f"Edad: {detalles['edad']} años")
                print(f"peso: {detalles['peso']}Kg")
            else:
                print(f"La mascota {mascota} no esta registrada")
        else:
            print(f"El cliente {cliente} no esta registrado")

    elif opcion == 5:
        # Calcular promedio de peso
        cliente = input("Ingrese el nombre de el Cliente: ")
        if cliente in servidor:
            mascotas = servidor[cliente]["mascotas"]
            if len(mascotas) == 0:
                print(f"El cliente {cliente} no tiene mascotas registradas.")
            else:
                total_peso = sum(detalles["peso"] for detalles in mascotas.values())
                promedio = total_peso / len(mascotas)
                print(f"El promedio de peso de las mascotas de {cliente} es {promedio:.2f} kg.")
        else:
            print(f"El cliente {cliente} no esta registrado")
    elif opcion == 6:
        # Encontrar mascota más pesada
        mascota_mas_pesada = None
        peso_maximo = -1
        for cliente, info in servidor.items():
            for mascota, detalles in info["mascotas"].items():
                if detalles["peso"] > peso_maximo:
                    peso_maximo = detalles["peso"]
                    mascota_mas_pesada = (mascota, cliente, detalles)
        if mascota_mas_pesada:
            print(f"La mascota más pesada es {mascota_mas_pesada[0]} del cliente {mascota_mas_pesada[1]} con un peso de {mascota_mas_pesada[2]['peso']} kg.")
        else:
            print("No hay mascotas registradas.")

    elif opcion == 7:
        # Eliminar mascota
        cliente = input("Ingrese el nombre de el Cliente: ")
        if cliente in servidor:
            mascota = input("Ingrese el nombre de la mascota a eliminar: ")
            if mascota in servidor[cliente]["mascotas"]:
                del servidor[cliente]["mascotas"][mascota]
                print(f"La mascota {mascota} ha sido eliminada del cliente {cliente}.")
            else:
                print(f"La mascota {mascota} no esta registrada para el cliente {cliente}.")
        else:
            print(f"El cliente {cliente} no esta registrado")

    elif opcion == 8:
        # Eliminar cliente
        cliente = input("Ingrese el nombre de el Cliente a eliminar: ")
        if cliente in servidor:
            del servidor[cliente]
            print(f"El cliente {cliente} ha sido eliminado.")
        else:
            print(f"El cliente {cliente} no esta registrado")

    elif opcion == 9:
        print("Saliendo del sistema. ¡Hasta luego!")

        # cuantas macotas tiene cada cliente
        for cliente, info in servidor.items():
            num_mascotas = len(info["mascotas"])
            print(f"El cliente {cliente} tiene {num_mascotas} mascota(s).")

        #Cliente con mas mascotas
        cliente_con_mas_mascotas = None
        max_mascotas = -1
        for cliente, info in servidor.items():
            num_mascotas = len(info["mascotas"])
            if num_mascotas > max_mascotas:
                max_mascotas = num_mascotas
                cliente_con_mas_mascotas = cliente
        if cliente_con_mas_mascotas:
            print(f"El cliente con más mascotas es {cliente_con_mas_mascotas} con {max_mascotas} mascota(s).")

        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 9.")

            

