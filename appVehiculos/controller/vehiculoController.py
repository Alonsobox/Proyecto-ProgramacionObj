from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import QDate
from repository.vehiculoRepository import VehiculoRepository
from repository.combustionRepository import SeleccionCombustion
from repository.seleccionMarca import SeleccionMarca
from repository.seleccionModelo import SeleccionModelo
from model.vehiculo import Vehiculo

class VehiculoController:
    def __init__(self):
        self.ventana = uic.loadUi("view/fmvehiculo.ui")
        self.vehiculoRepository = VehiculoRepository()
        self.seleccionCombustion= SeleccionCombustion()
        self.seleccionMarca = SeleccionMarca()
        self.seleccionarModelo = SeleccionModelo()
        self.listarVehiculo()
        self.listarSeleccionCombustion()
        self.listarSeleccionMarca()
        self.listarSeleccionModelo()
        self.ventana.tblVehiculo.cellClicked.connect(self.tblVehiculocellclicked)
        self.ventana.btnguardar.clicked.connect(self.btnguardarclick)
        self.ventana.btnEliminar.clicked.connect(self.btnEliminarClick)
        self.ventana.btnlimpiar.clicked.connect(self.btnlimpiarclick)

    def btnlimpiarclick(self):
        self.ventana.txtCodigo.setText("")
        self.ventana.txtCodigo.setEnabled(True)
        self.ventana.txtColor.setText("")
        self.ventana.txtAno.setText("")
        self.ventana.cboCombustion.setCurrentIndex(-1)       
        self.ventana.cboMarca.setCurrentIndex(-1)       ##limpia el CBX seleccionando un indice no valido
        self.ventana.cboModelo.setCurrentIndex(-1)       

    def tblVehiculocellclicked(self, fila):
        idvehiculo = self.ventana.tblVehiculo.item(fila, 0).text().strip()
        self.ventana.txtCodigo.setText(idvehiculo)
        objVehiculo = self.vehiculoRepository.obtenerVehiculo(idvehiculo)
        
        if objVehiculo:
            self.ventana.txtColor.setText(objVehiculo[1])
            self.ventana.txtAno.setText(str(objVehiculo[2]))
            self.ventana.cboCombustion.setCurrentText(objVehiculo[3])
            self.ventana.cboMarca.setCurrentText(objVehiculo[4])
            self.ventana.cboModelo.setCurrentText(objVehiculo[5])

    def btnguardarclick(self):
        codVeh = self.ventana.txtCodigo.text()
        colorVeh = self.ventana.txtColor.text()
        añoVeh = self.ventana.txtAno.text()
        codCombus = self.ventana.cboCombustion.currentData()
        codMar = self.ventana.cboMarca.currentData()
        codMod = self.ventana.cboModelo.currentData()
        objVehiculo = Vehiculo(codVeh,colorVeh,añoVeh,codCombus,codMar,codMod)

        if self.vehiculoRepository.obtenerVehiculo(objVehiculo.codVeh) is None:## busca el vendedor por codigo, sino lo encuentra inserta
            self.vehiculoRepository.insertarVehiculo(objVehiculo)               
        else:                                                           ##el vendedor Existe en la BD, entonces actualiza
            self.vehiculoRepository.actualizarVehiculo(objVehiculo)             
        self.listarVehiculo()
        self.btnlimpiarclick()


    
  
            
    def listarVehiculo(self):
        vehiculos = self.vehiculoRepository.listarVehiculo()
        self.ventana.tblVehiculo.setRowCount(len(vehiculos))
        fila = 0
        for objVehiculo in vehiculos:
            # if len(objVendedor) >= 5:  
            self.ventana.tblVehiculo.setItem(fila, 0, QTableWidgetItem(str(objVehiculo[0])))
            self.ventana.tblVehiculo.setItem(fila, 1, QTableWidgetItem(str(objVehiculo[1])))
            self.ventana.tblVehiculo.setItem(fila, 2, QTableWidgetItem(str(objVehiculo[2])))
            self.ventana.tblVehiculo.setItem(fila, 3, QTableWidgetItem(str(objVehiculo[3])))
            self.ventana.tblVehiculo.setItem(fila, 4, QTableWidgetItem(str(objVehiculo[4])))
            self.ventana.tblVehiculo.setItem(fila, 5, QTableWidgetItem(str(objVehiculo[5])))
            fila +=1

    def listarSeleccionCombustion(self):
        combustion = self.seleccionCombustion.listarSeleccionCombustion()
        for combu in combustion:
            self.ventana.cboCombustion.addItem(combu[1],combu[0])

        # combustion = ["GLP", "Electrico", "Gasolida"] 
        # self.ventana.cboCombustion.addItems(combustion)

    def listarSeleccionMarca(self):
        selecciones = self.seleccionMarca.listarSeleccionMarca()
        for seleccion in selecciones:
            self.ventana.cboMarca.addItem(seleccion[1],seleccion[0])

    def listarSeleccionModelo(self):
        modelos = self.seleccionarModelo.listarSeleccionModelo()
        for modelo in modelos:
            self.ventana.cboModelo.addItem(modelo[1],modelo[0])


    def btnEliminarClick(self):
        codVeh = self.ventana.txtCodigo.text().strip()
        self.vehiculoRepository.eliminarVehiculo(codVeh)
        self.listarVehiculo()
        self.btnlimpiarclick()
