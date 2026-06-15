from datetime import datetime

ARCHIVO = "usuarios.txt"

def validar_archivo():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        with open("errores.txt", "w", encoding="utf-8") as archivo_errores, \
             open("usuarios_validos.txt", "w", encoding="utf-8") as archivo_validos:
            for linea in lineas:
                partes = linea.strip().split(",")
                if len(partes) != 3:
                    print(f"Error en la línea: {linea.strip()} - Formato incorrecto.")
                    archivo_errores.write(f"{linea.strip()} - Formato incorrecto.\n")
                elif partes[0] == "":
                    print(f"Error en la línea: {linea.strip()} - El nombre no puede estar vacío.")
                    archivo_errores.write(f"{linea.strip()} - El nombre no puede estar vacío.\n")
                elif partes[1] == "":
                    print(f"Error en la línea: {linea.strip()} - La edad no puede estar vacía.")
                    archivo_errores.write(f"{linea.strip()} - La edad no puede estar vacía.\n")
                else:
                    try:
                        edad = int(partes[1])
                    except ValueError:
                        print(f"Error en la línea: {linea.strip()} - La edad debe ser numérica.")
                        archivo_errores.write(f"{linea.strip()} - La edad debe ser numérica.\n")
                        continue

                    if edad < 0:
                        print(f"Error en la línea: {linea.strip()} - La edad no puede ser negativa.")
                        archivo_errores.write(f"{linea.strip()} - La edad no puede ser negativa.\n")
                    else:
                        archivo_validos.write(linea)
                        
    except PermissionError:
        print("No se tienen permisos para leer el archivo.")            
    except FileNotFoundError:
        print("No se encontró el archivo de usuarios.")
    except ValueError as error:
        print(f"Error de validación: {error}")
    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")



def registrar_usuario():
    try:

        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            nombres_existentes = [linea.strip().split(",")[0] for linea in lineas]

        nombre = input("Ingrese el nombre del usuario:")

        if nombre == "":
            print("El nombre no puede estar vacío.")
            return

        if nombre in nombres_existentes:
            print("El usuario ya está registrado.")
            return

        

        edad = int(input("Ingrese la edad del usuario:"))

        if edad < 0:
            print("La edad no puede ser negativa.")
            return
        with open(ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre},{edad},{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        print("Usuario registrado exitosamente.")
    
    except ValueError:
        print("La edad debe de ser numérica")
    
    except PermissionError:
        print("No se tienen permisos para escribir en el archivo.")

    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")
            
    
def mostrar_usuarios():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            if not lineas:
                print("No hay usuarios registrados.")
                return
            
            print("\nUsuarios registrados:")

            for linea in lineas:
                nombre, edad, fecha_registro = linea.strip().split(",")
                print(f"Nombre: {nombre}, Edad: {edad}, Fecha de registro: {fecha_registro}")

    except FileNotFoundError:
        print("No se encontró el archivo de usuarios")

    except PermissionError:
        print("No se tienen permisos para leer el archivo.")

    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")

def buscar_usuario():
    try:
        nombre_buscar = input("Ingrese el nombre del usuario a buscar:").strip()
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            encontrado = False

            for linea in lineas:
                nombre, edad, fecha_registro = linea.strip().split(",")
                if nombre.lower() == nombre_buscar.lower():
                    print(f"Usuario encontrado: Nombre: {nombre}, Edad: {edad}, Fecha de registro: {fecha_registro}")
                    encontrado = True
                    break
            
            if not encontrado:
                print("Usuario no encontrado.")

    except FileNotFoundError:
        print("No se encontró el archivo de usuarios")

    except PermissionError:
        print("No se tienen permisos para leer el archivo.")

    except Exception as error:
        print(f"Ocurrió un error inesperado: {error}")

def menu():
    opcion = ""
    while opcion != "5":

        print("\n ==== USUARIOS ====")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Buscar usuario")
        print("4. Validar archivo")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            buscar_usuario()
        elif opcion == "4":
            validar_archivo()
        elif opcion == "5":
            print("Programa finalizado.")
        else:
            print("Opción no válida. Intente nuevamente.")

menu()

"""
Modificar el programa para:

Buscar usuarios.
Evitar usuarios duplicados.
Validar un archivo al momento de leerlo y en caso de errores mostrarlos
Crear archivo de errores. Meter los datos buenos en un archivo y los malos en otro
Registrar fecha y hora de creación.
"""