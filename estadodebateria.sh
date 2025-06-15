#!/bin/bash

# Requiere: upower, notify-send
# Revisa el estado de la batería cada 10 minutos

INTERVALO=600  # en segundos (10 min)

function obtener_estado_bateria() {
    # Detecta el path del dispositivo de batería
    BATERIA=$(upower -e | grep battery)
    # Obtiene porcentaje
    PORCENTAJE=$(upower -i "$BATERIA" | grep -E "percentage" | awk '{print $2}')
    # Obtiene estado (charging/discharging)
    ESTADO=$(upower -i "$BATERIA" | grep -E "state" | awk '{print $2}')
    
    # Notifica al usuario
    notify-send "Estado de Batería" "$PORCENTAJE restante - Estado: $ESTADO"
    
    # También imprime en terminal
    echo "[*] $PORCENTAJE - $ESTADO"
}

echo "[+] Iniciando monitor de batería (Ctrl+C para salir)..."

while true; do
    obtener_estado_bateria
    sleep "$INTERVALO"
done
