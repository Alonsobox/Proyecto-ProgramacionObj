from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from repository.vendedorRepository import VendedorRepository
from model.vendedor import Vendedor

class VendedorController:

    def __init__(self):
        self.ventana = uic.loadUi("view/fmvendedor.ui")
        self.vendedorrepository = VendedorRepository()
        self.listarVendedor()
        self.ventana.tblVendedores.cellClicked.connect(self.tblvendedorescellclicked)
        self.ventana.btnguardar.clicked.connect(self.btnguardarclick)
        self.ventana.btnEliminar.clicked.connect(self.btnEliminarClick)
        self.ventana.btnlimpiar.clicked.connect(self.btnlimpiarclick)


    def btnlimpiarclick(self):
        self.ventana.txtCodigo.setText("")
        self.ventana.txtCodigo.setEnabled(True)
        self.ventana.txtNombre.setText("")
        self.ventana.txtApellido.setText("")
        self.ventana.txtSueldo.setText("")
        self.ventana.txtCantVentas.setText("")

    def tblvendedorescellclicked(self, fila):
        idvendedor = self.ventana.tblVendedores.item(fila, 0).text().strip()
        self.ventana.txtCodigo.setText(idvendedor)
        objVendedor = self.vendedorrepository.obtenerVendedor(idvendedor)
        
        if objVendedor:
            self.ventana.txtNombre.setText(objVendedor[1])
            self.ventana.txtApellido.setText(objVendedor[2])
            self.ventana.txtSueldo.setText(str(objVendedor[3]))  
            self.ventana.txtCantVentas.setText(str(objVendedor[4]))  
            

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
        self.btnlimpiarclick()


    
  
            
    def listarVendedor(self):
        vendedores = self.vendedorrepository.listarVendedor()
        self.ventana.tblVendedores.setRowCount(len(vendedores))
        fila = 0
        for objVendedor in vendedores:
            # if len(objVendedor) >= 5:  # Verifica que hay al menos 5 elementos
            self.ventana.tblVendedores.setItem(fila, 0, QTableWidgetItem(str(objVendedor[0])))
            self.ventana.tblVendedores.setItem(fila, 1, QTableWidgetItem(str(objVendedor[1])))
            self.ventana.tblVendedores.setItem(fila, 2, QTableWidgetItem(str(objVendedor[2])))
            self.ventana.tblVendedores.setItem(fila, 3, QTableWidgetItem(str(objVendedor[3])))
            self.ventana.tblVendedores.setItem(fila, 4, QTableWidgetItem(str(objVendedor[4])))
                # Si la columna 6 no existe, omite esta línea
            # else:
            #     print(f"Error: objVendedor no tiene suficientes elementos: {objVendedor}")
            fila += 1

    def btnEliminarClick(self):
        codPer = self.ventana.txtCodigo.text().strip()
        self.vendedorrepository.eliminarVendedor(codPer)
        self.listarVendedor()
        self.btnlimpiarclick()



