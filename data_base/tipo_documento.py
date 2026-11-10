from data_base.utils import pedir_texto, siguiente_id

# Tabla TIPO_DOCUMENTO (simulada con una lista de diccionarios)
tipos_documento = [
    {"id_tipo_doc": 1, "nombre_doc": "Cédula de Ciudadanía"},
    {"id_tipo_doc": 2, "nombre_doc": "Tarjeta de Identidad"},
    {"id_tipo_doc": 3, "nombre_doc": "Cédula de Extranjería"},
    {"id_tipo_doc": 4, "nombre_doc": "Pasaporte"},
]


def ingresar_tipo_documento():
    id_tipo_doc = siguiente_id(tipos_documento, "id_tipo_doc")
    nombre_doc = pedir_texto("Ingrese el nombre del tipo de documento: ", 50, True)

    tipo_documento = {
        "id_tipo_doc": id_tipo_doc,
        "nombre_doc": nombre_doc,
    }
    tipos_documento.append(tipo_documento)
    print("Se guardo un tipo de documento:", tipo_documento)
    return tipo_documento


def mostrar_tipo_documento():
    print("--- TIPO_DOCUMENTO ---")
    for fila in tipos_documento:
        print(fila)


def tipo_documento():
    op = ""
    while op != "0":
        print('''
    1. ingresar un tipo de documento
    2. mostrar los tipos de documento
    0. volver
    ''')
        op = input("Ingrese una opcion: ")

        if op == "1":
            ingresar_tipo_documento()
        elif op == "2":
            mostrar_tipo_documento()
        elif op == "0":
            print("Volviendo al menu principal...")
        else:
            print("Error: opcion no valida.")


if __name__ == "__main__":
    tipo_documento()
