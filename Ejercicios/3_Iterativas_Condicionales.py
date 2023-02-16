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

# nombre = sys.argv[1]

# if (len(nombre)>=6 and len(nombre)<=12):
#     if (nombre.isalnum() == True):
#         print(True)
#     else:
#         print("El nombre de usuario puede contener solo letras y números")
# else:
#     print("El nombre de usuario debe contener entre 6 a 12 caracteres")


#----Ejercicio 2----#
# Escribir un programa que almacene la cadena de caracteres de una contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

# contra = "qwerty"
# while True:
#     contra_ingresada = input("Escriba la contraseña: ")
#     if (contra_ingresada == contra):
#         print("La contraseña ingresada es la correcta")
#         break
        


#----Ejercicio 3----#
# Escribir un programa que capture una palabra ingresada como argumento de entrada
# y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

palabra = sys.argv[1]

for i in range(1,len(palabra)+1):
    letra = palabra[-i]
    print(letra)
