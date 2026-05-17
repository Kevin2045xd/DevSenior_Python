"""
Sistema de Gestión de Biblioteca
🎯 Objetivo del reto

Diseñar la estructura de datos más adecuada para representar una biblioteca utilizando listas, diccionarios, conjuntos y tuplas.

El reto no consiste únicamente en almacenar datos, sino en pensar como un arquitecto de software, seleccionando la estructura correcta para cada tipo de información.

📚 Contexto

Una biblioteca necesita almacenar información sobre:

Libros
Autores
Usuarios
Préstamos
Fechas
Categorías

Tu equipo debe diseñar un modelo de datos que permita representar toda esta información de forma organizada y sin redundancias.

📝 Requerimientos del sistema
1. Libros

Cada libro debe almacenar:

ISBN
Título
Año de publicación
Lista de autores
Categorías
Número total de copias
Número de copias disponibles
2. Autores

Cada autor debe tener:

Identificación única
Nombre
Nacionalidad
Año de nacimiento
3. Usuarios

Cada usuario debe almacenar:

ID
Nombre completo
Correo electrónico
Teléfono
4. Préstamos

Cada préstamo debe registrar:

ID del préstamo
Usuario
ISBN del libro
Fecha de préstamo
Fecha de devolución
Estado (activo, devuelto, atrasado)
5. Fechas

Las fechas deben almacenarse usando una estructura apropiada.

6. Categorías

No deben existir categorías repetidas.

🎯 Parte 1 — Diseñar el esquema de datos

Construyan una estructura principal llamada biblioteca que contenga toda la información.

Sugerencia:
biblioteca = {
    "autores": {},
    "libros": {},
    "usuarios": {},
    "prestamos": {}
}
🎯 Parte 2 — Cargar datos de ejemplo

Agregar al menos:

3 autores
5 libros
4 usuarios
3 préstamos
🎯 Parte 3 — Consultas a resolver

El programa debe mostrar:

Todos los libros disponibles.
Todos los libros de un autor específico.
Todos los préstamos activos.
Usuarios con préstamos atrasados.
Categorías existentes.
Libro más prestado.
Cantidad total de libros.
Cantidad total de préstamos activos.
🎯 Parte 4 — Justificación técnica

El equipo debe explicar:

¿Por qué usaron diccionarios para ciertas entidades?
¿Por qué las categorías son conjuntos?
¿Por qué las fechas pueden representarse como tuplas?
¿Qué ventajas tiene evitar redundancia?
🎯 Parte 5 — Refactorización

Analicen el siguiente diseño deficiente:

biblioteca = [
    ["978001", "Python Básico", "Juan Pérez", "Programación"],
    ["978002", "Python Avanzado", "Juan Pérez", "Programación"],
    ["978003", "Bases de Datos", "Ana Gómez", "Tecnología"]
]
Preguntas
¿Qué redundancias existen?
¿Qué problemas tendría este diseño?
¿Cómo lo reestructurarían?
🏅 Bonus

Agregar:

Historial de préstamos por usuario.
Búsqueda por categoría.
Ranking de usuarios con más préstamos.
"""

biblioteca = {
    "autores": {},
    "libros": {},
    "usuarios": {},
    "prestamos": {}
}



# Carga de tres autores
"""
Identificación única
Nombre
Nacionalidad
Año de nacimiento
"""

biblioteca["autores"]["4567654567"] = {
    "nombre"  : "Rafael" ,
    "nacionalidad" : "colombiano",
    "anio_nacimiento" : "1930"
}

biblioteca["autores"]["1234567890"] = {
    "nombre"  : "Gabriel Garcia Marquez" ,
    "nacionalidad" : "colombiano",
    "anio_nacimiento" : "1927"
}



biblioteca["autores"]["9876543210"] = {
    "nombre"  : "Isabel Allende" ,
    "nacionalidad" : "chilena",
    "anio_nacimiento" : "1942"
}

# agregar cinco libros
"""
ISBN
Título  
Año de publicación
Lista de autores
Categorías
Número total de copias
Número de copias disponibles
"""
biblioteca["libros"]["978001"] = {
    "titulo" : "Cien años de soledad",
    "anio_publicacion" : "1967",
    "autores" : ["4567654567"],
    "categorias" : {"literatura", "realismo mágico"},
    "total_copias" : 5,
    "copias_disponibles" : 3
}

biblioteca["libros"]["978002"] = {
    "titulo" : "El amor en los tiempos del cólera",
    "anio_publicacion" : "1985",
    "autores" : ["4567654567"],
    "categorias" : {"literatura", "romance"},
    "total_copias" : 3,
    "copias_disponibles" : 2
}

biblioteca["libros"]["978003"] = {
    "titulo" : "La casa de los espíritus",
    "anio_publicacion" : "1982",
    "autores" : ["9876543210"],
    "categorias" : {"literatura", "realismo mágico"},
    "total_copias" : 4,
    "copias_disponibles" : 2
}

biblioteca["libros"]["978004"] = {
    "titulo" : "El otoño del patriarca",
    "anio_publicacion" : "1975",
    "autores" : ["4567654567"],
    "categorias" : {"literatura", "realismo mágico"},
    "total_copias" : 2,
    "copias_disponibles" : 1
}

biblioteca["libros"]["978005"] = {
    "titulo" : "Eva Luna",
    "anio_publicacion" : "1993",
    "autores" : ["9876543210"], # los "[]" se usan para indicar que es una lista, aunque en este caso solo hay un autor, se mantiene la estructura para permitir futuros libros con múltiples autores
    "categorias" : {"literatura", "romance"},
    "total_copias" : 3,
    "copias_disponibles" : 0
}

# Agregar cuatro usuarios
"""
ID
Nombre completo 
Correo electrónico
Teléfono
"""
biblioteca["usuarios"]["001"] = {
    "nombre_completo" : "Carlos Pérez",
    "correo_electronico" : "carlos.perez@example.com",
    "telefono" : "1234567890"
}
biblioteca["usuarios"]["002"] = {
    "nombre_completo" : "Ana Gómez",
    "correo_electronico" : "ana.gomez@example.com",
    "telefono" : "0987654321"
}
biblioteca["usuarios"]["003"] = {
    "nombre_completo" : "Luis Martínez",
    "correo_electronico" : "luis.martinez@example.com",
    "telefono" : "1111111111"
}
biblioteca["usuarios"]["004"] = {
    "nombre_completo" : "María Rodríguez",
    "correo_electronico" : "maria.rodriguez@example.com",
    "telefono" : "2222222222"
}

# Agregar tres préstamos
"""
ID
ID del libro
ID del usuario
Fecha de préstamo
Fecha de devolución
Estado
"""
biblioteca["prestamos"]["001"] = {
    "id_libro" : "978001",
    "id_usuario" : "001",
    "fecha_prestamo" : "2023-10-01",
    "fecha_devolucion" : "2023-10-15",
    "estado" : "activo"
}
biblioteca["prestamos"]["002"] = {
    "id_libro" : "978002",
    "id_usuario" : "002",
    "fecha_prestamo" : "2023-10-05",
    "fecha_devolucion" : "2023-10-19",
    "estado" : "activo"
}
biblioteca["prestamos"]["003"] = {
    "id_libro" : "978003",
    "id_usuario" : "003",
    "fecha_prestamo" : "2023-10-10",
    "fecha_devolucion" : "2023-10-24",
    "estado" : "activo"
}

# mostrar libros

print("------Libros disponibles-------")

for libro, detalles in biblioteca["libros"].items():
    if detalles["copias_disponibles"] > 0:
        print(detalles)

# mostrar libros de un autor específico

autor_id = "4567654567"
print(f"------Libros del autor {biblioteca['autores'][autor_id]['nombre']}-------")

for libro, detalles in biblioteca["libros"].items():
    if autor_id in detalles["autores"]:
        print(libro, detalles["titulo"])


# Mostar prestamos activos
print("------Préstamos activos-------")

for prestamo, info in biblioteca["prestamos"].items(): 
    if info["estado"] == "activo":
        print(info)

# Usuarios con préstamos atrasados
print("------Usuarios con préstamos atrasados-------")

for prestamo, info in biblioteca["prestamos"].items():
    if info["estado"] == "atrasado":
        usuario_id = info["id_usuario"]
        print(biblioteca["usuarios"][usuario_id]["nombre_completo"])

# Categorías existentes
print("------Categorías existentes-------")
categorias = set()
for libro, detalles in biblioteca["libros"].items():
    categorias.update(detalles["categorias"])
print(categorias)


