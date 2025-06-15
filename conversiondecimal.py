# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 12:22:19 2020

@author: lord-drestuction
"""

def decimal_a_binario(dec):
    decimal = int(dec)
    print(decimal,  "in binario es :", bin(decimal))

def decimal_a_octal(dec):
    decimal =int(dec)
    print(decimal,  "in octal es :", oct(decimal))
    
def decimal_a_exa(dec):
    decimal =int(dec)
    print(decimal,  "in exadecimal es :", hex(decimal))


dec = input("ingrese su numeroa cnvertir :")
decimal_a_binario(dec)
decimal_a_octal(dec)
decimal_a_exa(dec)
