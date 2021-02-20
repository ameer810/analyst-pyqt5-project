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
                        n.text =f'  {5}'
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
                        n.text =f'  {5}'
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
                        n.text =f'  {5}'
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
                        n.text =f'  {5}'
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
                        n.text =f'  {5}'
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
                        n.text =f'  {5}'
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
                        n.text =f'  {5}'
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
                        n.text =f'  {5}'
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
                        n.text =f'  {5}'
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
                        n.text =f'  {5}'
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
                        n.text =f'  {5}'
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
                        n.text =f'  {5}'
                        n.style.font.name = 'Tahoma'
                        n.style.font.bold = True
                        n.style.font.size = Pt(12)
                if n.text == 'Date:    /     / 20':
                    n.text = f'Date:   {day} /  {month} / {year}'
                    n.style.font.name = 'Tahoma'
                    n.style.font.bold = True
                    n.style.font.size = Pt(14)
                print('1'+n.text+'2')
document.save('word/مختبر بغـداد.docx')
f.close()
'''
1     أســم الـمــريــض    :2
1حـضـرة الـدكتـور    الـفاضـــل :                                                                                            الـمـحـتـرم2
1Toxoplasma IgG2
1Toxoplasma IgM2
1Cytomegalo Virus IgG2
1Cytomegalo Virus IgM2
1Rubella IgG2
1Rubella IgM2
1Anti - Phspholipin IgG2
1Anti - Phspholipin  IgM2
1Anti - Cardiolipin  IgG2
1Anti - Cardiolipin  IgM2
1Herps   IgG2
1Herpes  IgM2


1T32
1T42
1TSH2
1LH2
1FSH2
1Prolactin2
1Testosterone2

'''
# f = open('word/GUE latest.docx', 'rb')
# f.read()
#
# document = Document(f)
# for i in document.tables:
#     for k in i.rows:
#         for j in k.cells:
#             for n in j.paragraphs:
#                 if n.text == 'أسـم المريض :       المحترم':
#                     n.style.font.name = 'Monotype Koufi'
#                     n.style.font.bold = True
#                     n.style.font.size = Pt(11)
#                     n.text = 'أسـم المريض :5       المحترم'
#
#                 if n.text == 'حضرة الدكتور   :       المحترم':
#                     n.style.font.name = 'Monotype Koufi'
#                     n.style.font.bold = True
#                     n.style.font.size = Pt(11)
#                     n.text = f'حضرة الدكتور   : {5}      المحترم'
#
#                 if n.text == 'Appearance :':
#                             n.style.font.name = 'Tahoma'
#                             n.style.font.size = Pt(14)
#                             n.text = f'Appearance : {6}'
#
#                 if n.text == 'Reaction      :':
#                             n.style.font.name = 'Tahoma'
#                             n.style.font.size = Pt(14)
#                             n.text = f'Reaction      : {6}'
#
#                 if n.text == 'Albumin       :':
#                             n.style.font.name = 'Tahoma'
#                             n.style.font.size = Pt(14)
#                             n.text = f'Albumin       : {6}'
#
#                 if n.text == 'Sugar          :':
#                             n.style.font.name = 'Tahoma'
#                             n.style.font.size = Pt(14)
#                             n.text = f'Sugar          : {6}'
#
#                 if n.text == 'RBCs         :':
#                             n.style.font.name = 'Tahoma'
#                             n.style.font.size = Pt(14)
#                             n.text = f'RBCs         : {6}'
#
#                 if n.text == 'Pus cells    :':
#                             n.style.font.name = 'Tahoma'
#                             n.style.font.size = Pt(14)
#                             n.text = f'Pus cells    : {6}'
#
#                 if n.text == 'Epith .cells :':
#                             n.style.font.name = 'Tahoma'
#                             n.style.font.size = Pt(14)
#                             n.text = f'Epith .cells : {6}'
#
#                 if n.text == 'Crystals     :':
#                             n.style.font.name = 'Tahoma'
#                             n.style.font.size = Pt(14)
#                             n.text = f'Crystals     : {6}'
#
#                 if n.text == 'Casts        :':
#                             n.style.font.name = 'Tahoma'
#                             n.style.font.size = Pt(14)
#                             n.text = f'Casts        : {6}'
#
#                 if n.text == 'Other        :':
#                             n.style.font.name = 'Tahoma'
#                             n.style.font.size = Pt(14)
#                             n.text = f'Other        : {6}'
#                 if n.text == 'Date:    /     / 20':
#                             n.style.font.name = 'Tahoma'
#                             n.style.font.bold = True
#                             n.style.font.size = Pt(14)
#                             n.text = f'Date:   {10} /  {3} / {2120}'
#
# document.save('word/GUE latest.docx')
# f.close()
# f = open('word/bio latest17.docx', 'rb')
# f.read()
# document = Document(f)
# for i in document.tables:
#     for k in i.rows:
#         for j in k.cells:
#             for n in j.paragraphs:
#                 if n.text == 'أسـم المريض :       المحترم':
#                     n.text = f'أسـم المريض :{"kf"}       المحترم'
#                     n.style.font.name = 'Monotype Koufi'
#                     n.style.font.bold = True
#                     n.style.font.size = Pt(11)
#                 if n.text == 'mg/dl':
#                     n.style.font.name = 'Tahoma'
#                     n.style.font.bold = False
#                     n.style.font.size = Pt(20)
#                     n.text ='mg/dl'
#                 if n.text == 'حضرة الدكتور   :       المحترم':
#                     n.text = f'حضرة الدكتور   : {"doctor"}      المحترم'
#                     n.style.font.name = 'Monotype Koufi'
#                     n.style.font.bold = True
#                     n.style.font.size = Pt(11)
#
#                 if n.text == 'Random  blood sugar :':
#                             n.text = f'Random  blood sugar : {3}'
#                             n.style.font.name = 'Tahoma'
#                             n.style.font.bold = True
#                             n.style.font.size = Pt(11)
#                 if n.text == 'Blood Urea               :':
#
#                             n.text = f'Blood Urea               : {3}'
#                             n.style.font.name = 'Tahoma'
#                             n.style.font.bold = True
#                             n.style.font.size = Pt(11)
#                 if n.text == 'S. Creatinin               :':
#                             n.text = f'S. Creatinin               : {3}'
#                             n.style.font.name = 'Tahoma'
#                             n.style.font.bold = True
#                             n.style.font.size = Pt(11)
#                 if n.text == 'S. Uric acid                  :':
#                             n.text = f'S. Uric acid                  : {3}'
#                             n.style.font.name = 'Tahoma'
#                             n.style.font.bold = True
#                             n.style.font.size = Pt(11)
#                 if n.text == 'S. Cholesterol            :':
#                             n.text = f'S. Cholesterol            : {3}'
#                             n.style.font.name = 'Tahoma'
#                             n.style.font.bold = True
#                             n.style.font.size = Pt(11)
#                 if n.text == 'S. Triglycerid             :':
#                             n.text = f'S. Triglycerid             : {3}'
#                             n.style.font.name = 'Tahoma'
#                             n.style.font.bold = True
#                             n.style.font.size = Pt(11)
#                 if n.text == 'Total serum Bilirubin:':
#                             n.text = f'Total serum Bilirubin: {3}'
#                             n.style.font.name = 'Tahoma'
#                             n.style.font.bold = True
#                             n.style.font.size = Pt(11)
#                 if n.text == 'S.Calcium :':
#                             n.text = f'S.Calcium : {3}'
#                             n.style.font.name = 'Tahoma'
#                             n.style.font.bold = True
#                             n.style.font.size = Pt(11)
#                 if n.text == 'Vitamin D              :':
#                             n.text = f'Vitamin D              : {3}'
#                             n.style.font.name = 'Tahoma'
#                             n.style.font.bold = True
#                             n.style.font.size = Pt(11)
#
#                 if n.text == 'Date:    /     / 20':
#                     n.text = f'Date:   {10} /  {2} / {8239}'
#                     n.style.font.name = 'Tahoma'
#                     n.style.font.bold = True
#                     n.style.font.size = Pt(11)
# document.save('word/bio latest17.docx')
# f.close()