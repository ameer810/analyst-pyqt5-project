from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from multy import Ui_Dialog as dialog

class MultyDialog(QDialog,dialog):
    def __init__(self,parent=None):
        super(MultyDialog, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
# from docx import *
#
# analysts = ['analyst1-bio', 'analyst2-bio', 'analyst3-bio', 'analyst4-hemo', 'analyst5-hemo', 'analyst6-GSE']
# category = ['bio', 'hemo', 'GSE']
# num_category = [3, 2, 1]#عدد كل عنصر كل category
# results = ['first', 'two', 'three', 'four', 'five', 'six']
# f = open('mytestdocx.docx', 'rb')
# f.read()
# document = Document(f)
# mynum = 0
# count = 1
# all_items=[]
# all_items_index=[]
# for c in category:
#     all_items.append(str(c+' :'))
#     all_items_index.append(count)
#     print(count, c)
#     for sub in analysts:
#         if c in sub:
#             count += 1
#             all_items.append(str('   '+sub+' :'))
#             all_items_index.append(count)
#             print("\t ", count, sub)
#     count += 1
# print(all_items)
# print(all_items_index)
# for n in document.paragraphs:
#     for row in range(0,len(all_items)):
#         if n.text==str(all_items_index[row]):
#             n.text=str(all_items[row])
#     for row2 in range(0,len(analysts)):
#         if n.text=='   '+str(analysts[row2])+' :':
#             print('yes')
#             n2 = n.add_run(str(results[row2]))
#
# document.save('mytestdocxrs.docx')
# f.close()