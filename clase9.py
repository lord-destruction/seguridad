# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 17:42:33 2020

@author: lord-drestuction
"""

###POO

##pardigmas de PROGRAMCION

##POP  programacion oreintada a procediminetos
        ## fortran cobol basic
        ##Desventjas
            ##unidades de codigo muy grandes en aplicaciones muy complejas
            ##aplicaciones complejas el codigo  es deficil de decifrar
            ##poco reutilisable
            ##si existe error en una linea el programa peta completo
            ##codigo spaguetti
            ##dificil de depurar en caso de error
            
##consiste en trasladar la naturaleza del los objetos a a codigo de programacion
##la naturaleza de un objeto es  qeu tienen un estado , un comportamineto, propiedades,
## un carrro el estado puede ser varado o andadndo 
## un carro las propiedades color tipode carro  tamaño #de ejes ##vetanas
## comportamiento puede arrancar acelerar frenar             
##POO  programacion orientada a objetos


#orientado aobjetos 
#    C++.java .net        
#ventajas
#modula r
#es  reutilizable herencia
# puede manejar ecxepciones de codigo en caso de fallos
#posee encapsulamiento
            
            
##clase 
##objeto 
##instancia de clase 
##ejemplar de clase 
##mudularizacion 
##encapsulacion 
## herencia
##polimorfismo
            
#conceptos terminos
            ##clase: caracteristicas  comunes de un grupo de objetos
            ##instancia de clase: objeto o un ejemplar de una clase   similar a objeto o ejemplar de clase 
            ##                    caracteristicas qeu hacen diferente a los objetos unos de otros
            ## modularizaion: conjunto de clases perteneciente a una aplicacion 
            ##                permite utilizar clases de un lugar a otro
            ## encapsulacion: es la diferencia que tienen 2 clases y que permite ejecutar una rutina de otra
            ##                sin que estas sepan qeu hace cada una. pero estan conectadas mediante metodos de
            ##                acceso
            ##objeto:    acceseder a las propiedades del objeto     micoche.ancho=alto        
            ##objeto:    acceseder a comportamineto del objeto     micoche.arranca()
            
            
            
            
##Metodo   comportamiento una funcion especial qeu pertenece a la clase           
            
            
class Coche():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False                               ## estara parado
            
    def arrancar(self):
        ##self hacer referencia al objeto que pertenece a la clase
        self.enmarcha=True

                                      ## this.
    def estado(self):
        if(self.enmarcha):
            return"el carro esta andando"
        else:
            return"el coche esta parado"
            
michoche=Coche()                                 ##instancia de clase no se utiliza new

print("el largo del carro es ", michoche.largoChasis)
print("la cantidad de llantas que tiene el carrro es ", michoche.ruedas)


michoche.arrancar()            
print (michoche.estado())
## esta clase tiene 4 prpiedades y 2 comportamientos
###  priemro hacemos que el carro arranque y posteriormente decimos en que estado esta. 
###  como en el metodo arrancar el comportamiento del carro lo colocamos en verdadero.
###  este estado almacenado cambia, y en el comportamineto "estado" llamamos a lo que se tiene alamcenado
###  qeu en ese mometo cambio y es "True" mostrando asi en el estado enmarcha 
###  qeu el carro esta andando. 
###  Si quitamos el llamdo a la funcion arrancar el mostrara qeu el carro esta deteneido   
            
#############################################            
print("acontinuacion se agregara un nuevo objeto con un diferente comportamiento")
print ("------------------------------------------------------------------------")
micoche2=Coche()

print("el largo del carro es ", micoche2.largoChasis)
print("la cantidad de llantas que tiene el carrro es ", micoche2.ruedas)
print (micoche2.estado())            
            
            
            
            
############################################
class Coche2():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False                               ## estara parado ///ojo este es el estado inicial
        # y arrancar devolvera el estado del mismo
    def arrancar(self,arrancamos):#en este caso arrancamos espara un parametro o argumento para saber el estado
         
        ##self hacer referencia al objeto que pertenece a la clase
        self.enmarcha=arrancamos  #esta variable en marcha resibira por parametro lo qeu se le pase en arrancamos
                                    #si se le pasa true estara en marcha de lo contrario estara parado .|.
        
        if (self.enmarcha):
            return "el carro esta andando"
        else:
            return "el carro esta parado"
        
    def estado(self):
        print("El carro tiene ",self.ruedas,"un ancho de ",self.anchoChasis,"tiene un largo de ",self.largoChasis)

        ##mientra el metodo estado sera el encargado de devolver la informacion del objeto

micoche3=Coche2()
micoche4=Coche2()            
            

print(micoche3.arrancar(True))                       
micoche3.estado()
print ("--------------------------------------------------------------")

print(micoche4.arrancar(False))                       
micoche4.estado()
            
            
############################################################
#constructor definira el estado inicial qeu tengan los objetos qeu pertenescan a una clase
 
class Coche2():
    
    def __init__(self):  ##en este casoel constructor tiene el nombre de init a 
                         ##diferencia de java qeue l constructor por lo general se llama igual qeu la clase
        self.largoChasis=250
        self.anchoChasis=120
        self.ruedas=4
        self.enmarcha=False  


    def arrancar(self,arrancamos):#en este caso arrancamos espara un parametro o argumento para saber el estado
         
        ##self hacer referencia al objeto que pertenece a la clase
        self.enmarcha=arrancamos  #esta variable en marcha resibira por parametro lo qeu se le pase en arrancamos
                                    #si se le pasa true estara en marcha de lo contrario estara parado .|.
        
        if (self.enmarcha):
            return "el carro esta andando"
        else:
            return "el carro esta parado"
        
    def estado(self):
        print("El carro tiene ",self.ruedas,"un ancho de ",self.anchoChasis,"tiene un largo de ",self.largoChasis)

        ##mientra el metodo estado sera el encargado de devolver la informacion del objeto

micoche3=Coche2()#objeto1
micoche4=Coche2()#objeto2         
            

print(micoche3.arrancar(True))                       
micoche3.estado()
print ("--------------------------------------------------------------")

print(micoche4.arrancar(False))                       
micoche4.ruedas=7   ##fijese en este caso qeu estamos pasando el valor de 7 a las ruedas y esto no deberia de permitirse 
micoche4.estado()   ## por esete motivo se crea el concepto de encapsulacion


#Encapsulacion
# encvapsular o preoteger una propiedad para que no pueda ser modificada desde afuera de la clase o desde algun tipo de llamado
#por lo tanto la mejor manera de protegen dicha propiedad y qeu no sea modificada es becesario encapsular
#python se hace de la sig manera self.__propiedad
class Coche2():
    
    def __init__(self):  ##en este casoel constructor tiene el nombre de init a 
                         ##diferencia de java qeue l constructor por lo general se llama igual qeu la clase
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False  


    def arrancar(self,arrancamos):#en este caso arrancamos espara un parametro o argumento para saber el estado
         
        ##self hacer referencia al objeto que pertenece a la clase
        self.__enmarcha=arrancamos  #esta variable en marcha resibira por parametro lo qeu se le pase en arrancamos
                                    #si se le pasa true estara en marcha de lo contrario estara parado .|.
        
        if (self.__enmarcha):
            return "el carro esta andando"
        else:
            return "el carro esta parado"
        
    def estado(self):
        print("El carro tiene ",self.__ruedas,"un ancho de ",self.__anchoChasis,"tiene un largo de ",self.__largoChasis)

        ##mientra el metodo estado sera el encargado de devolver la informacion del objeto

micoche3=Coche2()#objeto1
micoche4=Coche2()#objeto2         
            

print(micoche3.arrancar(True))                       
micoche3.estado()
print ("--------------------------------------------------------------")

print(micoche4.arrancar(False))                       
micoche4.ruedas=7   ##fijese en este caso qeu estamos pasando el valor de 7 a las ruedas y esto no deberia de permitirse 
micoche4.estado()   ## por esete motivo se crea el concepto de encapsulacion

####detalle en cuando tgrata de modificar micoche4.ruedas=7 nole permite modificar  y pasa los valores por defecto
####declarados en el contructor ya encapsulado






############################################################################

numero= int(input("introdusca un numero: "))

if ((numero % 2)==0):
    print("usted es par")

elif ((numero % 2)!=0):
    print("usted es impar ")


if ((numero/numero==1) and (numero/1==numero) and (numero %2 == 1 )):
    print("usted es primo")

else:
    print("no es primo")


numero= int(input("introdusca un numero: "))

for x in range(numero):
    numero2=((numero-1)+(numero-2))
    print(numero2)














            
            
            
            
            
            