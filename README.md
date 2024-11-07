# Generador de Datos random de Pedidos para una base de datos en MySql

Este script de Python genera datos de prueba para la base de datos de un sistema logístico, específicamente para la tabla de Pedidos, el objetivo es poblar la bd con data para poder desarrollar proyectos personales, examenes, etc, puedes clonarlo y adaptarlo a tus requerimientos.

## Descripción

El script genera registros aleatorios para simular pedidos en un sistema de logística, incluyendo:
- Números de pedido únicos
- Fechas de creación aleatorias (últimos 30 días)
- Estados de pedido variados
- Precios aleatorios
- Relaciones con clientes, vendedores y productos existentes

## Requisitos

- Python 3 (yo use py 3.12)
- MySQL
- Librería mysql-connector-python


## Configuración

Asegúrate de tener configurada la base de datos con las siguientes credenciales:
```python
host='localhost'
user='root'
password='root'
database='el nombre de tu bd'
