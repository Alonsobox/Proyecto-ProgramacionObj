from utilitarios.ConexionBaseDatos import ConexionBaseDatos

class VendedorRepository:

    def __init__(self):
        self.conexion = ConexionBaseDatos().getConection()

    def listarVendedor(self):
        cursor = self.conexion.cursor()
        sql= "select cod_vendedor, nombre_vendedor, apellido_vendedor, sueldo_vendedor, ventas_vendedor from vendedor "
        cursor.execute(sql)
        return cursor.fetchall()
        
    def obtenerVendedor(self,codPer):
        cursor = self.conexion.cursor()
        sql = "select cod_vendedor, nombre_vendedor, apellido_vendedor, sueldo_vendedor, ventas_vendedor from vendedor where cod_vendedor = '{}".format(codPer)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarVendedor(self,objVendedor):
        cursor= self.conexion.cursor()
        sql = "INSERT INTO vendedor (nombre_vendedor,apellido_vendedor,sueldo_vendedor,ventas_vendedor) VALUES ('{}','{}','{}','{}')".format(objVendedor.nombrePer, objVendedor.apelliPer, objVendedor.sueldoVen, objVendedor.ventasVen)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()

    def actualizarVendedor(self,objVendedor):
        cursor = self.conexion.cursor()
        sql = "UPDATE vendedor SET nombre_vendedor = '{}', apellido_vendedor = '{}', sueldo_vendedor = '{}', ventas_vendedor = '{}' WHERE cod_vendedor = '{}' ".format(objVendedor.nombrePer, objVendedor.apelliPer, objVendedor.sueldoVen, objVendedor.ventasVen,objVendedor.codPer)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()