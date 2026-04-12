from abc import ABC, abstractmethod
from http import client

class Persona (ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def hablar(self):
        pass
    
class Veterinario(Persona):
    
    def mostrar_nombre(self):
        print(f"veterinario {self.nombre}")

    def hablar(self):
        return f"{self.nombre} esta hablando con un cliente"

    def atender(self):
        return f"{self.nombre} esta atendiendo a una mascota"

class Mascota:
    def __init__(self,nombre,especie):
        self.nombre = nombre
        self.especie = especie

    def mostrar_info(self):
        return f"Nombre: {self.nombre} Especie: {self.especie}"
    
class Consulta:
    def __init__(self, mascota, motivo):
        self.mascota = mascota
        self.motivo = motivo

    def mostrar_info(self):
        return f"Consulta para {self.mascota.nombre} ({self.mascota.especie}) por {self.motivo}"
    
class Ciente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mascotas = []

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def mostrar_mascotas(self):
        print(f"Cliente: {self.nombre} tiene las siguientes mascotas:")
        for mascota in self.mascotas:
            print(mascota.mostrar_info())

cliente1 = Ciente("Juan")
mascota1 = Mascota("Firulais", "Canino")
mascota2 = Mascota("Michi", "Felino")

cliente1.agregar_mascota(mascota1)
cliente1.agregar_mascota(mascota2)

veterinario1 = Veterinario("Dr. Smith") 
consulta1 = Consulta(mascota1, "Vacunación")

cliente1.mostrar_mascotas()

print(f"{veterinario1.atender()}")
print(consulta1.mostrar_info())