from flask import Flask, g, render_template, request
from database.conexion import Conexion
from classes.Cliente import Cliente
from classes.Reserva import Reserva

app = Flask(__name__)

DATABASE = 'database/houseHunterHotel.db'

def get_db():
    if 'db' not in g:
        g.db = Conexion(DATABASE)
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.conexion.close()

def inicializar_datos():
    with get_db() as db:
        if not Cliente.tabla_clientes_existe(db):
            Cliente.crear_tabla_clientes(db)
            Cliente.agregar_cliente(db, '43634567', 'Juan', 'Perez', '12345678', 'juanperez@gmail.com', 'Argentino')
            Cliente.agregar_cliente(db, '30433213', 'Ana', 'Belloni', '41325123', 'ana@gmail.com', 'Uruguayo')
        
        if not Reserva.tabla_reservas_existe(db):
            Reserva.crear_tabla_reservas(db)
            Reserva.agregar_reserva(db, '20241201', '20241210', 2, 999.00, 1, 1, 1)
            Reserva.agregar_reserva(db, '20240112', '20240212', 4, 1900.00, 1, 2, 1)

@app.route('/')
def index():
    inicializar_datos()
    return render_template('index.html')  

@app.route('/agregar_reserva', methods=['GET', 'POST'])
def agregar_reserva():
    return render_template('agregar_reserva.html')

@app.route('/guardar_reserva_nueva', methods=['GET', 'POST'])
def guardar_reserva_nueva():
    if request.method == 'POST':

        # Datos del cliente
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        email = request.form['email']
        nacionalidad = request.form['nacionalidad']

        # Datos de la reserva
        dni = request.form['dni']
        fecha_entrada = request.form['fecha_entrada']
        fecha_salida = request.form['fecha_salida']
        cantidad_huespedes = request.form['cantidad_huespedes']
        precio = request.form['precio']
        id_reserva_gestor = 1
        id_habitacion = 1 

        cliente = Cliente.obtener_cliente_por_dni(get_db(), dni)
        if cliente is None:
            Cliente.agregar_cliente(get_db(), dni, nombre, apellido, telefono, email, nacionalidad)
        
        id_cliente = Cliente.obtener_cliente_por_dni(get_db(), dni)[0]
        
        Reserva.agregar_reserva(get_db(), fecha_entrada, fecha_salida, cantidad_huespedes, precio, id_habitacion, id_cliente, id_reserva_gestor)

        return render_template('index.html')
    return render_template('index.html')

@app.route('/mostrar_reserva', methods=['GET', 'POST'])
def mostrar_reserva():
    if request.method == 'POST':
        try:
            numero_reserva = int(request.form['numero_reserva'])
            dni = int(request.form['dni'])
        except ValueError:
            return "Número de reserva no válido", 400

        reserva = Reserva.obtener_reserva(get_db(), numero_reserva)
        
        if reserva is None:
            return "No se encontró ninguna reserva con ese número.", 404
        
        cliente = Cliente.obtener_cliente(get_db(), int(reserva[6]))

        if dni != int(cliente[1]):
            return "El DNI no coincide con el DNI del cliente de la reserva.", 400
        
        return render_template('mostrar_reserva.html', reserva=reserva, cliente=cliente)
    return render_template('mostrar_reserva.html', reserva=None, cliente=None)

@app.route('/editar_reserva', methods=['GET', 'POST'])
def editar_reserva():
    if request.method == 'POST':
        id_reserva = request.form['id_reserva']
        nombre_cliente = request.form['cliente']
        fecha_entrada = request.form['fecha_entrada']
        fecha_salida = request.form['fecha_salida']
        cantidad_huespedes = request.form['cantidad_huespedes']
        precio = request.form['precio']
        tipo_habitacion = request.form['tipo_habitacion']
        origen_reserva = request.form['origen_reserva']

        return render_template('editar_reserva.html', id_reserva= id_reserva, nombre_cliente=nombre_cliente, fecha_entrada=fecha_entrada,fecha_salida=fecha_salida,cantidad_huespedes=cantidad_huespedes,precio=precio,tipo_habitacion=tipo_habitacion,origen_reserva=origen_reserva)
    return render_template('editar_reserva.html',id_reserva= None, nombre_cliente=None, fecha_entrada=None,fecha_salida=None,cantidad_huespedes=None,precio=None,tipo_habitacion=None,origen_reserva=None)

@app.route('/guardar_reserva_editada', methods=['GET', 'POST'])
def guardar_reserva_editada():
    if request.method == 'POST':
        id_reserva = request.form['id_reserva']
        fecha_entrada = request.form['fecha_entrada']
        fecha_salida = request.form['fecha_salida']
        cantidad_huespedes = request.form['cantidad_huespedes']
        precio = request.form['precio']
        tipo_habitacion = request.form['tipo_habitacion']
        origen_reserva = request.form['origen_reserva']

        Reserva.editar_reserva(get_db(),id_reserva, fecha_entrada, fecha_salida, cantidad_huespedes, precio, tipo_habitacion, origen_reserva)

        return render_template('index.html')
    return render_template('index.html')

@app.route('/eliminar_reserva', methods=['GET', 'POST'])
def eliminar_reserva():
    if request.method == 'POST':
        id_reserva = request.form['id_reserva']
        Reserva.eliminar_reserva(get_db(),id_reserva)

        return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
