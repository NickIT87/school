import smtplib
from email.mime.text import MIMEText

# Параметри для підключення до SMTP-сервера
smtp_server = 'smtp.gmail.com'
port = 587  # Порт для TLS (Transport Layer Security) шифрування
username = 'elanir358@gmail.com'
password = 'avtocvet1251'

# Ваша та отримувачева електронні адреси
from_addr = 'elanir358@gmail.com'
to_addr = 'mprytula@lycey35.ukr.education'

# Створення об'єкту листа
subject = 'Тема листа'
body = 'Тіло листа'

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = from_addr
msg['To'] = to_addr

# Встановлення з'єднання з SMTP-сервером
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()
    server.login(username, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
