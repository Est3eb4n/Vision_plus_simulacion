from datetime import datetime

# Funciones que se repetian en todos los archivos, por eso las deje aqui


def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Ingrese un numero entero valido.")


def pedir_texto(mensaje, largo_max, obligatorio=True):
    while True:
        texto = input(mensaje).strip()
        if texto == "" and obligatorio:
            print("Error: este campo no puede estar vacio.")
        elif len(texto) > largo_max:
            print("Error: maximo", largo_max, "caracteres.")
        elif texto == "":
            return None  # en la BD seria NULL
        else:
            return texto


def pedir_fecha(mensaje):
    while True:
        texto = input(mensaje)
        try:
            datetime.strptime(texto, "%Y-%m-%d")
            return texto
        except ValueError:
            print("Error: use el formato AAAA-MM-DD, por ejemplo 1990-05-14.")


def pedir_decimal(mensaje, minimo, maximo):
    while True:
        try:
            numero = float(input(mensaje))
        except ValueError:
            print("Error: Ingrese un numero valido (ej: 4.7012).")
            continue
        if numero < minimo or numero > maximo:
            print("Error: el valor debe estar entre", minimo, "y", maximo)
        else:
            return numero


def siguiente_id(tabla, campo_id):
    # simula el AUTO_INCREMENT de MySQL
    mayor = 0
    for fila in tabla:
        if fila[campo_id] > mayor:
            mayor = fila[campo_id]
    return mayor + 1


def buscar_por_id(tabla, campo_id, valor):
    for fila in tabla:
        if fila[campo_id] == valor:
            return fila
    return None


def pedir_id_existente(mensaje, tabla, campo_id, campo_nombre):
    # simula la FOREIGN KEY: el id tiene que existir en la otra tabla
    print("Opciones disponibles:")
    for fila in tabla:
        print("  ", fila[campo_id], "-", fila[campo_nombre])

    while True:
        valor = pedir_entero(mensaje)
        if buscar_por_id(tabla, campo_id, valor) is not None:
            return valor
        print("Error: el id", valor, "no existe en la tabla relacionada.")


def existe_par(tabla, campo_a, valor_a, campo_b, valor_b):
    for fila in tabla:
        if fila[campo_a] == valor_a and fila[campo_b] == valor_b:
            return True
    return False


def fecha_hora_actual():
    # simula TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
