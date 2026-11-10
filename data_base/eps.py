from data_base.utils import pedir_texto, siguiente_id

# Tabla EPS (simulada con una lista de diccionarios)
lista_eps = [
    {"id_eps": 1, "nombre_eps": "Sura EPS", "direccion_eps": "Calle 100 # 15-20", "telefono": "6013001111", "email": "contacto@sura.com.co"},
    {"id_eps": 2, "nombre_eps": "Sanitas EPS", "direccion_eps": "Carrera 7 # 45-10", "telefono": "6013002222", "email": "servicio@sanitas.com.co"},
    {"id_eps": 3, "nombre_eps": "Compensar EPS", "direccion_eps": "Avenida Caracas # 32-50", "telefono": "6013003333", "email": "atencion@compensar.com.co"},
    {"id_eps": 4, "nombre_eps": "Salud Total EPS", "direccion_eps": "Calle 26 # 68-15", "telefono": "6013004444", "email": "info@saludtotal.com.co"},
]


def ingresar_eps():
    id_eps = siguiente_id(lista_eps, "id_eps")
    nombre_eps = pedir_texto("Ingrese el nombre de la EPS: ", 100, True)
    direccion_eps = pedir_texto("Ingrese la direccion de la EPS (puede dejarlo vacio): ", 150, False)
    telefono = pedir_texto("Ingrese el telefono de la EPS (puede dejarlo vacio): ", 20, False)
    email = pedir_texto("Ingrese el email de la EPS (puede dejarlo vacio): ", 100, False)

    eps = {
        "id_eps": id_eps,
        "nombre_eps": nombre_eps,
        "direccion_eps": direccion_eps,
        "telefono": telefono,
        "email": email,
    }
    lista_eps.append(eps)
    print("Se guardo una EPS:", eps)
    return eps


def mostrar_eps():
    print("--- EPS ---")
    for fila in lista_eps:
        print(fila)


def eps():
    op = ""
    while op != "0":
        print('''
    1. ingresar una EPS
    2. mostrar las EPS
    0. volver
    ''')
        op = input("Ingrese una opcion: ")

        if op == "1":
            ingresar_eps()
        elif op == "2":
            mostrar_eps()
        elif op == "0":
            print("Volviendo al menu principal...")
        else:
            print("Error: opcion no valida.")


if __name__ == "__main__":
    eps()
