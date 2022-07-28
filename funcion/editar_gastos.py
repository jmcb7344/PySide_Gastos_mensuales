from PySide6.QtWidgets import *
from views.formulario_gastos import Gastos_mes
from PySide6.QtSql import QSqlQuery
from PySide6.QtCore import Qt
import os, shutil


class Pagos_Mes(QWidget, Gastos_mes):
    
    def __init__(self, parent=None, id=None):
        self._id = id
        self.paths = ''
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        #Funcionalidad de los botones 
        self.btn_agregar.clicked.connect(self.editar_pago)
        self.btn_salir.clicked.connect(self.salir)
        self.check_ingresos.toggled.connect(self.seleccion)
        self.check_Egresos.toggled.connect(self.seleccion)
        self.btn_PDF.clicked.connect(self.archivo_PDF)

        self.datos()

    def salir(self):
        self.close()

    def editar_pago(self):
        query = QSqlQuery()
        query.prepare("UPDATE gastos_mensuales SET fecha=date('now'), concepto=?, categoria=?, monto=?, nota=?, remito=?, tipo=? WHERE id=?")
        query.bindValue(0, self.comboBox.currentText())
        query.bindValue(1, self.comboBox_categoria.currentText())
        query.bindValue(3, self.txt_nota.text())
        if self.check_ingresos.isChecked():
            query.bindValue(5, self.check_ingresos.text())
            query.bindValue(2, abs(int(self.txt_monto.text())))
        else:
            query.bindValue(5, self.check_Egresos.text())
            query.bindValue(2, abs(int(self.txt_monto.text()))*-1)

        if self.paths == '' and self.txt_remito_PDF.text() == '':
            nueva_direccion = ''
        elif self.paths == '':
            pdf = self.txt_remito_PDF.text()
            nueva_direccion = shutil.copy(pdf, 'db_Gastos')
        elif self.txt_remito_PDF.text() == '':
            os.remove(self.paths)
            nueva_direccion = ''
        else:
            os.remove(self.paths)
            pdf = self.txt_remito_PDF.text()
            nueva_direccion = shutil.copy(pdf, 'db_Gastos')

        query.bindValue(4, nueva_direccion) 
        query.bindValue(6, self._id)
        query.exec()
        self.close()

    def seleccion(self, estado):
        
        if self.check_ingresos.isChecked():
            print(f'{estado} Ingreso')
            concepto_ingreso = ['Salario', 'Fondo de inversion', 'Plazo Fijo', 'Otro']
            categoria_ingreso = ['Ingreso']

            self.comboBox.clear()
            self.comboBox.addItems(concepto_ingreso)
            self.comboBox_categoria.clear()
            self.comboBox_categoria.addItems(categoria_ingreso)
        else:
            print(f'{estado} Egreso')
            concepto_egreso = ['Agua', 'Aseo personal', 'Combustible', 'Comidas / Cenas / Merienda', 'Compra dolares', 'Cuota Vehiculo', 'Cursos', 'Diversion', 'Electricidad', 'Estacionamiento', 'Expensas / Condominio', 'Gas', 'Gastos educativos', 'GYM', 'Impuesto patente/Vehiculo', 'Internet Wifi', 'Limpieza', 'Lujos', 'Mantenimineto Vehiculo', 'Mercado', 'Osio', 'Prestamo', 'Seguro Vehicular', 'Telefonia movil/Fija', 'Tv calbe/satelital','Alquiler / Hipoteca','Educacion','Gastos medicos','Otro','Reparaciones domicilio','Ropa','Tarjeta de credito']
            categoria_egreso = ['Domestico', 'Vacaciones', 'Esparcimiento', 'Lujos', 'Limpieza', 'Educacion', 'Bancario', 'Impuesto', 'Transporte', 'Osio', 'Otro']
            self.comboBox.clear()
            self.comboBox.addItems(concepto_egreso)
            self.comboBox_categoria.clear()
            self.comboBox_categoria.addItems(categoria_egreso)

    def datos(self):
        query = QSqlQuery()
        query.prepare('SELECT * FROM gastos_mensuales WHERE id=?')
        query.bindValue(0, self._id)
        query.exec()
        query.first()
        if query.value(7) == 'Ingreso':
            self.check_ingresos.setChecked(True)
        else:
            self.check_Egresos.setChecked(True)
        item = query.value(2)
        self.comboBox.setCurrentText(item)
        self.comboBox_categoria.setCurrentText(query.value(3))
        self.txt_monto.setText(str(query.value(4)))
        self.txt_nota.setText(query.value(5))
        self.paths = query.value(6)
        self.txt_remito_PDF.setText(query.value(6))

    def archivo_PDF(self):
        pdf, _ = QFileDialog.getOpenFileName(self, 'Abrir archivo', '.')
        self.txt_remito_PDF.setText(pdf)
        