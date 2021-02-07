from docx import *
from shutil import copyfile

f = open('new.docx', 'rb')
f.read()

document=Document(f)
for i in document.paragraphs:
    print('2',i.text,'1')
f.close()
copyfile('new.docx', 'h.docx')
