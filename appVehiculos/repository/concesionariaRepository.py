from utilitarios.ConexionBaseDatos import ConexionBaseDatos

class ConcesionariaRepository:

    def __init__(self):
        self.conexion = ConexionBaseDatos().getConection()