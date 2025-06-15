import os
import platform
import subprocess
import configparser

def get_windows_wifi_passwords():
    output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], encoding='latin-1')
    lines = output.split('\n')
    profiles = [line.split(":")[1].strip() for line in lines if "All User Profile" in line]

    for profile in profiles:
        try:
            result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'], encoding='latin-1')
            result_lines = result.split('\n')
            password_lines = [line for line in result_lines if "Key Content" in line]
            if password_lines:
                password = password_lines[0].split(":")[1].strip()
            else:
                password = "(Sin contraseña guardada)"
        except subprocess.CalledProcessError:
            password = "(Error al obtener información)"
        print(f"{profile:<32} | {password}")

def get_linux_wifi_passwords():
    path = "/etc/NetworkManager/system-connections/"
    print(f"{'SSID':<32} | Contraseña")
    print("-" * 50)

    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)
        config = configparser.ConfigParser()
        try:
            config.read(filepath)
            ssid = config.get("wifi", "ssid", fallback="(SSID no encontrado)")
            psk = config.get("wifi-security", "psk", fallback="(Sin contraseña guardada)")
            print(f"{ssid:<32} | {psk}")
        except Exception as e:
            print(f"{filename:<32} | Error: {e}")

if __name__ == "__main__":
    os_type = platform.system()

    print(f"\n[+] Sistema detectado: {os_type}\n")

    if os_type == "Windows":
        get_windows_wifi_passwords()
    elif os_type == "Linux":
        get_linux_wifi_passwords()
    else:
        print("Sistema no soportado para este script.")
