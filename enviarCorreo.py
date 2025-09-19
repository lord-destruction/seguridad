#!/usr/bin/env python3
"""
Script para enviar correos vía Gmail usando clave de aplicación.
@author: lord-drestuction

"""

import smtplib
from getpass import getpass

# Usuario fijo (correo del remitente)
SENDER_MAIL = "wilmer.fernadez18@gmail.com"

# Solicitar datos dinámicos
receivers_input = input("Ingrese destinatarios separados por coma: ").strip()
subject = input("Ingrese el asunto: ").strip()
body = input("Ingrese el mensaje: ").strip()

# Procesar destinatarios
receivers_list = [mail.strip() for mail in receivers_input.split(",")]

# Construir el mensaje
message = f"""From: {SENDER_MAIL}
To: {", ".join(receivers_list)}
Subject: {subject}

{body}
"""

try:
    password = getpass('Ingrese su clave de aplicación de Gmail: ')

    # Conexión segura con Gmail
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(SENDER_MAIL, password)

    smtpObj.sendmail(SENDER_MAIL, receivers_list, message)
    smtpObj.quit()
    print("✅ E-mail enviado con éxito.")
except Exception as e:
    print(f"❌ Error: no se pudo enviar el mensaje.\nDetalles: {e}")


# -*- coding: utf-8 -*-
#"""
#Created on Sun Nov 15 11:39:50 2020
#
#@author: lord-drestuction
#"""

#import smtplib

##__author__= " eldelfondotelaclava"

#sender_mail = input("ingrese su mail: ")
#receivers_mail = input("ingrese el destinatario: ")
##asunto = "correo de prueba"
#message = """From: From Persona %s 
#To: To Persons %s
#Suject: Sending SMTP email 
#esto es el mensaje envido
#"""%(sender_mail,receivers_mail)
#
#try:
#    password = input('ingrese el password: ')
#    smtpObj = smtplib.SMTP('gmail.com',587)
#    smtpObj.login(sender_mail,password)
#    smtpObj.sendmail(sender_mail,receivers_mail,message)
#    print("e-mail enviado con exito")
#except Exception:
#    print("error no ha podiso ser enviado el mensaje")
#
########################################
