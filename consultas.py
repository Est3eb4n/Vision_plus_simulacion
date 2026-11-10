from data_base.utils import buscar_por_id
from data_base.localidad import localidades
from data_base.tipo_documento import tipos_documento
from data_base.tipo_rh import tipos_rh
from data_base.eps import lista_eps
from data_base.condicion_medica import condiciones_medicas
from data_base.grado_discapacidad import grados_discapacidad
from data_base.barrio import barrios
from data_base.estado_alerta import estados_alerta
from data_base.tipo_alerta import tipos_alerta
from data_base.usuario import usuarios
from data_base.ubicacion import ubicaciones
from data_base.usuario_condicion import usuario_condiciones
from data_base.usuario_discapacidad import usuario_discapacidades
from data_base.lista_alertas import alertas


# Equivale a la consulta B de search_data.sql (alertas con usuario y ubicacion)
def consulta_alertas():
    print("--- Detalle de alertas ---")
    for a in alertas:
        # hacemos los JOIN a mano buscando cada id
        u = buscar_por_id(usuarios, "id_usuario", a["id_usuario"])
        td = buscar_por_id(tipos_documento, "id_tipo_doc", u["id_tipo_doc"])
        ta = buscar_por_id(tipos_alerta, "id_tipo_alerta", a["id_tipo_alerta"])
        ea = buscar_por_id(estados_alerta, "id_estado", ta["id_estado"])
        ub = buscar_por_id(ubicaciones, "id_ubicacion", a["id_ubicacion"])
        b = buscar_por_id(barrios, "id_barrio", ub["id_barrio"])
        l = buscar_por_id(localidades, "id_localidad", b["id_localidad"])

        print("Alerta", a["id_alerta"], "|", u["nombre"], "|", td["nombre_doc"], u["num_doc"])
        print("   Tipo:", ta["nombre_alerta"], "| Estado:", ea["nombre_estado"])
        print("   Lugar:", ub["direccion"], "-", b["nombre_barrio"], "-", l["nombre_localidad"])
        print("   Fecha:", a["fecha_hora"], "| Indicaciones:", a["indicaciones"])
        print()


# Equivale a la consulta C de search_data.sql (perfil medico)
def consulta_perfil_medico():
    print("--- Perfil medico de los usuarios ---")
    for u in usuarios:
        rh = buscar_por_id(tipos_rh, "id_rh", u["id_rh"])
        eps = buscar_por_id(lista_eps, "id_eps", u["id_eps"])

        condiciones = []
        for uc in usuario_condiciones:
            if uc["id_usuario"] == u["id_usuario"]:
                c = buscar_por_id(condiciones_medicas, "id_condicion", uc["id_condicion"])
                condiciones.append(c["tipo_condicion"])
        if len(condiciones) == 0:
            condiciones.append("Sin condicion registrada")

        discapacidades = []
        for ud in usuario_discapacidades:
            if ud["id_usuario"] == u["id_usuario"]:
                g = buscar_por_id(grados_discapacidad, "id_discapacidad", ud["id_discapacidad"])
                discapacidades.append(g["discapacidad"])
        if len(discapacidades) == 0:
            discapacidades.append("Sin discapacidad registrada")

        print(u["nombre"], "| RH:", rh["grupo_rh"], "| EPS:", eps["nombre_eps"])
        print("   Condiciones:", ", ".join(condiciones))
        print("   Discapacidad:", ", ".join(discapacidades))
        print()


if __name__ == "__main__":
    consulta_alertas()
    consulta_perfil_medico()
