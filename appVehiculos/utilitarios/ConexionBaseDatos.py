import pyodbc

class ConexionBaseDatos:

    def __init__(self) -> None:
        self.conexion = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=SQLINJECTION;'  
            'DATABASE=VentaVehiculos121'  
            'Trusted_Connection=yes;'
        )
    
    def getConexion(self):
        return self.conexion
