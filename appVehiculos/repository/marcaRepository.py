from utilitarios.ConexionBaseDatos import ConexionBaseDatos

class MarcaRepository:
    
    def __init__(self):
        self.conexion = ConexionBaseDatos().getConection()

    