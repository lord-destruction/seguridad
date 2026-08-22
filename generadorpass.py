import random

minuscula = "abcdefghijklmnñopqrstuvwxyz"
mayuscula = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numero = "0123456789"
simbolo = "[]{}()+-*/;,:.-^`´~¿¡'?=&%$@!|¬°"

all = minuscula+mayuscula+numero+simbolo
length = 18

pasword = "".join(random.sample(all,length))

print(pasword)