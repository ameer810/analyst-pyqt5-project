import datetime
import os
import sys
import time
import MySQLdb
# import pyautogui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from PyQt5.uic.properties import QtCore
from docx import *
from docx.shared import Pt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from win32com import client
import searchDialog
import searchWidget
import multyclass
from mymain import Ui_MainWindow as main_wind

FORM_CLASS, _ = loadUiType("design.ui")
show_all_sales_in_clients_page = False
user_id = 4
client_id_glob = 0
chick_if_add_new = False
if_print = False
analysts_name_glo = []
clients_name_glo = []
clients_name_glo_clients_page = []
from_start = False
first_text = ''
first_text2 = ''
first_text3 = ''
addTrue=True

mylist = ['Full GSE', 'Full GUE', 'Full SFA']
My_num = ['Appearance', 'Reaction:GUE', 'Albumin', 'Sugar', 'RBCs:GUE', 'Pus cells:GUE', 'Epith .cells',
          'Crystals',
          'Casts', 'Other:GUE', 'Volume', 'Reaction:SFA', 'Colour:SFA', 'Liquefaction', 'Motility:Active',
          'Motility:Sluggish', 'Motility:Dead', 'Morphology:Normal', 'Morphology:Abnormal',
          'Morphology:Pus cells', 'Other:SFA', 'Color:GSE', 'Consistency', 'E. Histolytica', 'G. Lembilia',
          'Ova', 'Pus cells:GSE', 'R.B.Cs:GSE', 'Bacteria:GSE', 'Bacteria:GUE', 'Monillia:GSE', 'Monillia:GUE',
          'Fatty drop:GSE', 'Fatty drop:GUE', 'Mucuse:GUE']

select_by_date = False
sd=None

# GSE_row1=[]

class mainapp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        global from_start
        super(mainapp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.tabWidget.tabBar().setVisible(False)
        self.DB_Connect()
        self.Delete_Files()
        self.add_clients_to_combo()
        from_start = True
        self.Show_All_The_Analysts()
        self.handel_buttons()
        self.Show_All_The_Sales()
        self.Show_all_analysts_in_combo()
        self.Show_all_buys()
        self.History()
        self.groupBox.setEnabled(False)
        self.Show_paths()
        self.add_Analyst_to_list()
        self.Auto_complete_combo()
        self.add_client_to_list()
        self.Auto_complete_combo2()
        self.add_client_to_list4()
        self.Auto_complete_combo4()
        self.dateEdit_3.setDate(datetime.date.today())

    def DB_Connect(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='12345', db='tahlel2', charset="utf8",
                                  use_unicode=True, port=3306)
        self.cur = self.db.cursor()

    def handel_buttons(self):
        global addTrue
        self.pushButton_15.clicked.connect(self.Light_Blue_Theme)
        self.pushButton_9.clicked.connect(self.Dark_Orange_Theme)
        self.pushButton_13.clicked.connect(self.Dark_Blue_Theme)
        self.pushButton_14.clicked.connect(self.Dark_Theme)
        self.pushButton_11.clicked.connect(self.Dark_Gray_Theme)
        self.pushButton.clicked.connect(self.Open_Sales_Page)
        self.pushButton_6.clicked.connect(self.Open_Login_Page)
        self.pushButton_4.clicked.connect(self.Open_Settings_Page)
        self.pushButton_12.clicked.connect(self.Open_Print_Page)
        self.pushButton_3.clicked.connect(self.Open_History_Page)
        self.pushButton_5.clicked.connect(self.Open_clients_Page)
        self.pushButton_2.clicked.connect(self.Open_Analyse_Page)
        self.pushButton_8.clicked.connect(self.Open_ResetPassword_Page)
        self.pushButton_17.clicked.connect(self.Sales_Page)
        self.pushButton_30.clicked.connect(self.get_client_id)
        # if not addTrue:
        self.comboBox_16.currentIndexChanged.connect(self.Chick_analyst_category)
        # QListView.currentChanged()
        # self.pushButton_31.clicked.connect(self.Chick_analyst_category)
        self.pushButton_32.clicked.connect(self.get_total_price)
        # self.pushButton_33.clicked.connect(self.Show_analyst_in_Edit_Or_Delete)
        self.comboBox_21.currentIndexChanged.connect(self.Show_analyst_in_Edit_Or_Delete)
        self.pushButton_29.clicked.connect(self.Clients_Page)
        self.pushButton_16.clicked.connect(self.Add_Buys)
        self.pushButton_20.clicked.connect(self.Show_All_The_Analysts)
        self.pushButton_27.clicked.connect(self.Edit_Analyst)
        self.pushButton_7.clicked.connect(self.Log_In_Chieck)
        self.pushButton_28.clicked.connect(self.Delete_Analyst)
        self.pushButton_22.clicked.connect(self.Delete_All_History_Data)
        self.pushButton_18.clicked.connect(self.Print_Sale_Data)
        self.pushButton_19.clicked.connect(self.Search_In_All_Sales)
        self.comboBox_20.currentIndexChanged.connect(self.Search_In_History)
        self.comboBox_24.currentIndexChanged.connect(self.Search_In_History)
        # self.pushButton_21.clicked.connect(self.Search_In_History)
        self.pushButton_35.clicked.connect(self.clear_data_in_sales)
        self.pushButton_10.clicked.connect(self.Reset_password)
        self.pushButton_26.clicked.connect(self.Add_Analyst)
        self.pushButton_34.clicked.connect(self.Preview)
        self.pushButton_23.clicked.connect(self.Print_empty_papers)
        self.pushButton_24.clicked.connect(self.Add_Path)
        self.pushButton_36.clicked.connect(self.Show_All_Clients)
        self.pushButton_39.clicked.connect(self.ADD_one_REsult_to_ANalyst_results)
        self.pushButton_40.clicked.connect(self.ADD_one_REsult_to_ANalyst_results_IN_EDITMODE)
        self.pushButton_41.clicked.connect(self.Remove_one_REsult_to_ANalyst_results_IN_EDITMODE)
        self.pushButton_43.clicked.connect(self.Show_search_Widget)
        self.pushButton_44.clicked.connect(self.Show_multy_Dialog)
        self.comboBox_16.view().pressed.connect(self.Set_Chick_State2)
        self.my_def()
        self.add_all_subCategory_toList()

    def add_all_subCategory_toList(self):
        global mylist
        mylist.clear()
        self.cur.execute(''' SELECT sub_category FROM addanalyst ''')
        data = self.cur.fetchall()
        for i in data:
            if i[0] not in mylist:
                mylist.append(i[0])

    def Set_Chick_State2(self, item):
        global sd
        nitem=self.comboBox_16.model().itemFromIndex(item)
        sd=item
        # if nitem.checkState() == Qt.Checked:
        #     nitem.setCheckState(Qt.Unchecked)
        # else:
        #     # print('ggggggg')
        #     nitem.setCheckState(Qt.Checked)


    def Set_Chick_State(self, item):
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
        else:
            item.setCheckState(Qt.Checked)

    def Show_multy_Dialog(self):
        self.Dialog = multyclass.MultyDialog()
        # if self.Dialog.pushButton.key==Qt.Key_Enter:
        #     print('jj')
        self.cur.execute(''' SELECT name,sub_category FROM addanalyst''')
        data = self.cur.fetchall()
        my_list = []
        for index1, i in enumerate(data):
            if data[index1][1] not in my_list:
                my_list.append(data[index1][1])
        all_listWidget = []
        all_pushButton = []
        for index, ii in enumerate(my_list):
            tab = QWidget()
            self.Dialog.tabWidget.addTab(tab, str(ii))
            self.Dialog.my_listWidget = QListWidget(tab)
            self.Dialog.my_listWidget.setObjectName("listWidget_+" + str(index + 1))
            all_listWidget.append(str("listWidget_+" + str(index + 1)))
            self.Dialog.my_listWidget.setGeometry(QRect(0, 10, 641, 491))
            font = QFont()
            font.setPointSize(11)
            self.Dialog.my_listWidget.setFont(font)
            item = QListWidgetItem()
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Checked)

            # item.setText(str())
            # self.Dialog.my_listWidget.addItem(item)
            ######################################
            ######################################
        for index2 in range(0, self.Dialog.tabWidget.count()):
            if index2 < self.Dialog.tabWidget.count():
                listWidget_object = self.Dialog.findChild(QListWidget, f"listWidget_+{index2 + 1}")
                listWidget_object.itemClicked.connect(self.Set_Chick_State)
                # QListWidget.keyPressEvent()
                # if listWidget_object.key()==Qt.Key_Enter:
                # print(listWidget_object.currentItem().text())
                for iy in range(0, len(data)):
                    if self.Dialog.tabWidget.tabText(index2) == str(data[iy][1]):
                        item = QListWidgetItem()
                        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                        item.setCheckState(Qt.Unchecked)
                        item.setText(str(data[iy][0]))
                        listWidget_object.addItem(item)
            else:
                # print('else')
                break
        self.Dialog.pushButton.clicked.connect(self.Handel_multy_Dialog)
        self.Dialog.exec_()

    def Handel_multy_Dialog(self):
        print('yeah my boy')
        for i in range(0, self.Dialog.tabWidget.count()):
            listWidget_object = self.Dialog.findChild(QListWidget, f"listWidget_+{i + 1}")
            for row in range(0, listWidget_object.count()):
                if listWidget_object.item(row).checkState() == Qt.Checked:
                    self.comboBox_16.setCurrentText(str(listWidget_object.item(row).text()))
                    self.Sales_Page()
                    print('1')
        self.Dialog.close()

    def Show_search_Widget(self):
        print('yesf')
        self.searchWidget = searchDialog.Dialog()
        # print(self.searchWidget.spinBox.value())
        self.searchWidget.show()
        self.searchWidget.pushButton_20.clicked.connect(self.Search_by_date)

    def Search_by_date(self):
        print('clicked')
        global select_by_date
        select_by_date = True
        self.Show_All_one_client_analyst()
        self.searchWidget.close()

    def add_data_to_my_num(self):
        global My_num
        self.cur.execute(
            ''' SELECT name FROM addanalyst WHERE sub_category=%s OR sub_category=%s Or sub_category=%s ''',
            ('GSE', 'GUE', 'SFA',))
        data = self.cur.fetchall()
        for item in data:
            My_num.append(item[0])

    def add_clients_to_combo(self):
        clients = []
        self.cur.execute(''' SELECT client_name FROM addclient ''')
        data = self.cur.fetchall()
        for row in data:
            if row[0] not in clients:
                clients.append(row[0])
        self.comboBox_4.clear()
        self.comboBox_4.addItem('')
        self.comboBox_4.addItems(clients)

    def ADD_one_REsult_to_ANalyst_results(self):
        global first_text
        first_text = self.comboBox_30.currentText()
        all_items = []
        for row in range(0, self.comboBox_30.count()):
            self.comboBox_30.setCurrentIndex(row)
            all_items.append(str(self.comboBox_30.currentText()))
        if str(first_text) not in all_items and first_text != '':
            self.comboBox_30.addItem(str(first_text))
            self.comboBox_30.setCurrentText('')
        else:
            self.comboBox_30.setCurrentText('')
            QMessageBox.information(self, '', 'هذا العنصر موجود بالفعل')
        # print(first_text,'here my boy')

    def ADD_one_REsult_to_ANalyst_results_IN_EDITMODE(self):
        global first_text2
        first_text2 = self.comboBox_31.currentText()
        all_items = []
        for row in range(0, self.comboBox_31.count()):
            self.comboBox_31.setCurrentIndex(row)
            all_items.append(str(self.comboBox_31.currentText()))
        if str(first_text2) not in all_items and first_text2 != '':
            self.comboBox_31.addItem(str(first_text2))
            self.comboBox_31.setCurrentText('')
        else:
            self.comboBox_31.setCurrentText('')
            QMessageBox.information(self, '', 'هذا العنصر موجود بالفعل')

    def Remove_one_REsult_to_ANalyst_results_IN_EDITMODE(self):
        self.comboBox_31.removeItem(self.comboBox_31.currentIndex())

    def Show_all_clients_without_search(self):
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
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.insertRow(0)
        l_data = ()
        for ih in all_data:
            hs_data = ih[0]['value']
            l_data += tuple(hs_data)
        for row, form in enumerate(l_data):
            for col, item in enumerate(form):
                if col == 3:
                    self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(l_data[row][4])))
                else:
                    self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1

            row_pos2 = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_pos2)

    def my_def(self):
        print('sdge')
        self.cur.execute(''' SELECT client_name FROM addclient ORDER BY -date ''')
        data = self.cur.fetchall()
        all_names = {}
        all_data = []
        id = 0

        for item in data:
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
        # self.tableWidget_2.setRowCount(0)
        # self.tableWidget_2.insertRow(0)
        l_data = ()
        for ih in all_data:
            hs_data = ih[0]['value']
            l_data += tuple(hs_data)
        # print(l_data, 'k')
        for row, form in enumerate(l_data):
            for col, item in enumerate(form):
                if col == 3:
                    self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(l_data[row][4])))
                else:
                    self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            row_pos = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_pos)

    def add_Analyst_to_list(self):
        self.cur.execute(''' SELECT name FROM addanalyst ''')
        data = self.cur.fetchall()
        for i in data:
            if i[0] not in analysts_name_glo:
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
        self.cur.execute(''' SELECT client_name FROM addclient WHERE DATE(date)=%s ''', (datetime.date.today(),))
        data = self.cur.fetchall()
        for i in data:
            if i[0] not in clients_name_glo:
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

    def add_client_to_list4(self):
        self.cur.execute(''' SELECT client_name FROM addclient''')
        data = self.cur.fetchall()
        for i in data:
            if i[0] not in clients_name_glo_clients_page:
                clients_name_glo_clients_page.append(i[0])

    def Auto_Complete4(self, model):
        model.setStringList(clients_name_glo_clients_page)

    def Auto_complete_combo4(self):
        combo = self.lineEdit_27
        completer = QCompleter()
        combo.setCompleter(completer)
        model = QStringListModel()
        completer.setModel(model)
        self.Auto_Complete4(model)

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

            if os.path.exists(r'%s\هرمونات مشترك latest.docx' % save_word_files):
                os.remove(r'%s\هرمونات مشترك latest.docx' % save_word_files)
        except Exception as e:
            word = client.Dispatch("Word.Application")
            word.ActiveDocument.Close()
            self.Delete_Files()
            print(e)

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
        copyes_num = self.spinBox_4.value()
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
        word.Documents.Open(r'%s\%s' % (word_files, file))
        for ihjk in range(1, copyes_num + 1):
            word.ActiveDocument.PrintOut(Background=False)
        QMessageBox.information(self, 'info', 'تمت الطباعة بنجاح')

        # time.sleep(2)
        # pyautogui.press('enter')
        # time.sleep(1.5)
        warning = QMessageBox.warning(self, '',
                                      "هل قمت بطباعة الملفات؟\n لا تضغط نعم الا لو قمت بطباعته",
                                      QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes:
            move = 1
            try:
                word.ActiveDocument.Close()
            except:
                pass
        # word.ActiveDocument.Close()

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
            try:
                if_print = True
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

                if os.path.exists(r'%s\هرمونات مشترك latest.docx' % save_word_files):
                    os.remove(r'%s\هرمونات مشترك latest.docx' % save_word_files)
            except:
                word = client.Dispatch("Word.Application")
                word.ActiveDocument.Close()
                self.Delete_Files()

    def Reset_password(self):
        user_name = self.lineEdit_7.text()
        self.cur.execute(''' SELECT * FROM adduser ''')
        data = self.cur.fetchall()
        ruser_name = ''
        a = 0
        for row in data:
            if row[1] == user_name:
                ruser_name = row[1]
            else:
                a = 5
        if a == 5:
            QMessageBox.information(self, 'info', 'اسم المستخدم الذي ادخلته غير صحيح')
        self.cur.execute(''' SELECT user_email,userpassword FROM adduser WHERE user_name=%s ''', (ruser_name,))
        email_data = self.cur.fetchone()
        email = "ameersaad810@gmail.com"  # the email where you sent the email
        password = "aahmpredtiddvxlo"
        send_to_email = email_data[0]  # for whom
        subject = "n"
        message = f'Hello.\n your password is {email_data[1]} '
        msg = MIMEMultipart()
        msg["From"] = email
        msg["To"] = send_to_email
        msg["Subject"] = subject

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, send_to_email, text)
        server.quit()
        print('ok')

    def clear_data_in_sales(self):
        self.comboBox_17.clear()
        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.insertRow(0)
        self.comboBox_4.clear()
        self.lineEdit_21.setText('')
        self.spinBox_7.setValue(20)
        self.doubleSpinBox_7.setValue(0)
        self.comboBox_14.setCurrentIndex(0)
        self.comboBox_16.setCurrentIndex(0)
        self.comboBox_17.setCurrentIndex(0)
        self.comboBox_15.setEnabled(True)
        self.comboBox_15.setCurrentIndex(0)
        self.textEdit.setPlainText('')
        self.comboBox_4.setEnabled(True)
        self.spinBox_7.setEnabled(True)
        self.comboBox_14.setEnabled(True)
        self.textEdit.setEnabled(True)
        self.spinBox.setValue(0)

    def Show_All_Clients(self):
        global show_all_sales_in_clients_page
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
            else:
                show_all_sales_in_clients_page = True
                self.Show_all_clients_without_search()
        except:
            pass
            # self.tableWidget_2.setRowCount(0)
            # self.tableWidget_2.insertRow(0)

    def Search_In_History(self):
        actionsd = self.comboBox_24.currentIndex()
        tabley = self.comboBox_20.currentIndex()
        if actionsd != 0 and tabley == 0:
            try:
                self.cur.execute(f'SELECT action,tabled,id,dates FROM his WHERE action = {actionsd} ORDER BY -dates')
            except Exception as e:
                print(e)
        elif tabley != 0 and actionsd == 0:
            try:
                self.cur.execute(f'SELECT action,tabled,id,dates FROM his WHERE tabled={tabley} ORDER BY -dates')
            except Exception as e:
                print(e)
        elif actionsd != 0 and tabley != 0:
            try:
                self.cur.execute(
                    f' SELECT action,tabled,id,dates FROM his WHERE action={actionsd} AND tabled={tabley} ORDER BY -dates')

            except Exception as e:
                print(e)
        else:
            try:
                self.cur.execute(
                    f' SELECT action,tabled,id,dates FROM his ORDER BY -dates')

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
            self.cur.execute(''' SELECT * FROM addclient WHERE client_name=%s AND DATE(date)=%s ORDER BY id''',
                             (client_name, datetime.date.today(),))
        else:
            self.cur.execute(''' SELECT * FROM addclient WHERE DATE(date)=%s ORDER BY -date''',
                             (datetime.date.today(),))
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
            else:
                self.Show_All_The_Sales()
        except:
            self.tableWidget_6.setRowCount(0)
            self.tableWidget_6.insertRow(0)
        self.Add_Data_To_history(6, 1)

    def Print_Sale_Data(self, prev):
        genuses = self.comboBox_14.currentIndex()
        all_analyst = []
        all_result = []
        all_units = []
        all_defults = []
        date = datetime.datetime.now()
        day = date.year
        month = date.month
        year = date.day
        word_type = []
        for row in range(0, self.tableWidget_5.rowCount() - 1):
            try:
                real_name = self.tableWidget_5.item(row, 0).text()
                analyst = self.tableWidget_5.item(row, 1).text()
            except:
                pass
            self.cur.execute(''' SELECT sub_category,unit,defult FROM addanalyst WHERE name=%s ''', (analyst,))
            if analyst not in all_analyst:
                all_analyst.append(str(analyst))
            data = self.cur.fetchone()
            if data != None:
                for item in data:
                    word_type.append(data[0])
                    all_units.append(data[1])
                    all_defults.append(data[2])
            try:
                result = self.tableWidget_5.cellWidget(row, 2).currentText()
            except:
                try:
                    result = self.tableWidget_5.item(row, 2).text()
                except:
                    pass
            all_result.append(str(result))
            try:
                real_doctor = self.tableWidget_5.item(row, 3).text()
            except:
                pass
        try:
            self.Bio_Word(real_name, real_doctor, all_analyst, all_result, all_units, all_defults, year, month, day,
                          word_type, prev, genuses)

        except Exception as e:
            print(e)
            QMessageBox.information(self, 'خطأ', 'هنالك خطأ يرجى مراجعة العملية')

        if prev != 'T':
            self.Delete_Files()
        for rowj in range(0, self.tableWidget_5.rowCount() - 1):
            try:
                r2_doctor = self.tableWidget_5.item(rowj, 3).text()
                r2_analyst_name = self.tableWidget_5.item(rowj, 1).text()
                r2_client_name = self.comboBox_4.currentText()
            except:
                pass
            try:
                r2_result = self.tableWidget_5.cellWidget(rowj, 2).currentText()
            except:
                try:
                    r2_result = self.tableWidget_5.item(rowj, 2).text()
                except:
                    pass
            try:
                self.cur.execute(
                    ''' UPDATE addnewitem SET doctor_name=%s ,analyst_name=%s ,analyst_result=%s WHERE client_name=%s AND analyst_name=%s''',
                    (r2_doctor, r2_analyst_name, r2_result, r2_client_name, r2_analyst_name))
                self.db.commit()
            except:
                print('exept')

    def get_total_price(self):
        total_price = 0
        GSE = ['Color:GSE', 'Consistency', 'Pus cells:GSE', 'R.B.Cs:GSE', 'E. Histolytica', 'Ova', 'Other:GSE',
               'Bacteria:GSE', 'Monillia:GSE', 'Fatty drop:GSE']
        GUE = ['Appearance', 'Reaction:GUE', 'Albumin', 'Sugar', 'RBCs:GUE', 'Pus cells:GUE', 'Epith .cells',
               'Crystals', 'Casts', 'Other:GUE', 'Bacteria:GUE', 'Monillia:GUE', 'Mucuse:GUE']
        SFA = ['Volume', 'Reaction:SFA', 'Colour:SFA', 'Liquefaction', 'Motility:Active', 'Motility:Sluggish',
               'Motility:Dead', 'Morphology:Normal', 'Morphology:Abnormal', 'Morphology:Pus cells', 'Other:SFA',
               'Count']
        My_num = ['Appearance', 'Reaction:GUE', 'Albumin', 'Sugar', 'RBCs:GUE', 'Pus cells:GUE', 'Epith .cells',
                  'Crystals',
                  'Casts', 'Other:GUE', 'Volume', 'Reaction:SFA', 'Colour:SFA', 'Liquefaction', 'Motility:Active',
                  'Motility:Sluggish', 'Motility:Dead', 'Morphology:Normal', 'Morphology:Abnormal',
                  'Morphology:Pus cells', 'Other:SFA', 'Color:GSE', 'Consistency', 'E. Histolytica', 'G. Lembilia',
                  'Ova', 'Pus cells:GSE', 'R.B.Cs:GSE', 'Bacteria:GSE', 'Bacteria:GUE', 'Monillia:GSE', 'Monillia:GUE',
                  'Fatty drop:GSE', 'Fatty drop:GUE', 'Mucuse:GUE']
        c_GSE = False
        c_GUE = False
        c_SFA = False
        rMy_num = 0
        for row in range(0, self.tableWidget_5.rowCount() - 1):
            try:
                analyst_name = self.tableWidget_5.item(row, 1).text()
            except:
                analyst_name = ''
            for kg in GSE:
                if kg == analyst_name:
                    c_GSE = True
            for kg1 in GUE:
                if kg1 == analyst_name:
                    c_GUE = True
            for kg2 in SFA:
                if kg2 == analyst_name:
                    c_SFA = True
            try:
                a = self.tableWidget_5.item(row, 4).text()
            except:
                a = 0
            try:
                total_price += int(a)
            except ValueError:
                a = 0
        if c_SFA == True:
            total_price += 3
        if c_GSE == True:
            total_price += 3
        if c_GUE == True:
            total_price += 3
        self.lineEdit_24.setText(str(total_price))

    def Sales_Page(self):
        print('iam run')
        # if self.comboBox_4.currentText()=='':
        #     QMessageBox.information(self,'تحذير','يرجى ادخال اسم المراجع')
        self.comboBox_4.setEnabled(False)
        self.spinBox_7.setEnabled(False)
        self.comboBox_14.setEnabled(False)
        self.comboBox_15.setEnabled(False)
        self.textEdit.setEnabled(False)
        global client_id_glob
        global chick_if_add_new
        global clients_name_glo
        global My_num
        # My_num = ['Appearance', 'Reaction:GUE', 'Albumin', 'Sugar', 'RBCs:GUE', 'Pus cells:GUE', 'Epith .cells',
        #           'Crystals',
        #           'Casts', 'Other:GUE', 'Volume', 'Reaction:SFA', 'Colour:SFA', 'Liquefaction', 'Motility:Active',
        #           'Motility:Sluggish', 'Motility:Dead', 'Morphology:Normal', 'Morphology:Abnormal',
        #           'Morphology:Pus cells', 'Other:SFA', 'Color:GSE', 'Consistency', 'E. Histolytica', 'G. Lembilia',
        #           'Ova', 'Pus cells:GSE', 'R.B.Cs:GSE', 'Bacteria:GSE', 'Bacteria:GUE', 'Monillia:GSE', 'Monillia:GUE',
        #           'Fatty drop:GSE', 'Fatty drop:GUE', 'Mucuse:GUE']
        analyst_name = self.comboBox_16.currentText()
        client_name = self.comboBox_4.currentText()
        client_age = self.spinBox_7.value()
        client_genus = self.comboBox_14.currentText()
        client_doctor = self.comboBox_15.currentText()
        client_genus = self.comboBox_14.currentText()
        analyst_or_clients_notes = self.textEdit.toPlainText()
        analyst_lineEdit_result = self.lineEdit_21.text()
        analyst_combo_result = self.comboBox_17.currentText()
        analyst_number_result = self.doubleSpinBox_7.value()
        client_id = self.spinBox.value()

        self.cur.execute('''SELECT price,category,sub_category FROM addanalyst WHERE name = %s''', (analyst_name,))
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
        clients_name_glo.append(str(client_name))
        for rowj in range(0, self.tableWidget_5.rowCount() - 1):
            try:
                r2_doctor = self.tableWidget_5.item(rowj, 3).text()
                r2_analyst_name = self.tableWidget_5.item(rowj, 1).text()
                r2_client_name = self.comboBox_4.currentText()
            except:
                r2_client_name = ''
                r2_analyst_name = ''
                r2_doctor = ''
            try:
                r2_result = self.tableWidget_5.cellWidget(rowj, 2).currentText()
            except:
                try:
                    r2_result = self.tableWidget_5.item(rowj, 2).text()
                except:
                    r2_result = ''
            try:
                self.cur.execute(
                    ''' UPDATE addnewitem SET doctor_name=%s ,analyst_name=%s ,analyst_result=%s WHERE client_name=%s AND analyst_name=%s''',
                    (r2_doctor, r2_analyst_name, r2_result, r2_client_name, r2_analyst_name))
                self.db.commit()
            except:
                print('except')
        self.cur.execute(
            ''' SELECT client_name,analyst_name,analyst_result,doctor_name,total_price FROM addnewitem WHERE client_name = %s AND DATE(date)=%s''',
            (self.comboBox_4.currentText(), datetime.date.today(),))
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
        chick_if_add_new = True
        try:
            axd1 = self.tableWidget_5.findItems('Fatty drop:GSE', Qt.MatchContains)
            axd2 = self.tableWidget_5.findItems('Mucuse:GUE', Qt.MatchContains)
            axd3 = self.tableWidget_5.findItems('Morphology:Pus cells', Qt.MatchContains)
            self.tableWidget_5.insertRow(axd1[0].row() + 1)
            # self.tableWidget_5.insertRow(axd1[0].row() + 2)
            self.tableWidget_5.insertRow(axd2[0].row() + 1)
            # self.tableWidget_5.insertRow(axd2[0].row() + 2)
            self.tableWidget_5.insertRow(axd3[0].row() + 1)
            # self.tableWidget_5.insertRow(axd3[0].row() + 2)
        except:
            pass
        for rowd in range(0, self.tableWidget_5.rowCount() - 1):
            all_name_items = []
            try:
                name = self.tableWidget_5.item(rowd, 0).text()
            except:
                pass
            try:
                rs_name = self.tableWidget_5.item(rowd, 1).text()
            except:
                rs_name = ''
            self.cur.execute('''SELECT results,category FROM addanalyst WHERE name=%s''', (rs_name,))
            results_data = self.cur.fetchall()
            mycobmbo = None
            object_type = ''
            if results_data:
                if results_data[0][1] == 'خيارات':
                    mycobmbo = QComboBox(self)
                    list_data = str(results_data[0][0]).replace("'", "")
                    list_data = list_data.split(',')
                    mycobmbo.addItems(list_data)
                    object_type = 'خيارات'
                if results_data[0][1] == 'عدد':
                    mycobmbo = QDoubleSpinBox(self)
                    object_type = 'عدد'
                if results_data[0][1] == 'خيارات مع تعديل':
                    mycobmbo = QComboBox(self)
                    mycobmbo.setEditable(True)
                    mycobmbo.addItems(results_data[0][0])
                    object_type = 'خيارات مع تعديل'
                if results_data[0][1] == 'حقل كتابة':
                    mycobmbo = QLineEdit(self)
                    object_type = 'حقل كتابة'
                # self.tableWidget_5.setItem(rowd, 0, QTableWidgetItem(the_name))
                # if rs_name == 'Color:GSE' or rs_name == 'Colour:SFA':
                #     mycobmbo = QComboBox(self)
                #     mycobmbo.addItems(['yallow', 'brown', 'green', 'milk'])
                # if rs_name == 'Consistency':
                #     mycobmbo = QComboBox(self)
                #     mycobmbo.addItems(['Solid', 'Liquid', 'Semi solid', 'Semi liquid', 'Mucoid'])
                # if rs_name == 'R.B.Cs:GSE' or rs_name == 'Pus cells:GSE' or rs_name == 'RBCs:GUE' or rs_name == 'Pus cells:GUE':
                #     mycobmbo = QComboBox(self)
                #     mycobmbo.addItems(['1 - 2', '1 - 3', '2 - 3', '2 - 4', '0 - 1', '0 - 2', '3 - 5', '4 - 6', '5 - 6',
                #                        '5 - 7', '6 - 8', '6 - 7', '+', '++', '+++', '++++', 'Full Field'])
                # if rs_name == 'E. Histolytica' or rs_name == 'G. Lembilia':
                #     mycobmbo = QComboBox(self)
                #     mycobmbo.addItems(['Cyst', 'Trophozoite'])
                # if rs_name == 'Ova':
                #     mycobmbo = QComboBox(self)
                #     mycobmbo.addItems(['Nill'])
                # if rs_name == 'Appearance':
                #     mycobmbo = QComboBox(self)
                #     mycobmbo.addItems(['Turbid', 'Clear'])
                # if rs_name == 'Reaction:GUE' or rs_name == 'Reaction:SFA':
                #     mycobmbo = QComboBox(self)
                #     mycobmbo.addItems(['Acidic', 'Alkaline'])
                # if rs_name == 'Albumin' or rs_name == 'Sugar':
                #     mycobmbo = QComboBox(self)
                #     mycobmbo.addItems(['Nil', '+', '++', '+++', 'Trace'])
                # if rs_name == 'Epith .cells':
                #     mycobmbo = QComboBox(self)
                #     mycobmbo.addItems(['Few', '+', '++', '+++', '++++'])
                # if rs_name == 'Crystals':
                #     mycobmbo = QComboBox(self)
                #     mycobmbo.addItems(['Am.Urate', 'Am.Phosphatase', 'Uric Acid', 'Ca.Oxalate'])
                # if rs_name == 'Casts':
                #     mycobmbo = QComboBox(self)
                #     mycobmbo.addItems(['Granular cast +', 'Granular cast ++', 'Granular cast +++'])
                #
                # if rs_name == 'Bacteria:GSE' or rs_name == 'Monillia:GSE' or rs_name == 'Fatty drop:GSE' or rs_name == 'Monillia:GUE' or rs_name == 'Fatty drop:GUE' or rs_name == 'Bacteria:GUE' or rs_name == 'Mucuse:GUE':
                #     mycobmbo = QComboBox(self)
                #     mycobmbo.addItems(['Few', '+', '++', '+++', '++++'])
                # if rs_name == 'Motility:Active' or rs_name == 'Motility:Sluggish' or rs_name == 'Motility:Dead' or rs_name == 'Morphology:Normal' or rs_name == 'Morphology:Abnormal' or rs_name == 'Morphology:Pus cells':
                #     mycobmbo = QComboBox(self)
                #     mycobmbo.addItems(
                #         ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60', '65', '70', '75', '80',
                #          '85'])
                # if rs_name == 'Volume':
                #     mycobmbo = QComboBox(self)
                #     mycobmbo.addItems(['0.5', '0.6', '0.7'])
                # if rs_name == 'Liquefaction':
                #     mycobmbo = QComboBox(self)
                #     mycobmbo.addItems(['5', '10', '15', '20', '25', '30', '35', '40', '45'])
                # print('mystatrt')

                r2_analyst_name = self.tableWidget_5.item(rowd, 1).text()
                r2_client_name = self.comboBox_4.currentText()
                self.cur.execute(
                    ''' SELECT  analyst_result  FROM addnewitem WHERE client_name=%s AND analyst_name=%s ''',
                    (r2_client_name, r2_analyst_name))
                myrs = self.cur.fetchall()
                if myrs != None:
                    if object_type == 'خيارات' or object_type == 'خيارات مع تعديل':
                        index = mycobmbo.findText(myrs[0][0], Qt.MatchFixedString)
                        mycobmbo.setCurrentIndex(index)
                    if object_type == 'عدد':
                        print('Tru')
                        if myrs[0][0] and myrs[0][0] != '':
                            mycobmbo.setValue(float(int(myrs[0][0])))
                    if object_type == 'حقل كتابة':
                        mycobmbo.setText(str(myrs[0][0]))
                self.tableWidget_5.setItem(rowd, 2, QTableWidgetItem(str('')))
                self.tableWidget_5.setCellWidget(rowd, 2, mycobmbo)
                if object_type == 'خيارات' or object_type == 'خيارات مع تعديل':
                    if mycobmbo.currentText() == '' or mycobmbo.currentText() == ' ':
                        mycobmbo.setCurrentIndex(0)
        self.tableWidget_5.scrollToBottom()
        self.get_total_price()
        self.Show_All_The_Sales()
        self.Show_all_clients_without_search()
        self.Add_Data_To_history(3, 1)
        self.History()
        # self.add_clients_to_combo()

    def Show_All_one_client_analyst(self):
        global client_id_glob
        global chick_if_add_new
        global select_by_date
        # print(select_by_date)
        My_num = ['Appearance', 'Reaction:GUE', 'Albumin', 'Sugar', 'RBCs:GUE', 'Pus cells:GUE', 'Epith .cells',
                  'Crystals',
                  'Casts', 'Other:GUE', 'Volume', 'Reaction:SFA', 'Colour:SFA', 'Liquefaction', 'Motility:Active',
                  'Motility:Sluggish', 'Motility:Dead', 'Morphology:Normal', 'Morphology:Abnormal',
                  'Morphology:Pus cells', 'Other:SFA', 'Color:GSE', 'Consistency', 'E. Histolytica', 'G. Lembilia',
                  'Ova', 'Pus cells:GSE', 'R.B.Cs:GSE', 'Bacteria:GSE', 'Bacteria:GUE', 'Monillia:GSE', 'Monillia:GUE',
                  'Fatty drop:GSE', 'Fatty drop:GUE', 'Mucuse:GUE']
        client_name = self.comboBox_4.currentText()
        # self.cur.execute('''
        #      SELECT client_name,analyst_name,analyst_result,doctor_name FROM addnewitem WHERE client_name = %s AND DATE(date)=%s
        # ''', (client_name,))
        # analyst_data = self.cur.fetchall()
        # need doctor name enabled i will make it with current text
        if self.spinBox.value() == 0 and chick_if_add_new == False:
            self.tableWidget_5.setRowCount(0)
            self.tableWidget_5.insertRow(0)
            self.comboBox_4.clear()
            self.lineEdit_21.setText('')
            self.spinBox_7.setValue(0)
            self.doubleSpinBox_7.setValue(0)
            self.comboBox_14.setCurrentIndex(0)
            self.comboBox_17.setCurrentIndex(0)
            self.textEdit.setPlainText('')
            self.comboBox_4.setEnabled(True)
            self.spinBox_7.setEnabled(True)
            self.comboBox_14.setEnabled(True)
            self.textEdit.setEnabled(True)
        if self.spinBox.value() != 0:
            if True:
                if select_by_date:
                    id = self.searchWidget.spinBox.value()
                    # print(id, 'jjj')
                    from_date = self.searchWidget.dateEdit_6.date()
                    to_date = self.searchWidget.dateEdit_5.date()
                    self.cur.execute(
                        '''SELECT client_name,analyst_name,analyst_result,doctor_name,total_price,client_id,client_age,genus,notes FROM addnewitem WHERE client_id = %s AND DATE(date)>=%s AND DATE(date)<=%s''',
                        (id, str(from_date.toPyDate()), str(to_date.toPyDate()),))
                else:
                    print('else3')
                    self.cur.execute(
                        '''SELECT client_name,analyst_name,analyst_result,doctor_name,total_price,client_age,genus,notes FROM addnewitem WHERE client_id = %s AND DATE(date)=%s''',
                        (self.spinBox.value(), datetime.date.today(),))
                analyst_data = self.cur.fetchall()
                # print(analyst_data)
                self.comboBox_15.setCurrentText(str(analyst_data[0][3]))
                self.comboBox_15.setEnabled(False)
                self.comboBox_14.setEnabled(False)
                self.comboBox_4.setCurrentText(analyst_data[0][0])
                self.comboBox_4.setEnabled(False)
                self.spinBox_7.setValue(int(analyst_data[0][5]))
                self.spinBox_7.setEnabled(False)
                if analyst_data[0][6] == 'ذكر':
                    self.comboBox_14.setCurrentIndex(1)
                    self.comboBox_14.setEnabled(False)
                if analyst_data[0][6] == 'انثى':
                    self.comboBox_14.setCurrentIndex(0)
                    self.comboBox_14.setEnabled(False)
                self.textEdit.setPlainText(str(analyst_data[0][7]))
                self.textEdit.setEnabled(False)

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

                try:
                    axd1 = self.tableWidget_5.findItems('Fatty drop:GSE', Qt.MatchContains)
                    axd2 = self.tableWidget_5.findItems('Mucuse:GUE', Qt.MatchContains)
                    axd3 = self.tableWidget_5.findItems('Morphology:Pus cells', Qt.MatchContains)
                    self.tableWidget_5.insertRow(axd1[0].row() + 1)
                    # self.tableWidget_5.insertRow(axd1[0].row() + 2)
                    self.tableWidget_5.insertRow(axd2[0].row() + 1)
                    # self.tableWidget_5.insertRow(axd2[0].row() + 2)
                    self.tableWidget_5.insertRow(axd3[0].row() + 1)
                    # self.tableWidget_5.insertRow(axd3[0].row() + 2)
                except:
                    print('ecxehue')
                    pass
                for rowd in range(0, self.tableWidget_5.rowCount() - 1):
                    all_name_items = []
                    name = ''
                    try:
                        name = self.tableWidget_5.item(rowd, 0).text()
                    except:
                        name = ''
                    self.tableWidget_5.setItem(rowd, 0, QTableWidgetItem(name))
                    try:
                        rs_name = self.tableWidget_5.item(rowd, 1).text()
                    except:
                        rs_name = ''
                    self.cur.execute('''SELECT results,category FROM addanalyst WHERE name=%s''', (rs_name,))
                    results_data = self.cur.fetchall()
                    mycobmbo = None
                    object_type = ''
                    if results_data:
                        if results_data[0][1] == 'خيارات':
                            mycobmbo = QComboBox(self)
                            list_data = str(results_data[0][0]).replace("'", "")
                            list_data = list_data.split(',')
                            mycobmbo.addItems(list_data)
                            object_type = 'خيارات'
                        if results_data[0][1] == 'عدد':
                            mycobmbo = QDoubleSpinBox(self)
                            object_type = 'عدد'
                        if results_data[0][1] == 'خيارات مع تعديل':
                            mycobmbo = QComboBox(self)
                            mycobmbo.setEditable(True)
                            mycobmbo.addItems(results_data[0][0])
                            object_type = 'خيارات مع تعديل'
                        if results_data[0][1] == 'حقل كتابة':
                            mycobmbo = QLineEdit(self)
                            object_type = 'حقل كتابة'
                        # self.tableWidget_5.setItem(rowd, 0, QTableWidgetItem(the_name))
                        # if rs_name == 'Color:GSE' or rs_name == 'Colour:SFA':
                        #     mycobmbo = QComboBox(self)
                        #     mycobmbo.addItems(['yallow', 'brown', 'green', 'milk'])
                        # if rs_name == 'Consistency':
                        #     mycobmbo = QComboBox(self)
                        #     mycobmbo.addItems(['Solid', 'Liquid', 'Semi solid', 'Semi liquid', 'Mucoid'])
                        # if rs_name == 'R.B.Cs:GSE' or rs_name == 'Pus cells:GSE' or rs_name == 'RBCs:GUE' or rs_name == 'Pus cells:GUE':
                        #     mycobmbo = QComboBox(self)
                        #     mycobmbo.addItems(['1 - 2', '1 - 3', '2 - 3', '2 - 4', '0 - 1', '0 - 2', '3 - 5', '4 - 6', '5 - 6',
                        #                        '5 - 7', '6 - 8', '6 - 7', '+', '++', '+++', '++++', 'Full Field'])
                        # if rs_name == 'E. Histolytica' or rs_name == 'G. Lembilia':
                        #     mycobmbo = QComboBox(self)
                        #     mycobmbo.addItems(['Cyst', 'Trophozoite'])
                        # if rs_name == 'Ova':
                        #     mycobmbo = QComboBox(self)
                        #     mycobmbo.addItems(['Nill'])
                        # if rs_name == 'Appearance':
                        #     mycobmbo = QComboBox(self)
                        #     mycobmbo.addItems(['Turbid', 'Clear'])
                        # if rs_name == 'Reaction:GUE' or rs_name == 'Reaction:SFA':
                        #     mycobmbo = QComboBox(self)
                        #     mycobmbo.addItems(['Acidic', 'Alkaline'])
                        # if rs_name == 'Albumin' or rs_name == 'Sugar':
                        #     mycobmbo = QComboBox(self)
                        #     mycobmbo.addItems(['Nil', '+', '++', '+++', 'Trace'])
                        # if rs_name == 'Epith .cells':
                        #     mycobmbo = QComboBox(self)
                        #     mycobmbo.addItems(['Few', '+', '++', '+++', '++++'])
                        # if rs_name == 'Crystals':
                        #     mycobmbo = QComboBox(self)
                        #     mycobmbo.addItems(['Am.Urate', 'Am.Phosphatase', 'Uric Acid', 'Ca.Oxalate'])
                        # if rs_name == 'Casts':
                        #     mycobmbo = QComboBox(self)
                        #     mycobmbo.addItems(['Granular cast +', 'Granular cast ++', 'Granular cast +++'])
                        #
                        # if rs_name == 'Bacteria:GSE' or rs_name == 'Monillia:GSE' or rs_name == 'Fatty drop:GSE' or rs_name == 'Monillia:GUE' or rs_name == 'Fatty drop:GUE' or rs_name == 'Bacteria:GUE' or rs_name == 'Mucuse:GUE':
                        #     mycobmbo = QComboBox(self)
                        #     mycobmbo.addItems(['Few', '+', '++', '+++', '++++'])
                        # if rs_name == 'Motility:Active' or rs_name == 'Motility:Sluggish' or rs_name == 'Motility:Dead' or rs_name == 'Morphology:Normal' or rs_name == 'Morphology:Abnormal' or rs_name == 'Morphology:Pus cells':
                        #     mycobmbo = QComboBox(self)
                        #     mycobmbo.addItems(
                        #         ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60', '65', '70', '75', '80',
                        #          '85'])
                        # if rs_name == 'Volume':
                        #     mycobmbo = QComboBox(self)
                        #     mycobmbo.addItems(['0.5', '0.6', '0.7'])
                        # if rs_name == 'Liquefaction':
                        #     mycobmbo = QComboBox(self)
                        #     mycobmbo.addItems(['5', '10', '15', '20', '25', '30', '35', '40', '45'])
                        # print('mystatrt')

                        r2_analyst_name = self.tableWidget_5.item(rowd, 1).text()
                        r2_client_name = self.comboBox_4.currentText()
                        self.cur.execute(
                            ''' SELECT  analyst_result  FROM addnewitem WHERE client_name=%s AND analyst_name=%s ''',
                            (r2_client_name, r2_analyst_name))
                        myrs = self.cur.fetchall()
                        if myrs != None:
                            if object_type == 'خيارات' or object_type == 'خيارات مع تعديل':
                                print('ssm,lskwow')
                                index = mycobmbo.findText(myrs[0][0], Qt.MatchFixedString)
                                mycobmbo.setCurrentIndex(index)
                            if object_type == 'عدد':
                                print('Tru')
                                if myrs[0][0] and myrs[0][0]!='':
                                    mycobmbo.setValue(float(int(myrs[0][0])))
                            if object_type == 'حقل كتابة':
                                mycobmbo.setText(str(myrs[0][0]))
                        self.tableWidget_5.setItem(rowd, 2, QTableWidgetItem(str('')))
                        self.tableWidget_5.setCellWidget(rowd, 2, mycobmbo)
                        if object_type == 'خيارات' or object_type == 'خيارات مع تعديل':
                            if mycobmbo.currentText() == '' or mycobmbo.currentText() == ' ':
                                mycobmbo.setCurrentIndex(0)




            # except Exception as e:
            #     print(e)
            #     QMessageBox.information(self, 'Error',
            #                             'الرقم الذي ادخلته غير صحيح يرجى ادخال رقم صحيح او مراجعة صفحة "كل المبيعات" للتأكد من الرقم')
            self.get_total_price()
            select_by_date = False
    def analyst_category_function(self,name):
        global addTrue
        print('starthh')
        # pationt_name = self.comboBox_4.currentText()
        # doctor_name = self.comboBox_15.currentText()
        analyst_name = self.comboBox_16.currentText()
        self.cur.execute('''SELECT category,results FROM addanalyst WHERE name = %s''', (analyst_name,))
        analyst_category = self.cur.fetchone()
        try:
            if analyst_category:
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
        except Exception as e:
            print(e)
            if name not in mylist:
                if not addTrue:
                    QMessageBox.information(self, 'تحذير', "يرجى اختيار تحليل صحيح")
        row_count = self.tableWidget_5.rowCount()
        print(name, 'here name')
        if name in mylist:
            # QStatusBar.showMessage(self,'يرجى الانتظار سيتم تنفيذ طلبك خلال ثواني')

            self.cur.execute('''SELECT name FROM addanalyst WHERE sub_category=%s ''',(str(name),))
            my_DATA = self.cur.fetchall()
            # print(GSE_DATA)
            for new in my_DATA:
                print(new[0])
                self.comboBox_16.setCurrentText(str(new[0]))
                self.Sales_Page()
                print('2')
            self.comboBox_16.setCurrentIndex(0)
        else:
            print('error here2')
        # if analyst_name == 'Full GUE':
        #     # QStatusBar.showMessage(self,'يرجى الانتظار سيتم تنفيذ طلبك خلال ثواني')
        #     self.cur.execute(''' SELECT name FROM addanalyst WHERE sub_category='GUE' ''')
        #     GUE_DATA = self.cur.fetchall()
        #     for new2 in GUE_DATA:
        #         self.comboBox_16.setCurrentText(str(new2[0]))
        #         self.Sales_Page()
        #     self.comboBox_16.setCurrentIndex(0)
        # if analyst_name == 'Full SFA':
        #     # QStatusBar.showMessage(self,'يرجى الانتظار سيتم تنفيذ طلبك خلال ثواني')
        #     self.cur.execute(''' SELECT name FROM addanalyst WHERE sub_category='SFA' ''')
        #     SFA_DATA = self.cur.fetchall()
        #     for new3 in SFA_DATA:
        #         self.comboBox_16.setCurrentText(str(new3[0]))
        #         self.Sales_Page()
        #     self.comboBox_16.setCurrentIndex(0)

        # colors = ['yallow', 'brown', 'green', 'milk']
        # RBCs_Pus_cells_GUE_GSE = ['1 - 2', '1 - 3', '2 - 3', '2 - 4', '0 - 1', '0 - 2', '3 - 5', '4 - 6', '5 - 6',
        #                           '5 - 7', '6 - 8', '6 - 7', '+', '++', '+++', '++++', 'Full Field']
        # Consistency = ['Solid', 'Liquid', 'Semi solid', 'Semi liquid', 'Mucoid']
        # G_Lembilia_E_Histolytica = ['Cyst', 'Trophozoite']
        # Epith_cells = ['Few', '+', '++', '+++', '++++']
        # Ova = ['Nil']
        # Appearance = ['Turbid', 'Clear']
        # Reaction = ['Acidic', 'Alkaline']
        # Sugar = ['Nil', '+', '++', '+++', 'Trace']
        # Crystals = ['Am.Urate', 'Am.Phosphatase', 'Uric Acid', 'Ca.Oxalate']
        # Casts = ['Granular cast +', 'Granular cast ++', 'Granular cast +++']
        # Blood_Group = ['A (+ve)', 'B (+ve)', 'AB (+ve)', 'O (+ve)', 'O (-ve)', 'A (-ve)', 'B (-ve)', 'AB (-ve)']
        # Pregnancy_test_in_urine_serum = ['Positive (+ve)', 'Negative (-ve)', 'Weak Positive']
        # Pregnancy_test_in_urine_serum2 = ['Positive (+ve)', 'Negative (-ve)']
        # Blood_Group = ['A(+ve)', 'B(+ve)', 'AB(+ve)', 'O(+ve)', 'O(-ve)', 'A(-ve)', 'B(-ve)', 'AB(-ve)']
        # test = ['Toxoplasma IgG', 'Toxoplasma IgM', 'Cytomegalo Virus IgG', 'Cytomegalo Virus IgM', 'Rubella IgG',
        #         'Rubella IgM', 'Anti - Phspholipin IgG', 'Anti - Phspholipin  IgM', 'Anti - Cardiolipin  IgG',
        #         'Anti - Cardiolipin  IgM', 'Herps   IgG', 'Herpes  IgM']
        # test_choices = ['0.5 Negative', '0.6 Negative', '0.7 Negative', '0.8 Negative', '1.1 Positive', '1.1 Positive',
        #                 '1.2 Positive', '1.3 Positive', '1.4 Positive', '1.5 Positive']
        # Hb = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        # motility = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
        if analyst_category:
            try:
                self.comboBox_17.clear()
                list_data = str(analyst_category[1]).replace("'", "")
                list_data = list_data.split(',')
                # print(list_data[1])
                for rr in range(0, len(list_data)):
                    self.comboBox_17.addItem(list_data[rr])
            except:
                print('erorr here')
    def Chick_analyst_category(self,item=None):
        # print(item,'here')
        global mylist
        global sd

        if self.comboBox_16.currentText() not in mylist and self.comboBox_16.currentIndex() != 0:
            # self.analyst_category_function(self.comboBox_16.currentText())
            pass
        if self.comboBox_16.currentText() in mylist:
            if self.comboBox_16.currentIndex() != 0:
                try:
                    ritem=self.comboBox_16.model().itemFromIndex(sd)
                    if ritem.checkState()==Qt.Unchecked:
                        ritem.setCheckState(Qt.Checked)
                        self.analyst_category_function(ritem.text())
                    else:
                        ritem.setCheckState(Qt.Unchecked)
                    # ritem.setCheckState(Qt.Unchecked)
                except Exception as e:
                    print(e)
                    print('erorr 404')

    def get_client_id(self):
        global client_id_glob
        client_id_glob = self.spinBox.value()
        self.Show_All_one_client_analyst()
        self.Add_Data_To_history(6, 1)
        self.History()

    def Show_All_The_Sales(self):
        global show_all_sales_in_clients_page
        self.cur.execute(''' SELECT client_name FROM addclient WHERE DATE(date)=%s ORDER BY -date ''',
                         (datetime.date.today(),))
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
        # if show_all_sales_in_clients_page:
        #     self.tableWidget_2.setRowCount(0)
        #     self.tableWidget_2.insertRow(0)
        l_data = ()
        for ih in all_data:
            hs_data = ih[0]['value']
            l_data += tuple(hs_data)
        for row, form in enumerate(l_data):
            for col, item in enumerate(form):
                if col == 3:
                    self.tableWidget_6.setItem(row, col, QTableWidgetItem(str(l_data[row][4])))
                    # if show_all_sales_in_clients_page:
                    #
                    #     self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(l_data[row][4])))
                else:
                    self.tableWidget_6.setItem(row, col, QTableWidgetItem(str(item)))
                    # if show_all_sales_in_clients_page:
                    #     self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            row_pos = self.tableWidget_6.rowCount()
            self.tableWidget_6.insertRow(row_pos)
            # if show_all_sales_in_clients_page:
            #     row_pos2 = self.tableWidget_2.rowCount()
            #     self.tableWidget_2.insertRow(row_pos2)
        # print(all_data)

    def Show_All_The_Analysts(self):
        global from_start
        search_type = self.comboBox_19.currentText()
        search_words = self.lineEdit_26.text()

        if self.comboBox_19.currentIndex() == 1:
            self.cur.execute(
                ''' SELECT name,category,defult,unit,price,sub_category FROM addanalyst WHERE name=%s ''',
                (search_words,))
        if self.comboBox_19.currentIndex() == 2:
            self.cur.execute(
                ''' SELECT name,category,defult,unit,price,sub_category FROM addanalyst WHERE price=%s ''',
                (search_words,))
        if self.comboBox_19.currentIndex() == 3:
            self.cur.execute(
                ''' SELECT name,category,defult,unit,price,sub_category FROM addanalyst WHERE sub_category=%s ''',
                (search_words,))
        if self.comboBox_19.currentIndex() == 0:
            self.cur.execute(
                ''' SELECT name,category,defult,unit,price,sub_category FROM addanalyst ORDER BY sub_category''')

        # combobox_value = ''
        # sql = ''
        # if search_type == 'اسم التحليل المطابق':
        #     combobox_value = 'name'
        # if search_type == 'السعر المطابق':
        #     combobox_value = 'price'
        # if search_type != 'اسم التحليل المطابق' and search_type != 'السعر المطابق':
        #     sql = ''' SELECT name,category,default_result1,default_result2,price,sub_category FROM addanalyst'''
        # else:
        #     sql = f' SELECT name,category,default_result1,default_result2,price,sub_category FROM addanalyst WHERE {combobox_value}=%s'
        # if type(search_words) == int:
        #     self.cur.execute(sql, search_words)
        # if type(search_words) == str:
        #     self.cur.execute(sql, search_words)

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
                if col == 5:
                    self.tableWidget_7.setItem(row, col, QTableWidgetItem(str(analyst_data[row][5])))

                self.tableWidget_7.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            row_pos = self.tableWidget_7.rowCount()
            self.tableWidget_7.insertRow(row_pos)
        if from_start:
            pass
        else:
            self.Add_Data_To_history(6, 2)
            self.History()

    def Add_Analyst(self):
        analyst_name = self.lineEdit_28.text()
        analyst_result_category = self.comboBox_22.currentText()
        analyst_price = self.spinBox_5.value()
        sub_category = self.comboBox_23.currentText()
        date = datetime.datetime.now()
        defult = self.textEdit_2.toPlainText()
        unit = self.textEdit_3.toPlainText()
        results_number = self.comboBox_30.count()
        results = []
        for i in range(0, results_number):
            self.comboBox_30.setCurrentIndex(i)
            results.append(str(self.comboBox_30.currentText()))
        # print(str(results))
        self.cur.execute(
            ''' INSERT INTO addanalyst (name,price,category,sub_category,date,defult,unit,results) VALUES(%s,%s,%s,%s,%s,%s,%s,%s) ''',
            (
                analyst_name, analyst_price, analyst_result_category, sub_category,
                date, defult, unit, str(results)[1:-1]))
        self.db.commit()
        QMessageBox.information(self, 'info', 'تم اضافة التحليل بنجاح')
        self.lineEdit_28.setText('')  # analyst_name =
        self.comboBox_22.setCurrentIndex(0)  # analyst_result_category =
        self.spinBox_5.setValue(0)  # analyst_price =
        self.comboBox_23.setCurrentIndex(0)  # sub_category =
        self.Show_all_analysts_in_combo()
        self.Add_Data_To_history(3, 2)
        self.History()

    def Show_analyst_in_Edit_Or_Delete(self):
        self.comboBox_31.clear()
        analyst_current_name = self.comboBox_21.currentText()
        analyst_current_index = self.comboBox_21.currentIndex()
        if not analyst_current_index:
            # QMessageBox.information(self, 'تحذير', "يرجى اختيار تحليل صحيح")
            self.comboBox_26.setCurrentText('')  # sub_category =
            self.comboBox_26.setCurrentIndex(0)  # sub_category =
            self.comboBox_25.setCurrentIndex(0)  # sub_category =
            self.lineEdit_29.setText('')  # analyst_name =
            self.comboBox_25.setCurrentText('')  # analyst_result_category =
            self.textEdit_5.setPlainText('')  # defult =
            self.textEdit_4.setPlainText('')  # unit =
            self.spinBox_6.setValue(0)  # analyst_price =
        else:
            self.cur.execute(
                ''' SELECT name,defult,unit,price,category,sub_category,results FROM addanalyst WHERE name=%s ''',
                (analyst_current_name,))
            data = self.cur.fetchall()
            if data:
                if data[0][6]:
                    list_data = str(data[0][6]).replace("'", "")
                    list_data = list_data.split(',')
                    # print(list(list_data))
                    # print(list_data)
                    # print(list_data[1])
                    for rr in range(0, len(list_data)):
                        self.comboBox_31.addItem(list_data[rr])  # results =
                self.comboBox_26.setCurrentText(str(data[0][5]))  # sub_category =
                self.lineEdit_29.setText(str(data[0][0]))  # analyst_name =
                self.comboBox_25.setCurrentText(str(data[0][4]))  # analyst_result_category =
                self.textEdit_5.setPlainText(data[0][1])  # defult =
                self.textEdit_4.setPlainText(data[0][2])  # unit =
                self.spinBox_6.setValue(data[0][3])  # analyst_price =
            # self.Add_Data_To_history(6, 2)
            # self.History()

    def Edit_Analyst(self):
        analyst_current_name = self.comboBox_21.currentText()
        analyst_name = self.lineEdit_29.text()
        analyst_result_category = self.comboBox_25.currentText()
        defult = self.textEdit_5.toPlainText()
        unit = self.textEdit_4.toPlainText()
        analyst_price = self.spinBox_6.value()
        sub_category = self.comboBox_26.currentText()
        date = datetime.datetime.now()
        results_number = self.comboBox_31.count()
        results = []
        for i in range(0, results_number):
            self.comboBox_31.setCurrentIndex(i)
            results.append(str(self.comboBox_31.currentText()))
        mysql = '''UPDATE addanalyst SET name=%s,defult=%s,unit=%s,price=%s,category=%s,sub_category=%s,date=%s,results=%s where name=%s'''
        values = (
            analyst_name, defult, unit, analyst_price, analyst_result_category, sub_category, date, str(results)[1:-1],
            analyst_name)
        self.cur.execute(mysql, values)
        self.db.commit()
        QMessageBox.information(self, 'info', 'تم تعديل التحليل بنجاح')
        self.comboBox_21.setCurrentIndex(0)  # analyst_current_name =
        self.lineEdit_29.setText('')  # analyst_name =
        self.comboBox_25.setCurrentIndex(0)  # analyst_result_category =
        self.textEdit_5.toPlainText()  # defult =
        self.textEdit_4.toPlainText()  # unit =
        self.spinBox_6.setValue(0)  # analyst_price =
        self.comboBox_26.setCurrentIndex(0)  # sub_category =
        self.Add_Data_To_history(4, 2)
        self.History()
        self.Show_all_analysts_in_combo()

    def Delete_Analyst(self):
        warning = QMessageBox.warning(self, 'احذر', "هل انت متأكد من انك تريد مسح التحليل",
                                      QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes:
            analyst_current_name = self.comboBox_21.currentText()
            sql = ''' DELETE FROM addanalyst WHERE name=%s '''
            self.cur.execute(sql, [(analyst_current_name)])
            self.db.commit()
            QMessageBox.information(self, 'info', 'تم حذف التحليل بنجاح')
            self.Show_all_analysts_in_combo()
            self.Add_Data_To_history(5, 2)
            self.History()
            self.Show_all_analysts_in_combo()

    def Show_all_analysts_in_combo(self):
        global mylist
        global addTrue
        addTrue=True
        self.cur.execute(
            ''' SELECT name FROM addanalyst WHERE sub_category=%s OR sub_category=%s OR sub_category=%s ORDER BY sub_category''',
            ('bio', 'هرمونات مشترك', 'hematology'))
        data = self.cur.fetchall()
        self.comboBox_21.clear()
        self.comboBox_16.clear()
        self.comboBox_26.clear()
        self.comboBox_22.clear()
        self.comboBox_26.addItem('----------------')
        self.comboBox_22.addItem('----------------')
        self.comboBox_21.addItem('----------------')
        self.comboBox_16.addItem('----------------')
        self.comboBox_3.addItem('----------------')
        self.comboBox_3.addItem('كل الاصناف')

        self.comboBox_16.addItems(mylist)
        self.comboBox_26.addItems(mylist)
        self.comboBox_22.addItems(mylist)
        self.comboBox_3.addItems(mylist)
        for item in data:
            self.comboBox_21.addItem(str(item[0]))
            self.comboBox_16.addItem(str(item[0]))
            self.comboBox_3.addItem(str(item[0]))
        for ii in range(0, self.comboBox_16.count()):
            self.comboBox_16.setCurrentIndex(ii)
            if self.comboBox_16.currentText() in mylist:
                # self.comboBox_16.setItemChecked(self.comboBox_16.currentIndex(),False)
                myitem = self.comboBox_16.model().item(self.comboBox_16.currentIndex(), self.comboBox_16.modelColumn())
                myitem.setCheckState(Qt.Unchecked)
        self.comboBox_16.setCurrentIndex(0)
        addTrue=False
        # self.handel_buttons()

    def Clients_Page(self):
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.insertRow(0)
        self.tableWidget_9.setRowCount(0)
        self.tableWidget_9.insertRow(0)
        id = self.spinBox_2.value()
        date = self.dateEdit_3.date()
        self.cur.execute(''' SELECT client_name,client_age,client_genus,client_doctor FROM addclient WHERE id=%s''',
                         (str(id),))
        client_data = self.cur.fetchall()
        self.cur.execute(
            ''' SELECT price,analyst_name,analyst_result,client_name,date FROM addnewitem WHERE client_id=%s AND DATE(date=%s)''',
            (str(id), str(date),))
        client_analyst_data = self.cur.fetchall()
        num = 0
        all_client_analyst = []
        total = 0
        rMy_num = 0
        GSE = ['Color:GSE', 'Consistency', 'Pus cells:GSE', 'R.B.Cs:GSE', 'E. Histolytica', 'Ova', 'Other:GSE',
               'Bacteria:GSE', 'Monillia:GSE', 'Fatty drop:GSE']
        GUE = ['Appearance', 'Reaction:GUE', 'Albumin', 'Sugar', 'RBCs:GUE', 'Pus cells:GUE', 'Epith .cells',
               'Crystals', 'Casts', 'Other:GUE', 'Bacteria:GUE', 'Monillia:GUE', 'Mucuse:GUE']
        SFA = ['Volume', 'Reaction:SFA', 'Colour:SFA', 'Liquefaction', 'Motility:Active', 'Motility:Sluggish',
               'Motility:Dead', 'Morphology:Normal', 'Morphology:Abnormal', 'Morphology:Pus cells', 'Other:SFA',
               'Count']

        c_GSE = False
        c_GUE = False
        c_SFA = False
        My_num = ['Appearance', 'Reaction:GUE', 'Albumin', 'Sugar', 'RBCs:GUE', 'Pus cells:GUE', 'Epith .cells',
                  'Crystals',
                  'Casts', 'Other:GUE', 'Volume', 'Reaction:SFA', 'Colour:SFA', 'Liquefaction', 'Motility:Active',
                  'Motility:Sluggish', 'Motility:Dead', 'Morphology:Normal', 'Morphology:Abnormal',
                  'Morphology:Pus cells', 'Other:SFA', 'Color:GSE', 'Consistency', 'E. Histolytica', 'G. Lembilia',
                  'Ova', 'Pus cells:GSE', 'R.B.Cs:GSE', 'Bacteria:GSE', 'Bacteria:GUE', 'Monillia:GSE', 'Monillia:GUE',
                  'Fatty drop:GSE', 'Fatty drop:GUE', 'Mucuse:GUE']
        for i in client_analyst_data:
            num += 1
        for price in range(0, num):
            if client_analyst_data[price][1] not in GSE and client_analyst_data[price][1] not in GUE and \
                    client_analyst_data[price][1] not in SFA:
                total += client_analyst_data[price][0]
        for k in range(0, num):
            for kg in GSE:
                if kg == client_analyst_data[k][1]:
                    c_GSE = True
            for kg1 in GUE:
                if kg1 == client_analyst_data[k][1]:
                    c_GUE = True
            for kg2 in SFA:
                if kg2 == client_analyst_data[k][1]:
                    c_SFA = True
        for j in range(0, num):
            all_client_analyst.append(str(client_analyst_data[j][1]))
        if c_SFA == True:
            total += 3
        if c_GSE == True:
            total += 3
        if c_GUE == True:
            total += 3
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
        self.tableWidget_9.setRowCount(0)
        self.tableWidget_9.insertRow(0)
        for row, form in enumerate(client_analyst_data):

            for col, item in enumerate(form):
                if col == 0:
                    self.tableWidget_9.setItem(row, col, QTableWidgetItem(str(client_analyst_data[0][3])))
                if col == 1:
                    self.tableWidget_9.setItem(row, col, QTableWidgetItem(str(client_analyst_data[row][1])))
                if col == 2:
                    self.tableWidget_9.setItem(row, col, QTableWidgetItem(str(client_analyst_data[row][2])))
                if col == 3:
                    self.tableWidget_9.setItem(row, col, QTableWidgetItem(str(client_analyst_data[row][4])))
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
            ''' INSERT INTO his VALUES (DEFAULT,%s,%s,%s,%s,%s)''',
            (user_id, action, table, datetime.datetime.now(), 1))
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
                    self.tableWidget_8.setItem(row, col, QTableWidgetItem(str(user_name[0])))
                if col == 1:
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

    def Show_avaliable_quantity(self):
        self.cur.execute(''' SELECT quantity FROM addbuys WHERE ''')
        quantity_avaliable = 0
        if quantity_avaliable < 1:
            date_quantity_ended = datetime.datetime.now()
            self.cur.execute(''' UPDATE addbuys SET quantity_avaliable=%s,date_ended=%s''',
                             (quantity_avaliable, date_quantity_ended))

    def Log_In_Chieck(self):
        global user_id
        user_name = self.lineEdit.text()
        user_password = self.lineEdit_2.text()
        self.cur.execute(''' SELECT id,user_password,user_name FROM adduser WHERE user_name=%s ''', (user_name,))
        # self.cur.execute(''' SELECT * FROM adduser ''')
        data = self.cur.fetchone()
        if data != None:
            if data[2] == user_name and data[1] == user_password:
                user_id = data[0]
                self.groupBox.setEnabled(True)
                self.tabWidget.setCurrentIndex(3)
                self.Add_Data_To_history(1, 5)
                self.History()
            else:
                warning = QMessageBox.warning(self, '',
                                              "كلمة المرور او اسم المستخدم غير صحيحة هل تريد استعادة كلمة المرور؟",
                                              QMessageBox.Yes | QMessageBox.No)
                if warning == QMessageBox.Yes:
                    self.Open_ResetPassword_Page()
        else:
            warning = QMessageBox.warning(self, '',
                                          "كلمة المرور او اسم المستخدم غير صحيحة هل تريد استعادة كلمة المرور؟",
                                          QMessageBox.Yes | QMessageBox.No)
            if warning == QMessageBox.Yes:
                self.Open_ResetPassword_Page()

    def Delete_All_History_Data(self):
        sql = '''DELETE FROM his'''
        self.cur.execute(sql)
        self.db.commit()
        QMessageBox.information(self, 'info', 'تم حذف محتويات السجل بنجاح')
        self.tableWidget_8.setRowCount(0)
        self.tableWidget_8.insertRow(0)

    def Open_Sales_Page(self):
        self.tabWidget.setCurrentIndex(3)

    def Open_Login_Page(self):
        self.tabWidget.setCurrentIndex(0)

    def Open_Settings_Page(self):
        self.tabWidget.setCurrentIndex(6)

    def Open_Print_Page(self):
        self.tabWidget.setCurrentIndex(7)

    def Open_History_Page(self):
        self.tabWidget.setCurrentIndex(5)

    def Open_clients_Page(self):
        self.tabWidget.setCurrentIndex(2)

    def Open_Analyse_Page(self):
        self.tabWidget.setCurrentIndex(4)

    def Open_ResetPassword_Page(self):
        self.tabWidget.setCurrentIndex(1)

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

    def Bio_Word(self, name, doctor, analysts, results, units, defults, year, month, day, word_types, prev, genus):
        global if_print
        self.cur.execute(''' SELECT * FROM paths WHERE id=1 ''')
        mydata = self.cur.fetchone()
        word_files = mydata[1]
        save_word_files = mydata[2]
        number_of_analysts = 0
        files = 0
        bio_analysts = 0
        hemo_analysts = 0
        GSE_analysts = 0
        GUE_analysts = 0
        SFA_analysts = 0
        HRMON_analysts = 0
        for tahlel in analysts:
            number_of_analysts += 1
        if number_of_analysts < 23:
            f = open(r'%s\test-mydocx.docx' % word_files, 'rb')
            f.read()
            document = Document(f)
        if number_of_analysts > 23 and number_of_analysts < 46:
            files = 2
            f = open(r'%s\test-mydocx.docx' % word_files, 'rb')
            f.read()
            document = Document(f)
            f2 = open(r'%s\test-mydocx2.docx' % word_files, 'rb')
            f2.read()
            document2 = Document(f2)
        if number_of_analysts > 46 and number_of_analysts < 69:
            files = 3
            f = open(r'%s\test-mydocx.docx' % word_files, 'rb')
            f.read()
            document = Document(f)
            f2 = open(r'%s\test-mydocx2.docx' % word_files, 'rb')
            f2.read()
            document2 = Document(f2)
            f3 = open(r'%s\test-mydocx3.docx' % word_files, 'rb')
            f3.read()
            document3 = Document(f3)
        row_num = False
        row_num2 = False
        number_of_analysts_in_que2 = 0
        for i in document.tables:
            for k in i.rows:
                for j in k.cells:
                    for n in j.paragraphs:
                        if n.text == 'أسـم المريض :':
                            if genus == 1:
                                n.text = f'أسـم المريض                                {name}'
                            else:
                                n.text = f'أسـم المريضة                                {name}'
                            run = n.runs
                            font = run[0].font
                            font.name = 'Monotype Koufi'
                            font.bold = True
                            font.size = Pt(11)
                        if n.text == 'حضرة الدكتورة   :':
                            if doctor == 'عدوية شمس سعيد':
                                n.text = f'حضرة الدكتورة                                {doctor}'
                            else:
                                n.text = f'حضرة الدكتور                                {doctor}'
                            run = n.runs
                            font = run[0].font
                            font.name = 'Monotype Koufi'
                            font.bold = True
                            font.size = Pt(11)
                        if n.text == 'المحترم':
                            if genus == 1:
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
                        for row in range(0, len(analysts)):
                            analyst_and_result = {
                                'analyst': analysts[row],
                                'result': results[row],
                                'unit': units[row],
                                'defult': defults[row]
                            }
                            if n.text == str(row + 1):
                                n.text = str(analyst_and_result['analyst']) + ' :'
                                run = n.runs
                                font = run[0].font
                                font.bold = True
                                font.size = Pt(11)
                                font.name = 'Tahoma'
                                n2 = n.add_run(str(analyst_and_result['result']))
                                run = n2
                                font = run.font
                                font.bold = False
                                font.size = Pt(11)
                                font.name = 'Tahoma'
                            if n.text == str(row + 1) + 'unit':
                                n.text = analyst_and_result['unit']
                                run1 = n
                                font1 = run1.runs[0].font
                                font1.bold = True
                                font1.size = Pt(12)
                                font1.name = 'Times New Roman'
                            if n.text == str(row + 1) + 'defult':
                                n.text = analyst_and_result['defult']
                                run1 = n
                                font1 = run1.runs[0].font
                                font1.bold = True
                                font1.size = Pt(12)
                                font1.name = 'Times New Roman'

                            number_of_analysts_in_que = 23
                            if bio_analysts != 0:
                                number_of_analysts_in_que -= 1
                            if hemo_analysts != 0:
                                number_of_analysts_in_que -= 1
                            if GSE_analysts != 0:
                                number_of_analysts_in_que -= 1
                            if GUE_analysts != 0:
                                number_of_analysts_in_que -= 1
                            if SFA_analysts != 0:
                                number_of_analysts_in_que -= 1
                            if HRMON_analysts != 0:
                                number_of_analysts_in_que -= 1
                            if row > number_of_analysts:
                                number_of_analysts_in_que2 = number_of_analysts_in_que
                                row_num = True
                                break

        if row_num:
            for i2 in document2.tables:
                for k2 in i2.rows:
                    for j2 in k2.cells:
                        for n2 in j2.paragraphs:
                            if n2.text == 'أسـم المريض :':
                                if genus == 1:
                                    n2.text = f'أسـم المريض                                {name}'
                                else:
                                    n2.text = f'أسـم المريضة                                {name}'
                                run = n2.runs
                                font = run[0].font
                                font.name = 'Monotype Koufi'
                                font.bold = True
                                font.size = Pt(11)
                            if n2.text == 'حضرة الدكتورة   :':
                                if doctor == 'عدوية شمس سعيد':
                                    n2.text = f'حضرة الدكتورة                                {doctor}'
                                else:
                                    n2.text = f'حضرة الدكتور                                {doctor}'
                                run = n2.runs
                                font = run[0].font
                                font.name = 'Monotype Koufi'
                                font.bold = True
                                font.size = Pt(11)
                            if n2.text == 'المحترم':
                                if genus == 1:
                                    n2.text = 'المحترم'
                                else:
                                    n2.text = 'المحترمة'
                                run = n2.runs
                                font = run[0].font
                                font.name = 'Monotype Koufi'
                                font.bold = True
                                font.size = Pt(11)
                            if n2.text == 'المحترمة2':
                                if doctor == 'عدوية شمس سعيد':
                                    n2.text = f'المحترمة'
                                else:
                                    n2.text = f'المحترم'
                                run = n2.runs
                                font = run[0].font
                                font.name = 'Monotype Koufi'
                                font.bold = True
                                font.size = Pt(11)
                            for row in range(number_of_analysts_in_que2, len(analysts)):
                                analyst_and_result = {
                                    'analyst': analysts[row],
                                    'result': results[row],
                                    'unit': units[row],
                                    'defult': defults[row]
                                }
                                if hemo_analysts != 0:
                                    if row == (bio_analysts + 1 + number_of_analysts_in_que2):
                                        if n.text == str(row - number_of_analysts_in_que2):
                                            n.text = str(word_types[bio_analysts])
                                if bio_analysts != 0:
                                    if row == 0 + 1 + number_of_analysts_in_que2:
                                        if n.text == str(row - number_of_analysts_in_que2):
                                            n.text = str(word_types[0])
                                if GSE_analysts != 0:
                                    if row == (hemo_analysts + bio_analysts + 1 + number_of_analysts_in_que2):
                                        if n.text == str(row - number_of_analysts_in_que2):
                                            n.text = str(word_types[hemo_analysts + bio_analysts])
                                if GUE_analysts != 0:
                                    if row == (
                                            hemo_analysts + bio_analysts + GSE_analysts + 1 + number_of_analysts_in_que2):
                                        if n.text == str(row - number_of_analysts_in_que2):
                                            n.text = str(word_types[hemo_analysts + bio_analysts + GSE_analysts])

                                if SFA_analysts != 0:
                                    if row == (
                                            hemo_analysts + bio_analysts + GSE_analysts + GUE_analysts + 1 + number_of_analysts_in_que2):
                                        if n.text == str(row - number_of_analysts_in_que2):
                                            n.text = str(
                                                word_types[hemo_analysts + bio_analysts + GSE_analysts + GUE_analysts])

                                if HRMON_analysts != 0:
                                    if row == (
                                            hemo_analysts + bio_analysts + GSE_analysts + GUE_analysts + SFA_analysts + 1 + number_of_analysts_in_que2):
                                        if n.text == str(row - number_of_analysts_in_que2):
                                            n.text = str(word_types[
                                                             hemo_analysts + bio_analysts + GSE_analysts + GUE_analysts + SFA_analysts])
                                if n2.text == str(row - number_of_analysts_in_que2 - 12):
                                    n2.text = str(analyst_and_result['analyst']) + ' :'
                                    run = n2.runs
                                    font = run[0].font
                                    font.bold = True
                                    font.size = Pt(11)
                                    font.name = 'Tahoma'
                                    n3 = n2.add_run(str(analyst_and_result['result']))
                                    run = n3
                                    font = run.font
                                    font.bold = False
                                    font.size = Pt(11)
                                    font.name = 'Tahoma'
                                if n2.text == str(row - number_of_analysts_in_que2 - 12) + 'unit':
                                    n2.text = analyst_and_result['unit']
                                    run1 = n2
                                    font1 = run1.runs[0].font
                                    font1.bold = True
                                    font1.size = Pt(12)
                                    font1.name = 'Times New Roman'
                                if n2.text == str(row - number_of_analysts_in_que2 - 12) + 'defult':
                                    n2.text = analyst_and_result['defult']
                                    run1 = n2
                                    font1 = run1.runs[0].font
                                    font1.bold = True
                                    font1.size = Pt(12)
                                    font1.name = 'Times New Roman'
                                if row > 46:
                                    row_num2 = True
                                    break
        if row_num2:
            for i3 in document3.tables:
                for k3 in i3.rows:
                    for j3 in k3.cells:
                        for n3 in j3.paragraphs:
                            if n3.text == 'أسـم المريض :':
                                if genus == 1:
                                    n3.text = f'أسـم المريض                                {name}'
                                else:
                                    n3.text = f'أسـم المريضة                                {name}'
                                run = n3.runs
                                font = run[0].font
                                font.name = 'Monotype Koufi'
                                font.bold = True
                                font.size = Pt(11)
                            if n3.text == 'حضرة الدكتورة   :':
                                if doctor == 'عدوية شمس سعيد':
                                    n3.text = f'حضرة الدكتورة                                {doctor}'
                                else:
                                    n3.text = f'حضرة الدكتور                                {doctor}'
                                run = n3.runs
                                font = run[0].font
                                font.name = 'Monotype Koufi'
                                font.bold = True
                                font.size = Pt(11)
                            if n3.text == 'المحترم':
                                if genus == 1:
                                    n3.text = 'المحترم'
                                else:
                                    n3.text = 'المحترمة'
                                run = n3.runs
                                font = run[0].font
                                font.name = 'Monotype Koufi'
                                font.bold = True
                                font.size = Pt(11)
                            if n3.text == 'المحترمة2':
                                if doctor == 'عدوية شمس سعيد':
                                    n3.text = f'المحترمة'
                                else:
                                    n3.text = f'المحترم'
                                run = n.runs
                                font = run[0].font
                                font.name = 'Monotype Koufi'
                                font.bold = True
                                font.size = Pt(11)
                            for row in range(46, len(analysts)):
                                analyst_and_result = {
                                    'analyst': analysts[row],
                                    'result': results[row],
                                    'unit': units[row],
                                    'defult': defults[row]
                                }
                                if n3.text == str(row - 45):
                                    n3.text = str(analyst_and_result['analyst']) + ' :'
                                    run = n3.runs
                                    font = run[0].font
                                    font.bold = True
                                    font.size = Pt(11)
                                    font.name = 'Tahoma'
                                    n4 = n3.add_run(str(analyst_and_result['result']))
                                    run = n4
                                    font = run.font
                                    font.bold = False
                                    font.size = Pt(11)
                                    font.name = 'Tahoma'
                                if n3.text == str(row + 1) + 'unit':
                                    n3.text = analyst_and_result['unit']
                                    run1 = n3
                                    font1 = run1.runs[0].font
                                    font1.bold = True
                                    font1.size = Pt(12)
                                    font1.name = 'Times New Roman'
                                if n3.text == str(row + 1) + 'defult':
                                    n3.text = analyst_and_result['defult']
                                    run1 = n3
                                    font1 = run1.runs[0].font
                                    font1.bold = True
                                    font1.size = Pt(12)
                                    font1.name = 'Times New Roman'
        document.save(r'%s\result.docx' % save_word_files)
        f.close()
        if files == 2:
            document2.save(r'%s\result2.docx' % save_word_files)
            f2.close()
        if files == 3:
            document3.save(r'%s\result3.docx' % save_word_files)
            f3.close()

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
                        word.ActiveDocument.PrintOut(Background=False)
                        # time.sleep(2)
                        # pyautogui.press('enter')
                        # time.sleep(1.5)
                        # word.ActiveDocument.Close()
                        move = 0
                        warning = QMessageBox.warning(self, '',
                                                      "هل قمت بطباعة الملف؟\n لا تضغط نعم الا لو قمت بطباعته",
                                                      QMessageBox.Yes | QMessageBox.No)
                        if warning == QMessageBox.Yes:
                            move = 1
                            try:
                                word.ActiveDocument.Close()
                            except:
                                pass
                        os.remove(r'%s\bio latest17.docx' % save_word_files)

                if move == 1:
                    if os.path.exists(r'%s\GSE latest.docx' % save_word_files):
                        word.Documents.Open(r'%s\GSE latest.docx' % save_word_files)
                        word.ActiveDocument.PrintOut(Background=False)
                        # time.sleep(2)
                        # pyautogui.press('enter')
                        # time.sleep(1.5)
                        # word.ActiveDocument.Close()
                        move = 0
                        warning = QMessageBox.warning(self, '',
                                                      "هل قمت بطباعة الملف؟\n لا تضغط نعم الا لو قمت بطباعته",
                                                      QMessageBox.Yes | QMessageBox.No)
                        if warning == QMessageBox.Yes:
                            move = 1
                            try:
                                word.ActiveDocument.Close()
                            except:
                                pass
                        os.remove(r'%s\GSE latest.docx' % save_word_files)

                if move == 1:

                    if os.path.exists(r'%s\SFA latest.docx' % save_word_files):
                        word.Documents.Open(r'%s\SFA latest.docx' % save_word_files)
                        word.ActiveDocument.PrintOut(Background=False)
                        # time.sleep(2)
                        # pyautogui.press('enter')
                        # time.sleep(1.5)
                        # word.ActiveDocument.Close()
                        move = 0
                        warning = QMessageBox.warning(self, '',
                                                      "هل قمت بطباعة الملف؟\n لا تضغط نعم الا لو قمت بطباعته",
                                                      QMessageBox.Yes | QMessageBox.No)
                        if warning == QMessageBox.Yes:
                            move = 1
                            try:
                                word.ActiveDocument.Close()
                            except:
                                pass
                        # word.ActiveDocument.Close()
                        os.remove(r'%s\SFA latest.docx' % save_word_files)

                if move == 1:

                    if os.path.exists(r'%s\GUE latest.docx' % save_word_files):
                        word.Documents.Open(r'%s\GUE latest.docx' % save_word_files)
                        word.ActiveDocument.PrintOut(Background=False)
                        # time.sleep(2)
                        # pyautogui.press('enter')
                        # time.sleep(1.5)
                        # word.ActiveDocument.Close()
                        move = 0
                        warning = QMessageBox.warning(self, '',
                                                      "هل قمت بطباعة الملف؟\n لا تضغط نعم الا لو قمت بطباعته",
                                                      QMessageBox.Yes | QMessageBox.No)
                        if warning == QMessageBox.Yes:
                            move = 1
                            try:
                                word.ActiveDocument.Close()
                            except:
                                pass
                        # word.ActiveDocument.Close()
                        os.remove(r'%s\GUE latest.docx' % save_word_files)

                if move == 1:

                    if os.path.exists(r'%s\hematology latest.docx' % save_word_files):
                        word.Documents.Open(r'%s\hematology latest.docx' % save_word_files)
                        word.ActiveDocument.PrintOut(Background=False)
                        # time.sleep(2)
                        # pyautogui.press('enter')
                        # time.sleep(1.5)
                        # word.ActiveDocument.Close()
                        move = 0
                        warning = QMessageBox.warning(self, '',
                                                      "هل قمت بطباعة الملف؟\n لا تضغط نعم الا لو قمت بطباعته",
                                                      QMessageBox.Yes | QMessageBox.No)
                        if warning == QMessageBox.Yes:
                            move = 1
                            try:
                                word.ActiveDocument.Close()
                            except:
                                pass
                        # word.ActiveDocument.Close()
                        os.remove(r'%s\hematology latest.docx' % save_word_files)

                if move == 1:

                    if os.path.exists(r'%s\هرمونات مشترك latest.docx' % save_word_files):
                        word.Documents.Open(r'%s\هرمونات مشترك latest.docx' % save_word_files)
                        word.ActiveDocument.PrintOut(Background=False)
                        # time.sleep(2)
                        # pyautogui.press('enter')
                        # time.sleep(1.5)
                        # word.ActiveDocument.Close()
                        move = 0
                        warning = QMessageBox.warning(self, '',
                                                      "هل قمت بطباعة الملف؟\n لا تضغط نعم الا لو قمت بطباعته",
                                                      QMessageBox.Yes | QMessageBox.No)
                        if warning == QMessageBox.Yes:
                            move = 1
                            try:
                                word.ActiveDocument.Close()
                            except:
                                pass
                        # word.ActiveDocument.Close()
                        os.remove(r'%s\هرمونات مشترك latest.docx' % save_word_files)
                self.Delete_Files()


        except Exception as e:
            print(e)


def main():
    app = QApplication(sys.argv)
    app.processEvents()
    window = mainapp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
