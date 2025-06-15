# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 21:33:07 2020

@author: lord-drestuction
"""

##GENERADORES

#que son 
# son extructuras  que extraen  valores de una funcion y se alamacenan en objetos qeu se pueden recorrer
# se alamacenan de uno en uno, y cada vez qeu se alamacena un valor  este permanece en estado pausado hasta
# qeu solicita el siguiente valor.  



#funcionamiento: se compara con una funcion normal   

#def generarnumepar():                      # def generarnumepar():
#        .                                       . 
#        . codigo                                .codigo
#        .                                       .
#    return numeropar                       # yield numeros
#    devuelve toda la lista(2 4 6 8 10)       [2 4 6 8 10] objeto generador iterable 
#
#
#que utilidad tienen
#son mas eficiaentes que las funciones tradicionales
#muy utilis con listas de valore s infinitos
#bajo determinados esenarios en ma util devolver  valroes de uno en uno
#
#sitaxis
#
#Def generanumeros():
#    yield numeros    tambien puede llevar un return
#

numero= int(input("introdusca la cantidad de numeros pares qeu desea: "))

def generaPare(limite):           #  funcion de numeros pares  pero ponemos un limite  para que no se valal a infinito
    num=1                         #  varible
    milista=[]                    #  lista qeu almacenara los numeros pares
    while num<limite:             #  se crea un un bucle qeu mientras el numero sea menor que el limite ejecute
        milista.append(num*2)     #  agregue a la lista el valor de la varible numero numero 1*2 = 2 y este valor se almacenara en la lista 
        num=num+1                 #  ahora el numero es igual al numero mas 1 osea 2 y numero *2 es 4 y asi susesivamente 
    return milista                #  devuelve la que hay en lista
print (generaPare(numero))

###########

numero= int(input("introdusca la cantidad de numeros pares qeu desea: "))

def generaPare(limite):           #  funcion de numeros pares  pero ponemos un limite  para que no se valal a infinito
    num=1                         #  varible
   
    while num<limite:             #  se crea un un bucle qeu mientras el numero sea menor que el limite ejecute
        yield num*2                   #  agregue a la lista el valor de la varible numero numero 1*2 = 2 y este valor se almacenara en la lista 
        num=num+1                     #  ahora el numero es igual al numero mas 1 osea 2 y numero *2 es 4 y asi susesivamente 
    
devuelvePares=generaPare(numero)

for i in devuelvePares:
    print (i)


##############################


numero= int(input("introdusca la cantidad de numeros pares qeu desea: "))

def generaPare(limite):           #  funcion de numeros pares  pero ponemos un limite  para que no se valal a infinito
    num=1                         #  varible
   
    while num<limite:             #  se crea un un bucle qeu mientras el numero sea menor que el limite ejecute
        yield num*2                   #  agregue a la lista el valor de la varible numero numero 1*2 = 2 y este valor se almacenara en la lista 
        num=num+1                     #  ahora el numero es igual al numero mas 1 osea 2 y numero *2 es 4 y asi susesivamente 
    
devuelvePares=generaPare(numero)

print (next(devuelvePares)) 
print ("aqui hay mas codigo...")
print ("aqui hay mas codigo...")
print ("aqui hay mas codigo...")
print ("aqui hay mas codigo...")
print ("aqui hay mas codigo...")
print ("aqui hay mas codigo...")
print (next(devuelvePares))     
print ("aqui hay mas codigo...")
print ("aqui hay mas codigo...")
print ("aqui hay mas codigo...")
print ("aqui hay mas codigo...")
print ("aqui hay mas codigo...")
print ("aqui hay mas codigo...")    
print ("aqui hay mas codigo...")
print ("aqui hay mas codigo...")
print ("aqui hay mas codigo...")
print ("aqui hay mas codigo...")
print ("aqui hay mas codigo...")
print ("aqui hay mas codigo...")    
print (next(devuelvePares))     
###########################################################################

def devuelveCiudad(*ciudades):                 ##* numero indetermndo de elementos y son en forma de tupla
    for elemento in ciudades:
        for subelemto in elemento:
            yield subelemto
        
ciudadesDevueltas=devuelveCiudad("popayn","cali","bogota","medellin","pasto")


print (next(ciudadesDevueltas))

print (next(ciudadesDevueltas))

#####################
def devuelveCiudad(*ciudades):                 ##* numero indetermndo de elementos y son en forma de tupla
    for elemento in ciudades:
        #for subelemto in elemento:
            yield from elemento                 ## hace l mismo qeu el for anidado desde el preimer for
                                                ## saca los dos elemtento pertenecientes al subelemento
                                                ## en este caso 1 elemnto es ciudad y subelemtos son las letras
                                                ## de las que esta compuesta cada ciudad
        
ciudadesDevueltas=devuelveCiudad("popayn","cali","bogota","medellin","pasto")


print (next(ciudadesDevueltas))

print (next(ciudadesDevueltas))




























