from utilitarios.ConexionBaseDatos import ConexionBaseDatos

class ClienteRepository:

    def __init__(self):
        self.conexion = ConexionBaseDatos().getConexion()