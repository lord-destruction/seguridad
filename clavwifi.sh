#!/bin/bash

echo -e "SSID                          | Contraseña"
echo "---------------------------------|--------------------------"

for file in /etc/NetworkManager/system-connections/*; do
    ssid=$(grep '^ssid=' "$file" | cut -d= -f2)
        psk=$(grep '^psk=' "$file" | cut -d= -f2)
            if [ -z "$psk" ]; then
                    psk="(Sin contraseña guardada)"
                        fi
                            printf "%-32s | %s\n" "$ssid" "$psk"
                            done

