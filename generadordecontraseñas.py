#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 15:56:05 2025

@author: lorddestruction
"""

import secrets
import string

def solicitar_opcion(pregunta):
    while True:
        respuesta = input(pregunta + " (s/n): ").lower()
        if respuesta in ['s', 'n']:
            return respuesta == 's'
        else:
            print("[!] Ingresa 's' para sí o 'n' para no.")

def generar_password(longitud, usar_minus, usar_mayus, usar_num, usar_simbolos):
    minusculas = "abcdefghijklmnñopqrstuvwxyz"
    mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    numeros = "0123456789"
    simbolos = "[]{}()+-*/;,:.-^`´~¿¡'?=&%$@!|¬°"

    conjunto = ""
    if usar_minus:
        conjunto += minusculas
    if usar_mayus:
        conjunto += mayusculas
    if usar_num:
        conjunto += numeros
    if usar_simbolos:
        conjunto += simbolos

    if not conjunto:
        raise ValueError("Debes seleccionar al menos un tipo de carácter.")

    return ''.join(secrets.choice(conjunto) for _ in range(longitud))


def main():
    print("\n=== Generador de Contraseñas Seguras ===\n")

    try:
        longitud = int(input("Longitud de la contraseña (recomendado: mínimo 12): "))
        if longitud <= 0:
            raise ValueError
    except ValueError:
        print("[!] Debes ingresar un número válido.")
        return

    usar_minus = solicitar_opcion("¿Incluir minúsculas?")
    usar_mayus = solicitar_opcion("¿Incluir mayúsculas?")
    usar_num = solicitar_opcion("¿Incluir números?")
    usar_simbolos = solicitar_opcion("¿Incluir símbolos especiales?")

    try:
        password = generar_password(longitud, usar_minus, usar_mayus, usar_num, usar_simbolos)
    except ValueError as e:
        print(f"[!] Error: {e}")
        return

    print("\n[+] Contraseña generada:\n" + password)

    # Copia al portapapeles si pyperclip está instalado
    try:
        import pyperclip
        pyperclip.copy(password)
        print("[*] Contraseña copiada al portapapeles.")
    except ImportError:
        print("[*] Instala pyperclip si quieres copiarla automáticamente (pip install pyperclip).")


if __name__ == '__main__':
    main()
