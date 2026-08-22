#!/usr/bin/python2.7 -tt
#
#
#
import base64,codecs,sys

##funcion qeu limpia la base en root13

def encodeString(str):
	clearTextStr = base64.b64encode(str)
	return codecs.encode(clearTextStr[::-1], 'rot13')

#funcion de encriptar rot13 a 64 y luego limpia el text
def decodeString(str):
	rot13Str = codecs.decode(str[::-1], 'rot13')
	return base64.b64encode(rot13Str)

#funcion de menu
def print_menu():
	print 30 * '-' , "MENU" , 30 * '-'
	print('1. Encrypt:  borrar texto a base64 y luego a rot13 ')
	print('2. Decrypt:  rot13 a base64 y luego a borrar texto ')
	print('3. Exit')
	print 67 * '-'

def main():
	loop = True
	while loop:
		print_menu()
		cambio = input ("ingrese enter para cambiar entre  le menu [1 - 3]: ")
		if cambio == 1:
			clearTextStr = raw_input('ingrese el text a enryptar: ')
			cryptoResult = encodeString(clearTextStr)
			print('\n')
			print('encriptacion resultante: ')
			loop = False
		elif cambio == 2:
			rot13Str = raw_input('por favor ingrese el valor rot13 para descifrar : ')
			cryptoResult = decodeString(rot13Str)
			print('\n')
			print('desencriptacion resultante: ')
			loop = False
		elif cambio == 3:
			exit()
		else:
			raw_imput('no sea pendejo de una opcion valdia....')
	print (cryptoResult)

if __name__ == '__main__':
	main()
#end file



			














