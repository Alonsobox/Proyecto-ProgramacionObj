from utilitarios.ConexionBaseDatos import ConexionBaseDatos

class ProveedorRepository:

    def __init__(self):
        self.conexion = ConexionBaseDatos().getConection()

    def listarProveedor(self):
        cursor = self.conexion.cursor()
        sql = "select cod_proveedor, nombre_proveedor, telefono_proveedor, stock_proveedor, direccion_proveedor from proveedor "
        cursor.execute(sql)
        return cursor.fetchall()
    
    def obtenerProveedor(self,codPro):
        cursor= self.conexion.cursor()
        sql = "select cod_proveedor, nombre_proveedor, telefono_proveedor, stock_proveedor, direccion_proveedor from proveedor WHERE cod_proveedor = '{}'".format(codPro)
        cursor.execute(sql)
        return cursor.fetchall()
    
    def insertarProveedor(self, objProveedor):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO proveedor (nombre_proveedor, telefono_proveedor, stock_proveedor, direccion_proveedor) VALUES ('{}','{}','{}','{}')".format(objProveedor.nombrePro, objProveedor.telfPro, objProveedor.stockPro, objProveedor.direcPro)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()

    def actualizarProveedor(self,objProveedor):
        cursor = self.conexion.cursor()
        sql = "UPDATE proveedor SET nombre_proveedor = '{}', telefono_proveedor = '{}', stock_proveedor = '{}', direccion_proveedor = '{}' WHERE cod_proveedor = '{}'".format(objProveedor.nombrePro, objProveedor.telfPro, objProveedor.stockPro, objProveedor.direcPro, objProveedor.codPro)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()