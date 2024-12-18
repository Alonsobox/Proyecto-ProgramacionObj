from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from repository.clienteRepository import ClienteRepository
from model.cliente import Cliente

class ClienteControler:

    def __init__(self):
        self.ventana = uic.loadUi("view/fmcliente.ui")
        self.clienteRepository=ClienteRepository()
        self.listarCliente()
        self.ventana.tblClientes.cellClicked.connect(self.tblClientescellclicked)
        self.ventana.btnguardar.clicked.connect(self.btnguardarclick)
        self.ventana.btnlimpiar.clicked.connect(self.btnlimpiarclick)

    def btnlimpiarclick(self):
        self.ventana.txtCodigo.setText("")
        self.ventana.txtCodigo.setEnabled(True)
        self.ventana.txtNombre.setText("")
        self.ventana.txtApellido.setText("")
        self.ventana.txtTrabajo.setText("")
        self.ventana.txtTelefono.setText("")
        self.ventana.txtDireccion.setText("")

    def tblClientescellclicked(self, fila):
        idCliente = self.ventana.tblClientes.item(fila, 0).text().strip()
        self.ventana.txtCodigo.setText(idCliente)
        objCliente = self.clienteRepository.obtenerCliente(idCliente)
        
        if objCliente:
            self.ventana.txtNombre.setText(objCliente[1])
            self.ventana.txtApellido.setText(objCliente[2])
            self.ventana.txtTrabajo.setText(objCliente[3])
            self.ventana.txtTelefono.setText(str(objCliente[4]))  
            self.ventana.txtDireccion.setText(objCliente[5])
            

    def btnguardarclick(self):
        codPer = self.ventana.txtCodigo.text()
        nombrePer = self.ventana.txtNombre.text()
        apelliPer = self.ventana.txtApellido.text()
        trabaCli = self.ventana.txtTrabajo.text()
        telfCli = self.ventana.txtTelefono.text()
        direcCli = self.ventana.txtDireccion.text()
        objCliente= Cliente(codPer,nombrePer,apelliPer,trabaCli,telfCli,direcCli)
        
        if self.clienteRepository.obtenerCliente(objCliente.codPer) is None:## busca el vendedor por codigo, sino lo encuentra inserta
            self.clienteRepository.insertarCliente(objCliente)               
        else:                                                           ##el vendedor Existe en la BD, entonces actualiza
            self.clienteRepository.actualizarCliente(objCliente)             
        self.listarCliente()


    
  
            
    def listarCliente(self):
        clientes = self.clienteRepository.listarCliente()
        self.ventana.tblClientes.setRowCount(len(clientes))
        fila = 0
        for objCliente in clientes:
            
            self.ventana.tblClientes.setItem(fila, 0, QTableWidgetItem(str(objCliente[0])))
            self.ventana.tblClientes.setItem(fila, 1, QTableWidgetItem(str(objCliente[1])))
            self.ventana.tblClientes.setItem(fila, 2, QTableWidgetItem(str(objCliente[2])))
            self.ventana.tblClientes.setItem(fila, 3, QTableWidgetItem(str(objCliente[3])))
            self.ventana.tblClientes.setItem(fila, 4, QTableWidgetItem(str(objCliente[4])))
            self.ventana.tblClientes.setItem(fila, 5, QTableWidgetItem(str(objCliente[5])))
            fila += 1
