from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from repository.marcaRepository import MarcaRepository
from model.marca import Marca

class MarcaController:

    def __init__(self):
        self.ventana = uic.loadUi("view/fmmarca.ui")
        self.marcarepository = MarcaRepository()
        self.listarMarca()
        self.ventana.tblMarca.cellClicked.connect(self.tblMarcaclicked)
        self.ventana.btnguardar.clicked.connect(self.btnguardarclick)
        self.ventana.btnEliminar.clicked.connect(self.btnEliminarclick)
        self.ventana.btnlimpiar.clicked.connect(self.btnlimpiarclick)

    def btnlimpiarclick(self):
        self.ventana.txtCodigo.setText("")
        self.ventana.txtCodigo.setEnabled(True)
        self.ventana.txtNombre.setText("")
        self.ventana.txtStock.setText("")

    def tblMarcaclicked(self, fila):
        idMarca = self.ventana.tblMarca.item(fila, 0).text().strip()
        self.ventana.txtCodigo.setText(idMarca)
        objProveedor = self.marcarepository.obtenerMarca(idMarca)
        
        if objProveedor:
            self.ventana.txtNombre.setText(objProveedor[1])
            self.ventana.txtStock.setText(str(objProveedor[2]))
            

    def btnguardarclick(self):
        codMar = self.ventana.txtCodigo.text()
        nombreMar = self.ventana.txtNombre.text()
        stockMar = self.ventana.txtStock.text()
        objMarca= Marca(codMar,nombreMar,stockMar)
        
        if self.marcarepository.obtenerMarca(objMarca.codMar) is None:## busca el vendedor por codigo, sino lo encuentra inserta
            self.marcarepository.insertarMarca(objMarca)               
        else:                                                           ##el vendedor Existe en la BD, entonces actualiza
            self.marcarepository.actualizarMarca(objMarca)             
        self.listarMarca()
        self.btnlimpiarclick()

    def btnEliminarclick(self):
        codMar = self.ventana.txtCodigo.text().strip()
        if not codMar:
            QtWidgets.QMessageBox.critical(self.ventana, "Error", "El código de la Marca es obligatorio.")
            return

        self.marcarepository.eliminarMarca(codMar)
        self.listarMarca()
        self.btnlimpiarclick()
    
  
            
    def listarMarca(self):
        marca = self.marcarepository.listarMarca()
        self.ventana.tblMarca.setRowCount(len(marca))
        fila = 0
        for objMarca in marca:
            self.ventana.tblMarca.setItem(fila, 0, QTableWidgetItem(str(objMarca[0])))
            self.ventana.tblMarca.setItem(fila, 1, QTableWidgetItem(str(objMarca[1])))
            self.ventana.tblMarca.setItem(fila, 2, QTableWidgetItem(str(objMarca[2])))
            fila += 1
    
    
