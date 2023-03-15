import os
import pandas as pan
import numpy as np
import matplotlib.pyplot as plt

datos = pan.read_csv("iris.csv",delimiter=";",decimal=".")

x=datos.iloc[:,0:4] #s.largo
x2=datos.iloc[:,2:3] #p.largo

array=[]
for j in range(150):
    array.append([0]*2) #dimensionar matriz

for j in range(150):
    for o in range(2):
        array[j][o]=x["s.largo"][j] #ingresar datos s.largo
    array[j][o]=x2["p.largo"][j] #ingresar datos p.largo


x_datos=np.array(array) #arreglo numpy con datos de s.largo y p.largo
y=datos.iloc[:,4:5]

    
vec = [] 
aux=1
for i in range(150):
    vec.append(aux)
    if i==101:
        aux-=1

clases = np.array(vec)

#funcion de activacion
def activacion(pesos,x,b):
    z=pesos * x
    if z.sum() + b > 0:
        return 1
    else:
        return 0

#fin funcion de activacion


print("****************************************Entranamiento del perceptron****************************************")
pesos = np.random.uniform(-1,1,size=2)
b = np.random.uniform(-1,1)
tasa_de_aprendizaje = 0.01
epocas = 1500
for epoca in range(epocas):
    error_total = 0
    for i in range (len(x_datos)):
        prediccion = activacion(pesos, x_datos[i],b)
        error = clases[i] - prediccion 
        error_total += error**2
        
        pesos[0] += tasa_de_aprendizaje * x_datos[i][0]*error
        pesos[1] += tasa_de_aprendizaje * x_datos[i][1]*error
        b += tasa_de_aprendizaje * error
    print(error_total, end=" ")

print ("\n\n-------Validacion para ver si son Setosa o Versicolor: --------") 
print ("Resultados: ",activacion(pesos,[6.0,4.0],b))

print ("\n\n-------Validacion para ver si es Virginica: --------")
print ("Resultados de la prueba: ",activacion(pesos,[6.9,5.1],b))