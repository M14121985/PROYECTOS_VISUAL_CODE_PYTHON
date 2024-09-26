import mysql.connector
from mysql.connector import Error

try:
    # Conectar a la base de datos
    db = mysql.connector.connect(
      host="localhost",
      port=3307,
      user="root",
      password="1234",
      database=""
    )

    cursor = db.cursor()
    # Comprobar si la conexión se ha realizado correctamente no es necesario pero es una buena practica
    if db.is_connected():
        print("Conectado a la base de datos")

    # Crear una base de datos
    cursor.execute("CREATE DATABASE IF NOT EXISTS test_db")
    cursor.execute("USE test_db")
    
    # Crear una tabla
    cursor.execute("CREATE TABLE IF NOT EXISTS Ejemplo (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(40), edad INT)")

    # Insertar datos en la tabla
    query = "INSERT INTO Ejemplo (nombre, edad) VALUES (%s, %s)"
    valores = [("marcos", 30), ("luis", 25), ("ana", 35), ("carlos", 40), ("luisa", 50), ("pedro", 45),
               ("sofia", 20), ("lucia", 22), ("jorge", 33), ("marta", 27), ("pablo", 29), ("carmen", 39),
               ("alberto", 49), ("elena", 24), ("victor", 26), ("raquel", 36), ("david", 46), ("natalia", 21),
               ("roberto", 23), ("juan", 29), ("maria", 26), ("pepe", 38), ("luis", 31), ("sara", 27), ("carla", 35),
                ("manuel", 40), ("luciana", 33), ("oscar", 29), ("diana", 36), ("alicia", 30), ("javier", 28),
                ("andres", 34), ("rodrigo", 37), ("valeria", 32), ("elisa", 39), ("ana", 25), ("pablo", 33),
                ("laura", 31), ("jose", 28), ("lucia", 26), ("carlos", 34), ("maria", 30), ("juan", 27), ("luis", 35),]
    
    cursor.executemany(query, valores)  # usamos executemany para insertar varios valores 
    db.commit()

    # Consultar datos de la tabla
    cursor.execute("SELECT * FROM Ejemplo")
    for elemento in cursor:# Recuperar los resultados de la consulta y mostrarlos SIN FETCHALL
        print("los datos de esta fila son: ", elemento)
        
    resultados = cursor.fetchall()# Recuperar los resultados de la consulta y mostrarlos OTRA OPCION DISTINTA A LA DE ARRIBA

    for fila in resultados:
        print(fila)

except mysql.connector.Error as err:
    print(f"Error en la base de datos: {err}")

finally:  # Cerrar la conexión
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()
        print("Conexión cerrada")
