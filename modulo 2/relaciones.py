# Relacion de asociacion
"""
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

class Pedido:
    def __init__(self, cliente, ):
        self.cliente = cliente

c1 = Cliente("Juan")
p1 = Pedido(c1)


# Relacion de agregacion (debil)

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

class Restaurante:
    def __init__(self,):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado) 

e = Empleado("Maria")
r = Restaurante()
r.agregar_empleado(e)



# Relacion de composicion (fuerte)

class Plato:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Pedido:
    def __init__(self, ):
        self.platos = []

    def agregar_plato(self, nombre, precio):
        plato = Plato(nombre, precio)
        self.platos.append(plato)


# p = Plato("Bandeja Paisa", 25000) Esto no se puede hacer porque el plato solo existe dentro del pedido

pedido = Pedido()
pedido.agregar_plato("sancocho", 15000)
pedido.agregar_plato("arroz con pollo", 20000)
"""

from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_salario(self):
        pass

class Mesero(Empleado):
    def calcular_salario(self):
        return 1000
    
class Cocinero(Empleado):
    def calcular_salario(self):
        return 2000
    
    