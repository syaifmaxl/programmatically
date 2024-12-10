import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

# Pengaturan email
sender_email = "saifrikdenim@gmail.com"
receiver_email = "mnindrazaka@gmail.com" 
subject = "2221400069 Tugas KDI 2024"
body = "Syaif Hakam"
attachment_path = "programmatically/sourcecode_program_tugas.py"

# Cek apakah file ada
if not os.path.exists(attachment_path):
    print(f"File {attachment_path} tidak ditemukan. Pastikan path benar.")
    exit()

# Buat pesan email
msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = receiver_email
msg.attach(MIMEText(body, 'plain'))

# Tambahkan lampiran
with open(attachment_path, 'rb') as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(attachment_path)}"')
    msg.attach(part)

# Kirim email
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(sender_email, 'ggsc dgti zktz jzvj')
    smtp.send_message(msg)
    print('Email terkirim!')
