from data_base.utils import pedir_texto, siguiente_id

# Tabla CONDICION_MEDICA (simulada con una lista de diccionarios)
condiciones_medicas = [
    {"id_condicion": 1, "tipo_condicion": "Hipertensión", "descripcion": "Presión arterial elevada de manera continua."},
    {"id_condicion": 2, "tipo_condicion": "Diabetes Tipo 2", "descripcion": "Niveles elevados de glucosa en sangre."},
    {"id_condicion": 3, "tipo_condicion": "Asma", "descripcion": "Enfermedad respiratoria crónica."},
    {"id_condicion": 4, "tipo_condicion": "Alergia a Medicamentos", "descripcion": "Reacción adversa a la penicilina y derivados."},
]


def ingresar_condicion_medica():
    id_condicion = siguiente_id(condiciones_medicas, "id_condicion")
    tipo_condicion = pedir_texto("Ingrese el tipo de condicion: ", 100, True)
    descripcion = pedir_texto("Ingrese la descripcion (puede dejarla vacia): ", 500, False)

    condicion_medica = {
        "id_condicion": id_condicion,
        "tipo_condicion": tipo_condicion,
        "descripcion": descripcion,
    }
    condiciones_medicas.append(condicion_medica)
    print("Se guardo una condicion medica:", condicion_medica)
    return condicion_medica


def mostrar_condicion_medica():
    print("--- CONDICION_MEDICA ---")
    for fila in condiciones_medicas:
        print(fila)


def condicion_medica():
    op = ""
    while op != "0":
        print('''
    1. ingresar una condicion medica
    2. mostrar las condiciones medicas
    0. volver
    ''')
        op = input("Ingrese una opcion: ")

        if op == "1":
            ingresar_condicion_medica()
        elif op == "2":
            mostrar_condicion_medica()
        elif op == "0":
            print("Volviendo al menu principal...")
        else:
            print("Error: opcion no valida.")


if __name__ == "__main__":
    condicion_medica()
