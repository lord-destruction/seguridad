# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 13:01:17 2019

@author: lord-drestuction
"""
###########################LISTAS
##que son las listas
## Son estructuras de  de datos que nos permiten  almacenar grandes volumenes de datos"son equivalentes
## a los arrays de otros lenguajes de programacion ". en las listas se pueden almacenar cualquier tipo 
## de valor , se pueden expandir o contraer dinamicamente aumentando sus indices o decreciendo 
## en sus indices 
####
##sintaxis
##NombreLista1=[] ## pueden ser listas vacias  o con infinidad de elementos
##NombreLista2=[elemento1,elemento2,elemento3,elemento4,elemento5,.....,elementoN]
##los elementos pertenecientes a a una lista son conocidos como indices
## Se empiezan  contar a partir del indice 0 hasta el indice N
## ejemplo LISTAEJEMPLO=[1,2,3,4,5,6,7,8] esta lista poseera 7 elementos ya que se empieza a contar apartir
## del indice 0 por lo tanto el 
## indice0 corresponde al valor 1 , el 
## indice1 corresponde al valor 2 , el
## indice2 corresponde al valor 3 , el
## indice3 corresponde al valor 4 , el
## indice4 corresponde al valor 5 , el
## indice5 corresponde al valor 6 , el
## indice6 corresponde al valor 7 , el
## indice7 corresponde al valor 8.

ListaEjemplo = ["maria","manuel","roberto","carlos"]
## si se deseara imprimir la lista debemos llamar a la lista por el nombre  y posteriormente 
## mostar todos los indices
print(ListaEjemplo[:])
## por el contrario si deseamos solamentye mostarr el elemnto amnuel lo hacemod de la siguiente manera
print(ListaEjemplo[1])
## si se desea ingresar a  un indice  que no existe mostarara un exepcion "list index out of range" 
## donde nos dice qeu eel eleimneto no existe po que esta fuera del rango
print(ListaEjemplo[7])
## si deseamoramos mostrar un indce negativo se puede teniendo en cuenta que nuestro ulñtimo indece
## de izquierda a derecha sera el valor -1 
print(ListaEjemplo[-3])
## si se posee una lista demaciado larga y deseeams acceder a un porcion especifica de la 
## lisat los podemos realizar de la siguiente manera.
## en este caso se mostraria desde  el indice 3 inclucive hasta el indice 5 excluytendo al  indice 6
ListaGrande = ["maria","manuel","roberto","carlos","rubi","mario", "marisol","daniel","carol" ]
print(ListaGrande[3:6])
## en el siguiente ejemplo se pude observer que si omitimos el primer indice el tomara ese 
## valor como = 0 y recorrera la lsiat ahasta el indice 5
print(ListaGrande[:6])
## por el contrario si se desea acceder a los elemtos indicados a apratir de el numero esto no dara
## que muetre a  partir del inidice 3 hasta el final
print(ListaGrande[3:])
## si deseamos insertar valore en la lista lo aremos de la siguinete manera tener en cuanta que 
## se agregara al final 
ListaGrande.append("rocio")
print(ListaGrande[:])
## pero si deseamos insertarlo en una posicion definida lo hariamos de la sigente manera en este caso lo
## insertara en el indice indicado desplanado al indice en 1 hacia adelante en este cso tomara el 
## valor de carlos ya que este es el 3. ahora leonor es el 3  y carlos sera el indice 4
ListaGrande.insert(3,"leonor")
print(ListaGrande[:])
## si deseamos insertar varios valores lo podemos realizar de la siguinete manera
ListaGrande.extend(["ana","rita","clara","monica","Yaned"])
print(ListaGrande[:])
##si quisieramos saber en que indice se encuantra en valor lo podremos realizar
## de la siguiente manera. y si exitste un elemento duplicad mopstrara el mas cerca al indice 0
print (ListaGrande.index("rubi"))
## saber si un elemento esta o no en un lista podems ver que rita esta en la lista no devolvera 
## un verdadero al contyrario de wilmer que me devolvera un false 
print ("rita" in ListaGrande)
print ("wilmer" in ListaGrande)
##si quisieramos elimionar a un elemento de la lista lo realizamos de la siguinete manera
ListaGrande.remove("maria")
print (ListaGrande[:])
## si queremos eliminar el ultim elelemnto  lo podemos hacer de la siguiente manera
ListaGrande.pop()
print (ListaGrande[:])

##de igual manera se pueden guardar distintos tipos de datos en una lisat
ListaDiferente=[1,1.36,"manuel ","aprende","python"]
print (ListaDiferente[:])
##
## si tenemos dos listas diferentes podemos realizar sumas pero en este caso la sumo 
## no funcona como opewardor  solo funciona como concatenador osea que la lista se agrega a al segunda 
## para formar una tercera lista 
 
Lista1=["ana","mauro",3.5,4,5]
Lista2=["bruce","willis",4.8,2,1]
Lista3=Lista1+Lista2
print(Lista3[:])

## de la misma manera funciona el * no es operador multiplicacion per si es un 
##repetidor de cantidad 
print(Lista3[:]*3)




























































