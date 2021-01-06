#!/usr/bin/env python3

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json
import argparse

parser = argparse.ArgumentParser(description = 'Manda Mensajes a Multiples Correos')
args = parser.parse_args()

correo = args.a
message = args.m
correo = str(correo)
message = str(message)

data = {}
with open('C_User.json') as f:
        data = json.load(f)

# Creamos objeto Multipart
msg = MIMEMultipart()
message = "ofertas!"
msg['From'] = data['user']

msg['To'] = correo
msg['Subject'] = "Alerta de ofertas"

# Autenticamos
msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.office365.com:587')
server.starttls()
print(data['user'])
server.login(data['user'], data['pass'])

# Enviamos
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
print("successfully sent email to %s:" % (msg['To']))
