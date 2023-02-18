import numpy as np

#~~~~~~~~~~ Creacion de matrices ~~~~~~~~~~#
mat = [[8, 14, -6], [12, 7, 4], [-11, 3, 21]]
#print(mat)

mat_to_np = np.array(mat)
#print(mat_to_np)

mat_np_random = np.random.randint(-20,20,size=(4,5))
#print(mat_np_random)

#~~~~~~~~~~ Manejo y operaciones con matrices ~~~~~~~~~~#
row = mat_to_np[0]
#print(row)

element = mat_to_np[0][1]
#print(element)

mat_a = np.random.randint(1,10,size=(2,2))
mat_b = np.random.randint(1,10,size=(2,2))
print("Matriz a: \n",mat_a)
print("Matriz b: \n",mat_b)

#---Suma
mat_suma = mat_a + mat_b

#---Resta
mat_resta = mat_a - mat_b

#---Multiplicacion
mat_mul = np.dot(mat_a,mat_b)

mat_mul_for = np.zeros((2,2))
for i in range(len(mat_a)):
    for j in range(len(mat_b[0])):
        for k in range(len(mat_a[0])):
            mat_mul_for[i][j] += mat_a[i][k] * mat_b[k][j]
# print("Multiplicacion con funcion dot: \n",mat_mul)
# print("Multiplicacion empleando bucles for: \n", mat_mul_for)

        