# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 17:07:12 2020

@author: lord-drestuction
"""


#!/usr/bin/python3

import requests, re, time, sys, signal  
from pwn import *

def def_handler(sig,frame):
    print("\n[!] Existein \n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)
time.sleep(10)

main_url = "http://192.168.0.168.0.1/admin/login.php "


if __name__ == '__main__':
    
    s= requests.session()
    
    with open('dictionary.txt') as fp:
        