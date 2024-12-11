from utilitarios.ConexionBaseDatos import ConexionBaseDatos

class ModeloRepository:

    def __init__(self):
        self.conexion = ConexionBaseDatos().getConexion()