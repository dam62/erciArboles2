import psycopg2

def connect():
    # Conectar a PostgreSQL
    conn = psycopg2.connect(
        dbname="videojuego",
        user="postgres",
        password="1234",
        host="192.168.96.128",
        port="5433"
    )
    return conn

def insertar_presonaje(nombre, vida, magia, ataque, defensa, rapidez, suerte):

    conn = connect()  # Conectar a la base de datos
    try:
        cursor = conn.cursor()  # Crear un cursor para ejecutar consultas SQL
        query = """
        INSERT INTO personaje (nombre, vida, magia, ataque, defensa, rapidez, suerte)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        # Ejecutar la consulta pasando los valores como parámetros
        cursor.execute(query, (nombre, vida, magia, ataque, defensa, rapidez, suerte))

        # Confirmar la transacción
        conn.commit()
        print("Personaje registrado correctamente.")

    except psycopg2.Error as e:
        print(f"Error en la base de datos: {e}")

    finally:
        if conn:
            cursor.close()  # Cerrar el cursor
            conn.close()  # Cerrar la conexión a la base de datos
