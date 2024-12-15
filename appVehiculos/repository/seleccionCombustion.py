from utilitarios.ConexionBaseDatos import ConexionBaseDatos

class SeleccionCombustion:

    def __init__(self):
        self.conexion = ConexionBaseDatos().getConection()

    def listarSeleccionCumbustion(self):
        cursor = self.conexion.cursor()
        sql = "select combus_vehiculo from vehiculo"
        cursor.execute(sql)
        return cursor.fetchall()