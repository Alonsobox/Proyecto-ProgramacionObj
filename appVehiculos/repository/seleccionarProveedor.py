from utilitarios.ConexionBaseDatos import ConexionBaseDatos

class SeleccionarProveedor:

    def __init__(self):
        self.conexion = ConexionBaseDatos().getConection()

    def listarSeleccionProveedor(self):
        cursor = self.conexion.cursor()
        sql = "select cod_proveedor, nombre_proveedor from proveedor"
        cursor.execute(sql)
        return cursor.fetchall()