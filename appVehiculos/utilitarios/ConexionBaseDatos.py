import pyodbc

class ConexionBaseDatos:

    def __init__(self) -> None:
        self.conexion = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=DESKTOP-FTL0H2O\SQLINJECTION;'  
            'DATABASE=VentaVehiculos;'  
            'Trusted_Connection=yes;'
        )
    
    def getConection(self):
        return self.conexion
