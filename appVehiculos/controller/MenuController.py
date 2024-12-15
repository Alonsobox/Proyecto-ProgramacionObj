from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication
from controller.vendedorController import VendedorController
from controller.vehiculoController import VehiculoController

class MenuController:

    def __init__(self):
        app = QApplication([])
        self.ventana = uic.loadUi("view/menu.ui")
        self.ventana.show()
        self.ventana.actionvendedor.triggered.connect(self.actionvendedorclick)
        self.ventana.actionVehiculo.triggered.connect(self.actionVehiculoclick)
        app.exec()

    def actionvendedorclick(self):
        self.fmvendedor = VendedorController()
        self.fmvendedor.ventana.show()

    def actionVehiculoclick(self):
        self.fmvehiculo = VehiculoController()
        self.fmvehiculo.ventana.show()
 