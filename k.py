# # # import smtplib
# # # from email.mime.text import MIMEText
# # # from email.mime.multipart import MIMEMultipart
# # #
# # # email = "ameersaad810@gmail.com" # the email where you sent the email
# # # password = "aahmpredtiddvxlo"
# # # send_to_email = "ameersaad810@gmail.com" # for whom
# # # subject = "its me"
# # # message = "This is a test email sent by Python. Isn't that cool?!"
# # # msg = MIMEMultipart()
# # # msg["From"] = email
# # # msg["To"] = send_to_email
# # # msg["Subject"] = subject
# # #
# # # msg.attach(MIMEText(message, 'plain'))
# # #
# # # server = smtplib.SMTP("smtp.gmail.com", 587)
# # # server.starttls()
# # # server.login(email, password)
# # # text = msg.as_string()
# # # server.sendmail(email, send_to_email, text)
# # # server.quit()
# # # print('ok')
# # # import requests
# # # #a=requests.post('https://ameersaad810.pythonanywhere.com/contact-us/api',{"place": 'jf',"phone_number": 3,"email": 'a@g.com',"content": 'kde',"time":'2021-03-16 16:27:30' })
# # # #print('ok')
# # # a=requests.get('https://ameersaad810.pythonanywhere.com/contact-us/').json()
# # # print(a)
# # from selenium import webdriver
# # import time
# # import pyautogui
# # # pyautogui.mouseInfo()
# # pyautogui.click(1162,1)
# # time.sleep(2)
# # pyautogui.doubleClick(50,580)
# # time.sleep(2)
# # pyautogui.doubleClick(334,20)
# # time.sleep(2)
# # pyautogui.hotkey('g')
# # time.sleep(2)
# # pyautogui.hotkey('enter')
# # from win32com import client
# # import time
# #
# # word = client.Dispatch("Word.Application")
# #
# # word.Documents.Open(r'F:\برنامج التحليلات\word\bio latest17.docx')
# # # # word.Application.ActivePrinter = "PostScript"
# # # word.ActiveDocument.PrintOut()
# # # time.sleep(2)
# # # word.ActiveDocument.Close()
# import os
# import pyautogui
# from time import sleep
# from win32com import client
# # from threading import Thread
# word = client.Dispatch("Word.Application")
#
# word.Documents.Open(r'F:\برنامج التحليلات\word\bio latest17.docx')
# # word.ActiveDocument()
#
# sleep(1)
# word.ActiveDocument.PrintOut()
# sleep(3)
#
# # my=os.startfile(r'F:\برنامج التحليلات\word\bio latest17.docx','print')
# sleep(2)
# pyautogui.press('left')
# pyautogui.press('enter')
# a=0
# for i in range(1,18):
#     a+=5
#     print(a,',',end='')
import sys, os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# class TableWidgetDragRows(QTableWidget):
#     def __init__(self, *args, **kwargs):
#         QTableWidget.__init__(self, *args, **kwargs)

#         self.setDragEnabled(True)
#         self.setAcceptDrops(True)
#         self.viewport().setAcceptDrops(True)
#         self.setDragDropOverwriteMode(False)
#         self.setDropIndicatorShown(True)

#         self.setSelectionMode(QAbstractItemView.SingleSelection)
#         self.setSelectionBehavior(QAbstractItemView.SelectRows)
#         self.setDragDropMode(QAbstractItemView.InternalMove)

#     def dropEvent(self, event):
#         if event.source() == self and (event.dropAction() == Qt.MoveAction or self.dragDropMode() == QAbstractItemView.InternalMove):
#             success, row, col, topIndex = self.dropOn(event)
#             if success:
#                 selRows = self.getSelectedRowsFast()

#                 top = selRows[0]
#                 # print 'top is %d'%top
#                 dropRow = row
#                 if dropRow == -1:
#                     dropRow = self.rowCount()
#                 # print 'dropRow is %d'%dropRow
#                 offset = dropRow - top
#                 # print 'offset is %d'%offset

#                 for i, row in enumerate(selRows):
#                     r = row + offset
#                     if r > self.rowCount() or r < 0:
#                         r = 0
#                     self.insertRow(r)
#                     # print 'inserting row at %d'%r


#                 selRows = self.getSelectedRowsFast()
#                 # print 'selected rows: %s'%selRows

#                 top = selRows[0]
#                 # print 'top is %d'%top
#                 offset = dropRow - top
#                 # print 'offset is %d'%offset
#                 for i, row in enumerate(selRows):
#                     r = row + offset
#                     if r > self.rowCount() or r < 0:
#                         r = 0

#                     for j in range(self.columnCount()):
#                         # print 'source is (%d, %d)'%(row, j)
#                         # print 'item text: %s'%self.item(row,j).text()
#                         source = QTableWidgetItem(self.item(row, j))
#                         # print 'dest is (%d, %d)'%(r,j)
#                         self.setItem(r, j, source)

#                 # Why does this NOT need to be here?
#                 # for row in reversed(selRows):
#                     # self.removeRow(row)

#                 event.accept()

#         else:
#             QTableView.dropEvent(event)

#     def getSelectedRowsFast(self):
#         selRows = []
#         for item in self.selectedItems():
#             if item.row() not in selRows:
#                 selRows.append(item.row())
#         return selRows

#     def droppingOnItself(self, event, index):
#         dropAction = event.dropAction()

#         if self.dragDropMode() == QAbstractItemView.InternalMove:
#             dropAction = Qt.MoveAction

#         if event.source() == self and event.possibleActions() & Qt.MoveAction and dropAction == Qt.MoveAction:
#             selectedIndexes = self.selectedIndexes()
#             child = index
#             while child.isValid() and child != self.rootIndex():
#                 if child in selectedIndexes:
#                     return True
#                 child = child.parent()

#         return False

#     def dropOn(self, event):
#         if event.isAccepted():
#             return False, None, None, None

#         index = QModelIndex()
#         row = -1
#         col = -1

#         if self.viewport().rect().contains(event.pos()):
#             index = self.indexAt(event.pos())
#             if not index.isValid() or not self.visualRect(index).contains(event.pos()):
#                 index = self.rootIndex()

#         if self.model().supportedDropActions() & event.dropAction():
#             if index != self.rootIndex():
#                 dropIndicatorPosition = self.position(event.pos(), self.visualRect(index), index)

#                 if dropIndicatorPosition == QAbstractItemView.AboveItem:
#                     row = index.row()
#                     col = index.column()
#                     # index = index.parent()
#                 elif dropIndicatorPosition == QAbstractItemView.BelowItem:
#                     row = index.row() + 1
#                     col = index.column()
#                     # index = index.parent()
#                 else:
#                     row = index.row()
#                     col = index.column()

#             if not self.droppingOnItself(event, index):
#                 # print 'row is %d'%row
#                 # print 'col is %d'%col
#                 return True, row, col, index

#         return False, None, None, None

#     def position(self, pos, rect, index):
#         r = QAbstractItemView.OnViewport
#         margin = 2
#         if pos.y() - rect.top() < margin:
#             r = QAbstractItemView.AboveItem
#         elif rect.bottom() - pos.y() < margin:
#             r = QAbstractItemView.BelowItem
#         elif rect.contains(pos, True):
#             r = QAbstractItemView.OnItem

#         if r == QAbstractItemView.OnItem and not (self.model().flags(index) & Qt.ItemIsDropEnabled):
#             r = QAbstractItemView.AboveItem if pos.y() < rect.center().y() else QAbstractItemView.BelowItem

#         return r


# class Window(QWidget):
#     def __init__(self):
#         super(Window, self).__init__()

#         layout = QHBoxLayout()
#         self.setLayout(layout)

#         self.table_widget = TableWidgetDragRows()
#         layout.addWidget(self.table_widget)

#         # setup table widget
#         self.table_widget.setColumnCount(2)
#         self.table_widget.setHorizontalHeaderLabels(['Colour', 'Model'])

#         items = [('Red', 'Toyota'), ('Blue', 'RV'), ('Green', 'Beetle')]
#         for i, (colour, model) in enumerate(items):
#             c = QTableWidgetItem(colour)
#             m = QTableWidgetItem(model)

#             self.table_widget.insertRow(self.table_widget.rowCount())
#             self.table_widget.setItem(i, 0, c)
#             self.table_widget.setItem(i, 1, m)

#         self.show()
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
class My_app(QtWidgets):
    def __init__(self):
        super(My_app, self).__init__()
        self.my()
    def my(self):
        mylineEdit=QtWidgets.QTableWidget()
        num=0
        mylineEdit.setObjectName("tableWidget_5")
        mylineEdit.setColumnCount(5)
        mylineEdit.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        mylineEdit.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        mylineEdit.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        mylineEdit.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        mylineEdit.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        mylineEdit.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        mylineEdit.setHorizontalHeaderItem(4, item)        # while True:
        analyst_data=(('hhu9o', 'Random  blood sugar', '1', 'عدوية شمس سعيد', '2'),)
        for row, form in enumerate(analyst_data):
            for col, item in enumerate(form):
                # if col==4:
                #     print(total_price,'here')
                # self.tableWidget_5.setItem(row, col, QTableWidgetItem(str(total_price)))
                # else:
                mylineEdit.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            row_pos = mylineEdit.rowCount()
            mylineEdit.insertRow(row_pos)
#
#
app = QApplication(sys.argv)
window = My_app()
window.show()
sys.exit(app.exec_())
# import win32api,win32print
# from win32com import client
# # fs= open(r'F:\برنامج التحليلات\word\GUE org.docx','rb')
# word=client.Dispatch('Word.Application')
# word.Documents.Open(r'F:\برنامج التحليلات\word\GUE org.docx')
# word.ActiveDocument.PrintOut()