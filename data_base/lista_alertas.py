from data_base.utils import fecha_hora_actual, pedir_id_existente, pedir_texto, siguiente_id
from data_base.usuario import usuarios
from data_base.tipo_alerta import tipos_alerta
from data_base.ubicacion import ubicaciones

# Tabla LISTA_ALERTAS (simulada con una lista de diccionarios)
alertas = [
    {"id_alerta": 1, "id_usuario": 1, "id_tipo_alerta": 1, "id_ubicacion": 1, "fecha_hora": "2026-11-01 08:15:00", "indicaciones": "Paciente presenta dolor agudo en el pecho."},
    {"id_alerta": 2, "id_usuario": 2, "id_tipo_alerta": 2, "id_ubicacion": 2, "fecha_hora": "2026-11-02 14:30:00", "indicaciones": "Reporte de robo en vía pública."},
    {"id_alerta": 3, "id_usuario": 3, "id_tipo_alerta": 3, "id_ubicacion": 3, "fecha_hora": "2026-11-03 19:45:00", "indicaciones": "Conato de incendio en edificio residencial."},
    {"id_alerta": 4, "id_usuario": 4, "id_tipo_alerta": 4, "id_ubicacion": 4, "fecha_hora": "2026-11-04 07:05:00", "indicaciones": "Colisión entre dos vehículos particulares."},
]


def ingresar_lista_alertas():
    id_alerta = siguiente_id(alertas, "id_alerta")
    id_usuario = pedir_id_existente("Ingrese el id de el usuario: ", usuarios, "id_usuario", "nombre")
    id_tipo_alerta = pedir_id_existente("Ingrese el id de el tipo de alerta: ", tipos_alerta, "id_tipo_alerta", "nombre_alerta")
    id_ubicacion = pedir_id_existente("Ingrese el id de la ubicacion: ", ubicaciones, "id_ubicacion", "direccion")
    fecha_hora = fecha_hora_actual()
    indicaciones = pedir_texto("Ingrese las indicaciones (puede dejarlas vacias): ", 500, False)

    lista_alertas = {
        "id_alerta": id_alerta,
        "id_usuario": id_usuario,
        "id_tipo_alerta": id_tipo_alerta,
        "id_ubicacion": id_ubicacion,
        "fecha_hora": fecha_hora,
        "indicaciones": indicaciones,
    }
    alertas.append(lista_alertas)
    print("Se guardo una alerta:", lista_alertas)
    return lista_alertas


def mostrar_lista_alertas():
    print("--- LISTA_ALERTAS ---")
    for fila in alertas:
        print(fila)


def lista_alertas():
    op = ""
    while op != "0":
        print('''
    1. ingresar una alerta
    2. mostrar las alertas
    0. volver
    ''')
        op = input("Ingrese una opcion: ")

        if op == "1":
            ingresar_lista_alertas()
        elif op == "2":
            mostrar_lista_alertas()
        elif op == "0":
            print("Volviendo al menu principal...")
        else:
            print("Error: opcion no valida.")


if __name__ == "__main__":
    lista_alertas()
