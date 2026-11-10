from data_base.usuario import ingresar_usuario
from data_base.contacto_emergencia import ingresar_contacto_emergencia
from data_base.usuario_condicion import ingresar_usuario_condicion
from data_base.usuario_discapacidad import ingresar_usuario_discapacidad


def registro_de_usuario():
    print("=== Registro de usuario ===")

    # paso 1: datos basicos
    usuario = ingresar_usuario()
    if usuario is None:
        return

    # paso 2: contacto de emergencia
    # (ingresar_contacto_emergencia pregunta el id del usuario, escriba el que se acaba de crear)
    print("Su nuevo id de usuario es:", usuario["id_usuario"])
    op = input("Desea agregar un contacto de emergencia? (s/n): ")
    while op == "s":
        ingresar_contacto_emergencia()
        op = input("Desea agregar otro contacto? (s/n): ")

    # paso 3: condiciones medicas
    op = input("Desea agregar una condicion medica? (s/n): ")
    while op == "s":
        ingresar_usuario_condicion()
        op = input("Desea agregar otra condicion? (s/n): ")

    # paso 4: discapacidad
    op = input("Desea agregar una discapacidad? (s/n): ")
    while op == "s":
        ingresar_usuario_discapacidad()
        op = input("Desea agregar otra discapacidad? (s/n): ")

    print("Registro terminado para:", usuario["nombre"])


if __name__ == "__main__":
    registro_de_usuario()
