class Reserva:

    @staticmethod
    def tabla_reservas_existe(db):
        cursor = db.conexion.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='reservas'")
        return cursor.fetchone() is not None

    @staticmethod
    def crear_tabla_reservas(conexion):
        conexion.execute(
            """CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha_entrada TEXT NOT NULL,
            fecha_salida TEXT NOT NULL,
            cantidad_huespedes INTEGER NOT NULL,
            precio REAL NOT NULL,
            id_habitacion INTEGER NOT NULL,
            id_cliente INTEGER NOT NULL,
            id_reserva_gestor INTEGER NOT NULL
            );""")
        conexion.commit()

    @staticmethod
    def agregar_reserva(conexion, fecha_entrada, fecha_salida, cantidad_huespedes, precio, id_habitacion, id_cliente, id_reserva_gestor):
        conexion.execute("""
            INSERT INTO reservas (fecha_entrada, fecha_salida, cantidad_huespedes, precio, id_habitacion, id_cliente, id_reserva_gestor)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (fecha_entrada, fecha_salida, cantidad_huespedes, precio, id_habitacion, id_cliente, id_reserva_gestor))
        conexion.commit()

    @staticmethod
    def editar_reserva(conexion, id, fecha_entrada, fecha_salida, cantidad_huespedes, precio, id_habitacion, origen_reserva):
        conexion.execute("""
            UPDATE reservas
            SET fecha_entrada = ?, fecha_salida = ?, cantidad_huespedes = ?, precio = ?, id_habitacion = ?, id_reserva_gestor = ?
            WHERE id = ?
        """, (fecha_entrada, fecha_salida, cantidad_huespedes, precio, id_habitacion, origen_reserva, id))
        conexion.commit()

    @staticmethod
    def mostrar_reservas(conexion):
        cursor = conexion.get_cursor()
        cursor.execute("SELECT * FROM reservas")
        return cursor.fetchall()

    @staticmethod
    def eliminar_reserva(conexion, id):
        conexion.execute("DELETE FROM reservas WHERE id=?", (id,))
        conexion.commit()

    @staticmethod
    def obtener_reserva(conexion, id):
        cursor = conexion.get_cursor()
        cursor.execute("SELECT * FROM reservas WHERE id=?", (id,))
        return cursor.fetchone()
