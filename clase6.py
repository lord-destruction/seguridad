# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 13:24:26 2019

@author: lord-drestuction
"""
#########################BUCLES
##bucle sirve para repitir muchas veces el mismo codigo
#ejemplo si no existiera el bucle repetir hasta

#
#codigo
#codigo
#codigo
#print ("ejemplo de mensaje")
#print ("ejemplo de mensaje")
#print ("ejemplo de mensaje")
#codigo
#codigo
#codigoe
# en este caso repetios el mimo mensaje tres veces y si en un caso tubierams que repetir 3000
# veces el mismo mensaje . no podemos ejecurar 3000 veces la misma linea seria demasido tedioso
# 
#tipos de bucles en python
#bucle determinado
#se ejecutan un numero determinado de veces
#se sabe de antemano cuantas veces se ejecutara el codifgo dentro del bucle
#
#bucle indeterminado
#
#se ejecutan un numero indeterminado de veces
#no se sabe de antemano cuantas veces se ejecutara el codifgo dentro del bucle
#el numero de ejecuciones dependera de las circunstancias de ejecucion del programa
#
#
#Forma de un bucle
#
#codigo
#codigo
#codigo
#    instruccion del bucle:
#        cuerpo del bucle
#
#codifgo 
#codigo
#
#sintaxis
#for variable in elemento a correr:
#    cuerpo del bucle



###el elemento a recorrer puede ser una lista,tupla, cadena, text,etc


####################################
for i in [1,1,1]:
    print ("hola")

###################################
for i in ["viernes","sabado","domingo"]:
    print ("hola")

##en este caso el for recorre el elemnto a y cada que encuentr un elemento imprime la palabra hola,
## asi hasta haber terminado el grupo de palabras en dicho elemento a recorrer    

###################################
for i in ["viernes","sabado","domingo"]:
    print (i)
## en este caso el for recorrera el elemento e imprimira la posicion de cada elemeto que posee 
## el elemto a recorarer

####### recorrer  strings 

##en el primer caso recorrera el la lista e inprimira hola por cada elemento de la lista 
##y con el termino end para que se eimprima seguido sin saltos de linea
    
for i in ["pildores","informacion","duele",3]:
    print ("hola", end="   ")
    


##en el segundo caso recorrera el string e inprimira hola por cada elemento de este 

for i in "wilmerestabasentadomirandoelnuevoamanecerderdelostiempos":
    print ("hola", end="   ")
    
#####################
email=False

for i in "wilmer.fernandez@makrosoft.co":
    
    if(i=="@"):
        email=True

if email==True:
    print("el email es correcto")
else:
    print("el email no es correcto ")

    
################
    
email=False
miemail=input("introduce el email : ")


for i in miemail:
    
    if(i=="@"):
        email=True

if email==True:
    print("el email es correcto")
else:
    print("el email no es correcto ")    


#################################

contador=0
miemail=input("introduce el email : ")


for i in miemail:
    
    if(i=="@" or i=="."):
        contador = contador+1

if email:
    print("el email es correcto")
else:
    print("el email no es correcto ")    
    

    
####### tipo range
    
    
for i in range(5): 
    print("hola")
    
######    
    
for i in range(5): 
    print (i)    
    
    
#####################


for i in range(5): 
    print (f"el valor de la variable {i}")  

    
##### imprime numeros que estan entre 5 y 10 incluyendo al 5 y hata el 9   
    ###la f la utilizam para unir textos con varibles y no utilizamos operadore de concatenacion
for i in range(5,10): 
    print (f"el valor de la variable {i}")     
    
#####imprime numeros que estan entre 5 y 50 pero que valla de 3 en 3
for i in range(5,50,3): 
    print (f"el valor de la variable {i}")     
    
##############################
email=False
miemail=input("introduce el email : ")

for i in range(len(miemail)):  ##recorrera el email  y en la sig linea si encuentra @ el mal es correcto
                               ## de lo contrario no 
    if miemail[i]=="@":
        email=True    

if email:
    print("el email es correcto")
else:
    print("el email no es correcto ")  
    
#########################################################
#########################################################

####### bucle WHILE
    
##SINTAXIS    mientras se cumpla la condicion el bucle ejecutara el cuerpo del bucle, 
##cuando la condicion es falsa se deja de ejecutar el bucle
    
    
##while condicion:
    ##cuerpo del bucle    
#############
    
    
i=1    
while i<=10: 
  print("hola mundo"+ str(i))
  i=i+1   ### si no se colaocara el contador el ciclo se iria infinitamente por que siempre serai 1 < 10
          ### por lo tanto hay que colocar un contador que hatga que el ciclo termine    
print("terino el bucle y bien")

#######################
edad= int(input("introdusca los datosde la edad: "))


while edad < 0 or edad >120:
    print ("usted ha introducdio una edad negativa")
    edad= int(input("introdusca los datos de la edad: "))

print("gracias por colaborar")
print("la edad es " + str(edad))



###################################
import math

print ("programa de la raiz cuadrada")
numero= int(input("introdusca el numero a calcular: "))


intentos=0

while numero<0:
    print("no se puede hallar raices negativas ""OJO"" ")

    if intentos==2:
        print ("haz consumido tus recursos o intentos. ")
        break;  ### si se llega a leer esta linea el concluira el ciclo
        
    numero= int(input("introdusca el numero a calcular: "))
    if numero<0:
        intentos =intentos+1

if intentos<2:
    solucion=math.sqrt(numero)
    print ("la raiz cuadrada de " + str(numero)+ " es" +str(solucion))

########################################

numero= int(input("introdusca el numero: "))
numero2= int(input("introdusca un numero mayor : ") + str(numero) + ": ")

while numero2 > numero:
    numero=numero2
    numero2=int(input("escriba el numero myor que") + str(numero) + ": ")
    
print ()
print (numero2, " no es mayor que ", str (numero))


##################################

numero= int(input("introdusca el numero: "))
suma=0

while numero >= 0:
    
    
    if (numero <0) :
        break
    
    else:
        suma = suma + numero
        numero= int(input(" intrudusca el numero "))

print ("exit")
print ("la sume  es : "+ str(suma) )

#########################################
##
##continue: salta a la sig iterasion del bucle. ejemple 0 1 2 3 4 5 6 7 8 9 
## este ees el ejemplo del cisclo que da 10 vueltas y se salta la instruccion 5   0 1 2 3 5 6 7 8 9 
##pass: devuelve un null como si no ejectura el bucle
##else: tiene la misma funcion qeu un en un condicional if per en este caso se cumple 
##cuando a terminado el bucle

#################
for letra in "buenos dias amiguitos":
    
    if letra=="o":
        continue
    
    print ("mirando que letra es : " + letra )
    
 #################################################
 
letras ="lacteos colombia le da sabor a tus desayunos todas las mñanas que sale el sol  XD XD XD"
contador=0
    
for  i in letras:
    
    if i==" ":
        continue
    contador+=1        
    
print(contador)
    
##############
while True:
    pass
## se cumple al condicion hasta qeu el usaurio de ctrl+c
##################################
    
email=input(" introdusca su email, por favor")


for i in email:
    if i=="@":
        arroba=True
        break;

else:
    arroba=False
    
print (arroba)


   



















