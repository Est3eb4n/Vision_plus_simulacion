from data_base.utils import pedir_texto, siguiente_id

# Tabla ESTADO_ALERTA (simulada con una lista de diccionarios)
estados_alerta = [
    {"id_estado": 1, "nombre_estado": "Activa"},
    {"id_estado": 2, "nombre_estado": "En Atencion"},
    {"id_estado": 3, "nombre_estado": "Resuelta"},
    {"id_estado": 4, "nombre_estado": "Cancelada"},
]


def ingresar_estado_alerta():
    id_estado = siguiente_id(estados_alerta, "id_estado")
    nombre_estado = pedir_texto("Ingrese el nombre del estado: ", 50, True)

    estado_alerta = {
        "id_estado": id_estado,
        "nombre_estado": nombre_estado,
    }
    estados_alerta.append(estado_alerta)
    print("Se guardo un estado de alerta:", estado_alerta)
    return estado_alerta


def mostrar_estado_alerta():
    print("--- ESTADO_ALERTA ---")
    for fila in estados_alerta:
        print(fila)


def estado_alerta():
    op = ""
    while op != "0":
        print('''
    1. ingresar un estado de alerta
    2. mostrar los estados de alerta
    0. volver
    ''')
        op = input("Ingrese una opcion: ")

        if op == "1":
            ingresar_estado_alerta()
        elif op == "2":
            mostrar_estado_alerta()
        elif op == "0":
            print("Volviendo al menu principal...")
        else:
            print("Error: opcion no valida.")


if __name__ == "__main__":
    estado_alerta()
