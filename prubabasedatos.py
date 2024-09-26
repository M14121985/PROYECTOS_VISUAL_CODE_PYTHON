from mysql import *
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="test_db"
)

cursor = conexion.cursor()

create_data_base = ''' CREATE DATABASE IF NOT EXISTS test_db'''

seleccionar_db = ''' USE test_db'''
cursor.execute(seleccionar_db)
conexion.commit()


# Definir la sentencia SQL para crear una tabla
create_table_query = '''
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    edad INT
)
'''

# Ejecutar la sentencia SQL
cursor.execute(create_table_query)

# Insertar datos en la tabla
insert_query = '''
INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)
'''

# Datos a insertar
datos_usuario = [('Juan', 30), ('María', 25), ('Carlos', 35), ('Ana', 40), ('Luis', 50), ('Pedro', 45), ('Sofía', 20), 
                 ('Lucía', 22), ('Jorge', 33), ('Marta', 27), ('Pablo', 29), ('Carmen', 39), ('Alberto', 49), ('Elena', 24),
                 ('Víctor', 26), ('Raquel', 36), ('David', 46), ('Natalia', 21), ('Roberto', 23)]

# Ejecutar la sentencia SQL con los datos
cursor.execute(insert_query, datos_usuario)

# Guardar los cambios
conexion.commit()

# Consultar datos de la tabla
select_query = 'usuarios'
 

"""SELECT * FROM usuarios
"""

# Ejecutar la consulta
cursor.execute(select_query)

# Obtener los resultados
filas = cursor.fetchall()

# Mostrar los resultados
for fila in filas:
    print(fila)

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
