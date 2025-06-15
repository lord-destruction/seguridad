# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 19:33:16 2019

@author: lord-drestuction
"""

#########CONDICIONALES III

#en python no existe el switch ya que se considera innesesario debido a que por su simplisidad 
#se puede realizar con simples if, en tros lenguajes se utiliza el switch cuando hay que evaluar muchismas
#condiciones encadenadas se pueden utilizar diccionarios u otros metodos
#tabien se puede utilizar concatenacion de operadores de comparacion lo que no permite evaluar cantidad 
#de condiciones encadenadas

edad=-100 ##pero que pasa si metemos un valor negativo es correcto pero nadie tiene menos x años por lo tanto
        ##es nesesario acotar esto ###probar con 8 y -8###

if 0<edad<100: ##esats condiciones se leeen de izquierda a derecha
    print ("edad correcta")
else:
    print("edad incorrecta")
    
###################

salario=int(input("introduce el salario"))
print("salario devengado: "+ str(salario))

if 30000<salario<50000:
    print("felicidades es usted el dueño del chuzo")

elif 15000<salario<=30000:
    print("usted es uno mas ")

else:
    print("eres una buena persona")
  
######################################
## operaradores logicos AND  OR  IN
 
    
    
print ("programa de becas de año 2019")
distancia_a_la_universidad=float(input("introduce la distancia en km a la universidad: "))
print (distancia_a_la_universidad)

nunero_hermanos=int(input(" introduca la cantidad de hermanos que posee: "))
print (nunero_hermanos)    

salario_familiar=float(input(" introduca el salario anual familiar: "))
print (salario_familiar)    

if distancia_a_la_universidad > 30 and nunero_hermanos > 3 and salario_familiar < 6000000 :   
    print("dale...  ha aplicado a la beca y la gano")

else: 
    print("no tiene derecho a beca")


####################################################
print ("programa de becas de año 2019")
distancia_a_la_universidad=float(input("introduce la distancia en km a la universidad: "))
print (distancia_a_la_universidad)

nunero_hermanos=int(input(" introduca la cantidad de hermanos que posee: "))
print (nunero_hermanos)    

salario_familiar=float(input(" introduca el salario anual familiar: "))
print (salario_familiar)    

if distancia_a_la_universidad > 30 and nunero_hermanos > 3 or salario_familiar < 6000000 :   
    print("dale...  ha aplicado a la beca y la gano")

else: 
    print("no tiene derecho a beca")


##############
#en el primer ejemplo cabe resaltar que la persona que aplica a ala beca debe de cumplir los tres requisitos
#do lo contrario no aplicara 

#en el segundo se deben de cumplir las dos primeras condiciones estrictamente pero se ignoran si cumple la 
#tercera
##############

print("toma de asignaturas facultad de medicina")
print ("asignaturas optadas : cirugiaI - cirugiaII - cirugiaIII ")
asignatura =input("escriba el numbre de la asignatura")

if asignatura in("cirugiaI","cirugiaII","cirugiaIII"):
    print("asignatura elegida: " + asignatura)
else:
    print("la asignatura no esta en la lista")

## en este caso el programa es case sentive por que el lenguaje es asi pero se puede sulionar 
##de la siguiente forma
###########


print("toma de asignaturas facultad de medicina")
print ("asignaturas optadas : CirugiaI - CirugiaII - CirugiaIII")

opcion = input("escriba el numbre de la asignatura : ")

asignatura= opcion.upper()

if asignatura in("CIRUGIAI","CIRUGIAII","CIRUGIAIII"):
    print("asignatura elegida: " + asignatura)
else:
    print("la asignatura no esta en la lista")    

## lower esto lo que ara es que lo que esta alamacenado en opcion  
## como asignatura lo convertira a minusculas 
## upper esto lo que ara es que lo que esta alamacenado en opcion
## como asignatura lo convertira a mayusculas


print("toma de asignaturas facultad de medicina")
print ("asignaturas optadas : CirugiaI - CirugiaII - CirugiaIII")

opcion = input("escriba el numbre de la asignatura : ")

asignatura= opcion.lower()

if asignatura in("cirugiai","cirugiaii","cirugiaiii"):
    print("asignatura elegida: " + asignatura)
else:
    print("la asignatura no esta en la lista")    



















    