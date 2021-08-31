import random
import time


# Método para generar n numeros aleatorios entre un rango definido
def numerosAleatorios(n, minimo, maximo):
    x = 0
    lista = []
    while x < n:
        numeroAleatorio = random.randint(minimo, maximo)
        lista.append(numeroAleatorio)
        x += 1
    return lista

# Método para calcular el tiempo de ejecución del algoritmo
def tiempoDeEjecucion(function):
    inicio = time.perf_counter()
    function
    final = time.perf_counter()
    return "El tiempo de ejecución fue de:", "{:.3}".format((final - inicio) * 1000), "ms"