from PySide6.QtSql import QSqlQuery
from PySide6.QtCharts import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Indicadores():

    def indicador_egreso(self):
        _meses = QSqlQuery()
        _mes_egreso = []
        for x in range(12):
            _meses.prepare("SELECT sum(monto) FROM gastos_mensuales WHERE tipo='Egreso' AND strftime('%m',fecha)=?")
            mes = str(x+1).rjust(2, '0')
            _meses.bindValue(0, mes)
            _meses.exec()
            _meses.first()
            if _meses.value(0) == '':
                _mes_egreso.append(0)
            else:
                _mes_egreso.append(_meses.value(0)*-1)

        #Varga de los datos de la grafica
        set_egreso = QBarSet('Total de Egreso')
        set_egreso.append(_mes_egreso)
        serie_egreso = QBarSeries()
        serie_egreso.append(set_egreso)

        #Creamos el Grafico
        chart_egreso = QChart()
        chart_egreso.addSeries(serie_egreso)
        chart_egreso.setTitle("Egresos Mensuales")
        chart_egreso.setAnimationOptions(QChart.SeriesAnimations)

        categoria = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

        ejeX_egreso = QBarCategoryAxis()
        ejeX_egreso.append(categoria)
        chart_egreso.addAxis(ejeX_egreso, Qt.AlignBottom)
        serie_egreso.attachAxis(ejeX_egreso)

        ejeY_egreso = QValueAxis()
        ejeY_egreso.setRange(0,min(_mes_egreso))
        chart_egreso.addAxis(ejeY_egreso, Qt.AlignLeft)
        serie_egreso.attachAxis(ejeY_egreso)

        chart_egreso.legend().setVisible(True)
        chart_egreso.legend().setAlignment(Qt.AlignBottom)
        chartView_egreso = QChartView(chart_egreso)
        chartView_egreso.setRenderHint(QPainter.Antialiasing)

        return chartView_egreso
        

    def indicador_ahorro(self):
        _meses_egreso = QSqlQuery()
        _meses_Ingreso = QSqlQuery()
        _mes_Ahorro = []

        for x in range(12):
            _meses_egreso.prepare("SELECT sum(monto) FROM gastos_mensuales WHERE tipo='Egreso' AND strftime('%m',fecha)=?")
            mes = str(x+1).rjust(2, '0')
            _meses_egreso.bindValue(0, mes)
            _meses_egreso.exec()
            _meses_Ingreso.prepare("SELECT sum(monto) FROM gastos_mensuales WHERE tipo='Ingreso' AND strftime('%m',fecha)=?")
            mes = str(x+1).rjust(2, '0')
            _meses_Ingreso.bindValue(0, mes)
            _meses_Ingreso.exec()
            _meses_Ingreso.first()
            _meses_egreso.first()
            ingreso = _meses_Ingreso.value(0)
            egreso = _meses_egreso.value(0)
            if _meses_egreso.value(0) == '':
                ingreso = 0
            if _meses_Ingreso.value(0) == '':
                egreso = 0
            try:
                ahorro = ((ingreso-abs(egreso))/ingreso)*100
                _mes_Ahorro.append(ahorro)
            except Exception as e:
                _mes_Ahorro.append(0)
        
        set_ahorro = QBarSet('Total de Ahorro')
        set_ahorro.append(_mes_Ahorro)
        serie_Ahorro = QBarSeries()
        serie_Ahorro.append(set_ahorro)

        chart_Ahorro = QChart()
        chart_Ahorro.addSeries(serie_Ahorro)
        chart_Ahorro.setTitle("% Ahorro Mensuales")
        chart_Ahorro.setAnimationOptions(QChart.SeriesAnimations)

        categoria = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
        ejeX_ahorro = QBarCategoryAxis()
        ejeX_ahorro.append(categoria)
        chart_Ahorro.addAxis(ejeX_ahorro, Qt.AlignBottom)
        serie_Ahorro.attachAxis(ejeX_ahorro)

        ejeY_Ahorro = QValueAxis()
        ejeY_Ahorro.setRange(0,max(_mes_Ahorro))
        chart_Ahorro.addAxis(ejeY_Ahorro, Qt.AlignLeft)
        serie_Ahorro.attachAxis(ejeY_Ahorro)

        chart_Ahorro.legend().setVisible(True)
        chart_Ahorro.legend().setAlignment(Qt.AlignBottom)
        chartView_ahorro = QChartView(chart_Ahorro)
        chartView_ahorro.setRenderHint(QPainter.Antialiasing)
        
        return chartView_ahorro