from utilitarios.ConexionBaseDatos import ConexionBaseDatos

class VendedorRepository:

    def __init__(self):
        self.conexion = ConexionBaseDatos().getConexion()

    def listarVendedor(self):
        cursor = self.conexion.cursor()
        sql= "select * from vendedor"
        cursor.execute(sql)
        return cursor.fetchall()
        