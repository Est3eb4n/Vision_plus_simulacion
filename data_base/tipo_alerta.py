from data_base.utils import pedir_id_existente, pedir_texto, siguiente_id
from data_base.estado_alerta import estados_alerta

# Tabla TIPO_ALERTA (simulada con una lista de diccionarios)
tipos_alerta = [
    {"id_tipo_alerta": 1, "id_estado": 1, "nombre_alerta": "Emergencia Médica"},
    {"id_tipo_alerta": 2, "id_estado": 1, "nombre_alerta": "Seguridad Ciudadana"},
    {"id_tipo_alerta": 3, "id_estado": 2, "nombre_alerta": "Incendio Estructural"},
    {"id_tipo_alerta": 4, "id_estado": 3, "nombre_alerta": "Accidente de Tránsito"},
]


def ingresar_tipo_alerta():
    id_tipo_alerta = siguiente_id(tipos_alerta, "id_tipo_alerta")
    id_estado = pedir_id_existente("Ingrese el id de el estado de la alerta: ", estados_alerta, "id_estado", "nombre_estado")
    nombre_alerta = pedir_texto("Ingrese el nombre de la alerta: ", 100, True)

    tipo_alerta = {
        "id_tipo_alerta": id_tipo_alerta,
        "id_estado": id_estado,
        "nombre_alerta": nombre_alerta,
    }
    tipos_alerta.append(tipo_alerta)
    print("Se guardo un tipo de alerta:", tipo_alerta)
    return tipo_alerta


def mostrar_tipo_alerta():
    print("--- TIPO_ALERTA ---")
    for fila in tipos_alerta:
        print(fila)


def tipo_alerta():
    op = ""
    while op != "0":
        print('''
    1. ingresar un tipo de alerta
    2. mostrar los tipos de alerta
    0. volver
    ''')
        op = input("Ingrese una opcion: ")

        if op == "1":
            ingresar_tipo_alerta()
        elif op == "2":
            mostrar_tipo_alerta()
        elif op == "0":
            print("Volviendo al menu principal...")
        else:
            print("Error: opcion no valida.")


if __name__ == "__main__":
    tipo_alerta()
