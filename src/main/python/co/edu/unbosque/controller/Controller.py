import random
import time
from src.main.python.co.edu.unbosque.model.AgoritmoDeOrdenamiento import mergeSort, burbuja, seleccion, radixSort, \
    quickSort


# Método para generar n numeros aleatorios entre un rango definido
def numerosAleatorios(n, minimo, maximo):
    x = 0
    lista = []
    while x < n:
        numeroAleatorio = random.randint(minimo, maximo)
        lista.append(numeroAleatorio)
        x += 1
    return lista


def listaOrdenada(n):
    x = 1
    lista = []
    while x <= n:
        lista.append(x)
        x += 1
    return lista


def listaInvertida(n):
    x = n
    i = 1
    lista = []
    while x >= i:
        lista.append(x)
        x -= 1
    return lista


# Método para calcular el tiempo de ejecución del algoritmo burbuja
def burbujaTime(lista):
    inicio = time.time()
    burbuja(lista)
    fin = time.time()
    print("El tiempo de ejecución fue de:", "{:.4}".format(fin - inicio), "Segundos")


# Método para calcular el tiempo de ejecución del algoritmo seleccion
def seleccionTime(lista):
    inicio = time.time()
    seleccion(lista)
    fin = time.time()
    print("El tiempo de ejecución fue de:", "{:.4}".format(fin - inicio), "Segundos")


# Método para calcular el tiempo de ejecución del algoritmo radixSort
def radixSortTime(lista):
    inicio = time.time()
    radixSort(lista)
    fin = time.time()
    print("El tiempo de ejecución fue de:", "{:.4}".format(fin - inicio), "Segundos")


# Método para calcular el tiempo de ejecución del algoritmo quickSort
def quickSortTime(lista):
    inicio = time.time()
    quickSort(lista)
    fin = time.time()
    print("El tiempo de ejecución fue de:", "{:.4}".format(fin - inicio), "Segundos")


# Método para calcular el tiempo de ejecución del algoritmo mergeSort
def mergeSortTime(lista):
    inicio = time.time()
    mergeSort(lista)
    fin = time.time()
    print("El tiempo de ejecución fue de:", "{:.4}".format(fin - inicio), "Segundos")
