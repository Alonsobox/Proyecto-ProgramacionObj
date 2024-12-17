from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from repository.modeloRepository import ModeloRepository
from model.modelo import Modelo

class ModeloController:

    def __init__(self):
        self.ventana = uic.loadUi("view/fmmodelo.ui")
        self.modelorepository = ModeloRepository()
        self.listarModelo()
        self.ventana.tblModelos.cellClicked.connect(self.tblModelosclicked)
        self.ventana.btnguardar.clicked.connect(self.btnguardarclick)
        self.ventana.btnlimpiar.clicked.connect(self.btnlimpiarclick)

    def btnlimpiarclick(self):
        self.ventana.txtCodigo.setText("")
        self.ventana.txtCodigo.setEnabled(True)
        self.ventana.txtDiseno.setText("")
        self.ventana.txtTecnologia.setText("")
        self.ventana.txtSeguridad.setText("")
        self.ventana.txtInterior.setText("")
        self.ventana.txtPrecio.setText("")

    def tblModelosclicked(self, fila):
        idModelo = self.ventana.tblModelos.item(fila, 0).text().strip()
        self.ventana.txtCodigo.setText(idModelo)
        objModelo = self.modelorepository.obtenerModelo(idModelo)
        
        if objModelo:
            self.ventana.txtDiseno.setText(objModelo[1])
            self.ventana.txtTecnologia.setText(objModelo[2])
            self.ventana.txtSeguridad.setText(objModelo[3])
            self.ventana.txtInterior.setText(objModelo[4])
            self.ventana.txtPrecio.setText(str(objModelo[5]))
            

    def btnguardarclick(self):
        codMod = self.ventana.txtCodigo.text()
        diseñoMod = self.ventana.txtDiseno.text()
        tecnologiaMod = self.ventana.txtTecnologia.text()
        seguridadMod = self.ventana.txtSeguridad.text()
        interiorMod = self.ventana.txtInterior.text()
        precio = self.ventana.txtPrecio.text()
        objModelo= Modelo(codMod,diseñoMod,tecnologiaMod,seguridadMod,interiorMod,precio)
        
        if self.modelorepository.obtenerModelo(objModelo.codMod) is None:## busca el vendedor por codigo, sino lo encuentra inserta
            self.modelorepository.insertarModelo(objModelo)               
        else:                                                           ##el vendedor Existe en la BD, entonces actualiza
            self.modelorepository.actualizarModelo(objModelo)             
        self.listarModelo()


    
  
            
    def listarModelo(self):
        model = self.modelorepository.listarModelo()
        self.ventana.tblModelos.setRowCount(len(model))
        fila = 0
        for objModelo in model:
            self.ventana.tblModelos.setItem(fila, 0, QTableWidgetItem(str(objModelo[0])))
            self.ventana.tblModelos.setItem(fila, 1, QTableWidgetItem(str(objModelo[1])))
            self.ventana.tblModelos.setItem(fila, 2, QTableWidgetItem(str(objModelo[2])))
            self.ventana.tblModelos.setItem(fila, 3, QTableWidgetItem(str(objModelo[3])))
            self.ventana.tblModelos.setItem(fila, 4, QTableWidgetItem(str(objModelo[4])))
            self.ventana.tblModelos.setItem(fila, 5, QTableWidgetItem(str(objModelo[5])))
            fila += 1