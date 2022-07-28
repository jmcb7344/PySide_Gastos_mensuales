from PySide6.QtWidgets import *
from views.formulario_gastos import Gastos_mes
from PySide6.QtSql import QSqlQuery
from PySide6.QtCore import Qt
import shutil


class Pagos_Mes(QWidget, Gastos_mes):
    #Ventana emergente que perminte agregar un nuevo ITEM
    def __init__(self, parent=None):
        super().__init__(parent, )
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        #Funcionalidad de los botones 
        self.btn_agregar.clicked.connect(self.agregar_pago)
        self.btn_salir.clicked.connect(self.salir)
        self.check_ingresos.toggled.connect(self.seleccion)
        self.check_Egresos.toggled.connect(self.seleccion)
        self.btn_PDF.clicked.connect(self.archivo_PDF)
        self.comboBox.currentTextChanged.connect(self.nuevo_concepto)

    def salir(self):
        #Cierra la ventana
        self.close()

    def agregar_pago(self):
        #Funcion para agregar un nuevo Item
        query = QSqlQuery()
        query.prepare("INSERT INTO gastos_mensuales(fecha, concepto, categoria, monto, tipo, nota, remito) VALUES (date('now'),?,?,?,?,?,?)")
        if self.comboBox.currentText() == 'Otro':
            query.bindValue(0, self.txt_concepto_nuevo.text())
        else:
            query.bindValue(0, self.comboBox.currentText())

        query.bindValue(1, self.comboBox_categoria.currentText())

        if  self.check_ingresos.isChecked():
            query.bindValue(3, self.check_ingresos.text())
            query.bindValue(2, abs(int(self.txt_monto.text())))
        else:
            query.bindValue(3, self.check_Egresos.text())
            query.bindValue(2, abs(int(self.txt_monto.text()))*-1)

        if self.txt_remito_PDF.text() == '':
            nueva_direccion = ''
        else:
            pdf = self.txt_remito_PDF.text()
            nueva_direccion = shutil.copy(pdf, 'db_Gastos')
        query.bindValue(4, self.txt_nota.text())
        query.bindValue(5, nueva_direccion)
        query.exec()
        self.close()

    def seleccion(self, estado):
        if self.check_ingresos.isChecked():
            concepto_ingreso = ['Salario', 'Fondo de inversion', 'Plazo Fijo', 'Otro']
            categoria_ingreso = ['Ingreso']
            self.comboBox.clear()
            self.comboBox.addItems(concepto_ingreso)
            self.comboBox_categoria.clear()
            self.comboBox_categoria.addItems(categoria_ingreso)

        else:
            concepto_egreso = ['Agua', 'Aseo personal', 'Combustible', 'Comidas / Cenas / Merienda', 'Compra dolares', 'Cuota Vehiculo', 'Cursos', 'Diversion', 'Electricidad', 'Estacionamiento', 'Expensas / Condominio', 'Gas', 'Gastos educativos', 'GYM', 'Impuesto patente/Vehiculo', 'Internet Wifi', 'Limpieza', 'Lujos', 'Mantenimineto Vehiculo', 'Mercado', 'Osio', 'Prestamo', 'Seguro Vehicular', 'Telefonia movil/Fija', 'Tv calbe/satelital','Alquiler / Hipoteca','Educacion','Gastos medicos','Reparaciones domicilio','Ropa','Tarjeta de credito','Otro']
            concepto_egreso.sort()
            categoria_egreso = ['Domestico', 'Vacaciones', 'Esparcimiento', 'Lujos', 'Limpieza', 'Educacion', 'Bancario', 'Impuesto', 'Transporte', 'Osio', 'Otro']
            self.comboBox.clear()
            self.comboBox.addItems(concepto_egreso)
            self.comboBox_categoria.clear()
            self.comboBox_categoria.addItems(categoria_egreso)

    def archivo_PDF(self):
        pdf, _ = QFileDialog.getOpenFileName(self, 'Abrir archivo', '.')
        self.txt_remito_PDF.setText(pdf)
        
    def nuevo_concepto(self):
        if self.comboBox.currentText() == 'Otro':
            self.txt_concepto_nuevo.setEnabled(True)