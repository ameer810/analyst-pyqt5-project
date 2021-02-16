import datetime
import sys

import MySQLdb
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

FORM_CLASS, _ = loadUiType("design.ui")
user_id = 1
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
        self.Show_All_The_Sales()
        self.Show_all_analysts_in_combo()
        self.Show_all_buys()
        self.History()

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
        self.pushButton_31.clicked.connect(self.Chick_analyst_category)
        self.pushButton_32.clicked.connect(self.get_total_price)
        self.pushButton_33.clicked.connect(self.Show_analyst_in_Edit_Or_Delete)
        self.pushButton_29.clicked.connect(self.Clients_Page)
        self.pushButton_16.clicked.connect(self.Add_Buys)
        self.pushButton_20.clicked.connect(self.Show_All_The_Analysts)
        self.pushButton_27.clicked.connect(self.Edit_Analyst)
        self.pushButton_7.clicked.connect(self.Log_In_Chieck)
        self.pushButton_28.clicked.connect(self.Delete_Analyst)
        self.pushButton_22.clicked.connect(self.Delete_All_History_Data)

    def Sales_Page(self):
        global client_id_glob
        global chick_if_add_new
        analyst_name = self.comboBox_16.currentText()
        # client_name='تتتب'
        # client_age=16
        client_genus = 'kdk'
        # client_doctor='kdk'
        client_name = self.lineEdit_20.text()
        client_age = self.spinBox_7.value()
        # client_genus = self.comboBox_14.currentText()
        client_doctor = self.comboBox_15.currentText()
        # analyst_client = self.comboBox_22.currentText()

        analyst_or_clients_notes = self.textEdit.toPlainText()
        analyst_lineEdit_result = self.lineEdit_21.text()
        analyst_combo_result = self.comboBox_17.currentText()
        analyst_number_result = self.spinBox_8.value()
        client_id = self.spinBox.value()
        latest_result = 1
        self.cur.execute('''
           INSERT INTO addclient (client_name,client_age,client_genus,client_doctor,date)
           VALUES (%s,%s,%s,%s,%s)
        ''', (client_name, client_age, client_genus, client_doctor, datetime.datetime.now()))
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
           INSERT INTO addnewitem (client_name,client_id,client_age,genus,doctor_name,notes,analyst_name,analyst_result,price,total_price,date)
           VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ''', (
            client_name, real_client_id, client_age, client_genus, client_doctor, analyst_or_clients_notes,
            analyst_name,
            latest_result,
            analyst_price, total_price, datetime.datetime.now()))
        self.db.commit()
        self.cur.execute('''
                                                     SELECT client_name,analyst_name,analyst_result,doctor_name,client_id,client_age,genus,notes FROM addnewitem WHERE client_name = %s
                                                ''', (self.lineEdit_20.text(),))
        analyst_data = self.cur.fetchall()

        print(analyst_data)
        print('start4')
        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.insertRow(0)

        for row, form in enumerate(analyst_data):
            for col, item in enumerate(form):
                self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            row_pos = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(row_pos)
        chick_if_add_new = True
        # self.Show_All_one_client_analyst()
        self.Add_Data_To_history(3, 1)
        self.History()

        # client_age = self.spinBox_7.setValue(0)
        # client_genus = self.comboBox_14.setCurrentIndex(0)
        # client_doctor = self.comboBox_15.setCurrentIndex(0)
        # # analyst_client = self.comboBox_22.setCurrentIndex(0)
        # analyst_name = self.comboBox_16.setCurrentIndex(0)
        # analyst_or_clients_notes = self.textEdit.setToPlainText()
        # analyst_lineEdit_result = self.lineEdit_21.setText('')
        # analyst_combo_result = self.comboBox_17.setCurrentIndex(0)
        # analyst_number_result = self.spinBox_8.setValue(0)
        # client_id = self.spinBox.setValue(0)
        chick_if_add_new = False
        # self.Show_All_one_client_analyst()


    def get_total_price(self):
        total_price = 0
        for row in range(0, self.tableWidget_5.rowCount() - 1):
            a = self.tableWidget_5.item(row, 4).text()
            if type(a) != int:
                a = 0
            total_price += int(a)
        self.lineEdit_24.setText(str(total_price))

    def Chick_analyst_category(self):
        analyst_name = self.comboBox_16.currentText()
        self.cur.execute('''SELECT category FROM addanalyst WHERE name = %s''', (analyst_name,))
        analyst_category = self.cur.fetchone()

        if analyst_category == 'عدد':
            self.comboBox_17.hide()
            self.lineEdit_21.hide()
            self.spinBox_8.show()
        if analyst_category == 'خيارات':
            self.lineEdit_21.hide()
            self.spinBox_8.hide()
            self.comboBox_17.show()
        if analyst_category == 'حقل كتابة':
            self.lineEdit_21.hide()
            self.spinBox_8.hide()
            self.comboBox_17.hide()
        if analyst_category == 'خيارات مع تعديل':
            self.lineEdit_21.hide()
            self.spinBox_8.hide()
            self.comboBox_17.setEditable(True)

    def Show_All_one_client_analyst(self):
        global client_id_glob
        global chick_if_add_new
        client_name = self.lineEdit_20.text()
        self.cur.execute('''
             SELECT client_name,analyst_name,analyst_result,doctor_name FROM addnewitem WHERE client_name = %s
        ''', (client_name,))
        analyst_data = self.cur.fetchall()
        print('start')
        if client_id_glob != 0 and chick_if_add_new != True:
            print('start2')
            self.cur.execute('''
                         SELECT client_name,analyst_name,analyst_result,doctor_name,client_id,client_age,genus,notes FROM addnewitem WHERE client_id = %s
                    ''', (self.spinBox.value(),))
            analyst_data = self.cur.fetchall()
            print(analyst_data)
            # need doctor name enabled i will make it with current text

            self.lineEdit_20.setText(analyst_data[0][0])
            self.lineEdit_20.setEnabled(False)
            self.spinBox_7.setValue(int(analyst_data[0][5]))
            self.spinBox_7.setEnabled(False)
            if analyst_data[0][6] == 'ذكر':
                self.comboBox_14.setCurrentIndex(0)
                self.comboBox_14.setEnabled(False)
            if analyst_data[0][6] == 'انثى':
                self.comboBox_14.setCurrentIndex(1)
                self.comboBox_14.setEnabled(False)
            self.textEdit.setPlainText(str(analyst_data[0][7]))
            self.textEdit.setEnabled(False)
        if client_id_glob ==0:
            print('start3')
            self.cur.execute('''
                                         SELECT client_name,analyst_name,analyst_result,doctor_name,client_id,client_age,genus,notes FROM addnewitem WHERE client_name = %s
                                    ''', (self.lineEdit_20.text(),))
            analyst_data=self.cur.fetchall()

        print(analyst_data)
        print('start4')
        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.insertRow(0)

        for row, form in enumerate(analyst_data):
            for col, item in enumerate(form):
                self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            row_pos = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(row_pos)
        if self.spinBox.value() == 0:
            self.tableWidget_5.setRowCount(0)
            self.tableWidget_5.insertRow(0)
            self.lineEdit_20.setText('')
            self.spinBox_7.setValue(0)
            self.comboBox_14.setCurrentIndex(0)
            self.textEdit.setPlainText('')
            self.lineEdit_20.setEnabled(True)
            self.spinBox_7.setEnabled(True)
            self.comboBox_14.setEnabled(True)
            self.textEdit.setEnabled(True)
        self.Show_All_The_Sales()


    def get_client_id(self):
        global client_id_glob
        client_id_glob = self.spinBox.value()
        self.Show_All_one_client_analyst()
        # self.Add_Data_To_history(6, 1)
        # self.History()

    def Show_All_The_Sales(self):
        self.cur.execute(''' SELECT * FROM addclient ORDER BY -date''')
        analyst_data = self.cur.fetchall()
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_6.insertRow(0)
        for row, form in enumerate(analyst_data):
            for col, item in enumerate(form):
                self.tableWidget_6.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            row_pos = self.tableWidget_6.rowCount()
            self.tableWidget_6.insertRow(row_pos)

    def Show_All_The_Analysts(self):
        search_type = self.comboBox_19.currentText()
        search_words = self.lineEdit_26.text()
        combobox_value = ''
        sql = ''
        if search_type == 'اسم التحليل المطابق':
            combobox_value = 'name'
        if search_type == 'السعر المطابق':
            combobox_value = 'price'
        if search_type != 'اسم التحليل المطابق' and search_type != 'السعر المطابق':
            sql = ''' SELECT name,category,default_result1,default_result2,price FROM addanalyst'''
        else:
            sql = f' SELECT name,category,default_result1,default_result2,price FROM addanalyst WHERE {combobox_value}=%s'
        if type(search_words) == int:
            self.cur.execute(sql, int(search_words, ))
        if type(search_words) == str:
            self.cur.execute(sql, str(search_words, ))
        analyst_data = self.cur.fetchall()
        self.tableWidget_7.setRowCount(0)
        self.tableWidget_7.insertRow(0)
        for row, form in enumerate(analyst_data):
            for col, item in enumerate(form):
                if col == 1:
                    category = ''
                    if analyst_data[row][1] == 'خيارات':
                        category = 'خيارات'
                    if analyst_data[row][1] == 'عدد':
                        category = 'عدد'
                    if analyst_data[row][1] == 'خيارات مع تعديل':
                        category = 'خيارات مع تعديل'
                    if analyst_data[row][1] == 'حقل كتابة':
                        category = 'حقل كتابة'

                    self.tableWidget_7.setItem(row, col, QTableWidgetItem(str(category)))
                self.tableWidget_7.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            row_pos = self.tableWidget_7.rowCount()
            self.tableWidget_7.insertRow(row_pos)
        self.Add_Data_To_history(6, 2)
        self.History()

    def Add_Analyst(self):
        analyst_name = self.lineEdit_28.text()
        analyst_result_category = self.comboBox_22.currentText()
        analyst_result1 = self.doubleSpinBox_3.value()
        analyst_result2 = self.doubleSpinBox_2.value()
        analyst_price = self.doubleSpinBox.value()
        date = datetime.datetime.now()
        self.cur.execute(
            ''' INSERT INTO addanalyst (name,default_result1,default_result2,price,category,date) VALUES(%s,%s,%s,%s,%s,%s) ''',
            (analyst_name, analyst_result1, analyst_result2, analyst_result_category, analyst_price, date))
        self.Add_Data_To_history(3, 2)
        self.History()

    def Show_analyst_in_Edit_Or_Delete(self):
        analyst_current_name = self.comboBox_21.currentText()
        self.cur.execute(
            ''' SELECT name,default_result1,default_result2,price,category,date FROM addanalyst WHERE name=%s ''',
            (analyst_current_name,))
        data = self.cur.fetchall()
        print(data)
        analyst_name = self.lineEdit_29.setText(str(data[0][0]))
        analyst_result_category = self.comboBox_23.setCurrentIndex(0)
        analyst_result1 = self.doubleSpinBox_4.setValue(data[0][1])
        analyst_result2 = self.doubleSpinBox_5.setValue(data[0][2])
        analyst_price = self.doubleSpinBox_6.setValue(data[0][3])
        self.Add_Data_To_history(6, 2)
        self.History()

    def Edit_Analyst(self):
        analyst_current_name = self.comboBox_21.currentText()
        analyst_name = self.lineEdit_29.text()
        analyst_result_category = self.comboBox_23.currentText()
        analyst_result1 = self.doubleSpinBox_4.value()
        analyst_result2 = self.doubleSpinBox_5.value()
        analyst_price = self.doubleSpinBox_6.value()
        date = datetime.datetime.now()
        self.cur.execute(
            ''' UPDATE  addanalyst SET name=%s,default_result1=%s,default_result2=%s,price=%s,category=%s,date=%s ''',
            (analyst_name, analyst_result1, analyst_result2, analyst_result_category, analyst_price, date))
        self.db.commit()
        self.Add_Data_To_history(4, 2)
        self.History()

    def Delete_Analyst(self):

        warning = QMessageBox.warning(self, 'احذر', "هل انت متأكد من انك تريد مسح التحليل",
                                      QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes:
            analyst_current_name = self.comboBox_21.currentText()
            sql = ''' DELETE FROM addanalyst WHERE name=%s '''
            self.cur.execute(sql, [(analyst_current_name)])
            self.Show_all_analysts_in_combo()
        self.Add_Data_To_history(5, 2)
        self.History()

    def Show_all_analysts_in_combo(self):
        self.cur.execute(''' SELECT name FROM addanalyst ''')
        data = self.cur.fetchall()
        for item in data:
            self.comboBox_21.addItem(str(item[0]))

    def Clients_Page(self):
        id = self.spinBox_2.value()
        self.cur.execute(''' SELECT client_name,client_age,client_genus,client_doctor FROM addclient WHERE id=%s''',
                         (str(id),))
        client_data = self.cur.fetchall()
        self.cur.execute(
            ''' SELECT total_price,analyst_name,analyst_result,client_name FROM addnewitem WHERE client_id=%s''',
            (str(id),))
        client_analyst_data = self.cur.fetchall()
        print(client_analyst_data)
        num = 0
        all_client_analyst = []
        for i in client_analyst_data:
            total = 0
            num += 1
            for k in range(0, num):
                total += int(client_analyst_data[k][0])
        for j in range(0, num):
            all_client_analyst.append(str(client_analyst_data[j][1]))

        for row, form in enumerate(client_data):

            for col, item in enumerate(form):
                self.tableWidget_4.setItem(row, 4, QTableWidgetItem(str(num)))
                self.tableWidget_4.setItem(row, 5, QTableWidgetItem(str(all_client_analyst)))
                self.tableWidget_4.setItem(row, 6, QTableWidgetItem(str(total)))
                self.tableWidget_4.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1

            row_pos = self.tableWidget_4.rowCount()
            self.tableWidget_4.insertRow(row_pos)

        for row, form in enumerate(client_analyst_data):

            for col, item in enumerate(form):
                if col == 0:
                    self.tableWidget_9.setItem(row, col, QTableWidgetItem(str(client_analyst_data[0][3])))
                if col == 1:
                    self.tableWidget_9.setItem(row, col, QTableWidgetItem(str(client_analyst_data[row][1])))
                if col == 2:
                    self.tableWidget_9.setItem(row, col, QTableWidgetItem(str(client_analyst_data[row][2])))
                col += 1

            row_pos = self.tableWidget_9.rowCount()
            self.tableWidget_9.insertRow(row_pos)
        self.Add_Data_To_history(6, 5)
        self.History()

    def Add_Buys(self):
        item_name = self.lineEdit_13.text()
        item_type = self.comboBox_6.currentText()
        quantity = self.spinBox_3.value()
        quantity_avaliable = quantity
        signal_item_price = self.lineEdit_12.text()
        total_item_price = self.lineEdit_11.text()
        date_create_before = self.dateEdit.date()
        date_create = str(date_create_before.toPyDate())
        self.cur.execute(
            ''' INSERT INTO addbuys (item_name,signal_item_price,total_price,buys_type,quantity,date) VALUES (%s,%s,%s,%s,%s,%s)'''
            , (item_name, signal_item_price, total_item_price, item_type, quantity, date_create))
        self.db.commit()
        self.Show_all_buys()
        self.Add_Data_To_history(3, 4)
        self.History()

    def Show_all_buys(self):
        self.cur.execute(''' SELECT item_name,buys_type,quantity,signal_item_price,total_price,date FROM addbuys ''')
        data = self.cur.fetchall()
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.insertRow(0)
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget_3.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            row_pos = self.tableWidget_3.rowCount()
            self.tableWidget_3.insertRow(row_pos)

    def Add_Data_To_history(self, action, table):
        global user_id
        self.cur.execute(
            ''' INSERT INTO his VALUES (DEFAULT,%s,%s,%s,%s,%s)''', (user_id, action, table, datetime.datetime.now(),1))
        self.db.commit()

    def History(self):
        self.cur.execute('''SELECT * FROM his ORDER BY -dates''')
        analyst_data = self.cur.fetchall()
        self.tableWidget_8.setRowCount(0)
        self.tableWidget_8.insertRow(0)
        for row, form in enumerate(analyst_data):
            for col, item in enumerate(form):
                if col == 0:
                    sql = '''SELECT uid FROM his WHERE id =%s'''
                    self.cur.execute(sql, [item])
                    data = self.cur.fetchone()
                    sql = '''SELECT user_name FROM adduser WHERE id =%s'''
                    self.cur.execute(sql, [data[0]])
                    user_name = self.cur.fetchone()
                    print(user_name)
                    self.tableWidget_8.setItem(row, col, QTableWidgetItem(str(user_name)))
                if col == 1:
                    print(item, '')
                    action = ''
                    if analyst_data[row][2] == 1:
                        action = 'تسجيل الدخول'
                    if analyst_data[0][2] == 2:
                        action = 'تسجيل الخروج'
                    if analyst_data[row][2] == 3:
                        action = 'اضافة'
                    if analyst_data[row][2] == 4:
                        action = 'تعديل'
                    if analyst_data[row][2] == 5:
                        action = 'حذف'
                    if analyst_data[row][2] == 6:
                        action = 'بحث'
                    if analyst_data[row][2] == 7:
                        action = 'طباعة'
                    self.tableWidget_8.setItem(row, col, QTableWidgetItem(str(action)))
                if col == 2:
                    tables = ''
                    print(item)
                    if analyst_data[row][3] == 1:
                        tables = 'مبيع يومي'
                    if analyst_data[row][3] == 2:
                        tables = 'تحليل'
                    if analyst_data[row][3] == 3:
                        tables = 'مشتريات'
                    if analyst_data[row][3] == 4:
                        tables = 'مراجعين'
                    self.tableWidget_8.setItem(row, col, QTableWidgetItem(str(tables)))
                if col == 3:
                    self.tableWidget_8.setItem(row, col, QTableWidgetItem(str(analyst_data[row][4])))

                col += 1
            row_pos = self.tableWidget_8.rowCount()
            self.tableWidget_8.insertRow(row_pos)

    # def Show_avaliable_quantity(self):
    #     self.cur.execute(''' SELECT quantity FROM addbuys WHERE ''')
    #     quantity_avaliable = 0
    #     if quantity_avaliable < 1:
    #         date_quantity_ended = datetime.datetime.now()
    #         self.cur.execute(''' UPDATE addbuys SET quantity_avaliable=%s,date_ended=%s''',
    #                          (quantity_avaliable, date_quantity_ended))
    def Log_In_Chieck(self):
        global user_id
        user_name = self.lineEdit.text()
        user_password = self.lineEdit_2.text()
        self.cur.execute(''' SELECT * FROM adduser ''')
        data = self.cur.fetchall()
        for row in data:
            if row[1] == user_name and row[2] == user_password:
                user_id = row[0]
                print('gg')
        print(data)

    def Delete_All_History_Data(self):
        sql = ''' DELETE FROM his WHERE def=%s'''
        self.cur.execute(sql,[(1)])
        QMessageBox.information(self, 'info', 'تم حذف محتويات السجل بنجاح')

    def Open_Sales_Page(self):
        self.tabWidget.setCurrentIndex(3)

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
        self.Show_All_The_Analysts()

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
