# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 19:32:04 2019

@author: lord-drestuction
"""

##CONDICIONALES
##flujo de ejecucion es orden con que en un programa se ejecutan sus instrucciones

## condicional if

## sintaxis
## instruccion
## instruccion
## if (condicion)
    ## instruccion
    ## instruccion
## instruccion
## instruccion
### en este caso se realizan un cierto numero de instrucciones antes de ser llamado la intruccion if
## dado el caso que se cumpla cierta condiccion. se ejecuta una serie de instrucciones. 
## ya que se debe de cumplir que sea verdqadero o falso   en cada caso toma un camino y ejecutara ciertas 
## instrucciones 

Numero1=6
Numero2=5
if Numero1>Numero2:
	print("el mayor de los numero1 ")
else:
	print("el mayor es el numero 2 ")


## en el ejemplo anterior podemos observar que cuando el numero 1 es mayor que el numero 2  el resultado
## es la impresion de el "mayor de los numero1" dado el caso que no se cumpla la condicion 
## pasara al otro caso y mostrara "el mayor es el numero 2 "


print ("evalacon de la notas de un alaumno")
NotaAlumno=input()

def Evaluar(nota):
    valoracion="aprobado"
    if nota<3:
        valoracion=" huy puedes haber perdido"
    return valoracion

print (Evaluar(int(NotaAlumno)))    
    

## de la misma manera podemos introducir estos condicionales en una funcion evaluando, esta la condicon cuando 
## sea necesaria. podems observar que la funcion Evaluar, evalua un dato llamado nota, la cual es pedida 
## por consola y es casteada a un valor entero. ya que en python al pasar un valor por un input es tomado como
## string o cadena de texto.Una vez hecho esto se mostrara la valoracion del estudiante, 
## si la nota es superior a tres. de lo contario devolvera la nueva valoracion la cual se 
## encuantradentro del ciclo.    

print ("verificacion de acceso")

Edad_usuario=int(input("ingrese la edad del usuario: "))

if Edad_usuario<18:
    print ("yuca no puede pasar")

else: 
    print ("bienvenido puede pasar")

###el uso del el esle grantiza que si una condicion no se cumple ingrese a la tra condicion.

print ("verificacion de acceso")

Edad_usuario=int(input("ingrese la edad del usuario: "))

if Edad_usuario<18:
    print ("yuca no puede pasar")
    
elif Edad_usuario>100:
    print ("puede haber un error")

else: 
    print ("bienvenido puede pasar")

##el uso de elif permite que se evaluen todos los condicionales  y si no se cumplen ingresa al else

print ("evalacon de la notas de un alaumno")


Notaalumno=int(input("Introduce la nota del estudiante"))

if Notaalumno<5:
    print ("insuficiente")
elif Notaalumno<6:
    print ("suficiente")
elif Notaalumno<7:
    print ("aceptable")
elif Notaalumno<9:
    print ("bueno")
else:
    print ("ecxelente")

###########################
print ("verificacon de accesso")

edadusuario = int(input("introducce la edad, por favor"))

if edadusuario<18:
    print ("no puedes pasar")
    
else:
    print ("puedes pasar y tu edad es : ", edadusuario )
    

print ("aplicacion terminada")

####
#Vamos ha hacer un programa el cual saque el mayor de tres numeros en caso de ser iguales dos numeros diga cual es diferente
numerouno  = int(input("introducce el primer numero, por favor"))
numerodos  = int(input("introducce el segundo numero, por favor"))
numerotres = int(input("introducce el tercer numero, por favor"))


if (numerouno == numerodos != numerotres):
    print("los numeros son iguales",numerouno,numerodos,"numero tres es diferente", numerotres )
    
else:
    if((numerouno > numerodos) and (numerouno > numerotres) and (numerodos > numerotres)):
        print("el mayor es",numerouno )
    if((numerouno > numerodos) and (numerouno > numerotres) and (numerotres > numerodos)):
        print("el mayor es",numerouno )
        
        
if (numerodos == numerotres != numerouno ):
    print("los numeros son iguales",numerodos,numerotres,"numero uno es diferente", numerouno)

else:
    if((numerodos > numerouno) and (numerodos > numerotres) and (numerouno > numerotres)):
        print("el mayor es",numerodos )
    if((numerodos > numerouno) and (numerodos > numerotres) and (numerotres > numerouno)):
        print("el mayor es",numerodos )    


if (numerotres == numerouno != numerodos ):
    print("los numeros son iguales",numerotres,numerouno,"numero dos es diferente", numerodos)

else:
    if((numerotres > numerouno) and (numerotres > numerodos) and (numerodos > numerouno)):
        print("el mayor es",numerotres )   
    if((numerotres > numerouno) and (numerotres > numerodos) and (numerouno > numerodos)):
        print("el mayor es",numerotres )
    
#
#Crea un programa que pida dos números por teclado. El programa tendrá una función
#llamada “DevuelveMax” encargada de devolver el número más alto de los dos introducidos.        


#Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos
#deberán ser almacenados en una lista y mostrar en consola el mensaje: “Los datos
#personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por teclado).

#Crea un programa que pida tres números por teclado. El programa imprime en consola
#la media aritmética de los números introducidos.

























    