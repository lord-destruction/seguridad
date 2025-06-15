#!/bin/bash

set -e

# Archivo inicial (puedes cambiarlo o pasarlo como argumento)
ARCHIVO_INICIAL="${1:-data.gzip}"

# Verifica que 7z esté instalado
command -v 7z > /dev/null || { echo "[!] '7z' no está instalado. Usa 'sudo apt install p7zip-full'"; exit 1; }

# Función para obtener el archivo descomprimido
obtener_archivo_contenido() {
    7z l "$1" | awk '/Name/{getline; getline; print $NF}'
}

# Bucle de descompresión recursiva
ACTUAL="$ARCHIVO_INICIAL"
echo "[+] Archivo inicial: $ACTUAL"

while true; do
    echo "[*] Descomprimiendo: $ACTUAL..."
    7z x "$ACTUAL" -y > /dev/null 2>&1 || { echo "[!] Fallo al descomprimir $ACTUAL"; exit 1; }

    # Obtener el nuevo archivo descomprimido
    SIGUIENTE=$(obtener_archivo_contenido "$ACTUAL")

    # Si hay más de uno, se toma el primero (puedes ajustarlo)
    if [[ "$SIGUIENTE" == *$'\n'* ]]; then
        SIGUIENTE=$(echo "$SIGUIENTE" | head -n1)
    fi

    echo "[*] Archivo extraído: $SIGUIENTE"

    # Verifica si el siguiente archivo es también comprimido
    if file "$SIGUIENTE" | grep -qiE "archive|compressed|gzip|bzip2|tar"; then
        ACTUAL="$SIGUIENTE"
        continue
    else
        echo "[+] Archivo final encontrado: $SIGUIENTE"
        echo "--------- CONTENIDO ---------"
        cat "$SIGUIENTE"
        echo "-----------------------------"
        break
    fi
done

# Limpieza (opcional)
echo "[*] Limpiando archivos temporales..."
rm -f data.* *.7z *.zip *.gz *.xz *.bz2 *.tar *.rar 2>/dev/null || true
