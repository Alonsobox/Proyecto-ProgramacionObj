from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import QDate
from repository.vehiculoRepository import VehiculoRepository
from model.vehiculo import Vehiculo

class VehiculoController:
    def __init__(self):
        self.ventana = uic.loadUi("view/vehiculo.ui")
        self.vehiculoRepository = VehiculoRepository()
        self.listarVehiculo()
        self.ventana.tblVehiculo.cellClicked.connect(self.tblVehiculocellclicked)
        self.ventana.btnguardar.clicked.connect(self.btnguardarclick)
        self.ventana.btnlimpiar.clicked.connect(self.btnlimpiarclick)

    def btnlimpiarclick(self):
        self.ventana.txtCodigo.setText("")
        self.ventana.txtCodigo.setEnabled(True)
        self.ventana.txtColor.setText("")
        self.ventana.dateVehiculo.setDate(QDate.currentDate())
        self.ventana.cboMarca.setCurrentIndex(-1)       ##limpia el CBX seleccionando un indice no valido
        self.ventana.cboCombustion.setCurrentIndex(-1)       
        self.ventana.cboModelo.setCurrentIndex(-1)       

    def tblVehiculocellclicked(self, fila):
        idvehiculo = self.ventana.tblVehiculo.item(fila, 0).text().strip()
        self.ventana.txtCodigo.setText(idvehiculo)
        objVehiculo = self.vendedorrepository.obtenerVendedor(idvehiculo)
        
        if objVehiculo:
            self.ventana.txtColor.setText(objVehiculo[1])
            self.ventana.txtApellido.setText(objVehiculo[2])
            self.ventana.txtSueldo.setText(str(objVehiculo[3]))  
            self.ventana.txtCantVentas.setText(str(objVehiculo[4]))  
            

    def btnguardarclick(self):
        codPer = self.ventana.txtCodigo.text()
        nombrePer = self.ventana.txtNombre.text()
        apelliPer = self.ventana.txtApellido.text()
        sueldoVen = self.ventana.txtSueldo.text()
        ventasVen = self.ventana.txtCantVentas.text()
        objVendedor= Vendedor(codPer,nombrePer,apelliPer,sueldoVen,ventasVen)
        
        if self.vendedorrepository.obtenerVendedor(objVendedor.codPer) is None:## busca el vendedor por codigo, sino lo encuentra inserta
            self.vendedorrepository.insertarVendedor(objVendedor)               
        else:                                                           ##el vendedor Existe en la BD, entonces actualiza
            self.vendedorrepository.actualizarVendedor(objVendedor)             
        self.listarVendedor()


    
  
            
    def listarVendedor(self):
        vendedores = self.vendedorrepository.listarVendedor()
        self.ventana.tblVendedores.setRowCount(len(vendedores))
        fila = 0
        for objVendedor in vendedores:
            # if len(objVendedor) >= 5:  
            self.ventana.tblVendedores.setItem(fila, 0, QTableWidgetItem(str(objVendedor[0])))
            self.ventana.tblVendedores.setItem(fila, 1, QTableWidgetItem(str(objVendedor[1])))
            self.ventana.tblVendedores.setItem(fila, 2, QTableWidgetItem(str(objVendedor[2])))
            self.ventana.tblVendedores.setItem(fila, 3, QTableWidgetItem(str(objVendedor[3])))
            self.ventana.tblVendedores.setItem(fila, 4, QTableWidgetItem(str(objVendedor[4])))
            fila +=1
