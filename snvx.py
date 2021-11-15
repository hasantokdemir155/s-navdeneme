
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from ssql import *
import pyodbc

import sys
from snv import *

def getr():
     ui.tableWidget.clear()
     a=ui.comboBox.currentText()
     ui.tableWidget.setHorizontalHeaderLabels(('ÖĞNO', 'AD','SOYAD','SINIF','SIRA','PUAN'))
     crs1.execute('exec snavdeg @snav=?',a)
     
     k=0
     for s in crs1 :
         
         for i in range(0,6): 
            ui.tableWidget.setItem(k,i,QTableWidgetItem(str(s[i])))   
         k=k+1   

uyg=QApplication(sys.argv)
penAna=QMainWindow()
ui=Ui_MainWindow()

ui.setupUi(penAna)
#╬ui.pushButton.clicked.connect(ekle) 
ui.tableWidget.setHorizontalHeaderLabels(('ÖĞNO', 'AD','SOYAD','SINIF','SIRA','PUAN'))
conn = pyodbc.connect(
       "Driver={SQL Server Native Client 11.0};"
       "Server=HASAN\SQLEXPRESS1;"
       "Database=ogrver;"
       "Trusted_Connection=yes;"
    )

crs=conn.cursor()
crs1=conn.cursor()
crs.execute('select snavadı from snavlar group by snavadı')

for i in crs:
    
    ui.comboBox.addItem(i[0])

ui.pushButton.clicked.connect(getr) 


penAna.show()
