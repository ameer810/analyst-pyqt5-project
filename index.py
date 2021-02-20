import datetime
import sys

import MySQLdb
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from docx import *
from shutil import copyfile
from docx.shared import Pt

FORM_CLASS, _ = loadUiType("design.ui")
user_id = 4
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
        self.db = MySQLdb.connect(host='localhost', user='root', password='12345', db='tahlel', charset="utf8",
                                  use_unicode=True, port=3308)
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
        self.pushButton_18.clicked.connect(self.Print_Sale_Data)
        self.pushButton_19.clicked.connect(self.Search_In_All_Sales)
        self.pushButton_21.clicked.connect(self.Search_In_History)

    def Show_All_Clients(self):
        self.cur.execute(''' SELECT * FROM addclient ''')
        data = self.cur.fetchone()
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.insertRow(0)
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            row_pos = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_pos)

    def Search_In_History(self):
        actionsd = self.comboBox_24.currentIndex()
        tabley = self.comboBox_20.currentIndex()
        # action = 0
        # if actions == 'تسجيل الدخول':
        #     action = 1
        # if actions == 'تسجيل الخروج':
        #     action = 2
        # if actions == 'اضافة':
        #     action = 3
        # if actions == 'تعديل':
        #     action = 4
        # if actions == 'حذف':
        #     action = 5
        # if actions == 'بحث':
        #     action = 6
        # if actions == 'طباعة':
        #     action = 7
        # tables = 0
        # if table == 'مبيع يومي':
        #     tables = 1
        # if table == 'تحليل':
        #     tables = 2
        # if table == 'مشتريات':
        #     tables = 3
        # if table == 'مراجعين':
        #     tables = 4

        if actionsd != 0 and tabley == 0:
            try:
                self.cur.execute(f'SELECT action,tabled,id,dates FROM history WHERE action = {actionsd}')
            except Exception as e:
                print(e)
        if tabley != 0 and actionsd == 0:
            try:
                self.cur.execute(f'SELECT action,tabled,id,dates FROM history WHERE tabled={tabley}')
            except Exception as e:
                print(e)
        if actionsd != 0 and tabley != 0:
            try:
                self.cur.execute(
                    f' SELECT action,tabled,id,dates FROM history WHERE action={actionsd} AND tabled={tabley} ')

            except Exception as e:
                print(e)
        data = self.cur.fetchall()
        self.tableWidget_8.setRowCount(0)
        self.tableWidget_8.insertRow(0)
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                if col == 0:
                    sql = '''SELECT uid FROM history WHERE id =%s'''
                    self.cur.execute(sql, [data[row][2]])
                    datas = self.cur.fetchone()
                    sql = '''SELECT user_name FROM adduser WHERE id =%s'''
                    self.cur.execute(sql, [datas[0]])
                    user_name = self.cur.fetchone()
                    self.tableWidget_8.setItem(row, col, QTableWidgetItem(str(user_name[0])))
                if col == 1:
                    action = ''
                    if data[row][0] == 1:
                        action = 'تسجيل الدخول'
                    if data[0][0] == 2:
                        action = 'تسجيل الخروج'
                    if data[row][0] == 3:
                        action = 'اضافة'
                    if data[row][0] == 4:
                        action = 'تعديل'
                    if data[row][0] == 5:
                        action = 'حذف'
                    if data[row][0] == 6:
                        action = 'بحث'
                    if data[row][0] == 7:
                        action = 'طباعة'
                    self.tableWidget_8.setItem(row, col, QTableWidgetItem(str(action)))
                if col == 2:
                    tables = ''
                    print(item)
                    if data[row][1] == 1:
                        tables = 'مبيع يومي'
                    if data[row][1] == 2:
                        tables = 'تحليل'
                    if data[row][1] == 3:
                        tables = 'مشتريات'
                    if data[row][1] == 4:
                        tables = 'مراجعين'
                    if data[row][1] == 5:
                        tables = 'مستخدم'
                    self.tableWidget_8.setItem(row, col, QTableWidgetItem(str(tables)))
                if col == 3:
                    self.tableWidget_8.setItem(row, col, QTableWidgetItem(str(data[row][3])))

                col += 1
            row_pos = self.tableWidget_8.rowCount()
            self.tableWidget_8.insertRow(row_pos)

    def Search_In_All_Sales(self):
        client_name = self.lineEdit_25.text()
        if client_name != '0':
            self.cur.execute(''' SELECT * FROM addclient WHERE client_name=%s ORDER BY -date''', (client_name,))
        else:
            self.cur.execute(''' SELECT * FROM addclient ORDER BY -date''')
        analyst_data = self.cur.fetchall()
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_6.insertRow(0)
        for row, form in enumerate(analyst_data):
            for col, item in enumerate(form):
                if col == 3:
                    self.tableWidget_6.setItem(row, col, QTableWidgetItem(str(analyst_data[row][4])))
                else:
                    self.tableWidget_6.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            row_pos = self.tableWidget_6.rowCount()
            self.tableWidget_6.insertRow(row_pos)
        self.Add_Data_To_history(6, 1)

    def Print_Sale_Data(self):
        all_analyst = []
        all_result = []
        date = datetime.datetime.now()
        day = date.year
        month = date.month
        year = date.day
        word_type = []
        for row in range(0, self.tableWidget_5.rowCount() - 1):
            real_name = self.tableWidget_5.item(row, 0).text()
            analyst = self.tableWidget_5.item(row, 1).text()
            self.cur.execute(''' SELECT sub_category FROM addanalyst WHERE name=%s ''', (analyst,))
            all_analyst.append(str(analyst))
            data = self.cur.fetchone()
            for item in data:
                word_type.append(data[0])
            result = self.tableWidget_5.item(row, 2).text()
            all_result.append(str(result))
            real_doctor = self.tableWidget_5.item(row, 3).text()
        print(word_type)
        self.Bio_Word(real_name, real_doctor, all_analyst, all_result, year, month, day, word_type)

    def get_total_price(self):
        total_price = 0
        for row in range(0, self.tableWidget_5.rowCount() - 1):
            a = self.tableWidget_5.item(row, 4).text()
            print(a, 'kk')
            try:
                total_price += int(a)
            except ValueError:
                a = 0
        print(total_price)
        self.lineEdit_24.setText(str(total_price))

    def Sales_Page(self):
        global client_id_glob
        global chick_if_add_new
        analyst_name = self.comboBox_16.currentText()

        client_name = self.lineEdit_20.text()
        client_age = self.spinBox_7.value()
        client_genus = self.comboBox_14.currentText()
        client_doctor = self.comboBox_15.currentText()
        client_genus = self.comboBox_14.currentText()

        analyst_or_clients_notes = self.textEdit.toPlainText()
        analyst_lineEdit_result = self.lineEdit_21.text()
        analyst_combo_result = self.comboBox_17.currentText()
        analyst_number_result = self.spinBox_8.value()
        client_id = self.spinBox.value()
        latest_result = 1
        self.cur.execute('''
           INSERT INTO addclient (client_name,client_age,client_genus,client_doctor,date)
           VALUES (%s,%s,%s,%s,%s)
        ''', (str(client_name), str(client_age), str(client_genus), str(client_doctor), str(datetime.datetime.now())))
        self.db.commit()
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
        self.Show_All_The_Sales()
        # self.Show_All_one_client_analyst()
        self.Add_Data_To_history(3, 1)
        self.History()
        # client_name = self.lineEdit_20.setText('')
        # client_age = self.spinBox_7.setValue(0)
        # client_genus = self.comboBox_14.setCurrentIndex(0)
        # client_doctor = self.comboBox_15.setCurrentIndex(0)
        # analyst_name = self.comboBox_16.setCurrentIndex(0)
        # analyst_or_clients_notes = self.textEdit.setPlainText('')
        # analyst_lineEdit_result = self.lineEdit_21.setText('')
        # analyst_combo_result = self.comboBox_17.setCurrentIndex(0)
        # analyst_number_result = self.spinBox_8.setValue(0)
        # client_id = self.spinBox.setValue(0)
        self.Show_All_one_client_analyst()

    def Show_All_one_client_analyst(self):
        global client_id_glob
        global chick_if_add_new
        client_name = self.lineEdit_20.text()
        self.cur.execute('''
             SELECT client_name,analyst_name,analyst_result,doctor_name FROM addnewitem WHERE client_name = %s
        ''', (client_name,))
        analyst_data = self.cur.fetchall()
        print('start')
        print('start2')
        self.cur.execute('''
                     SELECT client_name,analyst_name,analyst_result,doctor_name,client_id,client_age,genus,notes FROM addnewitem WHERE client_id = %s
                ''', (self.spinBox.value(),))
        analyst_data = self.cur.fetchall()
        print(analyst_data)
        # need doctor name enabled i will make it with current text
        if self.spinBox.value() == 0 and chick_if_add_new == False:
            print('kosy')
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
        if self.spinBox.value() != 0:
            try:
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
                if client_id_glob == 0:
                    print('start3')
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
                chick_if_add_new = False
                self.Show_All_The_Sales()

            except IndexError:
                QMessageBox.information(self, 'Error',
                                        'الرقم الذي ادخلته غير صحيح يرجى ادخال رقم صحيح او مراجعة صفحة "كل المبيعات" للتأكد من الرقم')

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
                if col == 3:
                    self.tableWidget_6.setItem(row, col, QTableWidgetItem(str(analyst_data[row][4])))
                else:
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
        sub_category = self.comboBox_23.currentText()
        date = datetime.datetime.now()
        self.cur.execute(
            ''' INSERT INTO addanalyst (name,default_result1,default_result2,price,category,sub_category,date) VALUES(%s,%s,%s,%s,%s,%s,%s) ''',
            (
                analyst_name, analyst_result1, analyst_result2, analyst_result_category, analyst_price, sub_category,
                date))
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
        sub_category = self.comboBox_26.currentText()
        date = datetime.datetime.now()
        self.cur.execute(
            ''' UPDATE  addanalyst SET name=%s,default_result1=%s,default_result2=%s,price=%s,category=%s,sub_category=%s,date=%s ''',
            (
                analyst_name, analyst_result1, analyst_result2, analyst_result_category, sub_category, analyst_price,
                date))
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
            ''' INSERT INTO history VALUES (DEFAULT,%s,%s,%s,%s,%s)''',
            (user_id, action, table, datetime.datetime.now(), 1))
        self.db.commit()

    def History(self):
        self.cur.execute('''SELECT * FROM history ORDER BY -dates''')
        analyst_data = self.cur.fetchall()
        self.tableWidget_8.setRowCount(0)
        self.tableWidget_8.insertRow(0)
        for row, form in enumerate(analyst_data):
            for col, item in enumerate(form):
                if col == 0:
                    sql = '''SELECT uid FROM history WHERE id =%s'''
                    self.cur.execute(sql, [item])
                    data = self.cur.fetchone()
                    sql = '''SELECT user_name FROM adduser WHERE id =%s'''
                    self.cur.execute(sql, [data[0]])
                    user_name = self.cur.fetchone()
                    print(user_name)
                    self.tableWidget_8.setItem(row, col, QTableWidgetItem(str(user_name[0])))
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
                    if analyst_data[row][3] == 5:
                        tables = 'مستخدم'
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
        self.Add_Data_To_history(1, 5)
        self.History()

    def Delete_All_History_Data(self):
        sql = ''' DELETE FROM history WHERE def=%s'''
        self.cur.execute(sql, [(1)])
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

    def Bio_Word(self, name, doctor, analysts, results, year, month, day, word_types):
        for word_type in word_types:
            if word_type == 'bio':
                f = open('word/bio latest17.docx', 'rb')
                f.read()
                document = Document(f)
                for i in document.tables:
                    for k in i.rows:
                        for j in k.cells:
                            for n in j.paragraphs:
                                if n.text == 'أسـم المريض :       المحترم':
                                    n.text = f'أسـم المريض :{name}       المحترم'
                                    n.style.font.name = 'Monotype Koufi'
                                    n.style.font.bold = True
                                    n.style.font.size = Pt(11)
                                if n.text == 'حضرة الدكتور   :       المحترم':
                                    n.text = f'حضرة الدكتور   : {doctor}      المحترم'
                                    n.style.font.name = 'Monotype Koufi'
                                    n.style.font.bold = True
                                    n.style.font.size = Pt(11)

                                if n.text == 'Random  blood sugar :':
                                    print('okkkkkkkkkkkk')
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Random  blood sugar':
                                            k = analyst_and_result['result']
                                            n.text = f'Random  blood sugar : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(11)
                                if n.text == 'Blood Urea               :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Blood Urea':
                                            k = analyst_and_result['result']

                                            n.text = f'Blood Urea               : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(11)
                                if n.text == 'S. Creatinin               :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'S. Creatinin':
                                            k = analyst_and_result['result']
                                            n.text = f'S. Creatinin               : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(11)
                                if n.text == 'S. Uric acid                  :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'S. Uric acid':
                                            k = analyst_and_result['result']
                                            n.text = f'S. Uric acid                  : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(11)
                                if n.text == 'S. Cholesterol            :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'S. Cholesterol':
                                            k = analyst_and_result['result']
                                            n.text = f'S. Cholesterol            : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(11)
                                if n.text == 'S. Triglycerid             :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'S. Triglycerid':
                                            k = analyst_and_result['result']
                                            n.text = f'S. Triglycerid             : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(11)
                                if n.text == 'Total serum Bilirubin:':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Total serum Bilirubin':
                                            k = analyst_and_result['result']
                                            n.text = f'Total serum Bilirubin: {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(11)
                                if n.text == 'S.Calcium :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'S.Calcium':
                                            k = analyst_and_result['result']
                                            n.text = f'S.Calcium : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(11)
                                if n.text == 'Vitamin D              :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Vitamin D':
                                            k = analyst_and_result['result']
                                            n.text = f'Vitamin D              : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(11)

                                if n.text == 'Date:    /     / 20':
                                    n.text = f'Date:   {day} /  {month} / {year}'
                                    n.style.font.name = 'Tahoma'
                                    n.style.font.bold = True
                                    n.style.font.size = Pt(11)
                document.save('word/bio latest17.docx')
                f.close()
            if word_type == 'GSE':
                f = open('word/GSE latest.docx', 'rb')
                f.read()

                document = Document(f)
                for i in document.tables:
                    for k in i.rows:
                        for j in k.cells:
                            for n in j.paragraphs:
                                if n.text == 'أسـم المريض :       المحترم':
                                    n.text = f'أسـم المريض :{name}       المحترم'
                                    n.style.font.name = 'Monotype Koufi'
                                    n.style.font.bold = True
                                    n.style.font.size = Pt(11)
                                if n.text == 'حضرة الدكتور   :       المحترم':
                                    n.text = f'حضرة الدكتور   : {doctor}      المحترم'
                                    n.style.font.name = 'Monotype Koufi'
                                    n.style.font.bold = True
                                    n.style.font.size = Pt(11)
                                if n.text == 'Color:':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Color':
                                            k = analyst_and_result['result']
                                            n.text = f'Color: {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(14)
                                if n.text == 'Consistency:':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Consistency':
                                            k = analyst_and_result['result']
                                            n.text = f'Consistency: {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(14)
                                if n.text == 'R.B.Cs:':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'R.B.Cs':
                                            k = analyst_and_result['result']
                                            n.text = f'R.B.Cs:: {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(14)
                                if n.text == 'Pus cells:':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Pus cells':
                                            k = analyst_and_result['result']
                                            n.text = f'Pus cells: {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(14)
                                if n.text == 'E. Histolytica:':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'E. Histolytica':
                                            k = analyst_and_result['result']
                                            n.text = f'E. Histolytica: {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(14)
                                if n.text == 'G. Lembilia:':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'G. Lembilia':
                                            k = analyst_and_result['result']
                                            n.text = f'G. Lembilia: {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(14)
                                if n.text == 'Ova:':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Ova':
                                            k = analyst_and_result['result']
                                            n.text = f'Ova: {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(14)
                                if n.text == 'Other:':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Other':
                                            k = analyst_and_result['result']
                                            n.text = f'Other: {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(14)
                                if n.text == 'Date:    /     / 20':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }

                                if n.text == 'Date:    /     / 20':
                                    n.text = f'Date:   {day} /  {month} / {year}'
                                    n.style.font.name = 'Tahoma'
                                    n.style.font.bold = True
                                    n.style.font.size = Pt(12)
                document.save('word/GSE latest.docx')
                f.close()
            if word_type == 'GUE':

                f = open('word/GUE latest.docx', 'rb')
                f.read()

                document = Document(f)
                for i in document.tables:
                    for k in i.rows:
                        for j in k.cells:
                            for n in j.paragraphs:
                                if n.text == 'أسـم المريض :       المحترم':
                                    n.text = f'أسـم المريض :{5}       المحترم'
                                    n.style.font.name = 'Monotype Koufi'
                                    n.style.font.bold = True
                                    n.style.font.size = Pt(11)
                                if n.text == 'حضرة الدكتور   :       المحترم':
                                    n.text = f'حضرة الدكتور   : {5}      المحترم'
                                    n.style.font.name = 'Monotype Koufi'
                                    n.style.font.bold = True
                                    n.style.font.size = Pt(11)
                                if n.text == 'Appearance :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Appearance':
                                            k = analyst_and_result['result']
                                            n.text = f'Appearance : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.size = Pt(14)
                                if n.text == 'Reaction      :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Reaction':
                                            k = analyst_and_result['result']
                                            n.text = f'Reaction      : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.size = Pt(14)
                                if n.text == 'Albumin       :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Albumin':
                                            k = analyst_and_result['result']
                                            n.text = f'Albumin       : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.size = Pt(14)
                                if n.text == 'Sugar          :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Sugar':
                                            k = analyst_and_result['result']
                                            n.text = f'Sugar          : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.size = Pt(14)
                                if n.text == 'RBCs         :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'RBCs':
                                            k = analyst_and_result['result']
                                            n.text = f'RBCs         : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.size = Pt(14)
                                if n.text == 'Pus cells    :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Pus cells':
                                            k = analyst_and_result['result']
                                            n.text = f'Pus cells    : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.size = Pt(14)
                                if n.text == 'Epith .cells :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Epith .cells':
                                            k = analyst_and_result['result']
                                            n.text = f'Epith .cells : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.size = Pt(14)
                                if n.text == 'Crystals     :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Crystals':
                                            k = analyst_and_result['result']
                                            n.text = f'Crystals     : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.size = Pt(14)
                                if n.text == 'Casts        :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Casts':
                                            k = analyst_and_result['result']
                                            n.text = f'Casts        : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.size = Pt(14)
                                if n.text == 'Other        :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Other':
                                            k = analyst_and_result['result']
                                            n.text = f'Other        : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.size = Pt(14)
                                if n.text == 'Date:    /     / 20':
                                    n.text = f'Date:   {day} /  {month} / {year}'
                                    n.style.font.name = 'Tahoma'
                                    n.style.font.bold = True
                                    n.style.font.size = Pt(14)
                document.save('word/GUE latest.docx')
                f.close()
            if word_type=='hematology':
                f = open('word/hematology latest.docx', 'rb')
                f.read()

                document = Document(f)
                for i in document.tables:
                    for k in i.rows:
                        for j in k.cells:
                            for n in j.paragraphs:
                                if n.text == 'أسـم المريض :       المحترم':
                                    n.text = f'أسـم المريض :{5}       المحترم'
                                    n.style.font.name = 'Monotype Koufi'
                                    n.style.font.bold = True
                                    n.style.font.size = Pt(11)
                                if n.text == 'حضرة الدكتور   :       المحترم':
                                    n.text = f'حضرة الدكتور   : {5}      المحترم'
                                    n.style.font.name = 'Monotype Koufi'
                                    n.style.font.bold = True
                                    n.style.font.size = Pt(11)
                                if n.text == 'Hb             :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Hb':
                                            k = analyst_and_result['result']
                                            n.text = f'Hb             : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(14)
                                if n.text == 'PCV           :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'PCV':
                                            k = analyst_and_result['result']
                                            n.text = f'PCV           : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(14)
                                if n.text == 'WBCs         :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'WBCs':
                                            k = analyst_and_result['result']
                                            n.text = f'WBCs         : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(14)
                                if n.text == 'E.S.R          :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'E.S.R':
                                            k = analyst_and_result['result']
                                            n.text = f'E.S.R          : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(14)
                                if n.text == 'Blood Group:':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Blood Group':
                                            k = analyst_and_result['result']
                                            n.text = f'Blood Group: {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(14)
                                if n.text == 'Rh:':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Rh':
                                            k = analyst_and_result['result']
                                            n.text = f'Rh: {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(14)
                                if n.text == 'Pregnancy test  in urine   :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Pregnancy test  in urine':
                                            k = analyst_and_result['result']
                                            n.text = f'Pregnancy test  in urine   : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(14)
                                if n.text == 'Pregnancy test  in serum  :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Pregnancy test  in serum':
                                            k = analyst_and_result['result']
                                            n.text = f'Pregnancy test  in serum  : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(14)
                                if n.text == 'R.B.Sugar                           :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'R.B.Sugar':
                                            k = analyst_and_result['result']
                                            n.text = f'R.B.Sugar                           : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(14)
                                if n.text == 'Bl. Urea                              :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Bl. Urea':
                                            k = analyst_and_result['result']
                                            n.text = f'Bl. Urea                              : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(14)
                                if n.text == 'Salmonella typhi  IgG :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Salmonella typhi  IgG':
                                            k = analyst_and_result['result']
                                            n.text = f'Salmonella typhi  IgG : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(14)
                                if n.text == 'Salmonella typhi  IgM :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Salmonella typhi  IgM':
                                            k = analyst_and_result['result']
                                            n.text = f'Salmonella typhi  IgM : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(14)
                                if n.text == 'Rose-Bengal test   :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Rose-Bengal test':
                                            k = analyst_and_result['result']
                                            n.text = f'Rose-Bengal test   : {k}'
                                            n.style.font.name = 'Tahoma'
                                            n.style.font.bold = True
                                            n.style.font.size = Pt(14)
                                if n.text == 'Date:    /     / 20':
                                    n.text = f'Date:   {day} /  {month} / {year}'
                                    n.style.font.name = 'Tahoma'
                                    n.style.font.bold = True
                                    n.style.font.size = Pt(14)
                document.save('word/hematology latest.docx')
                f.close()
            if word_type=='هرمونات مشترك':
                f = open('word/مختبر بغـداد.docx', 'rb')
                f.read()

                document = Document(f)

                for i in document.tables:
                    for k in i.rows:
                        for j in k.cells:

                            for n in j.paragraphs:
                                if n.text == '     أســم الـمــريــض    :':
                                    n.text = f'     أســم الـمــريــض    :{name}'
                                    n.style.font.name = 'Monotype Koufi'
                                    n.style.font.bold = True
                                    n.style.font.size = Pt(14)
                                if n.text == 'حـضـرة الـدكتـور    الـفاضـــل :                                                                                            الـمـحـتـرم':
                                    n.text = f'حـضـرة الـدكتـور    الـفاضـــل :{doctor}                                                                                            الـمـحـتـرم'
                                    n.style.font.name = 'Monotype Koufi'
                                    n.style.font.bold = True
                                    n.style.font.size = Pt(14)
                                if n.text == '0r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Toxoplasma IgG':
                                            k = analyst_and_result['result']
                                        n.text = f'  {5}'
                                        n.style.font.name = 'Tahoma'
                                        n.style.font.bold = True
                                        n.style.font.size = Pt(12)
                                if n.text == '1r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Toxoplasma IgM':
                                            k = analyst_and_result['result']
                                        n.text = f'  {5}'
                                        n.style.font.name = 'Tahoma'
                                        n.style.font.bold = True
                                        n.style.font.size = Pt(12)
                                if n.text == '2r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Cytomegalo Virus IgG':
                                            k = analyst_and_result['result']
                                        n.text = f'  {5}'
                                        n.style.font.name = 'Tahoma'
                                        n.style.font.bold = True
                                        n.style.font.size = Pt(12)
                                if n.text == '3r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Cytomegalo Virus IgM':
                                            k = analyst_and_result['result']
                                        n.text = f'  {5}'
                                        n.style.font.name = 'Tahoma'
                                        n.style.font.bold = True
                                        n.style.font.size = Pt(12)
                                if n.text == '4r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Rubella IgG':
                                            k = analyst_and_result['result']
                                        n.text = f'  {5}'
                                        n.style.font.name = 'Tahoma'
                                        n.style.font.bold = True
                                        n.style.font.size = Pt(12)
                                if n.text == '5r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Rubella IgM':
                                            k = analyst_and_result['result']
                                        n.text = f'  {5}'
                                        n.style.font.name = 'Tahoma'
                                        n.style.font.bold = True
                                        n.style.font.size = Pt(12)
                                if n.text == '6r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Anti - Phspholipin IgG':
                                            k = analyst_and_result['result']
                                        n.text = f'  {5}'
                                        n.style.font.name = 'Tahoma'
                                        n.style.font.bold = True
                                        n.style.font.size = Pt(12)
                                if n.text == '7r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Anti - Phspholipin  IgM':
                                            k = analyst_and_result['result']
                                        n.text = f'  {5}'
                                        n.style.font.name = 'Tahoma'
                                        n.style.font.bold = True
                                        n.style.font.size = Pt(12)
                                if n.text == '8r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Anti - Cardiolipin  IgG':
                                            k = analyst_and_result['result']
                                        n.text = f'  {5}'
                                        n.style.font.name = 'Tahoma'
                                        n.style.font.bold = True
                                        n.style.font.size = Pt(12)
                                if n.text == '9r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Anti - Cardiolipin  IgM':
                                            k = analyst_and_result['result']
                                        n.text = f'  {5}'
                                        n.style.font.name = 'Tahoma'
                                        n.style.font.bold = True
                                        n.style.font.size = Pt(12)
                                if n.text == '10r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Herps   IgG':
                                            k = analyst_and_result['result']
                                        n.text = f'  {5}'
                                        n.style.font.name = 'Tahoma'
                                        n.style.font.bold = True
                                        n.style.font.size = Pt(12)
                                if n.text == '11r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Herpes  IgM':
                                            k = analyst_and_result['result']
                                        n.text = f'  {5}'
                                        n.style.font.name = 'Tahoma'
                                        n.style.font.bold = True
                                        n.style.font.size = Pt(12)
                                if n.text == 'Date:    /     / 20':
                                    n.text = f'Date:   {day} /  {month} / {year}'
                                    n.style.font.name = 'Tahoma'
                                    n.style.font.bold = True
                                    n.style.font.size = Pt(14)
                                print('1' + n.text + '2')
                document.save('word/مختبر بغـداد.docx')
                f.close()



def main():
    app = QApplication(sys.argv)
    window = mainapp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
