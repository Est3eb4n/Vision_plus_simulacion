# Vision_plus - Simulacion de base de datos en Python

Simula en memoria la base `sistema_alertas` (16 tablas de `create_data_base.sql`)
con listas de diccionarios. Los datos iniciales salen de `Insertion_data.sql`.

## Como ejecutarlo
    python main.py

## Estructura
    main.py                  menu principal
    registro_de_usuario.py   registro paso a paso (usuario, contacto, condiciones, discapacidad)
    consultas.py             consultas B y C de search_data.sql
    data_base/               un archivo por tabla + utils.py

## Que se simula
- AUTO_INCREMENT: el id se genera solo.
- FOREIGN KEY: no deja usar un id que no exista en la otra tabla.
- UNIQUE: no deja repetir el numero de documento.
- NOT NULL: los campos obligatorios no pueden ir vacios.
- Los datos se pierden al cerrar el programa (no se guarda en disco).
