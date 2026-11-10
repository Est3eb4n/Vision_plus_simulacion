from data_base.utils import pedir_id_existente, pedir_texto, siguiente_id
from data_base.usuario import usuarios

# Tabla CONTACTO_EMERGENCIA (simulada con una lista de diccionarios)
contactos_emergencia = [
    {"id_contacto": 1, "id_usuario": 1, "nombre": "Ana Mendoza", "num_tel": "3101234567", "direccion": "Calle 122 # 15-30"},
    {"id_contacto": 2, "id_usuario": 2, "nombre": "Jorge Rodríguez", "num_tel": "3209876543", "direccion": "Carrera 5 # 69-10"},
    {"id_contacto": 3, "id_usuario": 3, "nombre": "Lucía Gómez", "num_tel": "3155558888", "direccion": "Carrera 7 # 18-40"},
    {"id_contacto": 4, "id_usuario": 4, "nombre": "Felipe Martínez", "num_tel": "3004441111", "direccion": "Calle 129 # 91-05"},
]


def ingresar_contacto_emergencia():
    id_contacto = siguiente_id(contactos_emergencia, "id_contacto")
    id_usuario = pedir_id_existente("Ingrese el id de el usuario: ", usuarios, "id_usuario", "nombre")
    nombre = pedir_texto("Ingrese el nombre del contacto: ", 100, True)
    num_tel = pedir_texto("Ingrese el telefono del contacto: ", 20, True)
    direccion = pedir_texto("Ingrese la direccion del contacto (puede dejarla vacia): ", 150, False)

    contacto_emergencia = {
        "id_contacto": id_contacto,
        "id_usuario": id_usuario,
        "nombre": nombre,
        "num_tel": num_tel,
        "direccion": direccion,
    }
    contactos_emergencia.append(contacto_emergencia)
    print("Se guardo un contacto de emergencia:", contacto_emergencia)
    return contacto_emergencia


def mostrar_contacto_emergencia():
    print("--- CONTACTO_EMERGENCIA ---")
    for fila in contactos_emergencia:
        print(fila)


def contacto_emergencia():
    op = ""
    while op != "0":
        print('''
    1. ingresar un contacto de emergencia
    2. mostrar los contactos de emergencia
    0. volver
    ''')
        op = input("Ingrese una opcion: ")

        if op == "1":
            ingresar_contacto_emergencia()
        elif op == "2":
            mostrar_contacto_emergencia()
        elif op == "0":
            print("Volviendo al menu principal...")
        else:
            print("Error: opcion no valida.")


if __name__ == "__main__":
    contacto_emergencia()
