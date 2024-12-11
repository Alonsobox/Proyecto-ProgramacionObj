from utilitarios.ConexionBaseDatos import ConexionBaseDatos

class FacturaRespository:

    def __init__(self):
        self.conexion = ConexionBaseDatos().getConection()