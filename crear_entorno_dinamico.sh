#!/bin/bash

echo "🛠️ Script para crear entornos virtuales Python dinámicamente"

# === RUTA BASE (por defecto si no se escribe nada) ===
read -p "📁 Ruta base (default: /home/lorddestruction/herramientas): " ruta_base
ruta_base=${ruta_base:-/home/lorddestruction/herramientas}

# === NOMBRE DEL PROYECTO ===
read -p "📌 Nombre del proyecto (ej: telegram, webapp, scraping): " nombre_proyecto

# === NOMBRE DEL ENTORNO VIRTUAL ===
read -p "🐍 Nombre del entorno virtual (default: venv): " nombre_entorno
nombre_entorno=${nombre_entorno:-venv}

# === CREAR LA RUTA COMPLETA ===
ruta_final="$ruta_base/$nombre_proyecto"
mkdir -p "$ruta_final"
cd "$ruta_final" || exit

# === CREAR EL ENTORNO VIRTUAL ===
python3 -m venv "$nombre_entorno"
echo "✅ Entorno virtual creado en: $ruta_final/$nombre_entorno"

# === ACTIVAR EL ENTORNO ===
echo "🔃 Activando entorno virtual..."
source "$nombre_entorno/bin/activate"
echo "🐍 Python actual: $(which python3)"

# === INSTALAR PAQUETES OPCIONALES ===
read -p "¿Deseas instalar paquetes ahora? (s/n): " instalar
if [[ "$instalar" == "s" ]]; then
    read -p "Introduce los paquetes separados por espacio: " paquetes
    pip install $paquetes
    echo "📦 Paquetes instalados: $paquetes"
fi

# === MENSAJE FINAL ===
echo -e "\n✅ Entorno preparado en $ruta_final"
echo " Puedes trabajar ahora dentro del entorno."
echo " Para salir, usa el comando: deactivate"

