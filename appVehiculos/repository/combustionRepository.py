from utilitarios.ConexionBaseDatos import ConexionBaseDatos

class SeleccionCombustion:

    def __init__(self):
        self.conexion = ConexionBaseDatos().getConection()

    def listarSeleccionCombustion(self):
        cursor = self.conexion.cursor()
        sql = "select cod_combus, tipoCombu_combus from combustion"
        cursor.execute(sql)
        return cursor.fetchall()