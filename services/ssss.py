from  email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib
import config

def send_email(to_addr, subject, text):
    msg = MIMEMultipart()
    msg['From'] = 'Gistura@yandex.ru'
    msg['To'] = 'Gistura@yandex.ru'
    msg['Subject'] = subject
    msg.attach(
        MIMEText(text, 'plain')
    )

    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    server.ehlo('Gistura@yandex.ru')
    server.login('Gistura@yandex.ru', 'Google3301')
    server.auth_plain()
    server.send_message(msg)
    server.quit()

send_email('Gistura@yandex.ru', 'ZDOROVA', 'KAK DELA')