from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from repository.proveedorRepository import ProveedorRepository
from model.proveedor import Proveedor

class ProveedorController:

    def __init__(self):
        self.ventana = uic.loadUi("view/fmproveedor.ui")
        self.provedorrepository = ProveedorRepository()
        self.listarProveedor()
        self.ventana.tblProveedor.cellClicked.connect(self.tblProveedorclicked)
        self.ventana.btnguardar.clicked.connect(self.btnguardarclick)
        self.ventana.btnEliminar.clicked.connect(self.btnEliminarClick)
        self.ventana.btnlimpiar.clicked.connect(self.btnlimpiarclick)

    def btnlimpiarclick(self):
        self.ventana.txtCodigo.setText("")
        self.ventana.txtCodigo.setEnabled(True)
        self.ventana.txtNombre.setText("")
        self.ventana.txtTelefono.setText("")
        self.ventana.txtStock.setText("")
        self.ventana.txtDireccion.setText("")

    def tblProveedorclicked(self, fila):
        idProveedor = self.ventana.tblProveedor.item(fila, 0).text().strip()
        self.ventana.txtCodigo.setText(idProveedor)
        objProveedor = self.provedorrepository.obtenerProveedor(idProveedor)
        
        if objProveedor:
            self.ventana.txtNombre.setText(objProveedor[1])
            self.ventana.txtTelefono.setText(str(objProveedor[2]))
            self.ventana.txtStock.setText(str(objProveedor[3]))
            self.ventana.txtDireccion.setText((objProveedor[4]))  
            

    def btnguardarclick(self):
        codPro = self.ventana.txtCodigo.text()
        nombrePro = self.ventana.txtNombre.text()
        telfPro = self.ventana.txtTelefono.text()
        stockPro = self.ventana.txtStock.text()
        direcPro = self.ventana.txtDireccion.text()
        objVendedor= Proveedor(codPro,nombrePro,telfPro,stockPro,direcPro)
        
        if self.provedorrepository.obtenerProveedor(objVendedor.codPro) is None:## busca el vendedor por codigo, sino lo encuentra inserta
            self.provedorrepository.insertarProveedor(objVendedor)               
        else:                                                           ##el vendedor Existe en la BD, entonces actualiza
            self.provedorrepository.actualizarProveedor(objVendedor)             
        self.listarProveedor()
        self.btnlimpiarclick()


    
  
            
    def listarProveedor(self):
        provedor = self.provedorrepository.listarProveedor()
        self.ventana.tblProveedor.setRowCount(len(provedor))
        fila = 0
        for objProveedor in provedor:
            # if len(objVendedor) >= 5:  # Verifica que hay al menos 5 elementos
            self.ventana.tblProveedor.setItem(fila, 0, QTableWidgetItem(str(objProveedor[0])))
            self.ventana.tblProveedor.setItem(fila, 1, QTableWidgetItem(str(objProveedor[1])))
            self.ventana.tblProveedor.setItem(fila, 2, QTableWidgetItem(str(objProveedor[2])))
            self.ventana.tblProveedor.setItem(fila, 3, QTableWidgetItem(str(objProveedor[3])))
            self.ventana.tblProveedor.setItem(fila, 4, QTableWidgetItem(str(objProveedor[4])))
                # Si la columna 6 no existe, omite esta línea
            # else:
            #     print(f"Error: objVendedor no tiene suficientes elementos: {objVendedor}")
            fila += 1
    

    def btnEliminarClick(self):
        codCon = self.ventana.txtCodigo.text().strip()
        self.provedorrepository.eliminarProveedor(codCon)
        self.listarProveedor()
        self.btnlimpiarclick()
