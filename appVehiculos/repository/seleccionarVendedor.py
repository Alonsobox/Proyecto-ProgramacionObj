from utilitarios.ConexionBaseDatos import ConexionBaseDatos

class SeleccionarVendedor:

    def __init__(self):
        self.conexion = ConexionBaseDatos().getConection()

    def listarSeleccionVendedor(self):
        cursor = self.conexion.cursor()
        sql = "select v.cod_vendedor, concat(v.nombre_vendedor, ' ', v.apellido_vendedor) as Nombre_Vendedor from vendedor v"
        cursor.execute(sql)
        return cursor.fetchall()