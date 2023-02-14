import sys

#----Ejercicio 1----#
#Crear un módulo para validación de nombres de usuarios. Dicho módulo, deberá cumplir con los siguientes 
#criterios de aceptación:
#-El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12.
#-El nombre de usuario debe ser alfanumérico.
#-Nombre de usuario con menos de 6 caracteres, retorna el mensaje "El nombre de usuario debe contener
#entre 6 a 12 caracteres"
#-Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el mensaje "El nombre de 
#usuario puede contener solo letras y números".
#-Nombre de usuario válido, retorna True.

nombre = sys.argv[1]

if (len(nombre)>=6 and len(nombre)<=12):
    if (nombre.isalnum() == True):
        print(True)
    else:
        print("El nombre de usuario puede contener solo letras y números")
else:
    print("El nombre de usuario debe contener entre 6 a 12 caracteres")










#----Ejercicio 2----#
#Crear un programa que de como resultado el termino "n" de la sucesion de Fibonacci. El "n" es numero
#ingresado como argumento de entrada