# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 14:32:52 2020

@author: lord-drestuction
"""

#####################
#Excepciones
#####################
#que es
#son errores que ocurren durante la ejecuion de una programa. siempre se puede ver 
#como algo inesperado a la ejecuacion correcta. 
#
#como controlarlas
#



def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):		
	return num1/num2
	

op1=(int(input("Introduce el primer número: ")))

op2=(int(input("Introduce el segundo número: ")))		
	
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")

##
##supongamos que existen muchisimas mas lineas de codigo despues de las anteriores 
##para lo anterior se probara una ejecucion correcta del programa en un caso donde deseamos 
##realizar una operacion de dos numeros el primer numero es 8 el segundo numero es 4 y realixamos
##la operacion division
##########################################################################
##Introduce el primer número: 8
##Introduce el segundo número: 4
##Introduce la operación a realizar (suma,resta,multiplica,divide): divide
##2.0
##Operación ejecutada. Continuación de ejecúción del programa 
########################################################################
##la ejucion de la aplicacion fue la siguiente donde en una circunstancia ideal seria la anterior
##pero qeu pasa si en un caso ipotetico el usuario digita como primer numero 8 y segundo numero 0
##la division entre acero no esta definida por lo tanto dara error la ejecucion en la funcion division y
##por lo tanto no se ejecutara el resto del programa AQUI ES DONDE SE DEVERIA UTILIZAR UNA EXCEPCION
##PARA QEU SI FALLA POR ALGO INESPERADO LA EJECUCION SIGA DE MANERA NORMAL
##
##
##
##  File "<ipython-input-11-4534c4f1a951>", line 35, in <module>  ## en este error se percibe qeu elñ error es en la funcion divide 
##    print(divide(op1,op2))
##
##  File "<ipython-input-11-4534c4f1a951>", line 14, in divide    ## en la funcion divide al retornar la division del numerouno entre numerodos
##   return num1/num2                                             ## retorna un error 
##
##ZeroDivisionError: division by zero                             ## con el nombre de excepcion  "ZeroDivisionError"
##                                                                ## en la cual se aprecioa la division por cero 
##                                                                ## este nombre de excepcion debemos tenerlo en cuanta par ejecutar la ecxepcion
##


def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
    
    try:		                                       #en caso de que la opercion valla bien ejecutara el codigo 
        return num1/num2                               #omittira la excepcion y prosiguira con el codigo 
    except ZeroDivisionError:                          # de lo CONTRARIO 
        print("no se puede dividir enrte 0")           #realizara el intent en el try pero como no se puede ejecutar la operacion
        return "operacion erronea"                     #saltara  a la execpcion y ejecutara lo siguiente y seguira con el codigo
                                                       #ojo si el error qeu se captura coincide al nombre que se le puso a la execpcion
                                                       #procedera a  ejcutar el contenido dentro de ella

op1=(int(input("Introduce el primer número: ")))

op2=(int(input("Introduce el segundo número: ")))		
	
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")
print("....")
print("....")
print("....")
print("....")
print("....")
print("....")

#####################################################################################



def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
    
    try:		                                     
        return num1/num2                               
    except ZeroDivisionError:                           
        print("no se puede dividir enrte 0")          
        return "operacion erronea"                     
                                                       
# rodeamos con una ecxepcion en caso de que el usuario introduca texto                                                       

while True:
    try:
        op1=(int(input("Introduce el primer número: ")))
        op2=(int(input("Introduce el segundo número: ")))
        
        break
    except ValueError: 
           print("los valores no son lo indicados ")
# en este caso mientras sea verdadera la condicion ejecuara las lineas introduccion de numero si son correctas ya que es un bucle infinito
# esto hace que se ejecute el break haciendo qeu se salga del while sin pasar por la excepcion 
#
#
#           
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")
print("....")
print("....")
print("....")
print("....")
print("....")
print("....")

########

##############################################


def divide():
    
    try:
        op1 = (float (input("intrudusca el primer numero: ")))
        op2 = (float (input("introducsca el segundo numero: ")))
        print("la dicision es : "+ str(op1/op2))
    
    except ValueError:
        print ("los valores intruducidos son erroneos")
        
    except ZeroDivisionError:
        print ("la division por cero no se puede")
    
    finally:
        print("calculo finalizado")
    
        print("suerte") 
## en este caso el finally se ejecura simpres qeu termine la excepciones 
## muy util para conexiones de bases de datos para close() para cerrar la conexion a la base de datos       
divide()

#######################

def divide():
    
    try:
        op1 = (float (input("intrudusca el primer numero: ")))
        op2 = (float (input("introducsca el segundo numero: ")))
        print("la dicision es : "+ str(op1/op2))
    
    except: 
    
        print("suerte a ocurrido un error") 
        
       ## en este caso el finally se ejecura simpres qeu termine la excepciones 
## notese en este caso es una excepcion general la cual se puede realizar pero deja a l usuario como 
## huy qeu paso aqui 
        
        
        
divide()

print("usted esta en la linea 2 000 000 de codigo ")

#########################
def divide():
    
    try:
        op1 = (float (input("intrudusca el primer numero: ")))
        op2 = (float (input("introducsca el segundo numero: ")))
        print("la dicision es : "+ str(op1/op2))
    
    finally: 
        print("suerte a ocurrido un error")
      ## en este caso no hay ecxepcion pero el programa continua mostrando lo siguiente
      ## tiene una ejecucion normal y finaliza luego muerstra el error
      ## pero al quitar el finally se producce error de codigo por que no hay excepcion ni finally
divide()


################################
##rise exepciones propias

def evaluaredad (edad):
    
    if edad<0:
        raise TypeError("no se permiten edades egativas")
    
    if edad<20:
        return "eres basatante joven"
    elif edad<40:
        return "toda via eres joven"
    elif edad<65:
        return "eres un maduro"
    elif edad<100:
        return "cuidadte del covid"

print (evaluaredad(18)) 

################################
import math

def calcularaiz(num1):
    
    if num1<0:
        raise ValueError("no se permiten numero egativas")    

    else:
       return math.sqrt(num1)

op1= (int(input("introduce un nuemro ")))

try:
    print (calcularaiz(op1))

except ValueError as ErrorDenumerogegaivo:    ##en caso de introcir #negativo saltara la excepcon con nombre                                               ##      
    print(ErrorDenumerogegaivo)               ## erroDnumeronegativo de tipo valuerrror y dando por temrinado
                                              ## la ejecion del programa
print ("exit")


















































