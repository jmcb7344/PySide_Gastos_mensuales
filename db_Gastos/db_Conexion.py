import sys, os
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from pathlib import Path

class Conexion():

    def adsPath(file):
        return str(Path(__file__).parent.absolute() / file)

    @classmethod
    def check(cls):
        if not os.path.exists(cls.adsPath("Gestor_Gastos.db")):
            cls.db_connect()
            cls.db_create()
        else:
            cls.db_connect()

    @classmethod
    def db_connect(cls):
        conexion = QSqlDatabase.addDatabase('QSQLITE')
        conexion.setDatabaseName(cls.adsPath("Gestor_Gastos.db"))
        try:
            conexion.open()
            print('Conexion exitosa')
        except TypeError as e:
            print(e)
            sys.exit()

    @classmethod
    def db_create(cls):
        query = QSqlQuery()
        query.exec_("""CREATE TABLE IF NOT EXISTS gastos_mensuales
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        fecha TEXT, 
                        concepto VARCHAR(50) NOT NULL, 
                        categoria VARCHAR(50) NOT NULL, 
                        monto NUMERIC NOT NULL, 
                        Nota TEXT, 
                        remito TEXT,
                        tipo VARCHAR(50)) """)
