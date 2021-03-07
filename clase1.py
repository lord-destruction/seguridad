#Python 3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32

#Warning:
#This Python interpreter is in a conda environment, but the environment has
#not been activated.  Libraries may fail to load.  To activate this environment
#please see https://conda.io/activation

#Type "help", "copyright", "credits" or "license" for more information.

#############################TIPOS DE VARIABLES###########################################################################
##esta es la clase de progaramacion de python. se empiesa por el tipo de datos existentes 
##los cuales son  
##NUMERICOS: que  de desglosan en otros tres tipos de datos los cuales son:
##enteros:enteros 0-9 -infinito y mas alla, hasta el infinito y mas alla. OJO pero enteros
##float:valores de coma flotante como -infinito.3 hasta infinito.3 o algun valor aproximado PI 3.16 euler, otros decimales negativos y posivos.
##complejos:
##TEXTOS:son de tipo texto debe ir entre comillas dobles  o simples o pueden llevar comillas triples
##BOOLEAN: son datos de toma de decicion verdadero o falso "true o false" se puede utilizar como bandera de toma de decicion.
#############################################################################################################################

#############################TIPOS DE OPERADORES###########################################################################
## OPERADFORES ARIMETICOS: son aquillos que me sirver para realizar algun tipo de opeacion  
## + realizar sumas adiciones ejmplo 3+4=7
## - realizar restas sustarcciones 3-4=-1
## * realizar multiplicaciones 3*4=12
## / realizar divisiones 3/4=0.75
## % es el resto de una division ejemplo 10/3=3  porque 3*3=9  y 9-10=1 este valor es el resto de la operacion por lo tanto este es el modulo
##** es el valor exponcial de un numero el cual se puede representar  asi 3 elevado a la 5 = 3**5
##// nos devuelve el valor entero de una divicion un ejemplo 9/2= 4.5 este opearacion nos devolvera el valor 4
##
## OPERADFORES COMPARACION: son aquillos con los que puedo realizar comparciones de entre valores o condiciones
## ==  un valor es igual a otro valor
## !=  un valr es diferente de otro valor
## >   un valor es estricatamente mayor que otro valor
## <   un valor es estricatamente menor que otro valor
## >=  un valor es mayor o igual que otro valor
## <=  un valor es menor o igual que otro valor
##
## OPERADFORES LOGICOS: son aquellos que permites evaluar mas de una ccomparacion a la vez
## AND  (condicion y condicion y condicion y condicion) sale algo de estas comparaciones si se cumplen todas
## OR 	(condicion o condicion o condicion o condicion) sale salgo, si almenos una se cumple
## NOT  
##
## OPERADFORES ASIGANACION: sirver para asignar valores a variables
## =  valor es igual a X ejemplo nombrevariable=8
## += es para sumarle un valor a cierta variable
## -= es para restarle un valor a cierta variable
## *= es para multiplicarle un valor a cierta variable
## /= es para dividirle un valor a cierta variable
## %= es para acerle la operacionde modulo a cierta variable
## **=  para acerle la operacionde exponencial a cierta variable
## //=  para acerle la operacionde devision entera a ciertavariable
##
## OPERADFORES ESPECIALES: comparar valres dentro de secuencias la veremos mas adelnate
## IS
## IS NOT
## IN
## NOT IN
##
## VARIABLE: es un espacion en memoria  que almacena un valor, el cual puede cambiar  durante la ejecucion de un programa,
##           la nomenclatura para el nombramientito de una varible puede ser la siguinete ejm : Nombre, nombre, nombre1, Nombre_apellido, 
##           por una buena practica es bueno dar nombre a las varibles con nombres claros a lo que se pienza que realize 
##            y su primer letra en mayuscula, Suma ,Valor_total_iva, Descuentos_de_nomina. mucho cuidado con los ls espacios si los nombre de las
##		     varibles si esta compuesto por mas de un nombre. muy importante que en python los variables estan definidas mucho por el dipo de dato
##			ejemplo Numero=3  este tipo de varible es asigando  como tipo de dato entero y la varibles numero es tomada como objeto.
##			ejemplo type(Numero) nos mostrara que es una clase de tipo int


##nos mostrara >>> >>> 
print ("hola mundo")

Numero1=7
Numero2=5
Numero3=3
Numero4=1
Numero5=1 

Suma=Numero1+Numero4
print("Suma: ",Suma)
type(Suma)

Resta=Numero3-Numero1
print("Resta: ",Resta)
type(Resta)

Multiplicacion=Numero1*Numero4
print("Multiplicacion: ",Multiplicacion)
type(Multiplicacion)

Division=Numero4/Numero1
print("Division: ",Division)
type(Division)

Mudulo=Numero3%Numero2
print("Mudulo: ",Mudulo)
type(Mudulo)

Exponencial=Numero3**Numero2
print("Exponencial: ",Exponencial)
type(Exponencial)

Division_entera=Numero3//Numero2
print("Division_entera: ",Division_entera)
type(Division_entera)

Mensaje=""" este es un mensaje 
con tres saltos de linea
para una prueba"""
print (Mensaje)
type(Mensaje)

Numero10 =5
Numero10 += 3
print("el numero es ",Numero10)

Numero10 =5
Numero10 -= 3
print("el numero es ",Numero10)

Numero10 =5
Numero10 *= 3
print("el numero es ",Numero10)

Numero10 =5
Numero10 /= 3
print("el numero es ",Numero10)

Numero10 =5
Numero10 %= 3
print("el numero es ",Numero10)

Numero10 =5
Numero10 **= 3
print("el numero es ",Numero10)

Numero10 =5
Numero10 //= 3
print("el numero es ",Numero10)


####OPERADORES DE COMPARACION

if Numero1>Numero2:
	print("el mayor de los numero1 ")
else:
	print("el mayor es el numero 2 ")	

if Numero1<Numero2:
	print("el menor de los numero1 ")
else:
	print("el menor es el numero 2 ")	

if Numero4>=Numero5:
	print("el numero 4 igual al numero 5 ")
else:
	print("ppues habria uno mayor y uno menoralguno de los dos ")

if Numero1<=Numero2:
	print("el menor de los numero1 ")
else:
	print("el menor es el numero 2 ")

if Numero1!=Numero2:
	print("el numero1 es diferente")
else:
	print("pues serian iguales")

if Numero4==Numero5:
	print("estos serian iguales")
else:
	print("pues serian diferentes")

###########################################
###    FUNCIONES
##Que son: un grupo de lineas de codigo.que  realizan una tarea asignada, estas pueden devolver
##valores, y poseen parametros y argumentos tambien son conocidas como metodos cuando se definen
##dentro de una clase.
##Utilidad: reultilizar el codigo cuando sea necesario
##Sintaxis: def Nombre_de_funcion():
##              instrucciones de la funcion
##              return(opcional)    
##    
###############
##Sintaxis: def Nombre_de_funcion(parametros):
##              instrucciones de la funcion
##              return(opcional)    
## 
## dentro de los parentesis se conoce  como zona de parametros o argumentos tener muy en cuanta los
## lods puntos y la identacion    
## tener en cuanta  que def es una palabra reservada del lenguaje y cada lenguakje de programacion
## posee las suyas    
##Ejcucion: en caso que una funcion no reciba parametros se ejecutad e la siguinte manera
    ## Nombre _funcion()
## en caso de que reciba parametros  Nombre _funcion(parametros)

print ("con amnuel estamos aprendiendo python")
print ("estamos aprendiendo instruciones basicas")
print ("esperemos que em entienda.")

##### si desearmos utilizar esto muchismas veces  por lo general se haria de la siguinte forma  
##y si son muchas veces que?

print ("con amnuel estamos aprendiendo python")
print ("estamos aprendiendo instruciones basicas")
print ("esperemos que em entienda.")

print ("con amnuel estamos aprendiendo python")
print ("estamos aprendiendo instruciones basicas")
print ("esperemos que em entienda.")

print ("con amnuel estamos aprendiendo python")
print ("estamos aprendiendo instruciones basicas")
print ("esperemos que em entienda.")


### la idea es realizar esto dentro de una funcion. debido a que,  si se desea utilizar estas lineas
### un millar de veces, no las vamos a escribir esa misma cantidad, solo se escribe un vez y se
### utilizan o se llaman solo donde sea necesario. 

def Esta_es_una_funcion(): ##declaracion de la funcion
    
    print ("con amnuel estamos aprendiendo python") ##intrucciones de la funcion
    print ("estamos aprendiendo instruciones basicas")
    print ("esperemos que em entienda.")

## esta funcion no cumple su cometido  hasta que sea llamada por lo tanto tiene que ser llamada
Esta_es_una_funcion() ##llamdo de la funcion

##se puede obervar que uestra funcion se puede llamar muchas veces en cual quier parte del codigo
##ejemplo
print("esto es una parte de el codigo que se planea haga algo para llamar luego a una funcion")
Esta_es_una_funcion()
print("llamamos a nuestra funcion la cual podria ejecutar algo  y luego la llamamos nuevamente")
Esta_es_una_funcion()
print("nuevamente realizamos algo  dentro de nuetro programa y podemos volver a llamar la funcion")
Esta_es_una_funcion()
print("podemos realizar muchisimas cosas antes de llamr a nuestra funcion nuevamente")
suma=Numero1+Numero2
resta=Numero1-Numero2
print ("la suma es:", suma)
print ("la resta es:",resta)  
Esta_es_una_funcion()

###Fnciones con paso de parametros

def Suma():
    Numero_uno=5
    Numero_dos=7
    print (Numero_uno + Numero_dos)
    
Suma()

## cabe resaltar que la potencialidad de un funcion es que realiz en este caso la suma
##  no de los mismos valores si no que sean diferentes. entonces utilizaremos los
## parametros o argumentos

def Suma(Numero_uno,Numero_dos):##declacion de la funcion  y xzoana de parametros
       print (Numero_uno + Numero_dos)
    
Suma(5,8)

Suma(35,57)

Suma(15,28)

## en este tipo de funcion los datos de entrada de la funcion son los parametos
## se poueden pasar la cantidad de parametros que se desee. Estos son alacenados
## en la zona de parametros de la funcion  posteriormente se realiza las suma para ser
## mostrada  estos paremetors pueden variar  con muchos tipos de datos 

def Suma(Nombre,Numero_uno,Numero_dos):##declacion de la funcion  y xzoana de parametros
       print ("mi nombre es ", Nombre ,"Y la suma es :",Numero_uno + Numero_dos)
    
Suma("Manuel",5,8)

Suma("Manuel",35,57)

Suma("Manuel",15,28)



##de igual manera si necesitamos retornar un valor 
def Suma(Numero_uno,Numero_dos):##declacion de la funcion  y xzoana de parametros
       resultado = Numero_uno + Numero_dos
       return resultado
    
print (Suma(5,8))

print (Suma(35,57))

print (Suma(15,28))

## otro ejemplo 
def Suma(Numero_uno,Numero_dos):##declacion de la funcion  y xzoana de parametros
       resultado = Numero_uno + Numero_dos
       return resultado
    
Almacena_resultado=Suma(5,8)
print (Almacena_resultado)
## esto no permite que dentro de nuetro programa en cualquier parte  sea alamacenado el resultado
## entregado por valores o informacion retornada por la funcion  para luego ser mostrada
##

##LISTAS





























