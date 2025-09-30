#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ==========================================
# 🧠 COMPILADOR BÁSICO estilo Python
# Autor: Wilmer 
# # Descripción:
#   Este script lee un archivo .myp
#   Traduce las instrucciones simples (ej: print "Hola")
#   Las convierte a código Python válido y lo ejecuta.
# ==========================================

import sys
import os

def compile_line(line):
    """
    🧩 Esta función recibe una línea del archivo .myp
    y la traduce a código Python real.
    Por ahora solo soportamos 'print "texto"'
    """
    # Si la línea comienza con la palabra print
    if line.startswith("print "):
        # Tomamos el texto después de print
        content = line[6:]
        # Retornamos la versión válida en Python
        return f'print({content})'
    else:
        # Si no sabemos traducir la línea, la devolvemos igual
        return line

def main():
    """
    🧠 Función principal:
    1. Verifica que exista el archivo .myp
    2. Crea un archivo .py equivalente
    3. Ejecuta el código traducido
    """

    # Nombre del archivo fuente (.myp)
    source_file = "programa.myp"

    # Si el archivo no existe, mostramos error
    if not os.path.exists(source_file):
        print(f"❌ No se encontró el archivo {source_file}")
        sys.exit(1)

    # Nombre del archivo de salida (.py)
    output_file = source_file.replace(".myp", ".py")

    # Abrimos el archivo fuente y de salida
    with open(source_file, "r") as src, open(output_file, "w") as out:
        for line in src:
            # Quitamos saltos y espacios
            clean_line = line.strip()

            # Ignoramos líneas vacías o comentarios (#)
            if not clean_line or clean_line.startswith("#"):
                continue

            # Compilamos (traducimos) la línea
            compiled = compile_line(clean_line)

            # Escribimos la versión traducida en el .py
            out.write(compiled + "\n")

    print(f"✅ Archivo compilado: {output_file}")
    print("🚀 Ejecutando programa traducido:\n")

    # Ejecutamos el programa resultante
    exec(open(output_file).read())

if __name__ == "__main__":
    main()
