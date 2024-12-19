from utilitarios.ConexionBaseDatos import ConexionBaseDatos

class MarcaRepository:
    
    def __init__(self):
        self.conexion = ConexionBaseDatos().getConection()

    def listarMarca(self):
        cursor = self.conexion.cursor()
        sql = "select cod_marca, nombre_marca, stock_marca from marca"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def obtenerMarca(self, codMar):
        cursor = self.conexion.cursor()
        sql = "select cod_marca, nombre_marca, stock_marca from marca WHERE cod_marca = '{}'".format(codMar)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarMarca(self, objMarca):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO marca (cod_marca,nombre_marca, stock_marca) VALUES ('{}','{}','{}')".format(objMarca.codMar,objMarca.nombreMar, objMarca.stockMar)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()

    def actualizarMarca(self, objMarca):
        cursor = self.conexion.cursor()
        sql = "UPDATE marca SET nombre_marca = '{}', stock_marca = '{}' WHERE cod_marca = '{}'".format(objMarca.nombreMar, objMarca.stockMar, objMarca.codMar)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()


    def eliminarMarca(self, codMar):
        cursor = self.conexion.cursor()
        sql = "DELETE FROM marca WHERE cod_marca = ?"
        cursor.execute(sql, (codMar,))
        self.conexion.commit()
        cursor.close()
