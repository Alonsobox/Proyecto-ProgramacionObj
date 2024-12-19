from utilitarios.ConexionBaseDatos import ConexionBaseDatos

class SeleccionarConcesionaria:

    def __init__(self):
        self.conexion = ConexionBaseDatos().getConection()

    def listarSeleccionConcesionaria(self):
        cursor = self.conexion.cursor()
        sql = "select c.cod_concesionaria, c.nombre_concesionaria from concesionaria c"
        cursor.execute(sql)
        return cursor.fetchall()