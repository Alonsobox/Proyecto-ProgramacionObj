from utilitarios.ConexionBaseDatos import ConexionBaseDatos

class ConcesionariaRepository:

    def __init__(self):
        self.conexion = ConexionBaseDatos().getConection()

    def listarConcesionaria(self):
        cursor = self.conexion.cursor()
        sql = "select c.cod_concesionaria, c.nombre_concesionaria, c.cantidad_trabaja_concesionaria, c.direccion_concesionaria, p.cod_proveedor from concesionaria c inner join proveedor p on c.cod_proveedor=p.cod_proveedor"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def obtenerConcesionaria(self,codCon):
        cursor = self.conexion.cursor()
        sql = "select c.cod_concesionaria, c.nombre_concesionaria, c.cantidad_trabaja_concesionaria, c.direccion_concesionaria, p.cod_proveedor from concesionaria c inner join proveedor p on c.cod_proveedor=p.cod_proveedor WHERE c.cod_concesionaria= '{}'".format(codCon)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarConcesionaria(self, objConcesionaria):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO concesionaria (nombre_concesionaria, cantidad_trabaja_concesionaria, direccion_concesionaria, cod_proveedor) VALUES ('{}','{}','{}','{}') ".format(objConcesionaria.nombreCon, objConcesionaria.canTrabCon, objConcesionaria.direcCon, objConcesionaria.codPro)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()

    def actualizarConcesionaria(self, objConcesionaria):
        cursor = self.conexion.cursor()
        sql= "UPDATE concesionaria SET nombre_concesionaria = '{}', cantidad_trabaja_concesionaria = '{}', direccion_concesionaria = '{}', cod_proveedor = '{}' WHERE cod_concesionaria = '{}'".format(objConcesionaria.nombreCon, objConcesionaria.canTrabCon, objConcesionaria.direcCon, objConcesionaria.codPro, objConcesionaria.codCon)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
