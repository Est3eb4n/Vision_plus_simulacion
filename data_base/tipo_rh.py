from data_base.utils import pedir_texto, siguiente_id

# Tabla TIPO_RH (simulada con una lista de diccionarios)
tipos_rh = [
    {"id_rh": 1, "grupo_rh": "O+"},
    {"id_rh": 2, "grupo_rh": "O-"},
    {"id_rh": 3, "grupo_rh": "A+"},
    {"id_rh": 4, "grupo_rh": "AB+"},
]


def ingresar_tipo_rh():
    id_rh = siguiente_id(tipos_rh, "id_rh")
    grupo_rh = pedir_texto("Ingrese el grupo RH (ej: O+): ", 10, True)

    tipo_rh = {
        "id_rh": id_rh,
        "grupo_rh": grupo_rh,
    }
    tipos_rh.append(tipo_rh)
    print("Se guardo un tipo de RH:", tipo_rh)
    return tipo_rh


def mostrar_tipo_rh():
    print("--- TIPO_RH ---")
    for fila in tipos_rh:
        print(fila)


def tipo_rh():
    op = ""
    while op != "0":
        print('''
    1. ingresar un tipo de RH
    2. mostrar los tipos de RH
    0. volver
    ''')
        op = input("Ingrese una opcion: ")

        if op == "1":
            ingresar_tipo_rh()
        elif op == "2":
            mostrar_tipo_rh()
        elif op == "0":
            print("Volviendo al menu principal...")
        else:
            print("Error: opcion no valida.")


if __name__ == "__main__":
    tipo_rh()
