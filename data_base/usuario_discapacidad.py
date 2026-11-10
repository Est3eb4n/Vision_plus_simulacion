from data_base.utils import existe_par, pedir_id_existente
from data_base.usuario import usuarios
from data_base.grado_discapacidad import grados_discapacidad

# Tabla USUARIO_DISCAPACIDAD (simulada con una lista de diccionarios)
usuario_discapacidades = [
    {"id_usuario": 1, "id_discapacidad": 3},
    {"id_usuario": 2, "id_discapacidad": 1},
    {"id_usuario": 3, "id_discapacidad": 2},
    {"id_usuario": 4, "id_discapacidad": 4},
]


def ingresar_usuario_discapacidad():
    id_usuario = pedir_id_existente("Ingrese el id de el usuario: ", usuarios, "id_usuario", "nombre")
    id_discapacidad = pedir_id_existente("Ingrese el id de el grado de discapacidad: ", grados_discapacidad, "id_discapacidad", "discapacidad")

    # la llave primaria es la pareja de los dos ids, no se puede repetir
    if existe_par(usuario_discapacidades, "id_usuario", id_usuario, "id_discapacidad", id_discapacidad):
        print("Error: esa relacion ya existe.")
        return None

    usuario_discapacidad = {
        "id_usuario": id_usuario,
        "id_discapacidad": id_discapacidad,
    }
    usuario_discapacidades.append(usuario_discapacidad)
    print("Se guardo una discapacidad de un usuario:", usuario_discapacidad)
    return usuario_discapacidad


def mostrar_usuario_discapacidad():
    print("--- USUARIO_DISCAPACIDAD ---")
    for fila in usuario_discapacidades:
        print(fila)


def usuario_discapacidad():
    op = ""
    while op != "0":
        print('''
    1. ingresar una discapacidad de un usuario
    2. mostrar las discapacidades de los usuarios
    0. volver
    ''')
        op = input("Ingrese una opcion: ")

        if op == "1":
            ingresar_usuario_discapacidad()
        elif op == "2":
            mostrar_usuario_discapacidad()
        elif op == "0":
            print("Volviendo al menu principal...")
        else:
            print("Error: opcion no valida.")


if __name__ == "__main__":
    usuario_discapacidad()
