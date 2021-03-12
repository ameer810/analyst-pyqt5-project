import datetime
import os

import time
import MySQLdb
import pyautogui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys

from docx import *
# from shutil import copyfile
from docx.shared import Pt
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

from win32com import client
from pydesign import Ui_MainWindow as main_wind
FORM_CLASS, _ = loadUiType("design.ui")
user_id = 4
client_id_glob = 0
chick_if_add_new = False
if_print = False
analysts_name_glo = []
clients_name_glo = []


class mainapp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(mainapp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.tabWidget.tabBar().setVisible(False)
        self.DB_Connect()
        self.Delete_Files()
        self.handel_buttons()
        self.Show_All_The_Sales()
        self.Show_all_analysts_in_combo()
        # self.Show_all_buys()
        # self.History()
        self.Show_All_Clients()
        # self.groupBox.setEnabled(False)
        self.Show_paths()
        self.add_Analyst_to_list()
        self.Auto_complete_combo()
        self.add_client_to_list()
        self.Auto_complete_combo2()

    def DB_Connect(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='12345', db='tahlel', charset="utf8",
                                  use_unicode=True, port=3306)
        self.cur = self.db.cursor()

    def handel_buttons(self):
        self.pushButton_15.clicked.connect(self.Light_Blue_Theme)
        self.pushButton_9.clicked.connect(self.Dark_Orange_Theme)
        self.pushButton_13.clicked.connect(self.Dark_Blue_Theme)
        self.pushButton_14.clicked.connect(self.Dark_Theme)
        self.pushButton_11.clicked.connect(self.Dark_Gray_Theme)
        self.pushButton.clicked.connect(self.Open_Sales_Page)
        # self.pushButton_6.clicked.connect(self.Open_Login_Page)
        self.pushButton_4.clicked.connect(self.Open_Settings_Page)
        self.pushButton_12.clicked.connect(self.Open_Print_Page)
        # self.pushButton_3.clicked.connect(self.Open_History_Page)
        self.pushButton_5.clicked.connect(self.Open_clients_Page)
        # self.pushButton_2.clicked.connect(self.Open_Analyse_Page)
        # self.pushButton_8.clicked.connect(self.Open_ResetPassword_Page)
        self.pushButton_17.clicked.connect(self.Sales_Page)
        self.pushButton_30.clicked.connect(self.get_client_id)
        self.pushButton_31.clicked.connect(self.Chick_analyst_category)
        self.pushButton_32.clicked.connect(self.get_total_price)
        # self.pushButton_33.clicked.connect(self.Show_analyst_in_Edit_Or_Delete)
        self.pushButton_29.clicked.connect(self.Clients_Page)
        # self.pushButton_16.clicked.connect(self.Add_Buys)
        # self.pushButton_20.clicked.connect(self.Show_All_The_Analysts)
        # self.pushButton_27.clicked.connect(self.Edit_Analyst)
        # self.pushButton_7.clicked.connect(self.Log_In_Chieck)
        # self.pushButton_28.clicked.connect(self.Delete_Analyst)
        # self.pushButton_22.clicked.connect(self.Delete_All_History_Data)
        self.pushButton_18.clicked.connect(self.Print_Sale_Data)
        self.pushButton_19.clicked.connect(self.Search_In_All_Sales)
        # self.pushButton_21.clicked.connect(self.Search_In_History)
        self.pushButton_35.clicked.connect(self.clear_data_in_sales)
        # self.pushButton_10.clicked.connect(self.Reset_password)
        # self.pushButton_26.clicked.connect(self.Add_Analyst)
        self.pushButton_34.clicked.connect(self.Preview)
        self.pushButton_23.clicked.connect(self.Print_empty_papers)
        self.pushButton_24.clicked.connect(self.Add_Path)
        self.pushButton_36.clicked.connect(self.Show_All_Clients)

    def add_Analyst_to_list(self):
        self.cur.execute(''' SELECT name FROM addanalyst ''')
        data = self.cur.fetchall()
        for i in data:
            analysts_name_glo.append(i[0])

    def Auto_Complete(self, model):
        model.setStringList(analysts_name_glo)

    def Auto_complete_combo(self):
        combo = self.comboBox_16
        completer = QCompleter()
        combo.setCompleter(completer)
        model = QStringListModel()
        completer.setModel(model)
        self.Auto_Complete(model)

    def add_client_to_list(self):
        self.cur.execute(''' SELECT client_name FROM addclient ''')
        data = self.cur.fetchall()
        for i in data:
            clients_name_glo.append(i[0])

    def Auto_Complete2(self, model):
        model.setStringList(clients_name_glo)

    def Auto_complete_combo2(self):
        combo = self.lineEdit_25, self.lineEdit_27
        completer = QCompleter()
        for i in combo:
            i.setCompleter(completer)
            model = QStringListModel()
            completer.setModel(model)
            self.Auto_Complete2(model)

    def Delete_Files(self):
        self.cur.execute(''' SELECT * FROM paths WHERE id=1 ''')
        mydata = self.cur.fetchone()
        word_files = mydata[1]
        save_word_files = mydata[2]
        try:
            if os.path.exists(r'%s\bio latest17.docx' % save_word_files):
                os.remove(r'%s\bio latest17.docx' % save_word_files)

            if os.path.exists(r'%s\GSE latest.docx' % save_word_files):
                os.remove(r'%s\GSE latest.docx' % save_word_files)

            if os.path.exists(r'%s\SFA latest.docx' % save_word_files):
                os.remove(r'%s\SFA latest.docx' % save_word_files)

            if os.path.exists(r'%s\GUE latest.docx' % save_word_files):
                os.remove(r'%s\GUE latest.docx' % save_word_files)

            if os.path.exists(r'%s\hematology latest.docx' % save_word_files):
                os.remove(r'%s\hematology latest.docx' % save_word_files)

            if os.path.exists(r'%s\هرمونات مشترك latest' % save_word_files):
                os.remove(r'%s\هرمونات مشترك latest' % save_word_files)
        except:
            pass

    def Show_paths(self):
        self.cur.execute(''' SELECT * FROM paths WHERE id=1 ''')
        mydata = self.cur.fetchone()
        word_files = mydata[1]
        save_word_files = mydata[2]
        self.lineEdit_14.setText(word_files)
        self.lineEdit_15.setText(save_word_files)

    def Add_Path(self):
        files_path = self.lineEdit_14.text()
        save_files_path = self.lineEdit_15.text()
        self.cur.execute(''' UPDATE paths SET file_path=%s,save_file_path=%s WHERE id=1''',
                         (files_path, save_files_path))
        self.db.commit()
        QMessageBox.information(self, '', 'تم تطبيق المعلومات بنجاح')
        self.Show_paths()

    def Print_empty_papers(self):
        self.cur.execute(''' SELECT * FROM paths WHERE id=1 ''')
        mydata = self.cur.fetchone()
        word_files = mydata[1]
        save_word_files = mydata[2]
        paper_type = self.comboBox_27.currentIndex()
        copyes_num = self.spinBox_4.Value()
        word = client.Dispatch("Word.Application")

        category = ''
        file = ''
        if paper_type == 0:
            category = 'bio'
            file = 'bio org.docx'
        if paper_type == 1:
            category = 'GSE'
            file = 'GSE org.docx'
        if paper_type == 2:
            category = 'GUE'
            file = 'GUE org.docx'
        if paper_type == 3:
            category = 'hematology'
            file = 'hematology org.docx'
        if paper_type == 5:
            category = 'SFA'
            file = 'SFA org.docx'
        if paper_type == 4:
            category = 'هرمونات مشترك'
            file = 'هرمونات مشترك الاصلي.docx'
        QMessageBox.information(self, 'info', 'تتم الطباعة الان')
        word.Documents.Open(r'%s\%s' % (word_files, file))
        word.ActiveDocument.PrintOut(Copies=copyes_num)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(1.5)
        word.ActiveDocument.Close()

    def Preview(self):
        global if_print
        self.Print_Sale_Data('T')
        self.cur.execute(''' SELECT * FROM paths WHERE id=1 ''')
        mydata = self.cur.fetchone()
        word_files = mydata[1]
        save_word_files = mydata[2]
        warning = QMessageBox.warning(self, '',
                                      "هل قمت بطباعة جميع الملفات التي تمت معاينتها؟\n لا تضغط نعم الا لو قمت بطباعتها",
                                      QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes:
            warning2 = QMessageBox.warning(self, '',
                                           "قم باغلاق جميع نوافذ تطبيق microsoft word. هل قمت باغلاقها؟",
                                           QMessageBox.Yes | QMessageBox.No)
            if warning2 == QMessageBox.Yes:
                print('now delete')
                if_print = True
                print('its start')
                if os.path.exists(r'%s\bio latest17.docx' % save_word_files):
                    os.remove(r'%s\bio latest17.docx' % save_word_files)

                if os.path.exists(r'%s\GSE latest.docx' % save_word_files):
                    os.remove(r'%s\GSE latest.docx' % save_word_files)

                if os.path.exists(r'%s\SFA latest.docx' % save_word_files):
                    os.remove(r'%s\SFA latest.docx' % save_word_files)

                if os.path.exists(r'%s\GUE latest.docx' % save_word_files):
                    os.remove(r'%s\GUE latest.docx' % save_word_files)

                if os.path.exists(r'%s\hematology latest.docx' % save_word_files):
                    os.remove(r'%s\hematology latest.docx' % save_word_files)

                if os.path.exists(r'%s\هرمونات مشترك latest' % save_word_files):
                    os.remove(r'%s\هرمونات مشترك latest' % save_word_files)

    # def Reset_password(self):
    #     user_name = self.lineEdit_7.text()
    #     self.cur.execute(''' SELECT * FROM adduser ''')
    #     data = self.cur.fetchall()
    #     ruser_name = ''
    #     a = 0
    #     for row in data:
    #         if row[1] == user_name:
    #             ruser_name = row[1]
    #         else:
    #             a = 5
    #     if a == 5:
    #         QMessageBox.information(self, 'info', 'اسم المستخدم الذي ادخلته غير صحيح')
    #     self.cur.execute(''' SELECT user_email,userpassword FROM adduser WHERE user_name=%s ''', (ruser_name,))
    #     email_data = self.cur.fetchone()
    # email = "ameersaad810@gmail.com" # the email where you sent the email
    # password = "aahmpredtiddvxlo"
    # send_to_email = email_data[0] # for whom
    # subject = "n"
    # message = f'Hello.\n your password is {email_data[1]} '
    # msg = MIMEMultipart()
    # msg["From"] = email
    # msg["To"] = send_to_email
    # msg["Subject"] = subject
    #
    # msg.attach(MIMEText(message, 'plain'))
    #
    # server = smtplib.SMTP("smtp.gmail.com", 587)
    # server.starttls()
    # server.login(email, password)
    # text = msg.as_string()
    # server.sendmail(email, send_to_email, text)
    # server.quit()
    # print('ok')

    def clear_data_in_sales(self):
        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.insertRow(0)
        self.lineEdit_20.setText('')
        self.lineEdit_21.setText('')
        self.spinBox_7.setValue(0)
        self.doubleSpinBox_7.setValue(0)
        self.comboBox_14.setCurrentIndex(0)
        self.comboBox_16.setCurrentIndex(0)
        self.comboBox_17.setCurrentIndex(0)
        self.comboBox_15.setEnabled(True)
        self.comboBox_15.setCurrentIndex(0)
        self.textEdit.setPlainText('')
        self.lineEdit_20.setEnabled(True)
        self.spinBox_7.setEnabled(True)
        self.comboBox_14.setEnabled(True)
        self.textEdit.setEnabled(True)

    def Show_All_Clients(self):
        client_name = self.lineEdit_27.text()
        if client_name != '0':
            self.cur.execute(''' SELECT * FROM addclient WHERE client_name=%s ORDER BY id''', (client_name,))
        else:
            self.cur.execute(''' SELECT * FROM addclient ORDER BY -date''')
        analyst_data = self.cur.fetchall()
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.insertRow(0)
        try:
            if client_name != '0' and client_name != '':
                for i, k in enumerate(analyst_data[0]):
                    if i == 3:
                        self.tableWidget_2.setItem(0, i, QTableWidgetItem(str(analyst_data[0][4])))
                    else:
                        self.tableWidget_2.setItem(0, i, QTableWidgetItem(str(k)))
                    print('ok')
            else:
                self.Show_All_The_Sales()
        except:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)

    def Search_In_History(self):
        actionsd = self.comboBox_24.currentIndex()
        tabley = self.comboBox_20.currentIndex()
        if actionsd != 0 and tabley == 0:
            try:
                self.cur.execute(f'SELECT action,tabled,id,dates FROM his WHERE action = {actionsd}')
            except Exception as e:
                print(e)
        elif tabley != 0 and actionsd == 0:
            try:
                self.cur.execute(f'SELECT action,tabled,id,dates FROM his WHERE tabled={tabley}')
            except Exception as e:
                print(e)
        elif actionsd != 0 and tabley != 0:
            try:
                self.cur.execute(
                    f' SELECT action,tabled,id,dates FROM his WHERE action={actionsd} AND tabled={tabley} ')

            except Exception as e:
                print(e)
        else:
            try:
                self.cur.execute(
                    f' SELECT action,tabled,id,dates FROM his')

            except Exception as e:
                print(e)
        data = self.cur.fetchall()
        self.tableWidget_8.setRowCount(0)
        self.tableWidget_8.insertRow(0)
        for row, form in enumerate(data):
            for col, item in enumerate(form):
                if col == 0:
                    sql = '''SELECT uid FROM his WHERE id =%s'''
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
            self.cur.execute(''' SELECT * FROM addclient WHERE client_name=%s ORDER BY id''', (client_name,))
        else:
            self.cur.execute(''' SELECT * FROM addclient ORDER BY -date''')
        analyst_data = self.cur.fetchall()
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_6.insertRow(0)
        try:
            if client_name != '0' and client_name != '':
                for i, k in enumerate(analyst_data[0]):
                    if i == 3:
                        self.tableWidget_6.setItem(0, i, QTableWidgetItem(str(analyst_data[0][4])))
                    else:
                        self.tableWidget_6.setItem(0, i, QTableWidgetItem(str(k)))
                    print('ok')
            else:
                self.Show_All_The_Sales()
        except:
            self.tableWidget_6.setRowCount(0)
            self.tableWidget_6.insertRow(0)
        # self.Add_Data_To_history(6, 1)

    def Print_Sale_Data(self, prev):
        genuses = self.comboBox_14.currentIndex()
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
            if data != None:
                for item in data:
                    word_type.append(data[0])
            result = self.tableWidget_5.item(row, 2).text()
            all_result.append(str(result))
            real_doctor = self.tableWidget_5.item(row, 3).text()
        try:
            self.Bio_Word(real_name, real_doctor, all_analyst, all_result, year, month, day, word_type, prev, genuses)
        except Exception as e:
            print(e)
            QMessageBox.information(self, 'خطأ', 'هنالك خطأ يرجى مراجعة العملية')
        if prev != 'T':
            self.Delete_Files()

    def get_total_price(self):
        total_price = 0
        My_num=['Appearance','Reaction','Albumin','Sugar','RBCs:GUE','Pus cells:GUE','Epith .cells','Crystals','Casts','Other:GUE','Volume','Reaction','Colour:SFA','Liquefaction','Count','Motility:Active','Motility:Sluggish','Motility:Dead','Morphology:Normal','Morphology:Abnormal','Morphology:Pus cells','Other:SFA','Color:GSE','Consistency','E. Histolytica','G. Lembilia','Ova','Pus cells:GSE','R.B.Cs:GSE']
        rMy_num=0
        for row in range(0, self.tableWidget_5.rowCount() - 1):
            analyst_name= self.tableWidget_5.item(row, 1).text()
            for kg in My_num:
                if kg ==analyst_name:
                    total_price+=3
                    rMy_num+=1
            a = self.tableWidget_5.item(row, 4).text()
            try:
                total_price += int(a)
            except ValueError:
                a = 0
        for num in range(1,rMy_num-1):
            total_price-=3
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
        analyst_number_result = self.doubleSpinBox_7.value()
        client_id = self.spinBox.value()

        self.cur.execute('''SELECT price,category FROM addanalyst WHERE name = %s''', (analyst_name,))
        analyst_price = self.cur.fetchone()

        latest_result = 1
        total_price = 0
        if analyst_price != None:
            if analyst_price[1] == 'عدد':
                latest_result = analyst_number_result
            if analyst_price[1] == 'خيارات':
                latest_result = analyst_combo_result
            if analyst_price[1] == 'حقل كتابة':
                latest_result = analyst_lineEdit_result
            if analyst_price[1] == 'خيارات مع تعديل':
                latest_result = analyst_combo_result
            total_price = int(analyst_price[0])
        self.cur.execute('''
                   INSERT INTO addclient (client_name,client_age,client_genus,client_doctor,date)
                   VALUES (%s,%s,%s,%s,%s)
                ''', (
            str(client_name), str(client_age), str(client_genus), str(client_doctor), str(datetime.datetime.now())))
        self.db.commit()
        self.cur.execute('''SELECT id FROM addclient WHERE client_name = %s''', (client_name,))
        real_client_id = self.cur.fetchone()
        self.cur.execute('''
           INSERT INTO addnewitem (client_name,client_id,client_age,genus,doctor_name,notes,analyst_name,analyst_result,price,total_price,date)
           VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ''', (
            client_name, real_client_id, client_age, client_genus, client_doctor, analyst_or_clients_notes,
            analyst_name,
            latest_result,
            total_price, total_price, datetime.datetime.now()))
        self.db.commit()
        self.cur.execute(
            ''' SELECT client_name,analyst_name,analyst_result,doctor_name,total_price FROM addnewitem WHERE client_name = %s''',
            (self.lineEdit_20.text(),))
        analyst_data = self.cur.fetchall()

        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.insertRow(0)

        for row, form in enumerate(analyst_data):
            for col, item in enumerate(form):
                # if col==4:
                #     print(total_price,'here')
                # self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(total_price)))
                # else:
                self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            row_pos = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(row_pos)
        print('first')
        chick_if_add_new = True
        self.Show_All_The_Sales()
        # self.Show_All_one_client_analyst()
        # self.Add_Data_To_history(3, 1)
        # self.History()
        # client_name = self.lineEdit_20.setText('')
        # client_age = self.spinBox_7.setValue(0)
        # client_genus = self.comboBox_14.setCurrentIndex(0)
        # client_doctor = self.comboBox_15.setCurrentIndex(0)
        # analyst_name = self.comboBox_16.setCurrentIndex(0)
        # analyst_or_clients_notes = self.textEdit.setPlainText('')
        # analyst_lineEdit_result = self.lineEdit_21.setText('')
        # analyst_combo_result = self.comboBox_17.setCurrentIndex(0)
        # analyst_number_result = self.doubleSpinBox_7.setValue(0)
        # client_id = self.spinBox.setValue(0)
        # self.Show_All_one_client_analyst()

    def Show_All_one_client_analyst(self):
        global client_id_glob
        global chick_if_add_new
        client_name = self.lineEdit_20.text()
        self.cur.execute('''
             SELECT client_name,analyst_name,analyst_result,doctor_name FROM addnewitem WHERE client_name = %s
        ''', (client_name,))
        analyst_data = self.cur.fetchall()
        self.cur.execute('''
                     SELECT client_name,analyst_name,analyst_result,doctor_name,total_price,client_id,client_age,genus,notes FROM addnewitem WHERE client_id = %s
                ''', (self.spinBox.value(),))
        analyst_data = self.cur.fetchall()
        # need doctor name enabled i will make it with current text
        if self.spinBox.value() == 0 and chick_if_add_new == False:
            self.tableWidget_5.setRowCount(0)
            self.tableWidget_5.insertRow(0)
            self.lineEdit_20.setText('')
            self.lineEdit_21.setText('')
            self.spinBox_7.setValue(0)
            self.doubleSpinBox_7.setValue(0)
            self.comboBox_14.setCurrentIndex(0)
            self.comboBox_17.setCurrentIndex(0)
            self.textEdit.setPlainText('')
            self.lineEdit_20.setEnabled(True)
            self.spinBox_7.setEnabled(True)
            self.comboBox_14.setEnabled(True)
            self.textEdit.setEnabled(True)
        if self.spinBox.value() != 0:
            try:
                self.comboBox_15.setCurrentText(str(analyst_data[0][3]))
                self.comboBox_15.setEnabled(False)
                self.comboBox_14.setEnabled(False)
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
                self.textEdit.setPlainText(str(analyst_data[0][8]))
                self.textEdit.setEnabled(False)
                if client_id_glob == 0:
                    self.cur.execute('''SELECT client_name,analyst_name,analyst_result,doctor_name FROM addnewitem WHERE client_name = %s''', (self.lineEdit_20.text(),))
                    analyst_data = self.cur.fetchall()

                self.tableWidget_5.setRowCount(0)
                self.tableWidget_5.insertRow(0)

                for row, form in enumerate(analyst_data):
                    for col, item in enumerate(form):
                        self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(item)))
                        col += 1
                    row_pos = self.tableWidget_5.rowCount()
                    self.tableWidget_5.insertRow(row_pos)
                print('two')
                chick_if_add_new = False
                self.Show_All_The_Sales()

            except IndexError:
                QMessageBox.information(self, 'Error',
                                        'الرقم الذي ادخلته غير صحيح يرجى ادخال رقم صحيح او مراجعة صفحة "كل المبيعات" للتأكد من الرقم')

    def Chick_analyst_category(self):
        analyst_name = self.comboBox_16.currentText()
        self.cur.execute('''SELECT category FROM addanalyst WHERE name = %s''', (analyst_name,))
        analyst_category = self.cur.fetchone()
        try:
            if analyst_category[0] == 'عدد':
                self.comboBox_17.hide()
                self.lineEdit_21.hide()
                self.doubleSpinBox_7.show()
            if analyst_category[0] == 'خيارات':
                self.lineEdit_21.hide()
                self.doubleSpinBox_7.hide()
                self.comboBox_17.show()
                self.comboBox_17.setEditable(False)
            if analyst_category[0] == 'حقل كتابة':
                self.lineEdit_21.show()
                self.doubleSpinBox_7.hide()
                self.comboBox_17.hide()
            if analyst_category[0] == 'خيارات مع تعديل':
                self.lineEdit_21.hide()
                self.doubleSpinBox_7.hide()
                # self.comboBox_17.clear()
                self.comboBox_17.show()
                self.comboBox_17.setEditable(True)
        except:
            QMessageBox.information(self, 'تحذير', "يرجى اختيار تحليل صحيح")
        colors = ['yallow', 'brown', 'green', 'milk']
        RBCs_Pus_cells_GUE_GSE = ['1 - 2', '1 - 3', '2 - 3', '2 - 4', '0 - 1', '0 - 2', '3 - 5', '4 - 6', '5 - 6',
                                  '5 - 7', '6 - 8', '6 - 7', '+', '++', '+++', '++++', 'Full Field']
        Consistency = ['Solid', 'Liquid', 'Semi solid', 'Semi liquid', 'Mucoid']
        G_Lembilia_E_Histolytica = ['Cyst', 'Trophozoite']
        Epith_cells = ['Few', '+', '++', '+++', '++++']
        Ova = ['Nil']
        Appearance = ['Turbid', 'Clear']
        Reaction = ['Acidic', 'Alkaline']
        Sugar = ['Nil', '+', '++', '+++', 'Trace']
        Crystals = ['Am.Urate', 'Am.Phosphatase', 'Uric Acid', 'Ca.Oxalate']
        Casts = ['Granular cast +', 'Granular cast ++', 'Granular cast +++']
        Blood_Group = ['A (+ve)', 'B (+ve)', 'AB (+ve)', 'O (+ve)', 'O (-ve)', 'A (-ve)', 'B (-ve)', 'AB (-ve)']
        Pregnancy_test_in_urine_serum = ['Positive (+ve)', 'Negative (-ve)']
        test = ['Toxoplasma IgG', 'Toxoplasma IgM', 'Cytomegalo Virus IgG', 'Cytomegalo Virus IgM', 'Rubella IgG',
                'Rubella IgM', 'Anti - Phspholipin IgG', 'Anti - Phspholipin  IgM', 'Anti - Cardiolipin  IgG',
                'Anti - Cardiolipin  IgM', 'Herps   IgG', 'Herpes  IgM']
        test_choices = ['0.5 Negative', '0.6 Negative', '0.7 Negative', '0.8 Negative', '1.1 Positive', '1.1 Positive',
                        '1.2 Positive', '1.3 Positive', '1.4 Positive', '1.5 Positive']
        self.comboBox_17.clear()
        if analyst_name == 'Colour:SFA' or analyst_name == 'Color:GSE':
            for item in colors:
                self.comboBox_17.addItem(str(item))
        if analyst_name == 'R.B.Cs:GSE' or analyst_name == 'Pus cells:GSE' or analyst_name == 'RBCs:GUE' or analyst_name == 'Pus cells:GUE':
            for item0 in RBCs_Pus_cells_GUE_GSE:
                self.comboBox_17.addItem(str(item0))
        if analyst_name == 'Consistency':
            for item1 in Consistency:
                self.comboBox_17.addItem(str(item1))
        if analyst_name == 'E. Histolytica' or analyst_name == 'G. Lembilia':
            for item2 in G_Lembilia_E_Histolytica:
                self.comboBox_17.addItem(str(item2))
        if analyst_name == 'Ova':
            for item4 in Ova:
                self.comboBox_17.addItem(str(item4))
        if analyst_name == 'Appearance':
            for item5 in Appearance:
                self.comboBox_17.addItem(str(item5))
        if analyst_name == 'Reaction':
            for item6 in Reaction:
                self.comboBox_17.addItem(str(item6))
        if analyst_name == 'Sugar' or analyst_name == 'Albumin':
            for item7 in Sugar:
                self.comboBox_17.addItem(str(item7))
        if analyst_name == 'Epith .cells':
            for item8 in Epith_cells:
                self.comboBox_17.addItem(str(item8))
        if analyst_name == 'Crystals':
            for item9 in Crystals:
                self.comboBox_17.addItem(str(item9))
        if analyst_name == 'Casts':
            for item10 in Casts:
                self.comboBox_17.addItem(str(item10))
        if analyst_name == 'Pregnancy test  in serum' or analyst_name == 'Pregnancy test  in urine' or analyst_name == 'Salmonella typhi  IgG' or analyst_name == 'Salmonella typhi  ImG' or analyst_name == 'Rose-Bengal test' or analyst_name == 'Rh'or analyst_name == 'HBS Ag'or analyst_name == 'HCV Ab'or analyst_name == 'HIV':
            for item11 in Pregnancy_test_in_urine_serum:
                self.comboBox_17.addItem(str(item11))
        for fitem in test:
            if analyst_name == fitem:
                for item12 in test_choices:
                    self.comboBox_17.addItem(str(item12))

    def get_client_id(self):
        global client_id_glob
        client_id_glob = self.spinBox.value()
        self.Show_All_one_client_analyst()
        # self.Add_Data_To_history(6, 1)
        # self.History()

    def Show_All_The_Sales(self):
        self.cur.execute(''' SELECT client_name FROM addclient ORDER BY -date ''')
        analyst_data = self.cur.fetchall()
        all_names = {}
        all_data = []
        id = 0

        for item in analyst_data:
            if item[0] not in all_names:
                all_names[item[0]] = 0

        for s in all_names.keys():
            self.cur.execute(''' SELECT id FROM addclient WHERE client_name=%s ORDER BY id ''', (s,))
            analyst_data2 = self.cur.fetchall()
            all_names[s] = analyst_data2[0][0]
            id = analyst_data2[0][0]
            self.cur.execute(''' SELECT * FROM addclient WHERE id=%s ORDER BY -date ''', (id,))
            latest_data = self.cur.fetchall()
            data = [{'name': s, 'value': latest_data}]
            all_data.append(data)
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_6.insertRow(0)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.insertRow(0)
        l_data = ()
        for ih in all_data:
            hs_data = ih[0]['value']
            l_data += tuple(hs_data)
        # print(l_data, 'k')
        for row, form in enumerate(l_data):
            for col, item in enumerate(form):
                # print(index)
                # if col ==0:
                #     self.tableWidget_6.setItem(row, col, QTableWidgetItem(str(item)))
                # if col == 1:
                #     self.tableWidget_6.setItem(row, col, QTableWidgetItem(str(item)))
                # if col == 2:
                #     self.tableWidget_6.setItem(row, col, QTableWidgetItem(str(item)))
                if col == 3:
                    self.tableWidget_6.setItem(row, col, QTableWidgetItem(str(l_data[row][4])))
                    self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(l_data[row][4])))
                else:
                    self.tableWidget_6.setItem(row, col, QTableWidgetItem(str(item)))
                    self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            row_pos = self.tableWidget_6.rowCount()
            self.tableWidget_6.insertRow(row_pos)
            row_pos = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_pos)
        # print(all_data)

    # def Show_All_The_Analysts(self):
    #     search_type = self.comboBox_19.currentText()
    #     search_words = self.lineEdit_26.text()
    #
    #     if self.comboBox_19.currentIndex() == 1:
    #         self.cur.execute(
    #             ''' SELECT name,category,default_result1,default_result2,price,sub_category FROM addanalyst WHERE name=%s ''',
    #             (search_words,))
    #     if self.comboBox_19.currentIndex() == 2:
    #         self.cur.execute(
    #             ''' SELECT name,category,default_result1,default_result2,price,sub_category FROM addanalyst WHERE price=%s ''',
    #             (search_words,))
    #     if self.comboBox_19.currentIndex() == 0:
    #         self.cur.execute(
    #             ''' SELECT name,category,default_result1,default_result2,price,sub_category FROM addanalyst''')
    #
    #     # combobox_value = ''
    #     # sql = ''
    #     # if search_type == 'اسم التحليل المطابق':
    #     #     combobox_value = 'name'
    #     # if search_type == 'السعر المطابق':
    #     #     combobox_value = 'price'
    #     # if search_type != 'اسم التحليل المطابق' and search_type != 'السعر المطابق':
    #     #     sql = ''' SELECT name,category,default_result1,default_result2,price,sub_category FROM addanalyst'''
    #     # else:
    #     #     sql = f' SELECT name,category,default_result1,default_result2,price,sub_category FROM addanalyst WHERE {combobox_value}=%s'
    #     # if type(search_words) == int:
    #     #     self.cur.execute(sql, search_words)
    #     # if type(search_words) == str:
    #     #     self.cur.execute(sql, search_words)
    #     analyst_data = self.cur.fetchall()
    #     self.tableWidget_7.setRowCount(0)
    #     self.tableWidget_7.insertRow(0)
    #     for row, form in enumerate(analyst_data):
    #         for col, item in enumerate(form):
    #             if col == 1:
    #                 category = ''
    #                 if analyst_data[row][1] == 'خيارات':
    #                     category = 'خيارات'
    #                 if analyst_data[row][1] == 'عدد':
    #                     category = 'عدد'
    #                 if analyst_data[row][1] == 'خيارات مع تعديل':
    #                     category = 'خيارات مع تعديل'
    #                 if analyst_data[row][1] == 'حقل كتابة':
    #                     category = 'حقل كتابة'
    #
    #                 self.tableWidget_7.setItem(row, col, QTableWidgetItem(str(category)))
    #             if col == 5:
    #                 self.tableWidget_7.setItem(row, col, QTableWidgetItem(str(analyst_data[row][5])))
    #
    #             self.tableWidget_7.setItem(row, col, QTableWidgetItem(str(item)))
    #             col += 1
    #         row_pos = self.tableWidget_7.rowCount()
    #         self.tableWidget_7.insertRow(row_pos)
    #     self.Add_Data_To_history(6, 2)
    #     self.History()

    # def Add_Analyst(self):
    #     analyst_name = self.lineEdit_28.text()
    #     analyst_result_category = self.comboBox_22.currentText()
    #     analyst_result1 = self.doubleSpinBox_3.value()
    #     analyst_result2 = self.doubleSpinBox_2.value()
    #     analyst_price = self.doubleSpinBox.value()
    #     sub_category = self.comboBox_23.currentText()
    #     date = datetime.datetime.now()
    #     self.cur.execute(
    #         ''' INSERT INTO addanalyst (name,default_result1,default_result2,price,category,sub_category,date) VALUES(%s,%s,%s,%s,%s,%s,%s) ''',
    #         (
    #             analyst_name, analyst_result1, analyst_result2, analyst_price, analyst_result_category, sub_category,
    #             date))
    #     self.db.commit()
    #     QMessageBox.information(self, 'info', 'تم اضافة التحليل بنجاح')
    #     analyst_name = self.lineEdit_28.setText('')
    #     analyst_result_category = self.comboBox_22.setCurrentIndex(0)
    #     analyst_result1 = self.doubleSpinBox_3.setValue(0)
    #     analyst_result2 = self.doubleSpinBox_2.setValue(0)
    #     analyst_price = self.doubleSpinBox.setValue(0)
    #     sub_category = self.comboBox_23.setCurrentIndex(0)
    #     self.Show_all_analysts_in_combo()
    #     self.Add_Data_To_history(3, 2)
    #     self.History()
    #
    # def Show_analyst_in_Edit_Or_Delete(self):
    #     analyst_current_name = self.comboBox_21.currentText()
    #     self.cur.execute(
    #         ''' SELECT name,default_result1,default_result2,price,category,sub_category,date FROM addanalyst WHERE name=%s ''',
    #         (analyst_current_name,))
    #     data = self.cur.fetchall()
    #     num = 0
    #     if data[0][4] == 'عدد':
    #         num = 4
    #     if data[0][4] == 'خيارات':
    #         num = 2
    #     if data[0][4] == 'حقل كتابة':
    #         num = 1
    #     if data[0][4] == 'خيارات مع تعديل':
    #         num = 3
    #     tp = 0
    #     if data[0][5] == 'bio':
    #         tp = 1
    #     if data[0][5] == 'GSE':
    #         tp = 2
    #     if data[0][5] == 'GUE':
    #         tp = 3
    #     if data[0][5] == 'hematology':
    #         tp = 4
    #     if data[0][5] == 'هرمونات مشترك':
    #         tp = 5
    #     sub_category = self.comboBox_26.setCurrentIndex(tp)
    #     analyst_name = self.lineEdit_29.setText(str(data[0][0]))
    #     analyst_result_category = self.comboBox_25.setCurrentIndex(num)
    #     analyst_result1 = self.doubleSpinBox_4.setValue(data[0][1])
    #     analyst_result2 = self.doubleSpinBox_5.setValue(data[0][2])
    #     analyst_price = self.doubleSpinBox_6.setValue(data[0][3])
    #     self.Add_Data_To_history(6, 2)
    #     self.History()
    #
    # def Edit_Analyst(self):
    #     analyst_current_name = self.comboBox_21.currentText()
    #     analyst_name = self.lineEdit_29.text()
    #     analyst_result_category = self.comboBox_23.currentText()
    #     analyst_result1 = self.doubleSpinBox_4.value()
    #     analyst_result2 = self.doubleSpinBox_5.value()
    #     analyst_price = self.doubleSpinBox_6.value()
    #     sub_category = self.comboBox_26.currentText()
    #     date = datetime.datetime.now()
    #     self.cur.execute(
    #         ''' UPDATE  addanalyst SET name=%s,default_result1=%s,default_result2=%s,price=%s,category=%s,sub_category=%s,date=%s WHERE name=%s ''',
    #         (
    #             analyst_name, analyst_result1, analyst_result2, analyst_price, analyst_result_category, sub_category,
    #             date, analyst_name))
    #     self.db.commit()
    #     QMessageBox.information(self, 'info', 'تم تعديل التحليل بنجاح')
    #     analyst_current_name = self.comboBox_21.setCurrentIndex(0)
    #     analyst_name = self.lineEdit_29.setText('')
    #     analyst_result_category = self.comboBox_23.setCurrentIndex(0)
    #     analyst_result1 = self.doubleSpinBox_4.setValue(0)
    #     analyst_result2 = self.doubleSpinBox_5.setValue(0)
    #     analyst_price = self.doubleSpinBox_6.setValue(0)
    #     sub_category = self.comboBox_26.setCurrentIndex(0)
    #     self.Add_Data_To_history(4, 2)
    #     self.History()
    #     self.Show_all_analysts_in_combo()
    #
    # def Delete_Analyst(self):
    #
    #     warning = QMessageBox.warning(self, 'احذر', "هل انت متأكد من انك تريد مسح التحليل",
    #                                   QMessageBox.Yes | QMessageBox.No)
    #     if warning == QMessageBox.Yes:
    #         analyst_current_name = self.comboBox_21.currentText()
    #         sql = ''' DELETE FROM addanalyst WHERE name=%s '''
    #         self.cur.execute(sql, [(analyst_current_name)])
    #         self.db.commit()
    #         QMessageBox.information(self, 'info', 'تم حذف التحليل بنجاح')
    #
    #         self.Show_all_analysts_in_combo()
    #     self.Add_Data_To_history(5, 2)
    #     self.History()
    #     self.Show_all_analysts_in_combo()

    def Show_all_analysts_in_combo(self):
        self.cur.execute(''' SELECT name FROM addanalyst ''')
        data = self.cur.fetchall()
        self.comboBox_21.clear()
        self.comboBox_16.clear()
        self.comboBox_21.addItem('----------------')
        self.comboBox_16.addItem('----------------')
        for item in data:
            self.comboBox_21.addItem(str(item[0]))

            self.comboBox_16.addItem(str(item[0]))

    def Clients_Page(self):
        id = self.spinBox_2.value()
        self.cur.execute(''' SELECT client_name,client_age,client_genus,client_doctor FROM addclient WHERE id=%s''',
                         (str(id),))
        client_data = self.cur.fetchall()
        self.cur.execute(
            ''' SELECT price,analyst_name,analyst_result,client_name FROM addnewitem WHERE client_id=%s''',
            (str(id),))
        client_analyst_data = self.cur.fetchall()
        num = 0
        all_client_analyst = []
        total = 0
        for i in client_analyst_data:
            num += 1
        for k in range(0, num):
            total += int(client_analyst_data[k][0])
        for j in range(0, num):
            all_client_analyst.append(str(client_analyst_data[j][1]))
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.insertRow(0)
        for row, form in enumerate(client_data):

            for col, item in enumerate(form):
                self.tableWidget_4.setItem(row, 4, QTableWidgetItem(str(num)))
                self.tableWidget_4.setItem(row, 5, QTableWidgetItem(str(','.join(all_client_analyst))))
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
        # self.Add_Data_To_history(6, 5)
        # self.History()

    # def Add_Buys(self):
    #     item_name = self.lineEdit_13.text()
    #     item_type = self.comboBox_6.currentText()
    #     quantity = self.spinBox_3.value()
    #     quantity_avaliable = quantity
    #     signal_item_price = self.lineEdit_12.text()
    #     total_item_price = self.lineEdit_11.text()
    #     date_create_before = self.dateEdit.date()
    #     date_create = str(date_create_before.toPyDate())
    #     self.cur.execute(
    #         ''' INSERT INTO addbuys (item_name,signal_item_price,total_price,buys_type,quantity,date) VALUES (%s,%s,%s,%s,%s,%s)'''
    #         , (item_name, signal_item_price, total_item_price, item_type, quantity, date_create))
    #     self.db.commit()
    #     self.Show_all_buys()
    # self.Add_Data_To_history(3, 4)
    # self.History()

    # def Show_all_buys(self):
    #     self.cur.execute(''' SELECT item_name,buys_type,quantity,signal_item_price,total_price,date FROM addbuys ''')
    #     data = self.cur.fetchall()
    #     self.tableWidget_3.setRowCount(0)
    #     self.tableWidget_3.insertRow(0)
    #     for row, form in enumerate(data):
    #         for col, item in enumerate(form):
    #             self.tableWidget_3.setItem(row, col, QTableWidgetItem(str(item)))
    #             col += 1
    #         row_pos = self.tableWidget_3.rowCount()
    #         self.tableWidget_3.insertRow(row_pos)

    # def Add_Data_To_history(self, action, table):
    #     global user_id
    #     self.cur.execute(
    #         ''' INSERT INTO his VALUES (DEFAULT,%s,%s,%s,%s,%s)''',
    #         (user_id, action, table, datetime.datetime.now(), 1))
    #     self.db.commit()

    # def History(self):
    #     self.cur.execute('''SELECT * FROM his ORDER BY -dates''')
    #     analyst_data = self.cur.fetchall()
    #     self.tableWidget_8.setRowCount(0)
    #     self.tableWidget_8.insertRow(0)
    #     for row, form in enumerate(analyst_data):
    #         for col, item in enumerate(form):
    #             if col == 0:
    #                 sql = '''SELECT uid FROM his WHERE id =%s'''
    #                 self.cur.execute(sql, [item])
    #                 data = self.cur.fetchone()
    #                 sql = '''SELECT user_name FROM adduser WHERE id =%s'''
    #                 self.cur.execute(sql, [data[0]])
    #                 user_name = self.cur.fetchone()
    #                 self.tableWidget_8.setItem(row, col, QTableWidgetItem(str(user_name[0])))
    #             if col == 1:
    #                 action = ''
    #                 if analyst_data[row][2] == 1:
    #                     action = 'تسجيل الدخول'
    #                 if analyst_data[0][2] == 2:
    #                     action = 'تسجيل الخروج'
    #                 if analyst_data[row][2] == 3:
    #                     action = 'اضافة'
    #                 if analyst_data[row][2] == 4:
    #                     action = 'تعديل'
    #                 if analyst_data[row][2] == 5:
    #                     action = 'حذف'
    #                 if analyst_data[row][2] == 6:
    #                     action = 'بحث'
    #                 if analyst_data[row][2] == 7:
    #                     action = 'طباعة'
    #                 self.tableWidget_8.setItem(row, col, QTableWidgetItem(str(action)))
    #             if col == 2:
    #                 tables = ''
    #                 if analyst_data[row][3] == 1:
    #                     tables = 'مبيع يومي'
    #                 if analyst_data[row][3] == 2:
    #                     tables = 'تحليل'
    #                 if analyst_data[row][3] == 3:
    #                     tables = 'مشتريات'
    #                 if analyst_data[row][3] == 4:
    #                     tables = 'مراجعين'
    #                 if analyst_data[row][3] == 5:
    #                     tables = 'مستخدم'
    #                 self.tableWidget_8.setItem(row, col, QTableWidgetItem(str(tables)))
    #             if col == 3:
    #                 self.tableWidget_8.setItem(row, col, QTableWidgetItem(str(analyst_data[row][4])))
    #
    #             col += 1
    #         row_pos = self.tableWidget_8.rowCount()
    #         self.tableWidget_8.insertRow(row_pos)

    # def Show_avaliable_quantity(self):
    #     self.cur.execute(''' SELECT quantity FROM addbuys WHERE ''')
    #     quantity_avaliable = 0
    #     if quantity_avaliable < 1:
    #         date_quantity_ended = datetime.datetime.now()
    #         self.cur.execute(''' UPDATE addbuys SET quantity_avaliable=%s,date_ended=%s''',
    #                          (quantity_avaliable, date_quantity_ended))
    # def Log_In_Chieck(self):
    #     global user_id
    #     user_name = self.lineEdit.text()
    #     user_password = self.lineEdit_2.text()
    #     self.cur.execute(''' SELECT id,user_password,user_name FROM adduser WHERE user_name=%s ''', (user_name,))
    #     # self.cur.execute(''' SELECT * FROM adduser ''')
    #     data = self.cur.fetchone()
    #     if data != None:
    #         if data[2] == user_name and data[1] == user_password:
    #             user_id = data[0]
    #             self.groupBox.setEnabled(True)
    #             self.tabWidget.setCurrentIndex(3)
    #             # self.Add_Data_To_history(1, 5)
    #             # self.History()
    #         else:
    #             warning = QMessageBox.warning(self, '',
    #                                           "كلمة المرور او اسم المستخدم غير صحيحة هل تريد استعادة كلمة المرور؟",
    #                                           QMessageBox.Yes | QMessageBox.No)
    #             if warning == QMessageBox.Yes:
    #                 self.Open_ResetPassword_Page()
    #     else:
    #         warning = QMessageBox.warning(self, '',
    #                                       "كلمة المرور او اسم المستخدم غير صحيحة هل تريد استعادة كلمة المرور؟",
    #                                       QMessageBox.Yes | QMessageBox.No)
    #         if warning == QMessageBox.Yes:
    #             self.Open_ResetPassword_Page()

    # def Delete_All_History_Data(self):
    #     sql = ''' DELETE FROM his'''
    #     self.cur.execute(sql)
    #     self.db.commit()
    #     QMessageBox.information(self, 'info', 'تم حذف محتويات السجل بنجاح')
    #     self.tableWidget_8.setRowCount(0)
    #     self.tableWidget_8.insertRow(0)

    def Open_Sales_Page(self):
        self.tabWidget.setCurrentIndex(3)

    # def Open_Login_Page(self):
    #     self.tabWidget.setCurrentIndex(0)

    def Open_Settings_Page(self):
        self.tabWidget.setCurrentIndex(6)

    def Open_Print_Page(self):
        self.tabWidget.setCurrentIndex(7)

    # def Open_History_Page(self):
    #     self.tabWidget.setCurrentIndex(5)

    def Open_clients_Page(self):
        self.tabWidget.setCurrentIndex(2)

    # def Open_Analyse_Page(self):
    #     self.tabWidget.setCurrentIndex(4)

    # def Open_ResetPassword_Page(self):
    #     self.tabWidget.setCurrentIndex(1)

    def Light_Blue_Theme(self):
        style = open('thems/light_blue.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Blue_Theme(self):
        style = open('thems/darkblue.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Gray_Theme(self):
        style = open('thems/darkgray.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Orange_Theme(self):
        style = open('thems/darkorange.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Dark_Theme(self):
        style = open('thems/qdark.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Bio_Word(self, name, doctor, analysts, results, year, month, day, word_types, prev, genus):
        global if_print
        self.cur.execute(''' SELECT * FROM paths WHERE id=1 ''')
        mydata = self.cur.fetchone()
        word_files = mydata[1]
        save_word_files = mydata[2]
        for word_type in word_types:
            if word_type == 'bio':
                f = open(r'%s\bio latest17.docx' % word_files, 'rb')
                f.read()
                document = Document(f)
                for i in document.tables:
                    for k in i.rows:
                        for j in k.cells:
                            for n in j.paragraphs:
                                if n.text == 'أسـم المريض :':
                                    if genus == 0:
                                        n.text = f'أسـم المريض :{name}'
                                    else:
                                        n.text = f'أسـم المريضة :{name}'
                                    run = n.runs
                                    font = run[0].font
                                    font.name = 'Monotype Koufi'
                                    font.bold = True
                                    font.size = Pt(11)
                                if n.text == 'حضرة الدكتورة   :':
                                    if doctor == 'عدوية شمس سعيد':
                                        n.text = f'حضرة الدكتورة   : {doctor}'
                                    else:
                                        n.text = f'حضرة الدكتور   : {doctor}'
                                    run = n.runs
                                    font = run[0].font
                                    font.name = 'Monotype Koufi'
                                    font.bold = True
                                    font.size = Pt(11)
                                if n.text == 'المحترم':
                                    if genus == 0:
                                        n.text = 'المحترم'
                                    else:
                                        n.text = 'المحترمة'
                                    run = n.runs
                                    font = run[0].font
                                    font.name = 'Monotype Koufi'
                                    font.bold = True
                                    font.size = Pt(11)
                                if n.text == 'المحترمة2':
                                    if doctor == 'عدوية شمس سعيد':
                                        n.text = f'المحترمة'
                                    else:
                                        n.text = f'المحترم'
                                    run = n.runs
                                    font = run[0].font
                                    font.name = 'Monotype Koufi'
                                    font.bold = True
                                    font.size = Pt(11)
                                if n.text == 'Random  blood sugar :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Random  blood sugar':
                                            k = analyst_and_result['result']
                                            n.text = f'Random  blood sugar : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(11)
                                            font.name = 'Tahoma'
                                if n.text == 'Blood Urea               :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Blood Urea':
                                            k = analyst_and_result['result']

                                            n.text = f'Blood Urea               : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(11)
                                            font.name = 'Tahoma'
                                if n.text == 'S. Creatinin               :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'S. Creatinin':
                                            k = analyst_and_result['result']
                                            n.text = f'S. Creatinin               : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(11)
                                            font.name = 'Tahoma'
                                if n.text == 'S. Uric acid                  :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'S. Uric acid':
                                            k = analyst_and_result['result']
                                            n.text = f'S. Uric acid                  : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(11)
                                            font.name = 'Tahoma'
                                if n.text == 'S. Cholesterol            :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'S. Cholesterol':
                                            k = analyst_and_result['result']
                                            n.text = f'S. Cholesterol            : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(11)
                                            font.name = 'Tahoma'
                                if n.text == 'S. Triglycerid             :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'S. Triglycerid':
                                            k = analyst_and_result['result']
                                            n.text = f'S. Triglycerid             : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(11)
                                            font.name = 'Tahoma'
                                if n.text == 'Total serum Bilirubin:':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Total serum Bilirubin':
                                            k = analyst_and_result['result']
                                            n.text = f'Total serum Bilirubin: {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(11)
                                            font.name = 'Tahoma'
                                if n.text == 'S.Calcium :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'S.Calcium':
                                            k = analyst_and_result['result']
                                            n.text = f'S.Calcium : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(11)
                                            font.name = 'Tahoma'
                                if n.text == 'Vitamin D              :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Vitamin D':
                                            k = analyst_and_result['result']
                                            n.text = f'Vitamin D              : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(11)
                                            font.name = 'Tahoma'

                                if n.text == 'Date:    /     / 20':
                                    n.text = f'Date:   {year} /  {month} / {day}'
                                    run = n.runs
                                    font = run[0].font
                                    font.bold = True
                                    font.size = Pt(11)
                                    font.name = 'Tahoma'
                document.save(r'%s\bio latest17.docx' % save_word_files)
                f.close()

            if word_type == 'GSE':
                f = open(r'%s\GSE latest.docx' % word_files, 'rb')
                f.read()

                document = Document(f)
                for i in document.tables:
                    for k in i.rows:
                        for j in k.cells:
                            for n in j.paragraphs:
                                if n.text == 'أسـم المريض :':
                                    if genus == 0:
                                        n.text = f'أسـم المريض :{name}'
                                    else:
                                        n.text = f'أسـم المريضة :{name}'
                                    run = n.runs

                                    font = run[0].font
                                    font.name = 'Monotype Koufi'
                                    font.bold = True
                                    font.size = Pt(11)
                                if n.text == 'حضرة الدكتورة   :':
                                    if doctor == 'عدوية شمس سعيد':
                                        n.text = f'حضرة الدكتورة   : {doctor}'
                                    else:
                                        n.text = f'حضرة الدكتور   : {doctor}'
                                    run = n.runs

                                    font = run[0].font
                                    font.name = 'Monotype Koufi'
                                    font.bold = True
                                    font.size = Pt(11)
                                if n.text == 'المحترم':
                                    if genus == 0:
                                        n.text = 'المحترم'
                                    else:
                                        n.text = 'المحترمة'
                                    run = n.runs

                                    font = run[0].font
                                    font.name = 'Monotype Koufi'
                                    font.bold = True
                                    font.size = Pt(11)
                                if n.text == 'المحترمة2':
                                    if doctor == 'عدوية شمس سعيد':
                                        n.text = f'المحترمة'
                                    else:
                                        n.text = f'المحترم'
                                    run = n.runs
                                    font = run[0].font
                                    font.name = 'Monotype Koufi'
                                    font.bold = True
                                    font.size = Pt(11)
                                if n.text == 'Color:':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Color':
                                            k = analyst_and_result['result']
                                            n.text = f'Color: {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(14)
                                            font.name = 'Tahoma'
                                if n.text == 'Consistency:':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Consistency':
                                            k = analyst_and_result['result']
                                            n.text = f'Consistency: {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(14)
                                            font.name = 'Tahoma'
                                if n.text == 'R.B.Cs:':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'R.B.Cs:GSE':
                                            k = analyst_and_result['result']
                                            n.text = f'R.B.Cs: {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(14)
                                            font.name = 'Tahoma'
                                if n.text == 'Pus cells:':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Pus cells:GSE':
                                            k = analyst_and_result['result']
                                            n.text = f'Pus cells: {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(14)
                                            font.name = 'Tahoma'
                                if n.text == 'E. Histolytica:':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'E. Histolytica':
                                            k = analyst_and_result['result']
                                            n.text = f'E. Histolytica: {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(14)
                                            font.name = 'Tahoma'
                                if n.text == 'G. Lembilia:':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'G. Lembilia':
                                            k = analyst_and_result['result']
                                            n.text = f'G. Lembilia: {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(14)
                                            font.name = 'Tahoma'
                                if n.text == 'Ova:':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Ova':
                                            k = analyst_and_result['result']
                                            n.text = f'Ova: {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(14)
                                            font.name = 'Tahoma'
                                if n.text == 'Bacteria    :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Bacteria:GUE':
                                            k = analyst_and_result['result']
                                            n.text = f'Bacteria    : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.size = Pt(14)
                                if n.text == 'Monillia     :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Monillia:GUE':
                                            k = analyst_and_result['result']
                                            n.text = f'Monillia     : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.size = Pt(14)
                                if n.text == 'Fatty drop:':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Fatty drop:GSE':
                                            k = analyst_and_result['result']
                                            n.text = f'Fatty drop: {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.size = Pt(14)
                                if n.text == 'Other:':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Other:GSE':
                                            k = analyst_and_result['result']
                                            n.text = f'Other: {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(14)
                                            font.name = 'Tahoma'
                                if n.text == 'Date:    /     / 20':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }

                                if n.text == 'Date:    /     / 20':
                                    n.text = f'Date:   {year} /  {month} / {day}'
                                    run = n.runs
                                    font = run[0].font
                                    font.bold = True
                                    font.size = Pt(12)
                                    font.name = 'Tahoma'
                document.save(r'%s\GSE latest.docx' % save_word_files)
                f.close()

            if word_type == 'GUE':

                f = open(r'%s\GUE latest.docx' % word_files, 'rb')
                f.read()

                document = Document(f)
                for i in document.tables:
                    for k in i.rows:
                        for j in k.cells:
                            for n in j.paragraphs:
                                if n.text == 'أسـم المريض :':
                                    if genus == 0:
                                        n.text = f'أسـم المريض :{name}'
                                    else:
                                        n.text = f'أسـم المريضة :{name}'
                                    run = n.runs
                                    font = run[0].font
                                    font.name = 'Monotype Koufi'
                                    font.size = Pt(11)
                                if n.text == 'حضرة الدكتورة   :':
                                    if doctor == 'عدوية شمس سعيد':
                                        n.text = f'حضرة الدكتورة   : {doctor}'
                                    else:
                                        n.text = f'حضرة الدكتور   : {doctor}'
                                    run = n.runs
                                    font = run[0].font
                                    font.name = 'Monotype Koufi'
                                    font.size = Pt(11)
                                if n.text == 'المحترم':
                                    if genus == 0:
                                        n.text = 'المحترم'
                                    else:
                                        n.text = 'المحترمة'
                                    run = n.runs

                                    font = run[0].font
                                    font.name = 'Monotype Koufi'
                                    font.bold = True
                                    font.size = Pt(11)
                                if n.text == 'المحترمة2':
                                    if doctor == 'عدوية شمس سعيد':
                                        n.text = f'المحترمة'
                                    else:
                                        n.text = f'المحترم'
                                    run = n.runs
                                    font = run[0].font
                                    font.name = 'Monotype Koufi'
                                    font.bold = True
                                    font.size = Pt(11)
                                if n.text == 'Appearance :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Appearance':
                                            k = analyst_and_result['result']
                                            n.text = f'Appearance : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.size = Pt(14)
                                if n.text == 'Reaction      :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Reaction':
                                            k = analyst_and_result['result']
                                            n.text = f'Reaction      : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.size = Pt(14)
                                if n.text == 'Albumin       :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Albumin':
                                            k = analyst_and_result['result']
                                            n.text = f'Albumin       : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.size = Pt(14)
                                if n.text == 'Sugar          :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Sugar':
                                            k = analyst_and_result['result']
                                            n.text = f'Sugar          : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.size = Pt(14)
                                if n.text == 'RBCs         :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'RBCs:GUE':
                                            k = analyst_and_result['result']
                                            n.text = f'RBCs         : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.size = Pt(14)
                                if n.text == 'Pus cells    :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Pus cells:GUE':
                                            k = analyst_and_result['result']
                                            n.text = f'Pus cells    : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.size = Pt(14)
                                if n.text == 'Epith .cells :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Epith .cells':
                                            k = analyst_and_result['result']
                                            n.text = f'Epith .cells : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.size = Pt(14)
                                if n.text == 'Crystals     :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Crystals':
                                            k = analyst_and_result['result']
                                            n.text = f'Crystals     : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.size = Pt(14)
                                if n.text == 'Casts        :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Casts':
                                            k = analyst_and_result['result']
                                            n.text = f'Casts        : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.size = Pt(14)
                                if n.text == 'Bacteria    :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Bacteria:GUE':
                                            k = analyst_and_result['result']
                                            n.text = f'Bacteria    : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.size = Pt(14)
                                if n.text == 'Monillia     :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Monillia:GUE':
                                            k = analyst_and_result['result']
                                            n.text = f'Monillia     : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.size = Pt(14)
                                if n.text == 'Other        :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Other:GUE':
                                            k = analyst_and_result['result']
                                            n.text = f'Other        : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.size = Pt(14)
                                if n.text == 'Date:    /     / 20':
                                    n.text = f'Date:   {year} /  {month} / {day}'
                                    run = n.runs
                                    font = run[0].font
                                    font.name = 'Tahoma'
                                    font.bold = True
                                    font.size = Pt(12)
                document.save(r'%s\GUE latest.docx' % save_word_files)
                f.close()

            if word_type == 'hematology':
                f = open(r'%s\hematology latest.docx' % word_files, 'rb')
                f.read()

                document = Document(f)
                for i in document.tables:
                    for k in i.rows:
                        for j in k.cells:
                            for n in j.paragraphs:
                                if n.text == 'أسـم المريض :':
                                    if genus == 0:
                                        n.text = f'أسـم المريض :{name}'
                                    else:
                                        n.text = f'أسـم المريضة :{name}'
                                    run = n.runs
                                    font = run[0].font
                                    font.name = 'Monotype Koufi'
                                    font.bold = True
                                    font.size = Pt(11)
                                if n.text == 'حضرة الدكتورة   :':
                                    if doctor == 'عدوية شمس سعيد':
                                        n.text = f'حضرة الدكتورة   : {doctor}'
                                    else:
                                        n.text = f'حضرة الدكتور   : {doctor}'
                                    run = n.runs
                                    font = run[0].font
                                    font.name = 'Monotype Koufi'
                                    font.bold = True
                                    font.size = Pt(11)
                                if n.text == 'المحترم':
                                    if genus == 0:
                                        n.text = 'المحترم'
                                    else:
                                        n.text = 'المحترمة'
                                    run = n.runs

                                    font = run[0].font
                                    font.name = 'Monotype Koufi'
                                    font.bold = True
                                    font.size = Pt(11)
                                if n.text == 'المحترمة2':
                                    if doctor == 'عدوية شمس سعيد':
                                        n.text = f'المحترمة'
                                    else:
                                        n.text = f'المحترم'
                                    run = n.runs
                                    font = run[0].font
                                    font.name = 'Monotype Koufi'
                                    font.bold = True
                                    font.size = Pt(11)
                                if n.text == 'Hb             :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Hb':
                                            k = analyst_and_result['result']
                                            n.text = f'Hb             : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = True
                                            font.size = Pt(12)
                                if n.text == 'PCV           :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'PCV':
                                            k = analyst_and_result['result']
                                            n.text = f'PCV           : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = True
                                            font.size = Pt(12)
                                if n.text == 'WBCs         :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'WBCs':
                                            k = analyst_and_result['result']
                                            n.text = f'WBCs         : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = True
                                            font.size = Pt(12)
                                if n.text == 'E.S.R          :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'E.S.R':
                                            k = analyst_and_result['result']
                                            n.text = f'E.S.R          : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = True
                                            font.size = Pt(12)
                                if n.text == 'Blood Group:':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Blood Group':
                                            k = analyst_and_result['result']
                                            n.text = f'Blood Group: {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = True
                                            font.size = Pt(12)
                                if n.text == 'Rh:':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Rh':
                                            k = analyst_and_result['result']
                                            n.text = f'Rh: {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = True
                                            font.size = Pt(12)
                                if n.text == 'Pregnancy test  in urine   :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Pregnancy test  in urine':
                                            k = analyst_and_result['result']
                                            n.text = f'Pregnancy test  in urine   : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = True
                                            font.size = Pt(12)
                                if n.text == 'Pregnancy test  in serum  :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Pregnancy test  in serum':
                                            k = analyst_and_result['result']
                                            n.text = f'Pregnancy test  in serum  : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = True
                                            font.size = Pt(12)
                                if n.text == 'R.B.Sugar                           :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'R.B.Sugar':
                                            k = analyst_and_result['result']
                                            n.text = f'R.B.Sugar                           : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = True
                                            font.size = Pt(12)
                                if n.text == 'Bl. Urea                              :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Bl. Urea':
                                            k = analyst_and_result['result']
                                            n.text = f'Bl. Urea                              : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = True
                                            font.size = Pt(12)
                                if n.text == 'Salmonella typhi  IgG :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Salmonella typhi  IgG':
                                            k = analyst_and_result['result']
                                            n.text = f'Salmonella typhi  IgG : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = True
                                            font.size = Pt(12)
                                if n.text == 'Salmonella typhi  IgM :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Salmonella typhi  IgM':
                                            k = analyst_and_result['result']
                                            n.text = f'Salmonella typhi  IgM : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = True
                                            font.size = Pt(12)
                                if n.text == 'Rose-Bengal test   :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Rose-Bengal test':
                                            k = analyst_and_result['result']
                                            n.text = f'HBS Ag   : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = True
                                            font.size = Pt(12)
                                if n.text == 'HBS Ag                                :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'HBS Ag':
                                            k = analyst_and_result['result']
                                            n.text = f'HBS Ag                                : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = True
                                            font.size = Pt(12)
                                if n.text == 'HCV Ab                                :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'HCV Ab':
                                            k = analyst_and_result['result']
                                            n.text = f'HCV Ab                                : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = True
                                            font.size = Pt(12)
                                if n.text == 'HIV                                      :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'HIV':
                                            k = analyst_and_result['result']
                                            n.text = f'HIV                                      : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = True
                                            font.size = Pt(12)
                                if n.text == 'Date:    /     / 20':
                                    n.text = f'Date:   {year} /  {month} / {day}'
                                    run = n.runs
                                    font = run[0].font
                                    font.name = 'Tahoma'
                                    font.bold = True
                                    font.size = Pt(12)

                document.save(r'%s\hematology latest.docx' % save_word_files)
                f.close()
            if word_type == 'SFA':
                f = open(r'%s\SFA latest.docx' % word_files, 'rb')
                f.read()
                document = Document(f)
                for i in document.tables:
                    for k in i.rows:
                        for j in k.cells:

                            for n in j.paragraphs:
                                if n.text == 'أسـم المريض :':
                                    if genus == 0:
                                        n.text = f'أسـم المريض :{name}'
                                    else:
                                        n.text = f'أسـم المريضة :{name}'
                                    run = n.runs
                                    font = run[0].font
                                    font.name = 'Monotype Koufi'
                                    font.bold = True
                                    font.size = Pt(11)
                                if n.text == 'حضرة الدكتورة   :':
                                    if doctor == 'عدوية شمس سعيد':
                                        n.text = f'حضرة الدكتورة   : {doctor}'
                                    else:
                                        n.text = f'حضرة الدكتور   : {doctor}'
                                    run = n.runs
                                    font = run[0].font
                                    font.name = 'Monotype Koufi'
                                    font.bold = True
                                    font.size = Pt(11)
                                if n.text == 'المحترم':
                                    if genus == 0:
                                        n.text = 'المحترم'
                                    else:
                                        n.text = 'المحترمة'
                                    run = n.runs

                                    font = run[0].font
                                    font.name = 'Monotype Koufi'
                                    font.bold = True
                                    font.size = Pt(11)
                                if n.text == 'المحترمة2':
                                    if doctor == 'عدوية شمس سعيد':
                                        n.text = f'المحترمة'
                                    else:
                                        n.text = f'المحترم'
                                    run = n.runs
                                    font = run[0].font
                                    font.name = 'Monotype Koufi'
                                    font.bold = True
                                    font.size = Pt(11)
                                if n.text == 'Volume       :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Volume':
                                            k = analyst_and_result['result']
                                            n.text = f'Volume       : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = False
                                            font.size = Pt(14)
                                if n.text == 'Reaction      :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Reaction':
                                            k = analyst_and_result['result']
                                            n.text = f'Reaction      : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = False
                                            font.size = Pt(14)
                                if n.text == 'Colour        :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Colour:SFA':
                                            k = analyst_and_result['result']
                                            n.text = f'Colour        : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = False
                                            font.size = Pt(14)
                                if n.text == 'Liquefaction :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Liquefaction':
                                            k = analyst_and_result['result']
                                            n.text = f'Liquefaction : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = False
                                            font.size = Pt(14)
                                if n.text == 'Count          :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Count':
                                            k = analyst_and_result['result']
                                            n.text = f'Count          : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = False
                                            font.size = Pt(14)
                                if n.text == 'Active          :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Motility:Active':
                                            k = analyst_and_result['result']
                                            n.text = f'Active          : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = False
                                            font.size = Pt(14)
                                if n.text == 'Sluggish       :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Motility:Sluggish':
                                            k = analyst_and_result['result']
                                            n.text = f'Sluggish       : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = False
                                            font.size = Pt(14)
                                if n.text == 'Dead           :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Motility:Dead':
                                            k = analyst_and_result['result']
                                            n.text = f'Dead           : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = False
                                            font.size = Pt(14)
                                if n.text == 'Normal        :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Morphology:Normal':
                                            k = analyst_and_result['result']
                                            n.text = f'Normal        : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = False
                                            font.size = Pt(14)
                                if n.text == 'Abnormal     :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Morphology:Abnormal':
                                            k = analyst_and_result['result']
                                            n.text = f'Abnormal     : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = False
                                            font.size = Pt(14)
                                if n.text == 'Pus cells       :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Morphology:Pus cells':
                                            k = analyst_and_result['result']
                                            n.text = f'Pus cells       : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = False
                                            font.size = Pt(14)
                                if n.text == 'Other           :':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Other:SFA':
                                            k = analyst_and_result['result']
                                            n.text = f'Other           : {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.name = 'Tahoma'
                                            font.bold = False
                                            font.size = Pt(14)
                                if n.text == 'Date:    /     / 20':
                                    n.text = f'Date:   {year} /  {month} / {day}'
                                    run = n.runs
                                    font = run[0].font
                                    font.name = 'Tahoma'
                                    font.bold = True
                                    font.size = Pt(12)
                                # print('1'+n.text+'2')
                # for kd in document.paragraphs:
                #     print('1'+kd.text+'2'+'h')
                document.save(r'%s\SFA latest.docx' % save_word_files)
                f.close()
            if word_type == 'هرمونات مشترك':
                f = open(r'%s\هرمونات مشترك latest.docx' % word_files, 'rb')
                f.read()

                document = Document(f)

                for i in document.tables:
                    for k in i.rows:
                        for j in k.cells:

                            for n in j.paragraphs:
                                if n.text == '     أســم الـمــريــض    :':
                                    if genus == 0:
                                        n.text = f'     أســم الـمــريــض    :{name}'
                                    else:
                                        n.text = f'     أســم الـمــريــضة    :{name}'
                                    run = n.runs
                                    font = run[0].font
                                    font.bold = True
                                    font.size = Pt(14)
                                    font.name = 'Monotype Koufi'
                                if n.text == 'حـضـرة الـدكتـورة    الـفاضـــلة :                                                                                            ':
                                    if doctor != 'عدوية شمس سعيد':
                                        n.text = f'حـضـرة الـدكتـور    الـفاضـــل : {doctor}'
                                    else:
                                        n.text = f'حـضـرة الـدكتـورة    الـفاضـــلة : {doctor}'
                                    run = n.runs
                                    font = run[0].font
                                    font.bold = True
                                    font.size = Pt(14)
                                    font.name = 'Monotype Koufi'
                                if n.text == 'الـمـحـتـرم':
                                    if genus == 0:
                                        n.text = 'المحترم'
                                    else:
                                        n.text = 'المحترمة'
                                    run = n.runs

                                    font = run[0].font
                                    font.name = 'Monotype Koufi'
                                    font.bold = True
                                    font.size = Pt(14)
                                if n.text == 'الـمـحـتـرمة2':
                                    if doctor == 'عدوية شمس سعيد':
                                        n.text = f'المحترمة'
                                    else:
                                        n.text = f'المحترم'
                                    run = n.runs
                                    font = run[0].font
                                    font.name = 'Monotype Koufi'
                                    font.bold = True
                                    font.size = Pt(14)
                                if n.text == '0r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Toxoplasma IgG':
                                            k = analyst_and_result['result']

                                            n.text = f'  {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(10)
                                            font.name = 'Tahoma'
                                if n.text == '1r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Toxoplasma IgM':
                                            k = analyst_and_result['result']

                                            # print(k, ng, 'here ohf')
                                            n.text = f'  {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(10)
                                            font.name = 'Tahoma'
                                if n.text == '2r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Cytomegalo Virus IgG':
                                            k = analyst_and_result['result']

                                            n.text = f'  {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(10)
                                            font.name = 'Tahoma'
                                if n.text == '3r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Cytomegalo Virus IgM':
                                            k = analyst_and_result['result']

                                            n.text = f'  {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(10)
                                            font.name = 'Tahoma'
                                if n.text == '4r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Rubella IgG':
                                            k = analyst_and_result['result']

                                            n.text = f'  {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(10)
                                            font.name = 'Tahoma'
                                if n.text == '5r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Rubella IgM':
                                            k = analyst_and_result['result']
                                            n.text = f'  {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(10)
                                            font.name = 'Tahoma'
                                if n.text == '6r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Anti - Phspholipin IgG':
                                            k = analyst_and_result['result']

                                            n.text = f'  {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(10)
                                            font.name = 'Tahoma'
                                if n.text == '7r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Anti - Phspholipin  IgM':
                                            k = analyst_and_result['result']
                                            n.text = f'  {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(10)
                                            font.name = 'Tahoma'
                                if n.text == '8r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Anti - Cardiolipin  IgG':
                                            k = analyst_and_result['result']

                                            n.text = f'  {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(10)
                                            font.name = 'Tahoma'
                                if n.text == '9r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Anti - Cardiolipin  IgM':
                                            k = analyst_and_result['result']

                                            n.text = f'  {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(10)
                                            font.name = 'Tahoma'
                                if n.text == '10r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Herps   IgG':
                                            k = analyst_and_result['result']

                                            n.text = f'  {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(10)
                                            font.name = 'Tahoma'
                                if n.text == '11r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Herpes  IgM':
                                            k = analyst_and_result['result']
                                            n.text = f'  {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(10)
                                            font.name = 'Tahoma'
                                if n.text == 'r0r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'T3':
                                            k = analyst_and_result['result']
                                            n.text = f'  {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(10)
                                            font.name = 'Tahoma'

                                if n.text == 'r1r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'T4':
                                            k = analyst_and_result['result']
                                            n.text = f'  {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(10)
                                            font.name = 'Tahoma'

                                if n.text == 'r2r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'TSH':
                                            k = analyst_and_result['result']
                                            n.text = f'  {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(10)
                                            font.name = 'Tahoma'

                                if n.text == 'r3r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'LH':
                                            k = analyst_and_result['result']
                                            n.text = f'  {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(10)
                                            font.name = 'Tahoma'

                                if n.text == 'r4r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'FSH':
                                            k = analyst_and_result['result']
                                            n.text = f'  {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(10)
                                            font.name = 'Tahoma'

                                if n.text == 'r5r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Prolactin':
                                            k = analyst_and_result['result']
                                            n.text = f'  {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(10)
                                            font.name = 'Tahoma'
                                if n.text == 'r6r':
                                    for row in range(0, len(analysts)):
                                        analyst_and_result = {
                                            'analyst': analysts[row],
                                            'result': results[row]
                                        }
                                        if analyst_and_result['analyst'] == 'Testosterone':
                                            k = analyst_and_result['result']
                                            n.text = f'  {k}'
                                            run = n.runs
                                            font = run[0].font
                                            font.bold = True
                                            font.size = Pt(10)
                                            font.name = 'Tahoma'
                                if n.text == 'Date:    /     / 20':
                                    n.text = f'Date:{year}/{month}/{day}'
                                    run = n.runs
                                    font = run[0].font
                                    font.bold = True
                                    font.size = Pt(12)
                                    font.name = 'Tahoma'
                                if n.text == '0r':
                                    n.text = ''
                                if n.text == '1r':
                                    n.text = ''
                                if n.text == '2r':
                                    n.text = ''
                                if n.text == '3r':
                                    n.text = ''
                                if n.text == '4r':
                                    n.text = ''
                                if n.text == '5r':
                                    n.text = ''
                                if n.text == '6r':
                                    n.text = ''
                                if n.text == '7r':
                                    n.text = ''
                                if n.text == '8r':
                                    n.text = ''
                                if n.text == '9r':
                                    n.text = ''
                                if n.text == '10r':
                                    n.text = ''
                                if n.text == '11r':
                                    n.text = ''
                                if n.text == 'r0r':
                                    n.text = ''
                                if n.text == 'r1r':
                                    n.text = ''
                                if n.text == 'r2r':
                                    n.text = ''
                                if n.text == 'r3r':
                                    n.text = ''
                                if n.text == 'r4r':
                                    n.text = ''
                                if n.text == 'r5r':
                                    n.text = ''
                                if n.text == 'r6r':
                                    n.text = ''
                for element in document.paragraphs:
                    if element.text == 'Date:    /     / 20':
                        element.text = f'Date:{year}/{month}/{day}'
                        run = element.runs
                        font = run[0].font
                        font.bold = True
                        font.size = Pt(12)
                        font.name = 'Tahoma'
                document.save(r'%s\هرمونات مشترك latest.docx' % save_word_files)
                f.close()

        try:
            if prev == 'T':
                word = client.Dispatch("Word.Application")
                if os.path.exists(r'%s\bio latest17.docx' % save_word_files):
                    word.Documents.Open(r'%s\bio latest17.docx' % save_word_files)
                if os.path.exists(r'%s\GSE latest.docx' % save_word_files):
                    word.Documents.Open(r'%s\GSE latest.docx' % save_word_files)
                if os.path.exists(r'%s\SFA latest.docx' % save_word_files):
                    word.Documents.Open(r'%s\SFA latest.docx' % save_word_files)
                if os.path.exists(r'%s\GUE latest.docx' % save_word_files):
                    word.Documents.Open(r'%s\GUE latest.docx' % save_word_files)
                if os.path.exists(r'%s\hematology latest.docx' % save_word_files):
                    word.Documents.Open(r'%s\hematology latest.docx' % save_word_files)
                if os.path.exists(r'%s\هرمونات مشترك latest.docx' % save_word_files):
                    word.Documents.Open(r'%s\هرمونات مشترك latest.docx' % save_word_files)


            else:
                move = 1
                word = client.Dispatch("Word.Application")
                if move == 1:
                    if os.path.exists(r'%s\bio latest17.docx' % save_word_files):

                        word.Documents.Open(r'%s\bio latest17.docx' % save_word_files)
                        # word.ActiveDocument()

                        # word.ActiveDocument.ActiveWindow.View()
                        word.ActiveDocument.PrintOut()
                        time.sleep(2)
                        pyautogui.press('enter')
                        time.sleep(1.5)
                        word.ActiveDocument.Close()
                        move = 0
                        warning = QMessageBox.warning(self, '',
                                                      "هل قمت بطباعة الملف؟\n لا تضغط نعم الا لو قمت بطباعته",
                                                      QMessageBox.Yes | QMessageBox.No)
                        if warning == QMessageBox.Yes:
                            move = 1
                        # word.ActiveDocument.Close()
                        os.remove(r'%s\bio latest17.docx' % save_word_files)

                if move == 1:
                    if os.path.exists(r'%s\GSE latest.docx' % save_word_files):
                        word.Documents.Open(r'%s\GSE latest.docx' % save_word_files)
                        word.ActiveDocument.PrintOut()
                        time.sleep(2)
                        pyautogui.press('enter')
                        time.sleep(1.5)
                        word.ActiveDocument.Close()
                        move = 0
                        warning = QMessageBox.warning(self, '',
                                                      "هل قمت بطباعة الملف؟\n لا تضغط نعم الا لو قمت بطباعته",
                                                      QMessageBox.Yes | QMessageBox.No)
                        if warning == QMessageBox.Yes:
                            move = 1
                        word.ActiveDocument.Close()
                        os.remove(r'%s\GSE latest.docx' % save_word_files)

                if move == 1:

                    if os.path.exists(r'%s\SFA latest.docx' % save_word_files):
                        word.Documents.Open(r'%s\SFA latest.docx' % save_word_files)
                        word.ActiveDocument.PrintOut()
                        time.sleep(2)
                        pyautogui.press('enter')
                        time.sleep(1.5)
                        word.ActiveDocument.Close()
                        move = 0
                        warning = QMessageBox.warning(self, '',
                                                      "هل قمت بطباعة الملف؟\n لا تضغط نعم الا لو قمت بطباعته",
                                                      QMessageBox.Yes | QMessageBox.No)
                        if warning == QMessageBox.Yes:
                            move = 1
                        # word.ActiveDocument.Close()
                        os.remove(r'%s\SFA latest.docx' % save_word_files)

                if move == 1:

                    if os.path.exists(r'%s\GUE latest.docx' % save_word_files):
                        word.Documents.Open(r'%s\GUE latest.docx' % save_word_files)
                        word.ActiveDocument.PrintOut()
                        time.sleep(2)
                        pyautogui.press('enter')
                        time.sleep(1.5)
                        word.ActiveDocument.Close()
                        move = 0
                        warning = QMessageBox.warning(self, '',
                                                      "هل قمت بطباعة الملف؟\n لا تضغط نعم الا لو قمت بطباعته",
                                                      QMessageBox.Yes | QMessageBox.No)
                        if warning == QMessageBox.Yes:
                            move = 1
                        word.ActiveDocument.Close()
                        os.remove(r'%s\GUE latest.docx' % save_word_files)

                if move == 1:

                    if os.path.exists(r'%s\hematology latest.docx' % save_word_files):
                        word.Documents.Open(r'%s\hematology latest.docx' % save_word_files)
                        word.ActiveDocument.PrintOut()
                        time.sleep(2)
                        pyautogui.press('enter')
                        time.sleep(1.5)
                        word.ActiveDocument.Close()
                        move = 0
                        warning = QMessageBox.warning(self, '',
                                                      "هل قمت بطباعة الملف؟\n لا تضغط نعم الا لو قمت بطباعته",
                                                      QMessageBox.Yes | QMessageBox.No)
                        if warning == QMessageBox.Yes:
                            move = 1
                        word.ActiveDocument.Close()
                        os.remove(r'%s\hematology latest.docx' % save_word_files)

                if move == 1:

                    if os.path.exists(r'%s\هرمونات مشترك latest.docx' % save_word_files):
                        word.Documents.Open(r'%s\هرمونات مشترك latest.docx' % save_word_files)
                        word.ActiveDocument.PrintOut()
                        time.sleep(2)
                        pyautogui.press('enter')
                        time.sleep(1.5)
                        word.ActiveDocument.Close()
                        move = 0
                        warning = QMessageBox.warning(self, '',
                                                      "هل قمت بطباعة الملف؟\n لا تضغط نعم الا لو قمت بطباعته",
                                                      QMessageBox.Yes | QMessageBox.No)
                        if warning == QMessageBox.Yes:
                            move = 1
                        # word.ActiveDocument.Close()
                        os.remove(r'%s\هرمونات مشترك latest.docx' % save_word_files)
                self.Delete_Files()


        except Exception as e:
            print(e)


def main():
    app = QApplication(sys.argv)
    window = mainapp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
