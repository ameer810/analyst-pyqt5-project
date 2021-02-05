from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui
import datetime
from PyQt5.uic import loadUiType
import sys
import os
from datetime import date
import MySQLdb
from MySQLdb import IntegrityError, OperationalError
from xlsxwriter import *

FORM_CLASS, _ = loadUiType("design.ui")

client_id_glob = 0
chick_if_add_new = False


class mainapp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(mainapp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.tabWidget.tabBar().setVisible(False)
        self.DB_Connect()
        self.handel_buttons()

    def DB_Connect(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='12345', db='tahlel')
        self.cur = self.db.cursor()

    def handel_buttons(self):
        self.lineEdit_22.hide()
        self.lineEdit_23.hide()
        self.label_42.hide()
        self.label_43.hide()
        self.pushButton_15.clicked.connect(self.Light_Blue_Theme)
        self.pushButton_9.clicked.connect(self.Dark_Orange_Theme)
        self.pushButton_13.clicked.connect(self.Dark_Blue_Theme)
        self.pushButton_14.clicked.connect(self.Dark_Theme)
        self.pushButton_11.clicked.connect(self.Dark_Gray_Theme)
        self.pushButton.clicked.connect(self.Open_Sales_Page)
        self.pushButton_6.clicked.connect(self.Open_Login_Page)
        self.pushButton_4.clicked.connect(self.Open_Settings_Page)
        self.pushButton_3.clicked.connect(self.Open_History_Page)
        self.pushButton_5.clicked.connect(self.Open_clients_Page)
        self.pushButton_2.clicked.connect(self.Open_Analyse_Page)
        self.pushButton_8.clicked.connect(self.Open_ResetPassword_Page)
        self.pushButton_17.clicked.connect(self.Sales_Page)
        self.pushButton_30.clicked.connect(self.get_client_id)

    def Sales_Page(self):
        global client_id_glob
        global chick_if_add_new
        # client_name='تتتب'
        # client_age=16
        client_genus = 'kdk'
        # client_doctor='kdk'
        client_name = self.lineEdit_20.text()
        client_age = self.spinBox_7.value()
        # client_genus = self.comboBox_14.currentText()
        client_doctor = self.comboBox_15.currentText()
        # analyst_client = self.comboBox_22.currentText()
        analyst_name = self.comboBox_16.currentText()
        analyst_or_clients_notes = self.textEdit.toPlainText()
        analyst_lineEdit_result = self.lineEdit_21.text()
        analyst_combo_result = self.comboBox_17.currentText()
        analyst_number_result = self.spinBox_8.value()
        client_id = self.spinBox.value()
        latest_result = 1
        self.cur.execute('''
           INSERT INTO addclient (client_name,client_age,client_genus,client_doctor)
           VALUES (%s,%s,%s,%s)
        ''', (client_name, client_age, client_genus, client_doctor))
        self.db.commit()
        self.cur.execute(''' SELECT * FROM addclient ''')
        client_data = self.cur.fetchall()
        self.cur.execute('''SELECT price FROM addanalyst WHERE name = %s''', (analyst_name,))
        analyst_price = self.cur.fetchone()
        self.cur.execute('''SELECT id FROM addclient WHERE client_name = %s''', (client_name,))
        real_client_id = self.cur.fetchone()

        self.db.commit()
        data = self.cur.fetchone()
        total_price = 1

        self.cur.execute('''
           INSERT INTO addnewitem (client_name,client_id,client_age,genus,doctor_name,notes,analyst_name,analyst_result,price,total_price)
           VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ''', (
            client_name, real_client_id, client_age, client_genus, client_doctor, analyst_or_clients_notes,
            analyst_name,
            latest_result,
            data, total_price))
        self.db.commit()
        chick_if_add_new = True
        self.Show_All_one_client_analyst()
        chick_if_add_new = False

    def Show_All_one_client_analyst(self):
        global client_id_glob
        global chick_if_add_new
        client_name = self.lineEdit_20.text()
        self.cur.execute('''
             SELECT client_name,analyst_name,analyst_result,doctor_name FROM addnewitem WHERE client_name = %s
        ''', (client_name,))
        analyst_data = self.cur.fetchall()
        print(analyst_data)

        if client_id_glob != 0 and chick_if_add_new != True:
            self.cur.execute('''
                         SELECT client_name,analyst_name,analyst_result,doctor_name,client_id FROM addnewitem WHERE client_id = %s
                    ''', (client_id_glob,))
            analyst_data = self.cur.fetchall()
            print(analyst_data)
            print(client_id_glob)
            # print(client_id_glob)
        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.insertRow(0)

        for row, form in enumerate(analyst_data):
            for col, item in enumerate(form):
                self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            row_pos = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(row_pos)
        self.Show_All_The_Sales()

    def get_client_id(self):
        global client_id_glob
        client_id_glob = self.spinBox.value()
        self.Show_All_one_client_analyst()

    def Show_All_The_Sales(self):
        self.cur.execute(''' SELECT * FROM addclient''')
        analyst_data = self.cur.fetchall()
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_6.insertRow(0)
        for row, form in enumerate(analyst_data):
            for col, item in enumerate(form):
                self.tableWidget_6.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            row_pos = self.tableWidget_6.rowCount()
            self.tableWidget_6.insertRow(row_pos)

    def Open_Sales_Page(self):
        self.tabWidget.setCurrentIndex(3)
        self.Show_All_The_Sales()

    def Open_Login_Page(self):
        self.tabWidget.setCurrentIndex(0)

    def Open_Settings_Page(self):
        self.tabWidget.setCurrentIndex(6)

    def Open_History_Page(self):
        self.tabWidget.setCurrentIndex(5)

    def Open_clients_Page(self):
        self.tabWidget.setCurrentIndex(2)

    def Open_Analyse_Page(self):
        self.tabWidget.setCurrentIndex(4)

    def Open_ResetPassword_Page(self):
        self.tabWidget.setCurrentIndex(1)

    def Light_Blue_Theme(self):
        style = open('themes/light_blue.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Blue_Theme(self):
        style = open('themes/darkblue.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Gray_Theme(self):
        style = open('themes/darkgray.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Orange_Theme(self):
        style = open('themes/darkorange.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Theme(self):
        style = open('themes/qdark.css', 'r')
        style = style.read()
        self.setStyleSheet(style)


def main():
    app = QApplication(sys.argv)
    window = mainapp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
