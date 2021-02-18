from docx import *
from shutil import copyfile
# def Bio_Word(word):
f = open('bio new.docx', 'rb')
f.read()

document=Document(f)
for i in document.paragraphs:
    word='hwio'
    if i.text=='         أسـم المريض :                                                                                                                                                            المحترم':
        i.text=f'         أسـم المريض :    {word}                                                                                                                                                        المحترم'
    if i.text=='         حضرة الدكتور :                                                                                                                                                        المحترم':
        i.text=f'         حضرة الدكتور :    {word}                                                                                                                                                    المحترم'
    if i.text=='Random  blood sugar :                                                   mg/dl                   (80 - 140)':
        i.text=f'Random  blood sugar :   {word}                                                mg/dl                   (80 - 140)'
    # if i.text=='Blood Urea               :                                                        mg/dl                    (20 – 45) ':
    #     i.text=f'Blood Urea               :   {word}                                                     mg/dl                    (20 – 45) '
    # if i.text==' S. Creatinin               :                                                     mg/dl                ( 0.7 – 1.4 )                          ':
    #     i.text=f' S. Creatinin               :   {word}                                                  mg/dl                ( 0.7 – 1.4 )                          '
    # if i.text=='S. Uric acid                  :                                                    mg/dl                       (3 – 7)             ':
    #     i.text=f'S. Uric acid                  :   {word}                                                 mg/dl                       (3 – 7)             '
    # if i.text=='S. Cholesterol            :                                                     mg/dl                 (150 – 250)                    ':
    #     i.text=f'S. Cholesterol            :   {word}                                                  mg/dl                 (150 – 250)                    '
    # if i.text=='S. Triglycerid             :                                                     mg/dl                  (65 – 180)                ':
    #     i.text=f'S. Triglycerid             :   {word}                                                  mg/dl                  (65 – 180)                '
    # if i.text=='Total serum Bilirubin:                                                   mg/dl                  (0.3 – 1.0)':
    #     i.text=f'Total serum Bilirubin:   {word}                                                mg/dl                  (0.3 – 1.0)'
    # if i.text=='S.Calcium               :                                                      mg/dl                  (8.8 – 10.2)':
    #     i.text=f'S.Calcium               :   {word}                                                   mg/dl                  (8.8 – 10.2)'
    # if i.text=='Vitamin D              :                                                          Deficient           ( 0 – 10 )':
    #     i.text=f'Vitamin D              :   {word}                                                       Deficient           ( 0 – 10 )'
    # # if i.text=='':
    # #     i.text=''
    # # if i.text=='':
    # #     i.text=''
    # # if i.text=='':
    # #     i.text=''
    print('2'+str(i.text)+'1')
document.save('bio new.docx')
f.close()
'''
2مختبر بغداد1
2للتحليلات المرضية والهرمونات                                                               بلد - شارع بنت الحسن      1
2موبايل : 078123856841
21
21
2         أسـم المريض :                                                                                                                                                            المحترم1
2         حضرة الدكتور :                                                                                                                                                        المحترم1
21
2Random  blood sugar :                                                   mg/dl                   (80 - 140)1
2                                                           1
2Blood Urea               :                                                        mg/dl                    (20 – 45) 1
21
2 S. Creatinin               :                                                     mg/dl                ( 0.7 – 1.4 )                          1
2S. Uric acid                  :                                                    mg/dl                       (3 – 7)             1
2S. Cholesterol            :                                                     mg/dl                 (150 – 250)                    1
2S. Triglycerid             :                                                     mg/dl                  (65 – 180)                1
2Total serum Bilirubin:                                                   mg/dl                  (0.3 – 1.0)1
21
2S.Calcium               :                                                      mg/dl                  (8.8 – 10.2)1
2    1
2Vitamin D              :                                                          Deficient           ( 0 – 10 )1
2                                                                                            Insufficient       ( 10 – 30 )1
2 Sufficient          ( 30 – 70 )               	1
21
2Examiner           1
2Date:                                 1
21
2بلد –  شارع بنت الحسن1
21
21

'''
