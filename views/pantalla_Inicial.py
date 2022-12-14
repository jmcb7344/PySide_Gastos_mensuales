from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Pantalla_inicial(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(901, 616)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 901, 615))
        self.ventana2 = QWidget()
        self.ventana2.setObjectName(u"ventana2")
        self.tabla_Ventana2 = QTableWidget(self.ventana2)
        if (self.tabla_Ventana2.columnCount() < 7):
            self.tabla_Ventana2.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_Ventana2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_Ventana2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_Ventana2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_Ventana2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_Ventana2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_Ventana2.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_Ventana2.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabla_Ventana2.setObjectName(u"tabla_Ventana2")
        self.tabla_Ventana2.setGeometry(QRect(10, 10, 641, 531))
        self.tabla_Ventana2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla_Ventana2.setAlternatingRowColors(True)
        self.tabla_Ventana2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla_Ventana2.setColumnCount(7)
        self.tabla_Ventana2.horizontalHeader().setVisible(True)
        self.tabla_Ventana2.horizontalHeader().setDefaultSectionSize(125)
        self.tabla_Ventana2.verticalHeader().setVisible(False)
        self.tabla_Ventana2.verticalHeader().setDefaultSectionSize(20)
        self.tabla_Ventana2.setColumnWidth(0, 10)
        self.tabla_Ventana2.setColumnWidth(1, 85)
        self.tabla_Ventana2.setColumnWidth(2, 150)
        self.tabla_Ventana2.setColumnWidth(4, 85)
        self.tabla_Ventana2.setColumnWidth(5, 250)
        self.btn_Nuevo_Pago = QPushButton(self.ventana2)
        self.btn_Nuevo_Pago.setObjectName(u"btn_Nuevo_Pago")
        self.btn_Nuevo_Pago.setGeometry(QRect(9, 550, 160, 30))
        font = QFont()
        font.setPointSize(8)
        self.btn_Nuevo_Pago.setFont(font)
        icon = QIcon()
        icon.addFile(u"../../Proyect/pySide_Gastos/icon/nuevo.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Nuevo_Pago.setIcon(icon)
        self.btn_Editar_Pago = QPushButton(self.ventana2)
        self.btn_Editar_Pago.setObjectName(u"btn_Editar_Pago")
        self.btn_Editar_Pago.setGeometry(QRect(250, 550, 160, 30))
        icon1 = QIcon()
        icon1.addFile(u"../../Proyect/pySide_Gastos/icon/editar.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Editar_Pago.setIcon(icon1)
        self.btn_Eliminar = QPushButton(self.ventana2)
        self.btn_Eliminar.setObjectName(u"btn_Eliminar")
        self.btn_Eliminar.setGeometry(QRect(490, 550, 160, 30))
        icon2 = QIcon()
        icon2.addFile(u"../../Proyect/pySide_Gastos/icon/delete.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Eliminar.setIcon(icon2)
        self.label_Total = QLabel(self.ventana2)
        self.label_Total.setObjectName(u"label_Total")
        self.label_Total.setGeometry(QRect(730, 540, 91, 31))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setUnderline(True)
        font1.setStrikeOut(False)
        self.label_Total.setFont(font1)
        self.label_Total.setAlignment(Qt.AlignCenter)
        self.label_Total_Edit = QLabel(self.ventana2)
        self.label_Total_Edit.setObjectName(u"label_Total_Edit")
        self.label_Total_Edit.setGeometry(QRect(790, 540, 71, 31))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        self.label_Total_Edit.setFont(font2)
        self.label_Total_Edit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_Total_moneda = QLabel(self.ventana2)
        self.label_Total_moneda.setObjectName(u"label_Total_moneda")
        self.label_Total_moneda.setGeometry(QRect(860, 540, 16, 31))
        self.label_Total_moneda.setFont(font2)
        self.label_Total_moneda.setAlignment(Qt.AlignCenter)
        self.box_Meses = QComboBox(self.ventana2)
        self.box_Meses.addItem("")
        self.box_Meses.addItem("")
        self.box_Meses.addItem("")
        self.box_Meses.addItem("")
        self.box_Meses.addItem("")
        self.box_Meses.addItem("")
        self.box_Meses.addItem("")
        self.box_Meses.addItem("")
        self.box_Meses.addItem("")
        self.box_Meses.addItem("")
        self.box_Meses.addItem("")
        self.box_Meses.addItem("")
        self.box_Meses.addItem("")
        self.box_Meses.setObjectName(u"box_Meses")
        self.box_Meses.setGeometry(QRect(660, 40, 231, 24))
        self.label_Ingresos_Edit = QLabel(self.ventana2)
        self.label_Ingresos_Edit.setObjectName(u"label_Ingresos_Edit")
        self.label_Ingresos_Edit.setGeometry(QRect(790, 510, 70, 31))
        self.label_Ingresos_Edit.setFont(font2)
        self.label_Ingresos_Edit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.signo_Ingreso_moneda = QLabel(self.ventana2)
        self.signo_Ingreso_moneda.setObjectName(u"signo_Ingreso_moneda")
        self.signo_Ingreso_moneda.setGeometry(QRect(860, 510, 16, 31))
        self.signo_Ingreso_moneda.setFont(font2)
        self.signo_Ingreso_moneda.setAlignment(Qt.AlignCenter)
        self.label_Ingresos = QLabel(self.ventana2)
        self.label_Ingresos.setObjectName(u"label_Ingresos")
        self.label_Ingresos.setGeometry(QRect(680, 510, 121, 31))
        self.label_Ingresos.setFont(font1)
        self.label_Ingresos.setAlignment(Qt.AlignCenter)
        self.label_select_mes = QLabel(self.ventana2)
        self.label_select_mes.setObjectName(u"label_select_mes")
        self.label_select_mes.setGeometry(QRect(658, 10, 231, 20))
        self.label_select_mes.setAlignment(Qt.AlignCenter)
        self.label_Gastos = QLabel(self.ventana2)
        self.label_Gastos.setObjectName(u"label_Gastos")
        self.label_Gastos.setGeometry(QRect(680, 480, 131, 31))
        self.label_Gastos.setFont(font1)
        self.label_Gastos.setAlignment(Qt.AlignCenter)
        self.label_Gastos_Edit = QLabel(self.ventana2)
        self.label_Gastos_Edit.setObjectName(u"label_Gastos_Edit")
        self.label_Gastos_Edit.setGeometry(QRect(790, 480, 70, 31))
        self.label_Gastos_Edit.setFont(font2)
        self.label_Gastos_Edit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.signo_Gastos_moneda = QLabel(self.ventana2)
        self.signo_Gastos_moneda.setObjectName(u"signo_Gastos_moneda")
        self.signo_Gastos_moneda.setGeometry(QRect(860, 480, 16, 31))
        self.signo_Gastos_moneda.setFont(font2)
        self.signo_Gastos_moneda.setAlignment(Qt.AlignCenter)
        self.btn_actualizar = QPushButton(self.ventana2)
        self.btn_actualizar.setObjectName(u"btn_actualizar")
        self.btn_actualizar.setGeometry(QRect(660, 80, 41, 24))
        icon3 = QIcon()
        icon3.addFile(u"../../Proyect/pySide_Gastos/icon/actualizar.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_actualizar.setIcon(icon3)
        self.tabWidget.addTab(self.ventana2, "")
        self.ventana3 = QWidget()
        self.ventana3.setObjectName(u"ventana3")
        self.grafica1 = QFrame(self.ventana3)
        self.grafica1.setObjectName(u"grafica1")
        self.grafica1.setGeometry(QRect(70, 10, 811, 280))
        self.grafica1.setFrameShape(QFrame.StyledPanel)
        self.grafica1.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_2 = QWidget(self.grafica1)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(9, 9, 791, 261))
        self.layout_Gastos = QVBoxLayout(self.verticalLayoutWidget_2)
        self.layout_Gastos.setSpacing(0)
        self.layout_Gastos.setObjectName(u"layout_Gastos")
        self.layout_Gastos.setContentsMargins(0, 0, 0, 0)
        self.btn_actualizar_grafica = QPushButton(self.ventana3)
        self.btn_actualizar_grafica.setObjectName(u"btn_actualizar_grafica")
        self.btn_actualizar_grafica.setGeometry(QRect(20, 280, 41, 31))
        self.btn_actualizar_grafica.setIcon(icon3)
        self.grafica2 = QFrame(self.ventana3)
        self.grafica2.setObjectName(u"grafica2")
        self.grafica2.setGeometry(QRect(70, 299, 811, 281))
        self.grafica2.setLayoutDirection(Qt.LeftToRight)
        self.grafica2.setFrameShape(QFrame.StyledPanel)
        self.grafica2.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.grafica2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 791, 261))
        self.layout_Ahorro = QVBoxLayout(self.verticalLayoutWidget)
        self.layout_Ahorro.setObjectName(u"layout_Ahorro")
        self.layout_Ahorro.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.ventana3, "")
        QWidget.setTabOrder(self.btn_actualizar_grafica, self.btn_Nuevo_Pago)
        QWidget.setTabOrder(self.btn_Nuevo_Pago, self.btn_Editar_Pago)
        QWidget.setTabOrder(self.btn_Editar_Pago, self.btn_Eliminar)
        QWidget.setTabOrder(self.btn_Eliminar, self.box_Meses)
        QWidget.setTabOrder(self.box_Meses, self.btn_actualizar)
        QWidget.setTabOrder(self.btn_actualizar, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.tabla_Ventana2)

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Gastos Personales", None))
        ___qtablewidgetitem = self.tabla_Ventana2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tabla_Ventana2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Fecha", None));
        ___qtablewidgetitem2 = self.tabla_Ventana2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Concepto", None));
        ___qtablewidgetitem3 = self.tabla_Ventana2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Categoria", None));
        ___qtablewidgetitem4 = self.tabla_Ventana2.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Monto $", None));
        ___qtablewidgetitem5 = self.tabla_Ventana2.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Observacion", None));
        ___qtablewidgetitem6 = self.tabla_Ventana2.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"PDF", None));
        self.btn_Nuevo_Pago.setText(QCoreApplication.translate("Form", u" Nuevo", None))
        self.btn_Editar_Pago.setText(QCoreApplication.translate("Form", u" Editar", None))
        self.btn_Eliminar.setText(QCoreApplication.translate("Form", u" Eliminar", None))
        self.label_Total.setText(QCoreApplication.translate("Form", u"Total:", None))
        self.label_Total_Edit.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_Total_moneda.setText(QCoreApplication.translate("Form", u"$", None))
        self.box_Meses.setItemText(0, QCoreApplication.translate("Form", u"Selecciona el mes", None))
        self.box_Meses.setItemText(1, QCoreApplication.translate("Form", u"Enero", None))
        self.box_Meses.setItemText(2, QCoreApplication.translate("Form", u"Febrero", None))
        self.box_Meses.setItemText(3, QCoreApplication.translate("Form", u"Marzo", None))
        self.box_Meses.setItemText(4, QCoreApplication.translate("Form", u"Abril", None))
        self.box_Meses.setItemText(5, QCoreApplication.translate("Form", u"Mayo", None))
        self.box_Meses.setItemText(6, QCoreApplication.translate("Form", u"Junio", None))
        self.box_Meses.setItemText(7, QCoreApplication.translate("Form", u"Julio", None))
        self.box_Meses.setItemText(8, QCoreApplication.translate("Form", u"Agosto", None))
        self.box_Meses.setItemText(9, QCoreApplication.translate("Form", u"Septiembre", None))
        self.box_Meses.setItemText(10, QCoreApplication.translate("Form", u"Octubre", None))
        self.box_Meses.setItemText(11, QCoreApplication.translate("Form", u"Noviembre", None))
        self.box_Meses.setItemText(12, QCoreApplication.translate("Form", u"Diciembre", None))

        self.label_Ingresos_Edit.setText(QCoreApplication.translate("Form", u"0", None))
        self.signo_Ingreso_moneda.setText(QCoreApplication.translate("Form", u"$", None))
        self.label_Ingresos.setText(QCoreApplication.translate("Form", u"Total Ingresos", None))
        self.label_select_mes.setText(QCoreApplication.translate("Form", u"Selecciona el mes", None))
        self.label_Gastos.setText(QCoreApplication.translate("Form", u"Total Gastos", None))
        self.label_Gastos_Edit.setText(QCoreApplication.translate("Form", u"0", None))
        self.signo_Gastos_moneda.setText(QCoreApplication.translate("Form", u"$", None))
        self.btn_actualizar.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ventana2), QCoreApplication.translate("Form", u"Pagos Mensuales", None))
        self.btn_actualizar_grafica.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ventana3), QCoreApplication.translate("Form", u"Graficos", None))
    # retranslateUi

