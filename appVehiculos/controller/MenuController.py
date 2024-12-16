from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication
from controller.vendedorController import VendedorController
from controller.vehiculoController import VehiculoController
from controller.proveedorController import ProveedorController

class MenuController:

    def __init__(self):
        app = QApplication([])
        self.ventana = uic.loadUi("view/menu.ui")
        self.ventana.show()
        self.ventana.actionvendedor.triggered.connect(self.actionvendedorclick)
        self.ventana.actionVehiculo.triggered.connect(self.actionVehiculoclick)
        self.ventana.actionProveedor.triggered.connect(self.actionProveedorclick)
        app.exec()

    def actionvendedorclick(self):
        self.fmvendedor = VendedorController()
        self.fmvendedor.ventana.show()

    def actionVehiculoclick(self):
        self.fmvehiculo = VehiculoController()
        self.fmvehiculo.ventana.show()
    
    def actionProveedorclick(self):
        self.fmproveedor = ProveedorController()
        self.fmproveedor.ventana.show()