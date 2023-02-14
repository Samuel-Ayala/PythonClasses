import sys

#----Ejercicio 1----#
#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
#Después debe mostrar por pantalla la paga que le corresponde.

num_horas = input("Numero de horas: ")
costo = input("Costo: ")
resultado = int(num_horas) * int(costo)
print(resultado)


#----Ejercicio 2----#
#Escriba un programa que convierta segundos a horas + minutos + segundos. Los segundos deben 
# ingresarse como argumento de entrada

# segundos = sys.argv[1]
# segundos = int(segundos)

# horas = segundos // 3600

# minutos = (segundos % 3600)//60

# segundos = (segundos % 3600)%60

# print(horas,minutos,segundos)



#----Ejercicio 3----#
#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla "la <n> entre 
#<m> da un cociente <c> y un resto <r>" donde <n> y <m> son los números introducidos por el usuario, 
#y <c> y <r> son el cociente y el resto de la división entera respectivamente.

# n = int(sys.argv[1])
# m = int(sys.argv[2])

# c = n//m
# r = n%m

# print("la ",n," entre ", m, " da un cociente ", c, " y un resto ", r)



