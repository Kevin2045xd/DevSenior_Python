"""
Ejercicio grupal: Sistema de gestión de hospital veterinario
Contexto

Una clínica veterinaria quiere desarrollar un sistema orientado a objetos para organizar su funcionamiento diario. El sistema debe permitir gestionar personas, mascotas, consultas, tratamientos, pagos y hospitalizaciones.

Los estudiantes deben analizar el problema, identificar las clases, construir el modelo UML y luego implementar una versión funcional en Python.

Objetivo del ejercicio

Diseñar e implementar un sistema en Python que permita modelar el funcionamiento básico de un hospital veterinario, aplicando correctamente relaciones entre clases y principios de POO.

Lo que debe incluir obligatoriamente
1. Clase abstracta

Debe existir una clase abstracta llamada Persona.

De ella deben heredar otras clases.

Atributos sugeridos:
nombre
documento
Método abstracto obligatorio:
mostrar_rol()
2. Herencia

Desde Persona deben heredar al menos estas clases:

Veterinario
Recepcionista
Cliente

Cada una debe implementar mostrar_rol() de forma diferente.

3. Asociación

Debe existir una relación de asociación entre:

Veterinario y Mascota

porque un veterinario puede atender muchas mascotas y una mascota puede ser atendida por distintos veterinarios en diferentes momentos.

Esa relación puede reflejarse en la clase Consulta, donde se conectan ambas clases.

4. Agregación

Debe existir una relación de agregación entre:

Cliente y Mascota

porque un cliente tiene mascotas, pero la mascota puede seguir existiendo aunque el cliente se elimine del sistema.

El cliente debe tener un atributo como:

mascotas = []

y un método:

agregar_mascota()
5. Composición

Debe existir una relación de composición entre:

Consulta y Tratamiento

porque una consulta crea sus tratamientos como parte de sí misma.

La idea es que el tratamiento nazca dentro de la consulta.

La clase Consulta puede tener:

lista de tratamientos
método crear_tratamiento()
6. Polimorfismo

Debe existir una clase abstracta llamada MetodoPago.

De ella deben heredar:

PagoEfectivo
PagoTarjeta
PagoTransferencia

Cada una debe implementar el método:

procesar_pago(monto)

Luego una clase Factura debe usar cualquier objeto de tipo MetodoPago para cobrar una consulta.

Clases mínimas sugeridas

Los estudiantes deben trabajar, como mínimo, con estas clases:

Persona (abstracta)
Veterinario
Recepcionista
Cliente
Mascota
Consulta
Tratamiento
Factura
MetodoPago (abstracta)
PagoEfectivo
PagoTarjeta
PagoTransferencia
Reglas del sistema
Persona

Clase abstracta.

Atributos:
nombre
documento
Método abstracto:
mostrar_rol()
Veterinario

Hereda de Persona.

Atributos:
especialidad
Métodos:
mostrar_rol()
atender_mascota()
Recepcionista

Hereda de Persona.

Métodos:
mostrar_rol()
registrar_cliente()
Cliente

Hereda de Persona.

Atributos:
telefono
lista de mascotas
Métodos:
mostrar_rol()
agregar_mascota()
mostrar_mascotas()
Mascota
Atributos:
nombre
especie
edad
peso
Métodos:
mostrar_info()
Consulta
Atributos:
mascota
veterinario
motivo
diagnostico
tratamientos
Métodos:
crear_tratamiento()
mostrar_resumen()
calcular_costo_consulta()

Aquí se evidencia:

asociación con Mascota
asociación con Veterinario
composición con Tratamiento
Tratamiento
Atributos:
nombre
costo
duracion_dias
Métodos:
mostrar_tratamiento()
MetodoPago

Clase abstracta.

Método abstracto:
procesar_pago(monto)
PagoEfectivo

Hereda de MetodoPago.

PagoTarjeta

Hereda de MetodoPago.

PagoTransferencia

Hereda de MetodoPago.

Cada una debe implementar procesar_pago() de forma distinta.

Factura
Atributos:
consulta
subtotal
impuesto
total
Métodos:
calcular_total()
pagar(metodo_pago)

Aquí se debe aplicar polimorfismo.
"""

from abc import ABC, abstractmethod

# ======================
# CLASE ABSTRACTA PERSONA
# ======================
class Persona(ABC):
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    @abstractmethod
    def mostrar_rol(self):
        pass

# ======================
# HERENCIA
# ======================
class Veterinario(Persona):
    def __init__(self, nombre, documento, especialidad):
        super().__init__(nombre, documento)
        self.especialidad = especialidad

    def mostrar_rol(self):
        return f"Veterinario - Especialidad: {self.especialidad}"

    def atender_mascota(self, mascota):
        print(f"El veterinario {self.nombre} atiende a {mascota.nombre}")


class Recepcionista(Persona):
    def mostrar_rol(self):
        return "Recepcionista"

    def registrar_cliente(self, cliente):
        print(f"Cliente {cliente.nombre} registrado correctamente.")


class Cliente(Persona):
    def __init__(self, nombre, documento, telefono):
        super().__init__(nombre, documento)
        self.telefono = telefono
        self.mascotas = []  # AGREGACIÓN

    def mostrar_rol(self):
        return "Cliente"

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)
        print(f"Mascota {mascota.nombre} agregada a {self.nombre}")

    def mostrar_mascotas(self):
        for m in self.mascotas:
            print(m.mostrar_info())

# ======================
# MASCOTA
# ======================
class Mascota:
    def __init__(self, nombre, especie, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def mostrar_info(self):
        return f"Mascota: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}, Peso: {self.peso}kg"

# ======================
# TRATAMIENTO
# ======================
class Tratamiento:
    def __init__(self, nombre, costo, duracion_dias):
        self.nombre = nombre
        self.costo = costo
        self.duracion_dias = duracion_dias

    def mostrar_tratamiento(self):
        return f"Tratamiento: {self.nombre}, Costo: {self.costo}, Duración: {self.duracion_dias} días"

# ======================
# CONSULTA (ASOCIACIÓN + COMPOSICIÓN)
# ======================
class Consulta:
    def __init__(self, mascota, veterinario, motivo, diagnostico):
        self.mascota = mascota
        self.veterinario = veterinario
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.tratamientos = []  # COMPOSICIÓN

    def crear_tratamiento(self, nombre, costo, duracion_dias):
        tratamiento = Tratamiento(nombre, costo, duracion_dias)
        self.tratamientos.append(tratamiento)

    def mostrar_resumen(self):
        print(f"Consulta de {self.mascota.nombre}")
        print(f"Veterinario: {self.veterinario.nombre}")
        print(f"Motivo: {self.motivo}")
        print(f"Diagnóstico: {self.diagnostico}")
        print("Tratamientos:")
        for t in self.tratamientos:
            print(" -", t.mostrar_tratamiento())

    def calcular_costo_consulta(self):
        total = sum(t.costo for t in self.tratamientos)
        return total

# ======================
# MÉTODO DE PAGO (POLIMORFISMO)
# ======================
class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass


class PagoEfectivo(MetodoPago):
    def procesar_pago(self, monto):
        return f"Pago en efectivo realizado por ${monto}"


class PagoTarjeta(MetodoPago):
    def procesar_pago(self, monto):
        return f"Pago con tarjeta aprobado por ${monto}"


class PagoTransferencia(MetodoPago):
    def procesar_pago(self, monto):
        return f"Pago por transferencia realizado por ${monto}"

# ======================
# FACTURA
# ======================
class Factura:
    def __init__(self, consulta):
        self.consulta = consulta
        self.subtotal = consulta.calcular_costo_consulta()
        self.impuesto = 0.19  # 19%
        self.total = 0

    def calcular_total(self):
        self.total = self.subtotal + (self.subtotal * self.impuesto)
        return self.total

    def pagar(self, metodo_pago: MetodoPago):
        total = self.calcular_total()
        print(metodo_pago.procesar_pago(total))

# ======================
# PRUEBA DEL SISTEMA
# ======================
if __name__ == "__main__":
    # Crear personas
    vet = Veterinario("Dr. Juan", "123", "Cirugía")
    cliente = Cliente("Carlos", "456", "3001234567")
    recep = Recepcionista("Ana", "789")

    # Registrar cliente
    recep.registrar_cliente(cliente)

    # Crear mascotas 
    mascota1 = Mascota("Firulais", "Perro", 5, 12)
    mascota2 = Mascota("Michi", "Gato", 3, 4)

    cliente.agregar_mascota(mascota1)
    cliente.agregar_mascota(mascota2)

    # Mostrar mascotas
    cliente.mostrar_mascotas()

    # Veterinario atiende UNA mascota 
    vet.atender_mascota(mascota1)

    # Crear consulta
    consulta = Consulta(mascota1, vet, "Dolor", "Infección")

    # Crear tratamientos 
    consulta.crear_tratamiento("Antibiótico", 50000, 7)
    consulta.crear_tratamiento("Vitaminas", 20000, 5)

    consulta.mostrar_resumen()

    # Factura
    factura = Factura(consulta)

    print("Total a pagar:", factura.calcular_total())

    # Pago 1 (tarjeta) 
    pago1 = PagoTarjeta()
    factura.pagar(pago1)

    # Pago 2 (efectivo) 
    pago2 = PagoEfectivo()
    factura.pagar(pago2)