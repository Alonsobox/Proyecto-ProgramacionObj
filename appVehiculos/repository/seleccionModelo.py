from utilitarios.ConexionBaseDatos import ConexionBaseDatos

class SeleccionModelo:

    def __init__(self):
        self.conexion = ConexionBaseDatos().getConection()

    def listarSeleccionModelo(self):
        cursor = self.conexion.cursor()
        sql = "select cod_modelo, diseño_modelo from modelo"
        cursor.execute(sql)
        return cursor.fetchall()