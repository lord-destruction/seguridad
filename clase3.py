# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:18:42 2019

@author: lord-drestuction
"""

##TUPLAS
##son muy parecidas  a las lisats pero al contrario de las anteriores estas no cambian despues de su creacion
##no permiten mover, añadir , eliminar elementos, busquedas se realiza de la misma manera que en lista.
## se permite ñla extraccion de lementos pero el resultado sera una tupla nueva.
## tambien esta permituido la comprobacion de existecia de un elemento en la tupla
## ventajas son mas rapidas  menos espacio, se pueden formatear strings, son utilizadas como claves de diccionario
##sintaxis NombreTupla=(element1, elemento2, elemento3.....elementoN ) al igual que la lista pero entre ()


LaTupla=("juan",13,1,26,"luz",21,"sandra","monica",25,38.8,"alfredo")
## podemos convertir una tupla en una lista y una lista en una tupla
miLista=list(LaTupla)
print (miLista)
print (LaTupla)
#como se puede ver la diferencia de  netre ambas una esta con corchestes y la otra con parentesis
LaLista=["manuel",13,1,26,"lucia",21,"margot","consuelo",25,38.8,"magali"]
miTupla=tuple(LaLista)
print(miTupla)
print(LaLista)
## se puede de esta manera buscar si un elemento se encuantra en una tupla se convierte en lista 
## y luego se busca en ella 
LaTuplaBus=("juan",13,1,26,"luz",21,"sandra","monica",25,38.8,"alfredo",21,"sargento",21,"angulo","sandra")
miLista=list(LaTuplaBus)
print ("monica" in LaTuplaBus)
##podemos contar el numero de veces que se encuantar un elemento en una tupla
print (LaTuplaBus.count(21))
print (LaTuplaBus.count("sandra"))
print (len(LaTuplaBus))## con len podemos contar la cantidad de elementos de la tupla

## se pueden hacer tuplas de un solo elemento
TuplaUnitaria=("manuel",)
print (len(TuplaUnitaria))
print (TuplaUnitaria)
##tambien podemos hacer una tupla de sin nescesidad de parentesis
TuplasinPar="juan",13,1,26,"luz",21,"sandra","monica",25,38.8,"alfredo",21,"sargento",21,"angulo","sandra"
print(TuplasinPar)
##listar el indice de un elemento en una tupla
print (LaTuplaBus.index("monica"))


#####podemos asiganar valores  de una tupla  qu sean correspondientes a una cirtu nuemero de datos 


TuplaCumple=("wilmer" ,8,3,1981)
nombre, dia, mes, anio= TuplaCumple
## podemos ver que al iprimir no importa el orden nos generara los adatos solicitados 
## a esto de le conoce como desempaquetado de tuplas
print(nombre)
print(anio)
print(mes)
print(dia) 

####################################
##DICCIONARIOS###
## nos permiten alamacenar enteros, decimales, textos, listas, tuplas, inclusive otros diccionarios 
## se utilizan manjenado una clave:valor para cada elemento almacendo.
## el orden es indiferente a ala hora de almacenar la informacion
##sistanxis diccionario={"Colombia":"Bogota","Francia":"Paris","Ecuador":"Quito","Rusia":"Berlin"}


Dicionario1={"Nicola":"Tesla","Enrico":"Fermi","Albert":"Einstein","Neils":"Bor","Isaac":"Newton","Nicolas":"Copernico"}
print (Dicionario1["Nicola"]) ##esto se puede hace para mostrar un valor asociado a una clave 
print (Dicionario1["Tesla"]) ### esta manera no funciona inversamente
print (Dicionario1)
##mostrar un diccionario y un valr asociado a una clave

Dicionario1["Italia"]="lisboa"
print (Dicionario1)
Dicionario1["Italia"]="Roma" ##lo que hace esto es que corrije el valor en caso de que no 
                             ##correspoandao este mal. en un diccionario  los valore s se remplazan
                             ##no pueden existirdos claves iguales
print (Dicionario1)                            
###
del Dicionario1["Neils"]
print (Dicionario1)
##podemos ver que se  ha eliminado un elemento del diccionario  indicando la clave, esto tambien borra el valor

Dicionario2={"Nicola":3,315.26:"Fermi","Albert":18,23:"Bor","Isaac":62,"Nicolas":"Copernico"}
##podemos creart diccionarios con diferentes tipos de datos 
print (Dicionario2)

LaLista=["francia","lucia","daxi","margot","consuelo","magali"]
Diccionario3={LaLista[0]:"esta en la casa de diome",LaLista[1]:"casa lucia",LaLista[2]:"casa margot",LaLista[3]:"cine",LaLista[4]:"pisisna",LaLista[5]:"almorzando"}
print (Diccionario3)
print (Diccionario3["francia"])

Diccionario4={10:"ronaldiño","nombre":"ronaldo de asis","Equipo":["Barcelona","Gremio","Milan","Flamenco","Mineiro"],"botin":["no tiene",2015]}
print (Diccionario4)

## podemos crear un dicionario que contenga utro diccionario dentro
Diccionario5={10:"messi","nombre":"leonel","Equipo":["Barcelona","Gremio","Milan","Flamenco","Mineiro"],"botin":{"temporadas":[2014,2015,215,2016,2017,2018]}}
print (Diccionario5)
print (Diccionario5["botin"])
print (Diccionario5.keys()) ### devuelve la lalves
print (Diccionario5.values())### devuelve los valores 
print (len(Diccionario5))##longitud del diccionario




















