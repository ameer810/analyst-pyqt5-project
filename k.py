# # import smtplib
# # from email.mime.text import MIMEText
# # from email.mime.multipart import MIMEMultipart
# #
# # email = "ameersaad810@gmail.com" # the email where you sent the email
# # password = "aahmpredtiddvxlo"
# # send_to_email = "ameersaad810@gmail.com" # for whom
# # subject = "its me"
# # message = "This is a test email sent by Python. Isn't that cool?!"
# # msg = MIMEMultipart()
# # msg["From"] = email
# # msg["To"] = send_to_email
# # msg["Subject"] = subject
# #
# # msg.attach(MIMEText(message, 'plain'))
# #
# # server = smtplib.SMTP("smtp.gmail.com", 587)
# # server.starttls()
# # server.login(email, password)
# # text = msg.as_string()
# # server.sendmail(email, send_to_email, text)
# # server.quit()
# # print('ok')
# # import requests
# # #a=requests.post('https://ameersaad810.pythonanywhere.com/contact-us/api',{"place": 'jf',"phone_number": 3,"email": 'a@g.com',"content": 'kde',"time":'2021-03-16 16:27:30' })
# # #print('ok')
# # a=requests.get('https://ameersaad810.pythonanywhere.com/contact-us/').json()
# # print(a)
# from selenium import webdriver
# import time
# import pyautogui
# # pyautogui.mouseInfo()
# pyautogui.click(1162,1)
# time.sleep(2)
# pyautogui.doubleClick(50,580)
# time.sleep(2)
# pyautogui.doubleClick(334,20)
# time.sleep(2)
# pyautogui.hotkey('g')
# time.sleep(2)
# pyautogui.hotkey('enter')