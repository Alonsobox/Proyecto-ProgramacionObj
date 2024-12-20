from utilitarios.ConexionBaseDatos import ConexionBaseDatos

class FacturaRespository:

    def __init__(self):
        self.conexion = ConexionBaseDatos().getConection()

    def listarFactura(self):
        cursor = self.conexion.cursor()
        sql = "select f.cod_factura, f.fecha_factura, f.importe_venta, CONCAT(c.nombre_cliente, ' ', c.apellido_cliente) as Nombre_Cliente, concat(ven.nombre_vendedor,' ',ven.apellido_vendedor) as Nombre_Vendedor, veh.cod_vehiculo, con.nombre_concesionaria  from factura f inner join cliente c on f.cod_cliente=c.cod_cliente inner join vendedor ven on f.cod_vendedor=ven.cod_vendedor inner join vehiculo veh on f.cod_vehiculo=veh.cod_vehiculo inner join concesionaria con on f.cod_concesionaria=con.cod_concesionaria"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def obtenerFactura(self, codFac):
        cursor = self.conexion.cursor()
        sql = "select f.cod_factura, f.fecha_factura, f.importe_venta, CONCAT(c.nombre_cliente, ' ', c.apellido_cliente) as Nombre_Cliente, concat(ven.nombre_vendedor,' ',ven.apellido_vendedor) as Nombre_Vendedor, veh.cod_vehiculo, con.nombre_concesionaria  from factura f inner join cliente c on f.cod_cliente=c.cod_cliente inner join vendedor ven on f.cod_vendedor=ven.cod_vendedor inner join vehiculo veh on f.cod_vehiculo=veh.cod_vehiculo inner join concesionaria con on f.cod_concesionaria=con.cod_concesionaria WHERE f.cod_factura='{}'".format(codFac)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarFactura(self,objFactura):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO factura (cod_factura,fecha_factura, importe_venta, cod_cliente, cod_vendedor, cod_vehiculo, cod_concesionaria) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(objFactura.codFac,objFactura.fechaFac, objFactura.importeFac, objFactura.codCli, objFactura.codVen, objFactura.codVeh, objFactura.codCon)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()


    def actualizarFactura(self, objFactura):
         cursor = self.conexion.cursor()
         sql = "UPDATE factura SET fecha_factura = ?, importe_venta = ?, cod_cliente = ?, cod_vendedor = ?, cod_vehiculo = ?, cod_concesionaria = ? WHERE cod_factura = ?" 
         values = (objFactura.fechaFac, objFactura.importeFac, objFactura.codCli, objFactura.codVen, objFactura.codVeh, objFactura.codCon, objFactura.codFac) 
         cursor.execute(sql, values) 
         self.conexion.commit() 
         cursor.close()

    def eliminarFactura(self, codFac):
        cursor = self.conexion.cursor()
        sql = "delete from factura where cod_factura= ?"
        cursor.execute(sql, (codFac,))
        self.conexion.commit()
        cursor.close()