from utilitarios.ConexionBaseDatos import ConexionBaseDatos

class ProveedorRepository:

    def __init__(self):
        self.conexion = ConexionBaseDatos().getConection()