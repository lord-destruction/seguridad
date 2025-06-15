#!/bin/bash

set -e

# Función de ayuda
function ayuda() {
    echo "Uso: $0 <archivo_o_directorio> <formato> [nombre_salida]"
    echo "Formatos soportados: zip, tar.gz, 7z, xz, bz2"
    exit 1
}

# Validación de parámetros
INPUT="$1"
FORMATO="$2"
SALIDA="$3"

if [[ -z "$INPUT" || -z "$FORMATO" ]]; then
    ayuda
fi

if [[ ! -e "$INPUT" ]]; then
    echo "[!] El archivo o directorio '$INPUT' no existe."
    exit 1
fi

# Si no se define salida, usa el nombre original
NOMBRE_BASE=$(basename "$INPUT")
SALIDA=${SALIDA:-"${NOMBRE_BASE}.${FORMATO}"}

# Compresión según formato
case "$FORMATO" in
    zip)
        echo "[*] Comprimiendo a ZIP..."
        zip -r "$SALIDA" "$INPUT" > /dev/null
        ;;
    tar.gz)
        echo "[*] Comprimiendo a TAR.GZ..."
        tar -czf "$SALIDA" "$INPUT"
        ;;
    7z)
        echo "[*] Comprimiendo a 7Z..."
        7z a "$SALIDA" "$INPUT" > /dev/null
        ;;
    xz)
        echo "[*] Comprimiendo a TAR.XZ..."
        tar -cJf "$SALIDA" "$INPUT"
        ;;
    bz2)
        echo "[*] Comprimendo a TAR.BZ2..."
        tar -cjf "$SALIDA" "$INPUT"
        ;;
    *)
        echo "[!] Formato no soportado: $FORMATO"
        ayuda
        ;;
esac

echo "[+] Compresión finalizada: $SALIDA"
