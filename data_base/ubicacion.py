from data_base.utils import pedir_decimal, pedir_id_existente, pedir_texto, siguiente_id
from data_base.barrio import barrios

# Tabla UBICACION (simulada con una lista de diccionarios)
ubicaciones = [
    {"id_ubicacion": 1, "id_barrio": 1, "direccion": "Calle 122 # 15-30", "latitud": 4.701234, "longitud": -74.0321},
    {"id_ubicacion": 2, "id_barrio": 2, "direccion": "Carrera 5 # 69-10", "latitud": 4.654321, "longitud": -74.0543},
    {"id_ubicacion": 3, "id_barrio": 3, "direccion": "Carrera 7 # 18-40", "latitud": 4.601122, "longitud": -74.0722},
    {"id_ubicacion": 4, "id_barrio": 4, "direccion": "Calle 129 # 91-05", "latitud": 4.745678, "longitud": -74.0987},
]


def ingresar_ubicacion():
    id_ubicacion = siguiente_id(ubicaciones, "id_ubicacion")
    id_barrio = pedir_id_existente("Ingrese el id de el barrio: ", barrios, "id_barrio", "nombre_barrio")
    direccion = pedir_texto("Ingrese la direccion: ", 150, True)
    latitud = pedir_decimal("Ingrese la latitud: ", -90, 90)
    longitud = pedir_decimal("Ingrese la longitud: ", -180, 180)

    ubicacion = {
        "id_ubicacion": id_ubicacion,
        "id_barrio": id_barrio,
        "direccion": direccion,
        "latitud": latitud,
        "longitud": longitud,
    }
    ubicaciones.append(ubicacion)
    print("Se guardo una ubicacion:", ubicacion)
    return ubicacion


def mostrar_ubicacion():
    print("--- UBICACION ---")
    for fila in ubicaciones:
        print(fila)


def ubicacion():
    op = ""
    while op != "0":
        print('''
    1. ingresar una ubicacion
    2. mostrar las ubicaciones
    0. volver
    ''')
        op = input("Ingrese una opcion: ")

        if op == "1":
            ingresar_ubicacion()
        elif op == "2":
            mostrar_ubicacion()
        elif op == "0":
            print("Volviendo al menu principal...")
        else:
            print("Error: opcion no valida.")


if __name__ == "__main__":
    ubicacion()
