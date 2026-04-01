class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
        

    def acelerar(self):
        return "El vehículo ha alcanzado 80 km/h"

class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo

    def acelerar(self):
        return "El coche ha alcanzado 120 km/h"

    def pilolear(self):
        return "El coche está piloteando"
    
class Moto(Vehiculo):
    def __init__(self, marca, tipo):
        super().__init__(marca)
        self.tipo = tipo

    def acelerar(self):
        return "La moto ha alcanzado 100 km/h"

    def hacer_caballito(self):
        return "La moto está haciendo un caballito"
    
class Camion(Vehiculo):
    def __init__(self, marca, capacidad):
        super().__init__(marca)
        self.capacidad = capacidad

    def acelerar(self):
        return "El camión ha alcanzado 60 km/h"

    def cargar(self):
        return "El camión está cargando"

v = Vehiculo("Toyota")
print(f"{v.marca} hace", v.acelerar())

c = Coche("Honda", "Civic")
print(f"{c.marca} {c.modelo} hace", c.acelerar())
print(c.pilolear())

m = Moto("Yamaha", "Deportiva")
print(f"{m.marca} {m.tipo} hace", m.acelerar())
print(m.hacer_caballito())

camion = Camion("Volvo", "20 toneladas")
print(f"{camion.marca} con capacidad de {camion.capacidad} hace", camion.acelerar())
print(camion.cargar())