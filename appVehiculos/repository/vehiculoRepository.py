from utilitarios.ConexionBaseDatos import ConexionBaseDatos

class VehiculoRepository:

    def __init__(self):
        self.conexion = ConexionBaseDatos().getConection()

    def listarVehiculo(self):
        cursor = self.conexion.cursor()
        sql = "select v.cod_vehiculo, v.color_vehiculo, v.año_vehiculo, v.combus_vehiculo, m.nombre_marca, mo.tecnologia_modelo from vehiculo v join marca m on v.cod_marca=m.cod_marca join modelo mo on v.cod_modelo=mo.cod_modelo"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def obtenerVehiculo(self,codVeh ):
        cursor = self.conexion.cursor()
        sql = "select v.cod_vehiculo, v.color_vehiculo, v.año_vehiculo, v.combus_vehiculo, m.nombre_marca, mo.tecnologia_modelo from vehiculo v join marca m on v.cod_marca=m.cod_marca join modelo mo on v.cod_modelo=mo.cod_modelo WHERE  v.cod_vehiculo = '{}' ".format(codVeh)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarVehiculo(self, objVehiculo):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO vehiculo (cod_vehiculo,color_vehiculo, año_vehiculo, combus_vehiculo, cod_marca, cod_modelo) VALUES ('{}','{}','{}','{}','{}','{}') ".format(objVehiculo.codVeh,objVehiculo.colorVeh, objVehiculo.añoVeh, objVehiculo.combusVeh, objVehiculo.codMar, objVehiculo.codMod)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()

    def actualizarVehiculo(self, objVehiculo):
        cursor = self.conexion.cursor()
        sql = "UPDATE vehiculo SET color_vehiculo = '{}', año_vehiculo = '{}', combus_vehiculo = '{}', cod_marca = '{}', cod_modelo = '{}' WHERE  cod_vehiculo = '{}'".format(objVehiculo.colorVeh, objVehiculo.añoVeh, objVehiculo.combusVeh, objVehiculo.codMar, objVehiculo.codMod, objVehiculo.codVeh)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
