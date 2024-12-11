from model.concesionaria import Concesionaria

class AreaVentas(Concesionaria):

    # Herencia
    def __init__(self, _codCon, _nombreCon, _canTrabCon, _codPro, _direcCon, _numPersonal, _descripPuestos, ) -> None:
        super().__init__(_codCon, _nombreCon, _canTrabCon, _codPro, _direcCon)
        self.numPersonal = _numPersonal
        self.descripPuestos= _descripPuestos