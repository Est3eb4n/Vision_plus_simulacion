from data_base.utils import pedir_texto, siguiente_id

# Tabla LOCALIDAD (simulada con una lista de diccionarios)
localidades = [
    {"id_localidad": 1, "nombre_localidad": "Usaquén"},
    {"id_localidad": 2, "nombre_localidad": "Chapinero"},
    {"id_localidad": 3, "nombre_localidad": "Santa Fe"},
    {"id_localidad": 4, "nombre_localidad": "Suba"},
]


def ingresar_localidad():
    id_localidad = siguiente_id(localidades, "id_localidad")
    nombre_localidad = pedir_texto("Ingrese el nombre de la localidad: ", 100, True)

    localidad = {
        "id_localidad": id_localidad,
        "nombre_localidad": nombre_localidad,
    }
    localidades.append(localidad)
    print("Se guardo una localidad:", localidad)
    return localidad


def mostrar_localidad():
    print("--- LOCALIDAD ---")
    for fila in localidades:
        print(fila)


def localidad():
    op = ""
    while op != "0":
        print('''
    1. ingresar una localidad
    2. mostrar las localidades
    0. volver
    ''')
        op = input("Ingrese una opcion: ")

        if op == "1":
            ingresar_localidad()
        elif op == "2":
            mostrar_localidad()
        elif op == "0":
            print("Volviendo al menu principal...")
        else:
            print("Error: opcion no valida.")


if __name__ == "__main__":
    localidad()
