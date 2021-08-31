import random
import time

from src.model.agoritmoDeOrdenamiento import AgoritmoDeOrdenamiento


class Controller:
    # Método para generar n numeros aleatorios entre un rango definido
    def numerosAleatorios(self, n, minimo, maximo):
        x = 0
        lista = []
        while x < n:
            numeroAleatorio = random.randint(minimo, maximo)
            lista.append(numeroAleatorio)
            x += 1
        return lista

    def listaOrdenada(self, n):
        x = 1
        lista = []
        while x <= n:
            lista.append(x)
            x += 1
        return lista

    def listaInvertida(self, n):
        x = n
        i = 1
        lista = []
        while x >= i:
            lista.append(x)
            x -= 1
        return lista

    # Método para calcular el tiempo de ejecución del algoritmo burbuja
    def burbujaTime(self, lista):
        inicio = time.time()
        AgoritmoDeOrdenamiento().burbuja(lista)
        fin = time.time()
        print("El tiempo de ejecución fue de:", "{:.4}".format(fin - inicio), "Segundos")

    # Método para calcular el tiempo de ejecución del algoritmo seleccion
    def seleccionTime(self, lista):
        inicio = time.time()
        AgoritmoDeOrdenamiento().seleccion(lista)
        fin = time.time()
        print("El tiempo de ejecución fue de:", "{:.4}".format(fin - inicio), "Segundos")

    # Método para calcular el tiempo de ejecución del algoritmo radixSort
    def radixSortTime(self, lista):
        inicio = time.time()
        AgoritmoDeOrdenamiento().radixSort(lista)
        fin = time.time()
        print("El tiempo de ejecución fue de:", "{:.4}".format(fin - inicio), "Segundos")

    # Método para calcular el tiempo de ejecución del algoritmo quickSort
    def quickSortTime(self, lista):
        inicio = time.time()
        AgoritmoDeOrdenamiento().quickSort(lista)
        fin = time.time()
        print("El tiempo de ejecución fue de:", "{:.4}".format(fin - inicio), "Segundos")

    # Método para calcular el tiempo de ejecución del algoritmo mergeSort
    def mergeSortTime(self, lista):
        inicio = time.time()
        AgoritmoDeOrdenamiento().mergeSort(lista)
        fin = time.time()
        print("El tiempo de ejecución fue de:", "{:.4}".format(fin - inicio), "Segundos")
