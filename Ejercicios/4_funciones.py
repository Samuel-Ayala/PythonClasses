import sys

#----Ejercicio 1----#
#Escribir una funcion que reciba un numero como argumento de entrada y diga si el
#numero es primo o no
def esprimo(n):
    contador = 0
    for i in range(1,n+1):
        resto = n%i
        if (resto == 0):
            contador += 1  
    if (contador > 2):
        print("El numero no es primo")
    else:
        print("Elnumero es primo")



#----Ejercicio 2----#
#Escribir una función que reciba un número entero positivo y devuelva su factorial.
def factorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial * i
    return factorial
    

if __name__ == "__main__":
    n = int(sys.argv[1])
    #esprimo(n)
    #fact = factorial(n)
    #print(fact)
