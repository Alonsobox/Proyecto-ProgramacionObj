from utilitarios.ConexionBaseDatos import ConexionBaseDatos

class VehiculoRepository:

    def __init__(self):
        self.conexion = ConexionBaseDatos().getConection()

    def listarVehiculo(self):
        cursor = self.conexion.cursor()
        sql = "select v.cod_vehiculo, v.color_vehiculo, v.año_vehiculo, com.tipoCombu_combus, m.nombre_marca, mo.diseño_modelo from vehiculo v join combustion com on v.cod_combus = com.cod_combus join marca m on v.cod_marca=m.cod_marca join modelo mo on v.cod_modelo=mo.cod_modelo"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def obtenerVehiculo(self,codVeh ):
        cursor = self.conexion.cursor()
        sql = "select v.cod_vehiculo, v.color_vehiculo, v.año_vehiculo, com.tipoCombu_combus, m.nombre_marca, mo.diseño_modelo from vehiculo v join combustion com on v.cod_combus = com.cod_combus join marca m on v.cod_marca=m.cod_marca join modelo mo on v.cod_modelo=mo.cod_modelo WHERE  v.cod_vehiculo = '{}' ".format(codVeh)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarVehiculo(self, objVehiculo):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO vehiculo (cod_vehiculo,color_vehiculo, año_vehiculo, cod_combus, cod_marca, cod_modelo) VALUES ('{}','{}','{}','{}','{}','{}') ".format(objVehiculo.codVeh,objVehiculo.colorVeh, objVehiculo.añoVeh, objVehiculo.codCombus, objVehiculo.codMar, objVehiculo.codMod)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()

    def actualizarVehiculo(self, objVehiculo):
        cursor = self.conexion.cursor()
        sql = "UPDATE vehiculo SET color_vehiculo = '{}', año_vehiculo = '{}', cod_combus = '{}', cod_marca = '{}', cod_modelo = '{}' WHERE  cod_vehiculo = '{}'".format(objVehiculo.colorVeh, objVehiculo.añoVeh, objVehiculo.codCombus, objVehiculo.codMar, objVehiculo.codMod, objVehiculo.codVeh)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()



    def eliminarVehiculo(self, codVeh):
        cursor = self.conexion.cursor()
        sql = "delete from vehiculo where cod_vehiculo= ?"
        cursor.execute(sql, (codVeh,))
        self.conexion.commit()
        cursor.close()
