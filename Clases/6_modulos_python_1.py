import numpy
import statistics
import time
import matplotlib.pyplot as plt

#~Numpy
arr1 = numpy.zeros(5) 
arr2 = numpy.random.randint(2,10,size=10)

arr3 = [2,5,9,4,7,11]
arr3 = numpy.array(arr3)

arr4 = [1,3,5,2,4,3]
arr4 = numpy.array(arr4)

print(arr1)
print(arr2)
print(arr3+arr4)


#~Statistics
media = statistics.mean(arr4)
mediana = statistics.median(arr4)
moda = statistics.mode(arr4)
gmean = statistics.geometric_mean(arr4)
hmean = statistics.harmonic_mean(arr4)

print(media,mediana,moda)


#~Time
start = time.time()
time.sleep(1)
end = time.time()
time1 = end - start

start = time.perf_counter()
time.sleep(1)
end = time.perf_counter()
time2 = end-start

print(time1,time2)


#~Matplotlib
x = numpy.array([1,2,3,4,5])
y = numpy.array([10,20,50,10,35])
plt.plot(x,y,label='Grafico continuo')
plt.title("Grafico 1")
plt.legend()
plt.show()

plt.bar(x,y,label = "Grafico de barras")
plt.legend()
plt.title("Grafico 2")
plt.show()
