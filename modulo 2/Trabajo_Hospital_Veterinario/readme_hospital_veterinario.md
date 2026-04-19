# README.md

## Sistema de Gestión de Hospital Veterinario 🐾

**Autor:** Kevin Stick Castellanos Castellanos

Este proyecto consiste en el desarrollo de un sistema orientado a objetos en Python que simula el funcionamiento básico de una clínica veterinaria.

El programa permite registrar personas, mascotas, consultas, tratamientos, facturación y pagos, aplicando correctamente los principios de Programación Orientada a Objetos (POO).

---

# Funcionamiento del programa

## 1. Gestión de personas

La clase principal es `Persona`, la cual sirve como base para representar a todas las personas del sistema.

De esta clase se derivan:

- `Veterinario`
- `Recepcionista`
- `Cliente`

Cada una tiene un rol diferente dentro del programa.

---

## 2. Registro de clientes

La recepcionista utiliza el método `registrar_cliente()` para registrar nuevos clientes en el sistema.

Después del registro, el cliente puede comenzar a asociar mascotas.

---

## 3. Registro de mascotas

Cada cliente puede agregar una o varias mascotas mediante:

`agregar_mascota()`

Cada mascota almacena:

- nombre
- especie
- edad
- peso

También se pueden visualizar con:

`mostrar_mascotas()`

---

## 4. Atención veterinaria

El veterinario atiende mascotas mediante:

`atender_mascota()`

Después de la atención se genera una consulta médica.

---

## 5. Consultas

La clase `Consulta` guarda toda la información relacionada con la atención médica:

- mascota atendida
- veterinario encargado
- motivo de consulta
- diagnóstico
- tratamientos formulados

También permite mostrar un resumen y calcular el costo total.

---

## 6. Tratamientos

Durante la consulta se crean tratamientos usando:

`crear_tratamiento()`

Cada tratamiento contiene:

- nombre
- costo
- duración en días

---

## 7. Facturación

Cuando finaliza la consulta se genera una factura.

La factura calcula:

- subtotal
- impuesto
- total a pagar

---

## 8. Pago

El sistema permite pagar con distintos métodos:

- efectivo
- tarjeta
- transferencia

Cada uno procesa el pago de forma diferente.

---

# Relaciones entre clases

# 1. Herencia

## Clases relacionadas:

- `Persona` → `Veterinario`
- `Persona` → `Recepcionista`
- `Persona` → `Cliente`

## ¿Cómo funciona?

La clase `Persona` contiene atributos comunes como:

- nombre
- documento

Las clases hijas heredan esos atributos y además agregan comportamientos propios.

### Ejemplo:

- `Veterinario` añade especialidad.
- `Recepcionista` registra clientes.
- `Cliente` administra mascotas.

---

# 2. Abstracción

## Clases relacionadas:

- `Persona`
- `MetodoPago`

## ¿Cómo funciona?

Estas clases fueron creadas como abstractas, lo que significa que no se usan directamente para crear objetos.

Sirven como plantilla obligatoria para otras clases.

### Ejemplo:

Toda clase que herede de `Persona` debe implementar:

`mostrar_rol()`

Toda clase que herede de `MetodoPago` debe implementar:

`procesar_pago()`

---

# 3. Asociación

## Clases relacionadas:

- `Consulta` ↔ `Mascota`
- `Consulta` ↔ `Veterinario`

## ¿Cómo funciona?

La clase `Consulta` necesita recibir una mascota y un veterinario para poder existir.

Cuando se crea una consulta, se conecta:

- qué mascota será atendida
- qué veterinario la atenderá

Esto representa una relación de trabajo entre clases independientes.

### Ejemplo:

Una mascota puede tener varias consultas con distintos veterinarios.

Un veterinario puede atender muchas mascotas.

---

# 4. Agregación

## Clases relacionadas:

- `Cliente` ◇── `Mascota`

## ¿Cómo funciona?

Un cliente contiene una lista de mascotas:

`mascotas = []`

Esto significa que el cliente agrupa mascotas dentro del sistema.

Sin embargo, las mascotas pueden existir por separado.

Si el cliente se elimina, la mascota no desaparece automáticamente.

### Ejemplo:

Primero se crea una mascota y luego se agrega al cliente.

---

# 5. Composición

## Clases relacionadas:

- `Consulta` ◆── `Tratamiento`

## ¿Cómo funciona?

Los tratamientos se crean directamente dentro de la consulta mediante:

`crear_tratamiento()`

Eso significa que el tratamiento pertenece a esa consulta específica.

No se crea por separado desde afuera.

Si la consulta desaparece, sus tratamientos también dejan de tener sentido.

---

# 6. Polimorfismo

## Clases relacionadas:

- `MetodoPago`
- `PagoEfectivo`
- `PagoTarjeta`
- `PagoTransferencia`
- `Factura`

## ¿Cómo funciona?

La factura puede recibir cualquier objeto de tipo método de pago.

Todos tienen el método:

`procesar_pago(monto)`

Pero cada clase responde diferente.

### Ejemplo:

- Efectivo → confirma pago en efectivo.
- Tarjeta → aprueba pago con tarjeta.
- Transferencia → confirma transferencia.

La clase `Factura` no necesita saber qué tipo de pago recibe, solo ejecuta el método.

---

# Resumen general de relaciones

| Tipo de relación | Clases involucradas |
|--------|-------------------|
| Herencia | Persona → Veterinario, Recepcionista, Cliente |
| Abstracción | Persona, MetodoPago |
| Asociación | Consulta ↔ Mascota / Consulta ↔ Veterinario |
| Agregación | Cliente ◇ Mascota |
| Composición | Consulta ◆ Tratamiento |
| Polimorfismo | Factura con métodos de pago |

---

# Tecnologías utilizadas

- Python 3
- Programación Orientada a Objetos
- Clases abstractas
- Herencia
- Polimorfismo

---

# Conclusión

El sistema organiza correctamente los procesos principales de una clínica veterinaria y aplica relaciones reales entre objetos.

Cada clase cumple una función específica y se conecta con otras mediante relaciones fundamentales de POO.

