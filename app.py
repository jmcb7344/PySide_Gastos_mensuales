import os, sys
from datetime import date
from views.pantalla_Inicial import Pantalla_inicial
from db_Gastos.db_Conexion import Conexion
from funcion.chart_gastos import Indicadores
from PySide6.QtWidgets import *
from PySide6.QtSql import QSqlQuery


class Gastos(QWidget, Pantalla_inicial):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        #Conexion a la Base de Datos, Creara una si no existe
        Conexion.check()

        #Comando de los botones
        self.box_Meses.currentIndexChanged.connect(self.mostar_pago_mes)
        self.btn_Nuevo_Pago.clicked.connect(self.agregar)
        self.btn_Editar_Pago.clicked.connect(self.editar)
        self.btn_Eliminar.clicked.connect(self.eliminar)
        self.btn_actualizar.clicked.connect(self.mostar_pago_mes)
        self.tabla_Ventana2.itemDoubleClicked.connect(self.ver_PDF)

        #Llamada a algunas funciones iniciales
        self.mostar_pago_mes()
        self.indicador()


    def agregar(self):
        #Abre una nueva pantalla para agregar gasto
        from funcion.nuevo_Gasto_mes import Pagos_Mes
        window = Pagos_Mes(self)
        window.show()

    def editar(self):
        #Abre una pantalla nueva para modificar un gasto
        from funcion.editar_gastos import Pagos_Mes
        select_row = self.tabla_Ventana2.selectedItems()

        if select_row:
            _id = int(select_row[0].text())
            window = Pagos_Mes(self, _id)
            window.show()
        else:
            print('Selecciones un Item')

    def eliminar(self):
        #Elimina el gasto seleccionado
        select_row = self.tabla_Ventana2.selectedItems()
        if select_row:
            _id = int(select_row[0].text())
            query = QSqlQuery()
            query.prepare('DELETE FROM gastos_mensuales WHERE id=?')
            query.bindValue(0, _id)
            query.exec()
        self.mostar_pago_mes()

    def mostar_pago_mes(self):
        #Carga automaticamente los gastos del mes en curso O del mes que se selccione
        if self.box_Meses.currentIndex() == 00:
            self.box_Meses.setCurrentIndex(date.today().month)
            mes = str(self.box_Meses.currentIndex()).rjust(2, '0')
        else:
            mes = str(self.box_Meses.currentIndex()).rjust(2, '0')

        index = 0 
        _seleccionar = QSqlQuery()
        _seleccionar.prepare("SELECT * FROM gastos_mensuales WHERE strftime('%m',fecha) = ?")
        _seleccionar.bindValue(0, mes)
        _seleccionar.exec()
        
        while _seleccionar.next():
            id = _seleccionar.value(0)
            fecha = _seleccionar.value(1)
            concepto = _seleccionar.value(2)
            categoria = _seleccionar.value(3)
            monto = _seleccionar.value(4)
            nota = _seleccionar.value(5)
            remito = _seleccionar.value(6)

            self.tabla_Ventana2.setRowCount(index + 1)
            self.tabla_Ventana2.setItem(index, 0, QTableWidgetItem(str(id)))
            self.tabla_Ventana2.setItem(index, 1, QTableWidgetItem(fecha))
            self.tabla_Ventana2.setItem(index, 2, QTableWidgetItem(concepto))
            self.tabla_Ventana2.setItem(index, 3, QTableWidgetItem(categoria))
            self.tabla_Ventana2.setItem(index, 4, QTableWidgetItem(str(monto)))
            self.tabla_Ventana2.setItem(index, 5, QTableWidgetItem(nota))
            self.tabla_Ventana2.setItem(index, 6, QTableWidgetItem(remito))

            index += 1

        self.total()

    def total(self):
        #Muestra el total de gastos, ingresos y el restante de los mismos
        _monto_egresos = QSqlQuery()
        _monto_egresos.prepare("SELECT sum(monto) FROM gastos_mensuales WHERE tipo='Egreso' AND strftime('%m',fecha)=?")
        _monto_egresos.bindValue(0, str(self.box_Meses.currentIndex()).rjust(2, '0'))
        _monto_egresos.exec()
        _monto_ingresos = QSqlQuery()
        _monto_ingresos.prepare("SELECT sum(monto) FROM gastos_mensuales WHERE tipo='Ingreso' AND strftime('%m',fecha)=?")
        _monto_ingresos.bindValue(0, str(self.box_Meses.currentIndex()).rjust(2, '0'))
        _monto_ingresos.exec()
        _monto_egresos.first()
        _monto_ingresos.first()
        ingreso = _monto_ingresos.value(0)
        egreso = _monto_egresos.value(0)
        if _monto_ingresos.value(0) == '':
            ingreso = 0
        if _monto_egresos.value(0) == '':
            egreso = 0
        total = ingreso - abs(egreso)
        self.label_Gastos_Edit.setText(str(egreso))
        self.label_Ingresos_Edit.setText(str(ingreso))
        self.label_Total_Edit.setText(str(total))


    def ver_PDF(self):
        #Abrira el pdf automaticamente
        select_row = self.tabla_Ventana2.selectedItems()
        if select_row:
            _id = select_row[6].text()
        if id == '':
            dialogo = QMessageBox.information(self, "Informacion", "No posee PDF para Motrar")
        else:
            os.startfile(_id)
        
    def indicador(self):
        #Genera las graficas de todos los meses
        self.layout_Gastos.addWidget(Indicadores.indicador_egreso(self))
        self.layout_Ahorro.addWidget(Indicadores.indicador_ahorro(self))



if __name__ == "__main__":
    app = QApplication([])
    widget = Gastos()
    widget.show()
    sys.exit(app.exec())
