from data_base.utils import pedir_fecha, pedir_id_existente, pedir_texto, siguiente_id
from data_base.tipo_documento import tipos_documento
from data_base.tipo_rh import tipos_rh
from data_base.eps import lista_eps

# Tabla USUARIO (simulada con una lista de diccionarios)
usuarios = [
    {"id_usuario": 1, "id_tipo_doc": 1, "num_doc": "1018456789", "nombre": "Carlos Mendoza", "fecha_nacimiento": "1990-05-14", "id_rh": 1, "id_eps": 1},
    {"id_usuario": 2, "id_tipo_doc": 1, "num_doc": "1020304050", "nombre": "María Rodríguez", "fecha_nacimiento": "1985-11-22", "id_rh": 2, "id_eps": 2},
    {"id_usuario": 3, "id_tipo_doc": 2, "num_doc": "1098765432", "nombre": "Andrés Gómez", "fecha_nacimiento": "2008-03-10", "id_rh": 3, "id_eps": 3},
    {"id_usuario": 4, "id_tipo_doc": 3, "num_doc": "5544332211", "nombre": "Laura Martínez", "fecha_nacimiento": "1995-08-30", "id_rh": 4, "id_eps": 4},
]


def ingresar_usuario():
    id_usuario = siguiente_id(usuarios, "id_usuario")
    id_tipo_doc = pedir_id_existente("Ingrese el id de el tipo de documento: ", tipos_documento, "id_tipo_doc", "nombre_doc")
    while True:
        num_doc = pedir_texto("Ingrese el numero de documento: ", 20, True)
        repetido = False
        for fila in usuarios:
            if fila["num_doc"] == num_doc:
                repetido = True
        if repetido:
            print("Error: ese num_doc ya esta registrado.")
        else:
            break
    nombre = pedir_texto("Ingrese el nombre del usuario: ", 100, True)
    fecha_nacimiento = pedir_fecha("Ingrese la fecha de nacimiento (AAAA-MM-DD): ")
    id_rh = pedir_id_existente("Ingrese el id de el tipo de RH: ", tipos_rh, "id_rh", "grupo_rh")
    id_eps = pedir_id_existente("Ingrese el id de la EPS: ", lista_eps, "id_eps", "nombre_eps")

    usuario = {
        "id_usuario": id_usuario,
        "id_tipo_doc": id_tipo_doc,
        "num_doc": num_doc,
        "nombre": nombre,
        "fecha_nacimiento": fecha_nacimiento,
        "id_rh": id_rh,
        "id_eps": id_eps,
    }
    usuarios.append(usuario)
    print("Se guardo un usuario:", usuario)
    return usuario


def mostrar_usuario():
    print("--- USUARIO ---")
    for fila in usuarios:
        print(fila)


def usuario():
    op = ""
    while op != "0":
        print('''
    1. ingresar un usuario
    2. mostrar los usuarios
    0. volver
    ''')
        op = input("Ingrese una opcion: ")

        if op == "1":
            ingresar_usuario()
        elif op == "2":
            mostrar_usuario()
        elif op == "0":
            print("Volviendo al menu principal...")
        else:
            print("Error: opcion no valida.")


if __name__ == "__main__":
    usuario()
