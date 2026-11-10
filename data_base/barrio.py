from data_base.utils import pedir_id_existente, pedir_texto, siguiente_id
from data_base.localidad import localidades

# Tabla BARRIO (simulada con una lista de diccionarios)
barrios = [
    {"id_barrio": 1, "id_localidad": 1, "nombre_barrio": "Santa Bárbara"},
    {"id_barrio": 2, "id_localidad": 2, "nombre_barrio": "Zona G"},
    {"id_barrio": 3, "id_localidad": 3, "nombre_barrio": "Las Nieves"},
    {"id_barrio": 4, "id_localidad": 4, "nombre_barrio": "San Cristobal"},
]


def ingresar_barrio():
    id_barrio = siguiente_id(barrios, "id_barrio")
    id_localidad = pedir_id_existente("Ingrese el id de la localidad del barrio: ", localidades, "id_localidad", "nombre_localidad")
    nombre_barrio = pedir_texto("Ingrese el nombre del barrio: ", 100, True)

    barrio = {
        "id_barrio": id_barrio,
        "id_localidad": id_localidad,
        "nombre_barrio": nombre_barrio,
    }
    barrios.append(barrio)
    print("Se guardo un barrio:", barrio)
    return barrio


def mostrar_barrio():
    print("--- BARRIO ---")
    for fila in barrios:
        print(fila)


def barrio():
    op = ""
    while op != "0":
        print('''
    1. ingresar un barrio
    2. mostrar los barrios
    0. volver
    ''')
        op = input("Ingrese una opcion: ")

        if op == "1":
            ingresar_barrio()
        elif op == "2":
            mostrar_barrio()
        elif op == "0":
            print("Volviendo al menu principal...")
        else:
            print("Error: opcion no valida.")


if __name__ == "__main__":
    barrio()
