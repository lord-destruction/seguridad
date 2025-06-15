# -*- coding: utf-8 -*-
"""
Extrae perfiles Wi-Fi y sus contraseñas almacenadas en Windows.
@author: lord-drestuction
"""

import subprocess

# Obtener todos los perfiles Wi-Fi guardados
output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], encoding='latin-1')
lines = output.split('\n')
profiles = [line.split(":")[1].strip() for line in lines if "All User Profile" in line]

# Recorrer cada perfil y obtener la clave (si existe)
for profile in profiles:
    try:
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'], encoding='latin-1')
        result_lines = result.split('\n')
        # Buscar la línea con la contraseña
        password_lines = [line for line in result_lines if "Key Content" in line]
        if password_lines:
            password = password_lines[0].split(":")[1].strip()
        else:
            password = "(Sin contraseña guardada)"
    except subprocess.CalledProcessError:
        password = "(Error al obtener información)"

    print(f"{profile:<30} | {password}")


