class Cliente:

    @staticmethod
    def tabla_clientes_existe(db):
        cursor = db.conexion.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='clientes'")
        return cursor.fetchone() is not None

    @staticmethod
    def crear_tabla_clientes(conexion):
        conexion.execute(
            """CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT, dni TEXT NOT NULL, nombre TEXT NOT NULL,
            apellido TEXT NOT NULL, telefono TEXT, email TEXT NOT NULL, nacionalidad TEXT
            );""")
        conexion.commit()

    @staticmethod
    def agregar_cliente(conexion, dni, nombre, apellido, telefono, email, nacionalidad):
        cursor = conexion.get_cursor()
        cursor.execute("""
            INSERT INTO clientes (dni, nombre, apellido, telefono, email, nacionalidad)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (dni, nombre, apellido, telefono, email, nacionalidad))
        conexion.commit()

    @staticmethod
    def editar_cliente(conexion, id, dni, nombre, apellido, telefono, email, nacionalidad):
        cursor = conexion.get_cursor()
        cursor.execute("""
            UPDATE clientes
            SET dni = ?, nombre = ?, apellido = ?, telefono = ?, email = ?, nacionalidad = ?
            WHERE id = ?
        """, (dni, nombre, apellido, telefono, email, nacionalidad, id))
        conexion.commit()

    @staticmethod
    def mostrar_clientes(conexion):
        cursor = conexion.get_cursor()
        cursor.execute("SELECT * FROM clientes")
        return cursor.fetchall()

    @staticmethod
    def eliminar_cliente(conexion, dni):
        cursor = conexion.get_cursor()
        cursor.execute("DELETE FROM clientes WHERE dni=?", (dni, ))
        conexion.commit()

    @staticmethod
    def obtener_cliente(conexion, id):
        cursor = conexion.get_cursor()
        cursor.execute("SELECT * FROM clientes WHERE id=?", (id, ))
        return cursor.fetchone()
    
    @staticmethod
    def obtener_cliente_por_dni(conexion, dni):
        cursor = conexion.get_cursor()
        cursor.execute("SELECT * FROM clientes WHERE dni=?", (dni, ))
        return cursor.fetchone()