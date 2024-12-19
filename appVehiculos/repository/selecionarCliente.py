from utilitarios.ConexionBaseDatos import ConexionBaseDatos

class SeleccionarCliente:

    def __init__(self):
        self.conexion = ConexionBaseDatos().getConection()

    def listarSeleccionCliente(self):
        cursor = self.conexion.cursor()
        sql = "select c.cod_cliente,concat(c.nombre_cliente, ' ', c.apellido_cliente) as Nombre_Cliente from cliente c"
        cursor.execute(sql)
        return cursor.fetchall()