import sys
import numpy as np

#----Ejercicio 1----#
#Escribir una función que reciba una muestra de números en una lista y devuelva su media.
def media(lista):
    sum = 0
    for i in range(len(lista)):
        sum += lista[i]
    media = sum/len(lista)
    return media


#----Ejercicio 2----#
#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palindromo.

def espalindromo(palabra):
    palabra_en_reversa = ""
    for i in range(1,len(palabra)+1):
        palabra_en_reversa += palabra[-i]
    
    if (palabra == palabra_en_reversa):
        print("Es palindromo")
    else:
        print("No es palindromo")


#----Ejercicio 3----#
#Escribir una función que reciba una muestra de números en una lista y devuelva otra 
#lista con sus cuadrados
def cuadrados(lista):
    lista2 = []
    for i in range(len(lista)):
        var = lista[i] ** 2
        lista2.append(var)
    return lista2


#----Ejercicio 4----#
#Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su
#media, mediana y moda.
def numeros(lista):
    #Media
    dicc = {}
    sum = 0
    for i in range(len(lista)):
        sum += lista[i]
    media = sum/len(lista)
    dicc["Media"] = media

    #Mediana
    if (len(lista)%2 == 0):
        lista_ordenada = np.sort(lista)
        indice1 = int(len(lista_ordenada)/2)
        indice2 = int(len(lista_ordenada)/2) - 1
        mediana = (lista_ordenada[indice1] + lista_ordenada[indice2])/2
    else:
        lista_ordenada = np.sort(lista)
        indice = int(len(lista_ordenada)/2)
        mediana = lista_ordenada[indice]
    dicc["Mediana"] = mediana

    #Moda
    dic_moda = {}
    for i in lista:
        key = str(i)
        if key in dic_moda.keys():
            dic_moda[key] += 1
        else:
            dic_moda[key] = 1
    
    len_moda = 0
    moda = 0
    for key in dic_moda.keys():
        if (dic_moda[key] > len_moda):
            len_moda = dic_moda[key]
            moda = int(key)
    dicc["Moda"] = moda
    return dicc





if __name__ == "__main__":
    arr = np.array([1,2,3,4,3])
    #med = media(arr)
    #rint(med)

    #palabra = sys.argv[1]
    #espalindromo(palabra)

    #lista_cuadrados = cuadrados(arr)
    #print(lista_cuadrados)

    diccionario = numeros(arr)
    print(diccionario)























