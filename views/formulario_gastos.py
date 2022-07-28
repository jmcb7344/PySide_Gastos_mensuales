from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Gastos_mes(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(320, 298)
        self.btn_salir = QPushButton(Form)
        self.btn_salir.setObjectName(u"btn_salir")
        self.btn_salir.setGeometry(QRect(9, 270, 301, 24))
        self.label_estimado = QLabel(Form)
        self.label_estimado.setObjectName(u"label_estimado")
        self.label_estimado.setGeometry(QRect(9, 133, 88, 16))
        self.label_real = QLabel(Form)
        self.label_real.setObjectName(u"label_real")
        self.label_real.setGeometry(QRect(9, 164, 91, 16))
        self.btn_agregar = QPushButton(Form)
        self.btn_agregar.setObjectName(u"btn_agregar")
        self.btn_agregar.setGeometry(QRect(9, 241, 301, 24))
        self.label_remito = QLabel(Form)
        self.label_remito.setObjectName(u"label_remito")
        self.label_remito.setGeometry(QRect(9, 191, 301, 21))
        self.label_remito.setAlignment(Qt.AlignCenter)
        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(120, 40, 190, 24))
        self.txt_monto = QLineEdit(Form)
        self.txt_monto.setObjectName(u"txt_monto")
        self.txt_monto.setGeometry(QRect(120, 131, 190, 24))
        self.txt_nota = QLineEdit(Form)
        self.txt_nota.setObjectName(u"txt_nota")
        self.txt_nota.setGeometry(QRect(120, 161, 190, 24))
        self.txt_remito_PDF = QLineEdit(Form)
        self.txt_remito_PDF.setObjectName(u"txt_remito_PDF")
        self.txt_remito_PDF.setGeometry(QRect(9, 211, 261, 24))
        self.btn_PDF = QPushButton(Form)
        self.btn_PDF.setObjectName(u"btn_PDF")
        self.btn_PDF.setGeometry(QRect(280, 211, 31, 24))
        self.label_categoria = QLabel(Form)
        self.label_categoria.setObjectName(u"label_categoria")
        self.label_categoria.setGeometry(QRect(9, 100, 98, 21))
        self.label_concepto_Pago = QLabel(Form)
        self.label_concepto_Pago.setObjectName(u"label_concepto_Pago")
        self.label_concepto_Pago.setGeometry(QRect(9, 40, 111, 21))
        self.txt_concepto_nuevo = QLineEdit(Form)
        self.txt_concepto_nuevo.setObjectName(u"txt_concepto_nuevo")
        self.txt_concepto_nuevo.setEnabled(False)
        self.txt_concepto_nuevo.setGeometry(QRect(120, 70, 190, 24))
        self.check_ingresos = QRadioButton(Form)
        self.check_ingresos.setObjectName(u"check_ingresos")
        self.check_ingresos.setGeometry(QRect(60, 10, 91, 22))
        self.check_Egresos = QRadioButton(Form)
        self.check_Egresos.setObjectName(u"check_Egresos")
        self.check_Egresos.setGeometry(QRect(180, 10, 91, 22))
        self.comboBox_categoria = QComboBox(Form)
        self.comboBox_categoria.addItem("")
        self.comboBox_categoria.setObjectName(u"comboBox_categoria")
        self.comboBox_categoria.setGeometry(QRect(120, 100, 190, 24))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Nuevo Pago", None))
        self.btn_salir.setText(QCoreApplication.translate("Form", u"Salir", None))
        self.label_estimado.setText(QCoreApplication.translate("Form", u"Monto $", None))
        self.label_real.setText(QCoreApplication.translate("Form", u"Observacion", None))
        self.btn_agregar.setText(QCoreApplication.translate("Form", u"Agregar", None))
        self.label_remito.setText(QCoreApplication.translate("Form", u"Cargar remito", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Selecciona categoria", None))

        self.txt_monto.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.btn_PDF.setText(QCoreApplication.translate("Form", u"...", None))
        self.label_categoria.setText(QCoreApplication.translate("Form", u"Categoria", None))
        self.label_concepto_Pago.setText(QCoreApplication.translate("Form", u"Concepto de pago", None))
        self.check_ingresos.setText(QCoreApplication.translate("Form", u"Ingreso", None))
        self.check_Egresos.setText(QCoreApplication.translate("Form", u"Egreso", None))
        self.comboBox_categoria.setItemText(0, QCoreApplication.translate("Form", u"Selecciona categoria", None))

    # retranslateUi

