from data_base.localidad import localidad
from data_base.estado_alerta import estado_alerta
from data_base.tipo_documento import tipo_documento
from data_base.tipo_rh import tipo_rh
from data_base.eps import eps
from data_base.condicion_medica import condicion_medica
from data_base.grado_discapacidad import grado_discapacidad
from data_base.barrio import barrio
from data_base.tipo_alerta import tipo_alerta
from data_base.usuario import usuario
from data_base.ubicacion import ubicacion
from data_base.contacto_emergencia import contacto_emergencia
from data_base.usuario_condicion import usuario_condicion
from data_base.usuario_discapacidad import usuario_discapacidad
from data_base.lugares_frecuentes import lugares_frecuentes
from data_base.lista_alertas import lista_alertas
from registro_de_usuario import registro_de_usuario
from consultas import consulta_alertas, consulta_perfil_medico


def main():
    print("=== VISION PLUS - Simulacion de base de datos sistema_alertas ===")
    op = ""

    while op != "0":
        print('''
     1. Localidad              9. Tipo de alerta
     2. Estado de alerta      10. Usuario
     3. Tipo de documento     11. Ubicacion
     4. Tipo de RH            12. Contacto de emergencia
     5. EPS                   13. Condiciones de usuario
     6. Condicion medica      14. Discapacidades de usuario
     7. Grado de discapacidad 15. Lugares frecuentes
     8. Barrio                16. Lista de alertas

    17. Registrar un usuario completo
    18. Consulta: detalle de alertas
    19. Consulta: perfil medico
     0. Salir
        ''')
        op = input("Ingrese una opcion: ")

        if op == "1":
            localidad()
        elif op == "2":
            estado_alerta()
        elif op == "3":
            tipo_documento()
        elif op == "4":
            tipo_rh()
        elif op == "5":
            eps()
        elif op == "6":
            condicion_medica()
        elif op == "7":
            grado_discapacidad()
        elif op == "8":
            barrio()
        elif op == "9":
            tipo_alerta()
        elif op == "10":
            usuario()
        elif op == "11":
            ubicacion()
        elif op == "12":
            contacto_emergencia()
        elif op == "13":
            usuario_condicion()
        elif op == "14":
            usuario_discapacidad()
        elif op == "15":
            lugares_frecuentes()
        elif op == "16":
            lista_alertas()
        elif op == "17":
            registro_de_usuario()
        elif op == "18":
            consulta_alertas()
        elif op == "19":
            consulta_perfil_medico()
        elif op == "0":
            print("Hasta luego!")
        else:
            print("Error: opcion no valida.")


main()
