from docx import *
from shutil import copyfile

# def Bio_Word(word):
from docx.shared import Pt

f = open('word/مختبر بغـداد.docx', 'rb')
f.read()

document = Document(f)

for i in document.tables:
    for k in i.rows:
        for j in k.cells:

            for n in j.paragraphs:
#                 # if n.text == 'أسـم المريض :       المحترم':
#                 #     n.text = f'أسـم المريض :{5}       المحترم'
#                 #     n.style.font.name = 'Monotype Koufi'
#                 #     n.style.font.bold = True
#                 #     n.style.font.size = Pt(11)
#                 # if n.text == 'حضرة الدكتور   :       المحترم':
#                 #     n.text = f'حضرة الدكتور   : {5}      المحترم'
#                 #     n.style.font.name = 'Monotype Koufi'
#                 #     n.style.font.bold = True
#                 #     n.style.font.size = Pt(11)
#                 # if n.text == 'Hb             :':
#                 #     for row in range(0, len(analysts)):
#                 #         analyst_and_result = {
#                 #             'analyst': analysts[row],
#                 #             'result': results[row]
#                 #         }
#                 #         if analyst_and_result['analyst'] == 'Hb':
#                 #             k = analyst_and_result['result']
#                 #             n.text = f'Hb             : {k}'
#                 #             n.style.font.name = 'Tahoma'
#                 #             n.style.font.bold = True
#                 #             n.style.font.size = Pt(14)
#                 # if n.text == 'Date:    /     / 20':
#                 #     n.text = f'Date:   {day} /  {month} / {year}'
#                 #     n.style.font.name = 'Tahoma'
#                 #     n.style.font.bold = True
#                 #     n.style.font.size = Pt(14)
                print('1'+n.text+'2')
document.save('word/مختبر بغـداد.docx')
f.close()
# '''
#
# '''