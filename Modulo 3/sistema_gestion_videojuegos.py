"""
Ejercicio Integrador en Python
Sistema de Gestión de una Tienda de Videojuegos
Objetivo
Desarrollar un programa en Python que permita administrar el inventario y las ventas de una tienda de videojuegos utilizando:
Variables
Condicionales (if, elif, else)
Ciclos (while, for)
Funciones
Colecciones (diccionarios y listas)
Enunciado del Problema
Una tienda de videojuegos desea llevar el control de sus productos y ventas.
Cada videojuego tendrá la siguiente información:
Código
Nombre
Plataforma (PC, PlayStation, Xbox, Nintendo)
Precio
Cantidad en inventario
La información se almacenará en un diccionario con la siguiente estructura:
Python
videojuegos = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10
    }
}
Menú Principal
El programa debe mostrar repetidamente el siguiente menú:
Plain text
===== TIENDA DE VIDEOJUEGOS =====
1. Agregar videojuego
2. Mostrar inventario
3. Buscar videojuego por código
4. Actualizar precio
5. Registrar venta
6. Mostrar estadísticas
7. Eliminar videojuego
8. Salir
Requisitos del Programa
1. Agregar videojuego
Crear una función que solicite los datos del videojuego y lo agregue al diccionario.
Validaciones:
No se debe permitir un código repetido.
El precio y la cantidad deben ser mayores que cero.
2. Mostrar inventario
Recorrer el diccionario e imprimir todos los videojuegos registrados.
3. Buscar videojuego por código
Solicitar un código y mostrar toda la información del videojuego si existe.
4. Actualizar precio
Permitir cambiar el precio de un videojuego existente.
5. Registrar venta
Solicitar:
Código del videojuego
Cantidad a vender
Validaciones:
El videojuego debe existir.
Debe haber suficiente inventario.
Acciones:
Restar del inventario.
Calcular el valor total de la venta.
Mostrar factura.
6. Mostrar estadísticas
Crear una función que muestre:
Total de videojuegos registrados.
Valor total del inventario.
Videojuego más costoso.
Videojuego con mayor cantidad disponible.
Promedio de precios.
7. Eliminar videojuego
Eliminar un videojuego por código.
8. Salir
Finalizar el programa.
Requisitos Técnicos
Funciones obligatorias
Debes implementar al menos las siguientes funciones:
Python
def agregar_videojuego(videojuegos):
def mostrar_inventario(videojuegos):
def buscar_videojuego(videojuegos):
def actualizar_precio(videojuegos):
def registrar_venta(videojuegos):
def mostrar_estadisticas(videojuegos):
def eliminar_videojuego(videojuegos):
def menu():
Datos Iniciales de Prueba
Python
videojuegos = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10
    },
    "VG002": {
        "nombre": "Zelda: Breath of the Wild",
        "plataforma": "Nintendo Switch",
        "precio": 220000,
        "cantidad": 5
    },
    "VG003": {
        "nombre": "Forza Horizon 5",
        "plataforma": "Xbox Series X",
        "precio": 210000,
        "cantidad": 8
    }
}
Ejemplo de Venta
Plain text
Ingrese código del videojuego: VG001
Ingrese cantidad a vender: 2

Factura:
Juego: FIFA 26
Precio unitario: $250000
Cantidad: 2
Total: $500000
Retos Adicionales (Opcionales)
Si terminas antes, agrega:
Buscar videojuegos por plataforma.
Mostrar videojuegos con inventario bajo (cantidad < 3).
Aplicar descuentos del 10% en ventas mayores a $500.000.
Guardar historial de ventas en una lista.
Mostrar el videojuego más vendido.
Conceptos que Practicarás
Diccionarios anidados
Listas
Funciones con parámetros y retorno
Condicionales
Ciclos while y for
Validación de datos
Cálculos estadísticos básicos
Nivel de Dificultad
Intermedio
Tiempo Estimado
2 a 3 horas
Resultado Esperado
Al finalizar tendrás un sistema completo de consola para administrar una tienda de videojuegos,
aplicando de forma práctica los principales fundamentos de Python.
"""

# Datos iniciales de prueba
videojuegos = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10
    },
    "VG002": {
        "nombre": "Zelda: Breath of the Wild",
        "plataforma": "Nintendo Switch",
        "precio": 220000,
        "cantidad": 5
    },
    "VG003": {
        "nombre": "Forza Horizon 5",
        "plataforma": "Xbox Series X",
        "precio": 210000,
        "cantidad": 8
    }
}
# Lista para registrar ventas
ventas = []

# Función para agregar un nuevo videojuego al inventario
def agregar_videojuego():

    codigo = input("Ingrese el codigo de el videojuego: ")
    if codigo in  videojuegos:
        print("El codigo ya existe")
        return
    
    nombre = input("Ingrese el nombre de el videojuego: ")
    plataforma = input("Ingrese la plataforma de el videojuego: ")
    cantidad = int(input("Ingrese la cantidad en inventario: "))
    if cantidad <= 0:
        print("La cantidad debe ser mayor que cero.")
        return
    
    precio = float(input("Ingrese el precio de el videojuego: "))
    if precio <= 0:
        print("El precio debe ser mayor que cero.")
        return
    
    videojuegos[codigo] = {
        "nombre": nombre,
        "plataforma": plataforma,
        "precio": precio,
        "cantidad": cantidad
    }
    print(f"Videojuego {nombre} agregado exitosamente.")

# Función para mostrar el inventario de videojuegos
def mostrar_inventario():
    if len(videojuegos) == 0:
        print("no hay videojuegos disponibles")
        return
    for videojuego, detalles in videojuegos.items():
        print(f"Videojuego: {detalles['nombre']}")
        print(f"Cantidad: {detalles['cantidad']}")
        print(f"Plataforma: {detalles['plataforma']}")
        print("-------------------------------")

def buscar_por_codigo():
    codigo = input("Ingrese el codigo de el videojuego: ")
    if codigo in videojuegos:
        detalles = videojuegos[codigo]
        print(f"Videojuego: {detalles['nombre']}")
        print(f"Cantidad: {detalles['cantidad']}")
        print(f"Plataforma: {detalles['plataforma']}")
        print(f"Precio: {detalles['precio']}")
    else:
        print("El videojuego no existe.")

# Función para actualizar el precio de un videojuego existente
def actualizar_precio():
    codigo = input("Ingrese el codigo de el videojuego: ")
    if codigo in videojuegos:
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        if nuevo_precio <= 0:
            print("El precio debe ser mayor que cero.")
            return
        videojuegos[codigo]["precio"] = nuevo_precio
        print(f"Precio de {videojuegos[codigo]['nombre']} actualizado a {nuevo_precio}.")
    else:
        print("El videojuego no existe.")

# Función para registrar una venta de un videojuego
# aplicando descuento y registrando la venta en una lista de ventas
def registrar_venta():
    codigo = input("Ingrese el codigo de el videojuego: ")
    if codigo in videojuegos:
        cantidad_a_vender = int(input("Ingrese la cantidad a vender: "))
        if cantidad_a_vender <= 0:
            print("La cantidad a vender debe ser mayor que cero.")
            return
        if videojuegos[codigo]["cantidad"] >= cantidad_a_vender:
            precio_unitario = videojuegos[codigo]["precio"]
            total_venta = precio_unitario * cantidad_a_vender
            if total_venta > 500000:
                total_venta *= 0.9  # Aplicar descuento del 10%
                print("Se aplicó un descuento del 10% por ser una venta mayor a $500.000.")
            videojuegos[codigo]["cantidad"] -= cantidad_a_vender
            ventas.append({
                "codigo": codigo,
                "nombre": videojuegos[codigo]["nombre"],
                "precio_unitario": precio_unitario,
                "cantidad": cantidad_a_vender,
                "total": total_venta
            })
            print("Factura:")
            print(f"Juego: {videojuegos[codigo]['nombre']}")
            print(f"Precio unitario: ${precio_unitario}")
            print(f"Cantidad: {cantidad_a_vender}")
            print(f"Total: ${total_venta:.2f}")
        else:
            print("No hay suficiente inventario para realizar la venta.")
    else:
        print("El videojuego no existe.")

# Función para mostrar estadísticas de los videojuegos registrados
def mostrar_estadisticas():
    total_videojuegos = len(videojuegos)
    valor_total_inventario = 0
    for videojuego,detalles in videojuegos.items():
        valor_total_inventario += detalles["precio"] * detalles["cantidad"]
    juego_mas_costoso = ""
    precio = 0
    for videojuego, detalles in videojuegos.items():
        if detalles["precio"] > precio:
            juego_mas_costoso = detalles["nombre"]
            precio = detalles["precio"]
    videojuego_mas_cantidad = ""
    cantidad = 0
    for videojuego, detalles in videojuegos.items():
        if detalles["cantidad"] > cantidad:
            videojuego_mas_cantidad = detalles["nombre"]
            cantidad = detalles["cantidad"]
    promedio_precios = 0
    suma_precios = 0
    for videojuego, detalles in videojuegos.items():
        suma_precios += detalles["precio"]
        
    promedio_precios = suma_precios / total_videojuegos if total_videojuegos > 0 else 0


        
    
    print(f"Total de videojuegos registrados: {total_videojuegos}")
    print(f"Valor total del inventario: ${valor_total_inventario}")
    print(f"Juego más costoso: {juego_mas_costoso} con un precio de ${precio}")
    print(f"Videojuego con mayor cantidad disponible: {videojuego_mas_cantidad} con una cantidad de {cantidad}")
    print(f"Promedio de precios: ${promedio_precios:.2f}")


# Función para eliminar un videojuego por código
def eliminar_videojuego():
    codigo = input("Ingrese el codigo de el videojuego: ")
    if codigo in videojuegos:
        del videojuegos[codigo]
        print("Videojuego eliminado exitosamente.")
    else:
        print("El videojuego no existe.")

# Funcion para buscar un videojuego por Plataforma
def buscar_por_plataforma():
    plataforma = input("Ingrese la plataforma de el videojuego: ")
    encontrados = []
    for videojuego, detalles in videojuegos.items():
        if detalles["plataforma"].lower() == plataforma.lower():
            encontrados.append(detalles)
    if len(encontrados) > 0:
        print(f"Videojuegos encontrados en la plataforma {plataforma}:")
        for juego in encontrados:
            print(f"Nombre: {juego['nombre']}, Precio: ${juego['precio']}, Cantidad: {juego['cantidad']}")
    else:
        print(f"No se encontraron videojuegos en la plataforma {plataforma}.")

#Función para mostrar videojuegos con inventario bajo (cantidad < 3)
def mostrar_inventario_bajo():
    print("Videojuegos con inventario bajo (cantidad < 3):")
    cantidad = 0
    for videojuego, detalles in videojuegos.items():
        if detalles["cantidad"] < 3:
            cantidad += 1
            print(f"Nombre: {detalles['nombre']}, Plataforma: {detalles['plataforma']}, Cantidad: {detalles['cantidad']}")
    if cantidad == 0:
        print("No hay videojuegos con inventario bajo.")

# Funcion para mostrar el juego más vendido
def mostrar_juego_mas_vendido():
    ventas_por_juego = {}
    for venta in ventas:
        codigo = venta["codigo"]
        cantidad_vendida = venta["cantidad"]
        if codigo in ventas_por_juego:
            ventas_por_juego[codigo] += cantidad_vendida 
        else:
            ventas_por_juego[codigo] = cantidad_vendida
    juego_mas_vendido = max(ventas_por_juego, key=ventas_por_juego.get)
    cantidad_mas_vendida = ventas_por_juego[juego_mas_vendido]
    print(f"El juego más vendido es {videojuegos[juego_mas_vendido]['nombre']} con {cantidad_mas_vendida} unidades vendidas.")

#Funcion para mostrar el regidtro de ventas
def mostrar_registro_ventas():
    print("Registro de ventas:")
    for venta in ventas:
        print(f"Juego: {venta['nombre']}, Precio unitario: ${venta['precio_unitario']}, Cantidad: {venta['cantidad']}, Total: ${venta['total']:.2f}")
# Función para mostrar el menú principal
def menu():
    while True:
        print("===== TIENDA DE VIDEOJUEGOS =====")
        print("1. Agregar videojuego")
        print("2. Mostrar inventario")
        print("3. Buscar videojuego por código")
        print("4. Actualizar precio")
        print("5. Registrar venta")
        print("6. Mostrar estadísticas")
        print("7. Eliminar videojuego")
        print("8. Buscar videojuego por plataforma")
        print("9. Mostrar videojuegos con inventario bajo")
        print("10. Mostrar juego más vendido")
        print("11. Mostrar registro de ventas")
        print("12. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_videojuego()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            buscar_por_codigo()
        elif opcion == "4":
            actualizar_precio()
        elif opcion == "5":
            registrar_venta()
        elif opcion == "6":
            mostrar_estadisticas()
        elif opcion == "7":
            eliminar_videojuego()
        elif opcion == "8":
            buscar_por_plataforma()
        elif opcion == "9":
            mostrar_inventario_bajo()
        elif opcion == "10":
            mostrar_juego_mas_vendido()
        elif opcion == "11":
            mostrar_registro_ventas()
        elif opcion == "12":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 12.")

# Ejecutar el menú principal
menu()