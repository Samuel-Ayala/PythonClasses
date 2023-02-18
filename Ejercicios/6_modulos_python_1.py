import numpy as np
import statistics as st
import matplotlib.pyplot as plt
import time

#----Ejercicio 1----#
#Crear un arreglo de 10 unos con Numpy
# a = np.ones(10)
# print(a)



#----Ejercicio 2----#
#Crear un arreglo con 20 numeros aleatorios entre 10 y 30. Luego, hallar la media, mediana, el valor
#maximo y el valor minimo. Graficar los resultados en un grafico de barra con su respectiva leyenda.
# arr = np.random.randint(10,30,size=20)
# media = st.mean(arr)
# mediana = st.median(arr)
# maximo = np.max(arr)
# minimo = np.min(arr)

# x = np.array(["Media","Mediana","Maximo","Minimo"])
# y = np.array([media,mediana,maximo,minimo])

# plt.bar(x,y)
# plt.title("Grafico de barras de valores estadisticos")
# plt.show()




#----Ejercicio 3----#
#Crear un arreglo con 20 numeros aleatorios entre 1 y 90. Luego, imprimir todos aquellos numeros 
#impares que son mayores a 40
# array = np.random.randint(1,90,size=20)
# for i in array:
#     if((i%2)!=0 and i>40):
#         print(i)




#----Ejercicio 4----#
#Crear un arreglo con 10000 valores aleatorios entre 1 y 1000. Luego, halle su mediana haciendo uso de
#métodos tradicionales y luego halle su mediana haciendo uso del modulo statistics. Halle el tiempo
#de ejecucion para cada caso y grafiquelo en barras.

arr = np.random.randint(1,1000,size=10000)

#Mediana tradicional
start1 = time.perf_counter()
if (len(arr)%2 == 0):
    lista_ordenada = np.sort(arr)
    indice1 = int(len(lista_ordenada)/2)
    indice2 = int(len(lista_ordenada)/2) - 1
    mediana = (lista_ordenada[indice1] + lista_ordenada[indice2])/2
else:
    lista_ordenada = np.sort(arr)
    indice = int(len(lista_ordenada)/2)
    mediana = lista_ordenada[indice]
end1 = time.perf_counter()
time1 = end1 - start1

#Mediana con Statistics
start2 = time.perf_counter()
mediana_st = st.median(arr)
end2 = time.perf_counter()
time2 = end2 - start2

x = ["Tiempo Mediana 1","Tiempo Mediana 2"]
y = [time1,time2]
plt.bar(x,y)
plt.show()











# arr = np.ones(10)
# print(arr)
###############################################################
# arr = np.random.randint(1,90,size=20)
# print(arr)
# for i in range(len(arr)):
#     if (arr[i] > 40 and arr[i]%2 != 0):
#         print(arr[i])
################################################################
# arr = np.random.randint(10,30,size=20)
# media = st.mean(arr)
# mediana = st.median(arr)
# maximo = np.max(arr)
# minimo = np.min(arr)

# x = np.array(["Media","Mediana","Maximo","Minimo"])
# y = np.array([media,mediana,maximo,minimo])

# plt.bar(x,y)
# plt.title("Grafico de barras de valores estadisticos")
# plt.show()
###############################################################
# arr = np.random.randint(1,100000,size=100)

# #Mediana manual
# start1 = time.perf_counter()
# if (len(arr)%2 == 0):
#     lista_ordenada = np.sort(arr)
#     indice1 = int(len(arr)/2)
#     indice2 = int(len(arr)/2) - 1
#     mediana = (lista_ordenada[indice1] + lista_ordenada[indice2])/2
# else:
#     lista_ordenada = arr.sort()
#     indice = int(len(arr)/2)
#     mediana = lista_ordenada[indice]
# end1 = time.perf_counter()
# time1 = end1 - start1

# #Mediana con Statistics
# start2 = time.perf_counter()
# mediana_st = st.median(arr)
# end2 = time.perf_counter()
# time2 = end2 - start2

# x = ["Tiempo Mediana 1","Tiempo Mediana 2"]
# y = [time1,time2]
# plt.bar(x,y)
# plt.show()