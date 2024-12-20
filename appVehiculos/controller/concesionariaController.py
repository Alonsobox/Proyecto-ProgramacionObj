from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from repository.concesionariaRepository import ConcesionariaRepository
from repository.seleccionarProveedor import SeleccionarProveedor
from model.concesionaria import Concesionaria

class ConcesionariaoController:
    def __init__(self):
        self.ventana = uic.loadUi("view/fmconcesionaria.ui")
        self.repositoryConcesionaria = ConcesionariaRepository()
        self.repositorySeleccionProveedor = SeleccionarProveedor()
        self.listarConcesionaria()
        self.listarSeleccionProveedor()
        self.ventana.tblConcesionarias.cellClicked.connect(self.tblConcesionariasclicked)
        self.ventana.btnguardar.clicked.connect(self.btnguardarclick)
        self.ventana.btnEliminar.clicked.connect(self.btnEliminarClick)
        self.ventana.btnlimpiar.clicked.connect(self.btnlimpiarclick)

    def btnlimpiarclick(self):
        self.ventana.txtCodigo.setText("")
        self.ventana.txtCodigo.setEnabled(True)
        self.ventana.txtNombre.setText("")
        self.ventana.txtCanTrabaja.setText("")
        self.ventana.cboProveedor.setCurrentIndex(-1)      
        self.ventana.txtDireccion.setText("")

    def tblConcesionariasclicked(self, fila):
        idConcesionaria = self.ventana.tblConcesionarias.item(fila, 0).text().strip()
        self.ventana.txtCodigo.setText(idConcesionaria)
        objConcesionaria = self.repositoryConcesionaria.obtenerConcesionaria(idConcesionaria)
        
        if objConcesionaria:
            self.ventana.txtNombre.setText(objConcesionaria[1])
            self.ventana.txtCanTrabaja.setText(str(objConcesionaria[2]))
            self.ventana.cboProveedor.setCurrentText(objConcesionaria[3])
            self.ventana.txtDireccion.setText(objConcesionaria[4])

    def btnguardarclick(self):
        codCon = self.ventana.txtCodigo.text()
        nombreCon = self.ventana.txtNombre.text()
        canTrabCon = self.ventana.txtCanTrabaja.text()
        codPro = self.ventana.cboProveedor.currentData()
        direcCon = self.ventana.txtDireccion.text()
        objConcesionaria = Concesionaria(codCon,nombreCon,canTrabCon,codPro,direcCon)

        if self.repositoryConcesionaria.obtenerConcesionaria(objConcesionaria.codCon) is None:## busca el vendedor por codigo, sino lo encuentra inserta
            self.repositoryConcesionaria.insertarConcesionaria(objConcesionaria)               
        else:                                                           ##el vendedor Existe en la BD, entonces actualiza
            self.repositoryConcesionaria.actualizarConcesionaria(objConcesionaria)             
        self.listarConcesionaria()
        self.btnlimpiarclick()
    
    def btnEliminarClick(self):
        codCon = self.ventana.txtCodigo.text().strip()
        if not codCon:
            QtWidgets.QMessageBox.critical(self.ventana, "Error", "El código del modelo es obligatorio.")
            return

        self.repositoryConcesionaria.eliminarConcesionaria(codCon)
        self.listarConcesionaria()
        self.btnlimpiarclick()



    
  
            
    def listarConcesionaria(self):
        concesionaria = self.repositoryConcesionaria.listarConcesionaria()
        self.ventana.tblConcesionarias.setRowCount(len(concesionaria))
        fila = 0
        for objConcesionaria in concesionaria:
            self.ventana.tblConcesionarias.setItem(fila, 0, QTableWidgetItem(str(objConcesionaria[0])))
            self.ventana.tblConcesionarias.setItem(fila, 1, QTableWidgetItem(str(objConcesionaria[1])))
            self.ventana.tblConcesionarias.setItem(fila, 2, QTableWidgetItem(str(objConcesionaria[2])))
            self.ventana.tblConcesionarias.setItem(fila, 3, QTableWidgetItem(str(objConcesionaria[3])))
            self.ventana.tblConcesionarias.setItem(fila, 4, QTableWidgetItem(str(objConcesionaria[4])))
            fila +=1

    def listarSeleccionProveedor(self):
        proveedores = self.repositorySeleccionProveedor.listarSeleccionProveedor()
        for proveedor in proveedores:
            self.ventana.cboProveedor.addItem(proveedor[1],proveedor[0])
