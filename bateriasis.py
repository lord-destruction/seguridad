# -*- coding: utf-8 -*-
"""
Notificador de batería multiplataforma.
@author: lord-drestuction
"""

import psutil
from plyer import notification
import time
import platform

CHECK_INTERVAL = 60 * 10  # 10 minutos

def get_battery_status():
    battery = psutil.sensors_battery()
    if battery is None:
        return None, None, None
    return battery.percent, battery.power_plugged, battery.secsleft

def notify(percent, plugged):
    estado = "Cargando" if plugged else "Usando batería"
    notification.notify(
        title="Estado de batería",
        message=f"{percent}% restante - {estado}",
        timeout=10
    )

def main():
    os_type = platform.system()
    print(f"[+] Sistema detectado: {os_type}")
    print("[*] Iniciando monitor de batería...\n")

    while True:
        percent, plugged, _ = get_battery_status()
        if percent is None:
            print("[!] No se detectó batería (¿PC de escritorio o VM?)")
            break
        print(f"[*] Batería: {percent}% {'(Cargando)' if plugged else '(En uso)'}")
        notify(percent, plugged)
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
