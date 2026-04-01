class Animal:
    def __init__(self,nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "Hace sonido generico"

"""
a = Animal("Trosky")
a.hacer_sonido()
print(a.nombre)
"""

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"

class Gato(Animal):
    def __init__(self,nombre,edad):
        super().__init__(nombre)
        self.edad = edad


p = Perro("Trosky")
print(f"{p.nombre} dice", p.hacer_sonido())


a = Animal("Firulais")
print(f"{a.nombre} dice", a.hacer_sonido() )

g = Gato("Garfield",5)
print(f"")
print(g.edad)

