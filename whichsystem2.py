import subprocess
import sys
import platform
import re

def get_value_ttl(address):
    os_type = platform.system()
    if os_type == "Windows":
        cmd = ["ping", "-n", "1", address]
    else:
        cmd = ["ping", "-c", "1", address]

    try:
        output = subprocess.check_output(cmd, stderr=subprocess.DEVNULL).decode()
    except subprocess.CalledProcessError:
        return None

    match = re.search(r"ttl[=|:](\d+)", output, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None

def detect_os_from_ttl(ttl):
    if ttl is None:
        return "Sin respuesta o TTL no detectado"

    if ttl >= 0 and ttl <= 64:
        return "Linux / Unix (posiblemente Android, FreeBSD, Solaris, macOS, OpenBSD)"
    elif ttl > 64 and ttl <= 128:
        return "Windows (7/10/11/Server)"
    elif ttl > 128 and ttl <= 255:
        return "Cisco / Equipos de red / Dispositivos embebidos"
    else:
        return "Sistema desconocido o TTL alterado"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python detect_os.py <IP>")
        sys.exit(1)

    ip = sys.argv[1]
    ttl = get_value_ttl(ip)
    os_detectado = detect_os_from_ttl(ttl)
    
    print(f"\n{ip} → TTL: {ttl if ttl is not None else 'N/A'} → Sistema estimado: {os_detectado}")


