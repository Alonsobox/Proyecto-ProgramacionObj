from model.persona import Persona

class Vendedor(Persona):

    def __init__(self, _codPer, _nombrePer, _apelliPer,_sueldoVen, _ventasVen):
        super().__init__(_codPer, _nombrePer, _apelliPer)
        self.sueldoVen= _sueldoVen
        self.ventasVen= _ventasVen

    # def __init__(self, _codVen, _nombreVen, _apelliVen, _sueldoVen, _ventasVen) -> None:
    #     self.codVen= _codVen
    #     self.nombreVen= _nombreVen
    #     self.apelliVen= _apelliVen
    #     self.sueldoVen= _sueldoVen
    #     self.ventasVen= _ventasVen

    # METODOS 

    def totalVentas(self):
        print("El total de ventas de este Vendedor")

    def añosEmpresa(self):
        print("Años de este vendedor trabajando en la empresa")
    
    def vacaciones(self):
        print("Las vacaciones de este trabajador")

    ##Metodo Sobreescrito

    