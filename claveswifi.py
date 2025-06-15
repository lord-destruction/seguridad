# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 12:31:51 2020

@author: lord-drestuction
"""

import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('latin').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', i, 'key=clear']).decode('latin').split('\n')
    results = [b.split(":")[1][1:-1] for b in data if "pass dela wifi" in b]

try:
    print ("{:<30} | {:<}".format(i, results[0]))
except IndexError:
    print ("{:<30} | {:<}".format(i, " "))

import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('latin').split('\n')
profiles = [x.split(':')[1][1:-1] for x in data if 'All User Profile' in x]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear'])
    results.decode('latin').split('\n')
    results = [y.split(':')[1][1:-1] for y in results if 'Key Content' in y]
    try:
        print('{:<30}| {:<}'.format(i, results[0]))
    except IndexError:
        print('{:<30}| {:<}'.format(i, ''))

