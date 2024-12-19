from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
from repository.facturaRepository import FacturaRespository
from repository.selecionarCliente import SeleccionarCliente
from repository.seleccionarVendedor import SeleccionarVendedor
from repository.seleccionarVehiculo import SeleccionarVehiculo
from repository.seleccionarConcesionaria import SeleccionarConcesionaria
from model.factura import Factura

class FacturaController:
    def __init__(self):
        self.ventana = uic.loadUi("view/factura.ui")
        self.facturaRepositort = FacturaRespository()
        self.seleccionarClienteRepository = SeleccionarCliente()
        self.selecionarVendedorRepository = SeleccionarVendedor()
        self.selecionarVehiculoRepository = SeleccionarVehiculo()
        self.seleccionarConcesionariaRepository= SeleccionarConcesionaria()
        self.listarFactura()
        self.listarSeleccionCliente()
        self.listarSeleccionVendedor()
        self.listarSeleccionVehiculo()
        self.listarSeleccionConcesionaria()
        self.ventana.tblFactura.cellClicked.connect(self.tblFacturacellclicked)
        self.ventana.btnguardar.clicked.connect(self.btnguardarclick)
        self.ventana.btnlimpiar.clicked.connect(self.btnlimpiarclick)

    def btnlimpiarclick(self):
        self.ventana.txtCodigo.setText("")
        self.ventana.txtCodigo.setEnabled(True)
        self.ventana.txtFecha.setText("")
        self.ventana.txtImporte.setText("")
        self.ventana.cboCliente.setCurrentIndex(-1)       
        self.ventana.cboVendedor.setCurrentIndex(-1)       
        self.ventana.cboVehiculo.setCurrentIndex(-1)       
        self.ventana.cboConcesionaria.setCurrentIndex(-1)       

    def tblFacturacellclicked(self, fila):
        idFactura = self.ventana.tblFactura.item(fila, 0).text().strip()
        self.ventana.txtCodigo.setText(idFactura)
        objFactura = self.facturaRepositort.obtenerFactura(idFactura)
        
        if objFactura:
            self.ventana.txtFecha.setText(str(objFactura[1]))
            self.ventana.txtImporte.setText(str(objFactura[2]))
            self.ventana.cboCliente.setCurrentText(objFactura[3])
            self.ventana.cboVendedor.setCurrentText(objFactura[4])
            self.ventana.cboVehiculo.setCurrentText(str(objFactura[5]))
            self.ventana.cboConcesionaria.setCurrentText(objFactura[6])


    def btnguardarclick(self):
        codFac = self.ventana.txtCodigo.text().strip()
        fechaFac = self.ventana.txtFecha.text().strip()
        importeFac = self.ventana.txtImporte.text().strip()
        codCli = self.ventana.cboCliente.currentData()
        codVen = self.ventana.cboVendedor.currentData()
        codVeh = self.ventana.cboVehiculo.currentData()
        codCon = self.ventana.cboConcesionaria.currentData()

        # Imprimir valores para depuración
        print(f"codFac: {codFac}, fechaFac: {fechaFac}, importeFac: {importeFac}, codCli: {codCli}, codVen: {codVen}, codVeh: {codVeh}, codCon: {codCon}")

        # Verificar que el código de la factura no esté vacío
        if not codFac:
            QtWidgets.QMessageBox.critical(self.ventana, "Error", "El código de la factura es obligatorio.")
            return

        # Verificar que importeFac sea un número válido
        try:
            importeFac = float(importeFac)
        except ValueError:
            QtWidgets.QMessageBox.critical(self.ventana, "Error", "El importe debe ser un número.")
            return

        # Obtener los valores actuales de la factura, si existen
        factura_actual = self.facturaRepositort.obtenerFactura(codFac)

        if factura_actual is None:     ##is none para verificar si la variable tiene el valor None
            # Para nuevas facturas, verificar que todos los campos estén presentes
            if not all([fechaFac, importeFac, codCli, codVen, codVeh, codCon]):## utilizamos not invertir la expresion booleana
                QtWidgets.QMessageBox.critical(self.ventana, "Error", "Todos los campos son obligatorios para nuevas facturas.")
                return
            # Crear un objeto de factura con los valores proporcionados
            objFactura = Factura(codFac, fechaFac, importeFac, codCli, codVen, codVeh, codCon)
            self.facturaRepositort.insertarFactura(objFactura)
        else:
            # Para facturas existentes, usar los valores actuales si los nuevos están vacíos
            fechaFac = fechaFac or factura_actual[1]
            importeFac = importeFac or factura_actual[2]
            codCli = codCli or factura_actual[3]
            codVen = codVen or factura_actual[4]
            codVeh = codVeh or factura_actual[5]
            codCon = codCon or factura_actual[6]
            # Crear un objeto de factura con los valores actuales y nuevos
            objFactura = Factura(codFac, fechaFac, importeFac, codCli, codVen, codVeh, codCon)
            self.facturaRepositort.actualizarFactura(objFactura)
        
        self.listarFactura()
        self.btnlimpiarclick()


    
  
            
    def listarFactura(self):
        factura = self.facturaRepositort.listarFactura()
        self.ventana.tblFactura.setRowCount(len(factura))
        fila = 0
        for objFactura in factura:
            self.ventana.tblFactura.setItem(fila, 0, QTableWidgetItem(str(objFactura[0])))
            self.ventana.tblFactura.setItem(fila, 1, QTableWidgetItem(str(objFactura[1])))
            self.ventana.tblFactura.setItem(fila, 2, QTableWidgetItem(str(objFactura[2])))
            self.ventana.tblFactura.setItem(fila, 3, QTableWidgetItem(str(objFactura[3])))
            self.ventana.tblFactura.setItem(fila, 4, QTableWidgetItem(str(objFactura[4])))
            self.ventana.tblFactura.setItem(fila, 5, QTableWidgetItem(str(objFactura[5])))
            self.ventana.tblFactura.setItem(fila, 6, QTableWidgetItem(str(objFactura[6])))
            fila +=1

    def listarSeleccionCliente(self):
        clientes = self.seleccionarClienteRepository.listarSeleccionCliente()
        for cliente in clientes:
            self.ventana.cboCliente.addItem(cliente[1],cliente[0])


    def listarSeleccionVendedor(self):
        vendedores = self.selecionarVendedorRepository.listarSeleccionVendedor()
        for vendedor in vendedores:
            self.ventana.cboVendedor.addItem(vendedor[1],vendedor[0])

    def listarSeleccionVehiculo(self):
        vehiculos = self.selecionarVehiculoRepository.listarSeleccionVehiculo()
        for vehiculo in vehiculos:
            self.ventana.cboVehiculo.addItem(vehiculo[1], vehiculo[0])
            # self.ventana.cboVehiculo.addItem(str(vehiculo[0]))

    def listarSeleccionConcesionaria(self):
        concesionarias = self.seleccionarConcesionariaRepository.listarSeleccionConcesionaria()
        for concesio in concesionarias:
            self.ventana.cboConcesionaria.addItem(concesio[1],concesio[0])
