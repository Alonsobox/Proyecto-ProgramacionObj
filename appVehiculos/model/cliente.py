from model.persona import Persona
class Cliente(Persona):

    def __init__(self, _codPer, _nombrePer, _apelliPer,_trabaCli, _telfCli, _direcCli):
        super().__init__(_codPer, _nombrePer, _apelliPer)
        self.trabaCli= _trabaCli
        self.telfCli= _telfCli
        self.direcCli= _direcCli




    # def __init__(self, _codCli, _nombreCli, _apelliCli, _trabaCli, _telfCli, _direcCli) -> None:
    #     self.codCli= _codCli
    #     self.nombreCli= _nombreCli
    #     self.apelliCli= _apelliCli
    #     self.trabaCli= _trabaCli
    #     self.telfCli= _telfCli
    #     self.direcCli= _direcCli
        

    def Regalo(self):
        print("Le regalamos una TV de 55' pulgadas")

    
    