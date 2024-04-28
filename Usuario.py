class Usuario:

    def __init__(self, nombre, tipo_empleado, usuario, constrasenia):
        self.nombre = nombre
        self.apellido = tipo_empleado
        self.email = usuario
        self.telefono = constrasenia

    """ Metodo para crear un usuario dentro de la base de datos """
    def create_user(nombre,tipo_empleado,usuario,constrasenia):
        """Realiza logica para crear un usuario en la base de datos."""
        pass

    """ Metodo para buscar un usuario dentro de la base de datos """
    def find_user(id):
        """Realiza logica para buscar un usuario en la base de datos."""
        pass

    """ Metodo para editr un usuario dentro de la base de datos """
    def edit_usuer(id,payload):
        """Realiza logica para editar un usuario en la base de datos."""
        pass
    
    """ Metodo para eliminar un usuario dentro de la base de datos """
    def delete_user(id):
        """Realiza logica para eliminar un usuario en la base de datos."""
        pass

   
