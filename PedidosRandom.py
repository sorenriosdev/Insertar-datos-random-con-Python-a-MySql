import mysql.connector
import random
from decimal import Decimal
from datetime import datetime, timedelta

# Conectar a la base de datos
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Hallomeinss24$',
    database='logisticFast'
)
cursor = conn.cursor()


# Función para obtener un ID aleatorio de una tabla
def obtener_id_aleatorio(tabla, campo_id):
    cursor.execute(f"SELECT {campo_id} FROM {tabla} ORDER BY RAND() LIMIT 1")
    return cursor.fetchone()[0]


# Función para generar una fecha aleatoria en los últimos 30 días
def generar_fecha_aleatoria():
    fecha_actual = datetime.now()
    dias_aleatorios = random.randint(0, 30)
    fecha_aleatoria = fecha_actual - timedelta(days=dias_aleatorios)
    return fecha_aleatoria.strftime('%Y-%m-%d %H:%M:%S')


# Función para generar un número de pedido único
def generar_numero_pedido():
    return f"2{random.randint(100, 999)}"


# Estados de pedido
estados_pedido = [
    'Registrado', 'En bodega', 'Ready to ship', 'En reparto',
    'Entrega fallida', 'Reingreso', 'Entregado', 'Cancelado', 'Siniestro'
]

# Insertar registros en la tabla Pedidos
registros_insertados = 0
numeros_pedido_usados = set()

while registros_insertados < 900:  # Ajusta este número según necesites
    id_cliente = obtener_id_aleatorio('Clientes', 'id_cliente')
    id_seller = obtener_id_aleatorio('Seller', 'id_seller')
    id_producto = obtener_id_aleatorio('Productos', 'id_producto')
    estado_actual = random.choice(estados_pedido)
    id_estado = estados_pedido.index(estado_actual) + 1  # Asumiendo que los IDs en EstadosPedido son secuenciales
    precio_total = round(Decimal(random.uniform(10, 1000)), 2)
    fecha_creacion = generar_fecha_aleatoria()

    # Generar un número de pedido único
    while True:
        numero_pedido = generar_numero_pedido()
        if numero_pedido not in numeros_pedido_usados:
            numeros_pedido_usados.add(numero_pedido)
            break

    # Insertar el registro en la tabla Pedidos
    try:
        cursor.execute("""
            INSERT INTO Pedidos (id_cliente, id_seller, id_estado, id_producto, fecha_creacion, precio_total, estado_actual, numero_pedido)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
        id_cliente, id_seller, id_estado, id_producto, fecha_creacion, precio_total, estado_actual, numero_pedido))
        registros_insertados += 1
    except mysql.connector.IntegrityError:
        # Si hay un error de integridad (e.g., duplicado), simplemente continuamos al siguiente intento
        continue

# Confirmar los cambios
conn.commit()

# Cerrar conexión
cursor.close()
conn.close()

print(f"Se han insertado {registros_insertados} registros en la tabla Pedidos.")
