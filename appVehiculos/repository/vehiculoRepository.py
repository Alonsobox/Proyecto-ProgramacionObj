from utilitarios.ConexionBaseDatos import ConexionBaseDatos

class VehiculoRepository:

    def __init__(self):
        self.conexion = ConexionBaseDatos().getConexion()