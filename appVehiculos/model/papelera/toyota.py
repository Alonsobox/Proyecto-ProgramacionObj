from model.proveedor import Proveedor

class Toyota(Proveedor):

    def __init__(self, _codPro, _nombrePro, _telfPro, _stockPro, _direcPro,_cantLocal, _informeVentas) -> None:
        super().__init__(_codPro, _nombrePro, _telfPro, _stockPro, _direcPro)
        self.cantLocal= _cantLocal
        self.informeVentas = _informeVentas

    def atencionCliente(self):
        print("Nosotros nos encargamos de Enviar los producto")