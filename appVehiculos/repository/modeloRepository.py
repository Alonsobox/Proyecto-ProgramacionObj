from utilitarios.ConexionBaseDatos import ConexionBaseDatos

class ModeloRepository:

    def __init__(self):
        self.conexion = ConexionBaseDatos().getConection()
    
    def listarModelo(self):
        cursor = self.conexion.cursor()
        sql = "select cod_modelo, diseño_modelo, tecnologia_modelo, seguridad_modelo, interior_modelo, precio from modelo"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def obtenerModelo(self,codMod):
        cursor = self.conexion.cursor()
        sql = "select cod_modelo, diseño_modelo, tecnologia_modelo, seguridad_modelo, interior_modelo, precio from modelo WHERE cod_modelo = '{}'".format(codMod)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarModelo(self,objModelo):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO modelo ( cod_modelo,diseño_modelo, tecnologia_modelo, seguridad_modelo, interior_modelo, precio) VALUES ('{}','{}','{}','{}','{}','{}') ".format(objModelo.codMod,objModelo.diseñoMod, objModelo.tecnologiaMod, objModelo.seguridadMod, objModelo.interiorMod, objModelo.precio)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()

    def actualizarModelo(self, objModelo):
        cursor = self.conexion.cursor()
        sql = "UPDATE modelo SET diseño_modelo = '{}', tecnologia_modelo = '{}', seguridad_modelo = '{}', interior_modelo = '{}', precio = '{}' WHERE  cod_modelo ='{}'".format(objModelo.diseñoMod, objModelo.tecnologiaMod, objModelo.seguridadMod, objModelo.interiorMod, objModelo.precio, objModelo.codMod)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
        
    def eliminarMarca(self, codMod):
        cursor = self.conexion.cursor()
        sql = "delete from modelo where cod_modelo = ?"
        cursor.execute(sql, (codMod,))
        self.conexion.commit()
        cursor.close()
