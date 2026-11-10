from data_base.utils import pedir_id_existente, pedir_texto, siguiente_id
from data_base.usuario import usuarios
from data_base.ubicacion import ubicaciones

# Tabla LUGARES_FRECUENTES (simulada con una lista de diccionarios)
lista_lugares = [
    {"id_lugar_frec": 1, "id_usuario": 1, "id_ubicacion": 1, "alias_lugar": "Casa"},
    {"id_lugar_frec": 2, "id_usuario": 2, "id_ubicacion": 2, "alias_lugar": "Oficina"},
    {"id_lugar_frec": 3, "id_usuario": 3, "id_ubicacion": 3, "alias_lugar": "Universidad"},
    {"id_lugar_frec": 4, "id_usuario": 4, "id_ubicacion": 4, "alias_lugar": "Casa de los padres"},
]


def ingresar_lugares_frecuentes():
    id_lugar_frec = siguiente_id(lista_lugares, "id_lugar_frec")
    id_usuario = pedir_id_existente("Ingrese el id de el usuario: ", usuarios, "id_usuario", "nombre")
    id_ubicacion = pedir_id_existente("Ingrese el id de la ubicacion: ", ubicaciones, "id_ubicacion", "direccion")
    alias_lugar = pedir_texto("Ingrese el alias del lugar (ej: Casa): ", 50, True)

    lugares_frecuentes = {
        "id_lugar_frec": id_lugar_frec,
        "id_usuario": id_usuario,
        "id_ubicacion": id_ubicacion,
        "alias_lugar": alias_lugar,
    }
    lista_lugares.append(lugares_frecuentes)
    print("Se guardo un lugar frecuente:", lugares_frecuentes)
    return lugares_frecuentes


def mostrar_lugares_frecuentes():
    print("--- LUGARES_FRECUENTES ---")
    for fila in lista_lugares:
        print(fila)


def lugares_frecuentes():
    op = ""
    while op != "0":
        print('''
    1. ingresar un lugar frecuente
    2. mostrar los lugares frecuentes
    0. volver
    ''')
        op = input("Ingrese una opcion: ")

        if op == "1":
            ingresar_lugares_frecuentes()
        elif op == "2":
            mostrar_lugares_frecuentes()
        elif op == "0":
            print("Volviendo al menu principal...")
        else:
            print("Error: opcion no valida.")


if __name__ == "__main__":
    lugares_frecuentes()
