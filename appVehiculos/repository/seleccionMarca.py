from utilitarios.ConexionBaseDatos import ConexionBaseDatos

class SeleccionMarca:

    def __init__(self):
        self.conexion = ConexionBaseDatos().getConection()

    def listarSeleccionMarca(self):
        cursor = self.conexion.cursor()
        sql = "select cod_marca,nombre_marca from marca"
        cursor.execute(sql)
        return cursor.fetchall()