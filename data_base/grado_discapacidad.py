from data_base.utils import pedir_texto, siguiente_id

# Tabla GRADO_DISCAPACIDAD (simulada con una lista de diccionarios)
grados_discapacidad = [
    {"id_discapacidad": 1, "discapacidad": "Visual Leve"},
    {"id_discapacidad": 2, "discapacidad": "Discapacidad visual moderada"},
    {"id_discapacidad": 3, "discapacidad": "Discapacidad visual grave"},
    {"id_discapacidad": 4, "discapacidad": "Ceguera"},
]


def ingresar_grado_discapacidad():
    id_discapacidad = siguiente_id(grados_discapacidad, "id_discapacidad")
    discapacidad = pedir_texto("Ingrese el grado de discapacidad: ", 100, True)

    grado_discapacidad = {
        "id_discapacidad": id_discapacidad,
        "discapacidad": discapacidad,
    }
    grados_discapacidad.append(grado_discapacidad)
    print("Se guardo un grado de discapacidad:", grado_discapacidad)
    return grado_discapacidad


def mostrar_grado_discapacidad():
    print("--- GRADO_DISCAPACIDAD ---")
    for fila in grados_discapacidad:
        print(fila)


def grado_discapacidad():
    op = ""
    while op != "0":
        print('''
    1. ingresar un grado de discapacidad
    2. mostrar los grados de discapacidad
    0. volver
    ''')
        op = input("Ingrese una opcion: ")

        if op == "1":
            ingresar_grado_discapacidad()
        elif op == "2":
            mostrar_grado_discapacidad()
        elif op == "0":
            print("Volviendo al menu principal...")
        else:
            print("Error: opcion no valida.")


if __name__ == "__main__":
    grado_discapacidad()
