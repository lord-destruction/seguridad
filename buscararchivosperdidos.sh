#!/bin/bash

# Pedir al usuario el archivo con las rutas
read -p "Ingrese la ruta del archivo que contiene las rutas a buscar: " ARCHIVO_RUTAS

# Pedir al usuario la carpeta de destino
read -p "Ingrese la carpeta donde se copiarán los archivos encontrados: " DESTINO

# Pedir al usuario el archivo log
read -p "Ingrese la ruta y nombre del archivo log: " LOG

# Crear carpeta destino si no existe
mkdir -p "$DESTINO"

# Vaciar log al inicio
> "$LOG"

# Verificar que el archivo de rutas exista
if [ ! -f "$ARCHIVO_RUTAS" ]; then
    echo "El archivo con rutas no existe: $ARCHIVO_RUTAS"
    exit 1
fi

# Leer línea por línea
while IFS= read -r ruta; do
    if [ -f "$ruta" ]; then
        echo "Encontrado: $ruta"
        cp "$ruta" "$DESTINO"/
    else
        echo "NO ENCONTRADA: $ruta" | tee -a "$LOG"
    fi
done < "$ARCHIVO_RUTAS"

echo "Proceso finalizado."
echo "Archivos encontrados en: $DESTINO"
echo "Log de no encontrados en: $LOG"
