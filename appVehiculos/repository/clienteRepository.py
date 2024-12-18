from utilitarios.ConexionBaseDatos import ConexionBaseDatos

class ClienteRepository:

    def __init__(self):
        self.conexion = ConexionBaseDatos().getConection()
    
    def listarCliente(self):
        cursor = self.conexion.cursor()
        sql= "select cod_cliente,nombre_cliente,apellido_cliente,trabajo_cliente,telefono_cliente,direccion_cliente from cliente"
        cursor.execute(sql)
        return cursor.fetchall()

    def obtenerCliente(self,codPersona):
        cursor = self.conexion.cursor()
        sql = "select cod_cliente,nombre_cliente,apellido_cliente,trabajo_cliente,telefono_cliente,direccion_cliente from cliente WHERE cod_cliente = ?"
        cursor.execute(sql,codPersona)
        return cursor.fetchone()

   
    
    def insertarCliente(self,objCliente):
        cursor= self.conexion.cursor()
        sql = "INSERT INTO cliente (cod_cliente,nombre_cliente,apellido_cliente,trabajo_cliente,telefono_cliente,direccion_cliente) VALUES ('{}','{}','{}','{}','{}','{}')".format(objCliente.codPer,objCliente.nombrePer, objCliente.apelliPer, objCliente.trabaCli, objCliente.telfCli, objCliente.direcCli)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()

    def actualizarCliente(self,objCliente):
        cursor = self.conexion.cursor()
        sql = "UPDATE cliente SET nombre_cliente = '{}', apellido_cliente = '{}', trabajo_cliente = '{}', telefono_cliente = '{}', direccion_cliente = '{}' WHERE cod_cliente = '{}' ".format(objCliente.nombrePer, objCliente.apelliPer, objCliente.trabaCli, objCliente.telfCli, objCliente.direcCli,objCliente.codPer)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()