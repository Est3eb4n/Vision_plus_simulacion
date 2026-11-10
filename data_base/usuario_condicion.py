from data_base.utils import existe_par, pedir_id_existente
from data_base.usuario import usuarios
from data_base.condicion_medica import condiciones_medicas

# Tabla USUARIO_CONDICION (simulada con una lista de diccionarios)
usuario_condiciones = [
    {"id_usuario": 1, "id_condicion": 1},
    {"id_usuario": 1, "id_condicion": 2},
    {"id_usuario": 2, "id_condicion": 3},
    {"id_usuario": 3, "id_condicion": 4},
]


def ingresar_usuario_condicion():
    id_usuario = pedir_id_existente("Ingrese el id de el usuario: ", usuarios, "id_usuario", "nombre")
    id_condicion = pedir_id_existente("Ingrese el id de la condicion medica: ", condiciones_medicas, "id_condicion", "tipo_condicion")

    # la llave primaria es la pareja de los dos ids, no se puede repetir
    if existe_par(usuario_condiciones, "id_usuario", id_usuario, "id_condicion", id_condicion):
        print("Error: esa relacion ya existe.")
        return None

    usuario_condicion = {
        "id_usuario": id_usuario,
        "id_condicion": id_condicion,
    }
    usuario_condiciones.append(usuario_condicion)
    print("Se guardo una condicion de un usuario:", usuario_condicion)
    return usuario_condicion


def mostrar_usuario_condicion():
    print("--- USUARIO_CONDICION ---")
    for fila in usuario_condiciones:
        print(fila)


def usuario_condicion():
    op = ""
    while op != "0":
        print('''
    1. ingresar una condicion de un usuario
    2. mostrar las condiciones de los usuarios
    0. volver
    ''')
        op = input("Ingrese una opcion: ")

        if op == "1":
            ingresar_usuario_condicion()
        elif op == "2":
            mostrar_usuario_condicion()
        elif op == "0":
            print("Volviendo al menu principal...")
        else:
            print("Error: opcion no valida.")


if __name__ == "__main__":
    usuario_condicion()
