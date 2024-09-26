import mysql.connector

# Datos de conexión a la base de datos
config = {
  'user': 'tu_usuario',
  'password': 'tu_contraseña',
  'host': 'localhost',  # o la dirección IP del servidor MySQL
  'database': 'nombre_de_tu_base_de_datos',
  'raise_on_warnings': True
}

# Conectar a la base de datos utilizando el enfoque 'with' para manejar la conexión
with mysql.connector.connect(**config) as conexion:
    # Se ejecutan las operaciones dentro de este bloque indentado
    # Por ejemplo, puedes crear un cursor dentro de este bloque para ejecutar consultas
    cursor = conexion.cursor()

    # Ejemplo: Consulta SQL simple
    cursor.execute("SELECT * FROM tabla_ejemplo")

    # Recuperar los resultados de la consulta
    resultados = cursor.fetchall()

    # Iterar sobre los resultados e imprimirlos
    for fila in resultados:
        print(fila)

# La conexión se cierra automáticamente al salir del bloque 'with'
