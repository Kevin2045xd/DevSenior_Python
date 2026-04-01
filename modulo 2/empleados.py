from abc import ABC, abstractmethod


class Trabajable(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class Empleado(ABC):

    def __init__ (self, nombre, salario_fijo):
        self.nombre = nombre
        self.salario_fijo = salario_fijo
    @abstractmethod
    def calcular_salario(self):
        pass

class Gerente(Empleado, Trabajable):
    def __init__(self, nombre, salario_fijo, bono):
        super().__init__(nombre, salario_fijo)
        self.bono = bono
        

    def calcular_salario(self):
        return self.salario_fijo + self.bono

    def trabajar(self):
        print(f"{self.nombre} está gerenciando el equipo.")

class Desarrollador(Empleado, Trabajable):
    def __init__(self, nombre, salario_fijo, lenguaje):
        super().__init__(nombre, salario_fijo)
        self.lenguaje = lenguaje


    def calcular_salario(self):
        return self.salario_fijo

    def trabajar(self):
        print(f"{self.nombre} está desarrollando código en {self.lenguaje}.")

class Diseñador(Empleado, Trabajable):
    def __init__(self, nombre, salario_fijo, especializacion):
        super().__init__(nombre, salario_fijo)

        self.especializacion = especializacion

    def calcular_salario(self):
        return self.salario_fijo
    
    def trabajar(self):
        print( self.nombre, "esta trabajando en ", self.especializacion)


empleados = [
    Gerente("Alice", 5000, 2000),
    Desarrollador("Bob", 3000, "Python"),
    Desarrollador("Charlie", 3200, "Java"),
    Diseñador("Raul",2700, "renderizado")
]

for empleado in empleados:
    empleado.trabajar()
    print("Salario:", empleado.calcular_salario())
    print("----------")
