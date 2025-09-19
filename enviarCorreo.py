# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 11:39:50 2020

@author: lord-drestuction
"""

import smtplib

##__author__= " eldelfondotelaclava"

sender_mail = input("ingrese su mail: ")
receivers_mail = input("ingrese el destinatario: ")
#asunto = "correo de prueba"
message = """From: From Persona %s 
To: To Persons %s
Suject: Sending SMTP email 
esto es el mensaje envido
"""%(sender_mail,receivers_mail)

try:
    password = input('ingrese el password: ')
    smtpObj = smtplib.SMTP('gmail.com',587)
    smtpObj.login(sender_mail,password)
    smtpObj.sendmail(sender_mail,receivers_mail,message)
    print("e-mail enviado con exito")
except Exception:
    print("error no ha podiso ser enviado el mensaje")

########################################
