class Proveedor:

    def __init__(self, _codPro, _nombrePro, _telfPro, _stockPro, _direcPro) -> None:
        self.codPro= _codPro
        self.nombrePro= _nombrePro
        self.telfPro= _telfPro
        self.stockPro= _stockPro
        self.direcPro= _direcPro
        


    #metodo que vamos a usar de ejemplo para sobreescribir    

    def atencionCliente(self):
        print("El personal debe atender a los clientes")