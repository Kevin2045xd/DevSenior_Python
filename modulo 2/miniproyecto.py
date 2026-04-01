class Producto:
    def __init__(self, id, nombre, precio, stock):
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    # Getters
    def get_id(self):
        return self.__id


    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_precio(self, precio):
        if precio > 0:
            self.__precio = precio
        else:
            print("El precio debe ser mayor que 0")

    def set_stock(self, stock):
        if stock >= 0:
            self.__stock = stock
        else:
            print("El stock no puede ser negativo")

    # Método para vender
    def vender(self, cantidad):
        if cantidad <= self.__stock:
            self.__stock -= cantidad
            print(f"Venta exitosa. Stock restante: {self.__stock}")
        else:
            print("Stock insuficiente")

    # Método para mostrar info
    def mostrar_info(self):
        print(f"ID: {self.__id} | Nombre: {self.__nombre} | Precio: ${self.__precio} | Stock: {self.__stock}")


class GestorProductos:
    def __init__(self):
        self.__productos = []

    # Crear producto
    def crear_producto(self, id, nombre, precio, stock):
        producto = Producto(id, nombre, precio, stock)
        self.__productos.append(producto)
        print(f"Producto '{nombre}' creado exitosamente")

    # Mostrar todos los productos
    def mostrar_productos(self):
        if not self.__productos:
            print("No hay productos registrados")
            return
        print("\n=== LISTA DE PRODUCTOS ===")
        for producto in self.__productos:
            producto.mostrar_info()
        print("=" * 30)

    # Buscar producto por ID
    def buscar_producto(self, id):
        for producto in self.__productos:
            if producto.get_id() == id:
                return producto
        return None

    # Actualizar precio
    def actualizar_precio(self, id, nuevo_precio):
        producto = self.buscar_producto(id)
        if producto:
            producto.set_precio(nuevo_precio)
            print(f"Precio actualizado a ${nuevo_precio}")
        else:
            print("Producto no encontrado")

    # Actualizar stock
    def actualizar_stock(self, id, nuevo_stock):
        producto = self.buscar_producto(id)
        if producto:
            producto.set_stock(nuevo_stock)
            print(f"Stock actualizado a {nuevo_stock}")
        else:
            print("Producto no encontrado")

    # Vender producto
    def vender_producto(self, id, cantidad):
        producto = self.buscar_producto(id)
        if producto:
            producto.vender(cantidad)
        else:
            print("Producto no encontrado")

    # Eliminar producto
    def eliminar_producto(self, id):
        for i, producto in enumerate(self.__productos):
            if producto.get_id() == id:
                nombre = producto.get_nombre()
                self.__productos.pop(i)
                print(f"Producto '{nombre}' eliminado")
                return
        print("Producto no encontrado")


# Función principal con menú
def main():
    gestor = GestorProductos()
    
    while True:
        print("\n" + "=" * 40)
        print("     SISTEMA DE GESTIÓN DE PRODUCTOS")
        print("=" * 40)
        print("1. Crear producto")
        print("2. Mostrar todos los productos")
        print("3. Buscar producto por ID")
        print("4. Actualizar precio")
        print("5. Actualizar stock")
        print("6. Vender producto")
        print("7. Eliminar producto")
        print("8. Salir")
        print("=" * 40)
        
        opcion = input("Selecciona una opción (1-8): ").strip()
        
        if opcion == "1":
            try:
                id_producto = int(input("ID del producto: "))
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio del producto: "))
                stock = int(input("Stock inicial: "))
                gestor.crear_producto(id_producto, nombre, precio, stock)
            except ValueError:
                print("Error: Ingresa valores válidos")
        
        elif opcion == "2":
            gestor.mostrar_productos()
        
        elif opcion == "3":
            try:
                id_buscar = int(input("Ingresa el ID a buscar: "))
                producto = gestor.buscar_producto(id_buscar)
                if producto:
                    print("\nProducto encontrado:")
                    producto.mostrar_info()
                else:
                    print("Producto no encontrado")
            except ValueError:
                print("Error: Ingresa un ID válido")
        
        elif opcion == "4":
            try:
                id_producto = int(input("ID del producto: "))
                nuevo_precio = float(input("Nuevo precio: "))
                gestor.actualizar_precio(id_producto, nuevo_precio)
            except ValueError:
                print("Error: Ingresa valores válidos")
        
        elif opcion == "5":
            try:
                id_producto = int(input("ID del producto: "))
                nuevo_stock = int(input("Nuevo stock: "))
                gestor.actualizar_stock(id_producto, nuevo_stock)
            except ValueError:
                print("Error: Ingresa un valor válido")
        
        elif opcion == "6":
            try:
                id_producto = int(input("ID del producto: "))
                cantidad = int(input("Cantidad a vender: "))
                gestor.vender_producto(id_producto, cantidad)
            except ValueError:
                print("Error: Ingresa valores válidos")
        
        elif opcion == "7":
            try:
                id_producto = int(input("ID del producto a eliminar: "))
                gestor.eliminar_producto(id_producto)
            except ValueError:
                print("Error: Ingresa un ID válido")
        
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Intenta de nuevo")


main()