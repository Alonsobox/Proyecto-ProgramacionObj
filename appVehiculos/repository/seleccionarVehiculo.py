from utilitarios.ConexionBaseDatos import ConexionBaseDatos

class SeleccionarVehiculo:

    def __init__(self):
        self.conexion = ConexionBaseDatos().getConection()

    def listarSeleccionVehiculo(self):
        cursor = self.conexion.cursor()
        sql = "select v.cod_vehiculo, m.nombre_marca from vehiculo v inner join marca m on v.cod_marca= m.cod_marca"
        cursor.execute(sql)
        return cursor.fetchall()