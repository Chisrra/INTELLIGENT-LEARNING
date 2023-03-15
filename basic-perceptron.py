"""Programa de clasificacion con Perceptron.
    Utiliza una neurona para clasificar las personas que acreditan una tarjeta 
    en base a su edad y ahorro"""
import matplotlib.pyplot as pyplot #Graficador
import numpy #Arrays

def activacion(pesos: numpy.array, x: numpy.array, teta: float):
    """Funcio de activasion que hace la prediccion de la salida en base a los pesos multiplicados por los valores de x y la suma de teta

    Args:
        pesos (numpy.array): array que contiene los pesos 
        x (numpy.array): array que contienen los valores de entrada
        teta (float): Valor del umbral

    Returns:
        int: retorna 0 (apagado) o 1 (encendido) 
    """
    z = pesos * x
    if z.sum() + teta > 0:
        return 1
    else:
        return 0


if __name__ == "__main__": 
    #persona = [edad, ahorro]
    personas = numpy.array([[0.3, 0.4], [0.4, 0.3], [0.3, 0.2], [0.4, 0.1], [0.5, 0.4], [0.4, 0.8], [0.6, 0.8], [0.5, 0.6], [0.7, 0.6], [0.8, 0.5]])
    # print(personas)
    target = numpy.array([0,0,0,0,0,1,1,1,1,1])
    
    #Graficador
    """
    pyplot.figure(figsize=(7,7))
    pyplot.title("Tarjeta Platinum", fontsize = 20)
    pyplot.scatter(personas[target==0].T[0],
                   personas[target==0].T[1],
                   marker="x", s=180, color="red",
                   linewidths=5, label="Denegada")
    pyplot.scatter(personas[target==1].T[0],
                   personas[target==1].T[1],
                   marker="o", s=180, color="blue",
                   linewidths=5, label="Aprobada")
    """
    #Entrenamiento
    pesos = numpy.random.uniform(-1,1, size=2)
    teta = numpy.random.uniform(-1,1)
    tazaAprendizaje = 0.01
    iteraciones = 100

    for itr in range(iteraciones):
        errorT = 0
        for i in range(len(personas)):
            prediccion = calculoP(pesos, personas[i], teta)
            error = target[i] - prediccion
            errorT += error**2
            pesos[0] += tazaAprendizaje * personas[i][0] * error
            pesos[1] += tazaAprendizaje * personas[i][1] * error
            teta += tazaAprendizaje * error
            
        print(f"Error en iteracion {itr+1}: {errorT}")