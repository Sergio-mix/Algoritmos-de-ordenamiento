import random
import time
from src.main.python.co.edu.unbosque.model.AgoritmoDeOrdenamiento import AgoritmoDeOrdenamiento

"""
Clase Controller, se encarga de mantener el control del
programa.
"""
class Controller:

    """Método para generar n numeros aleatorios entre un rango definido e ingresarlos a una lista"""
    def numerosAleatorios(self, n, minimo, maximo):
        """
        :param n: cantidad de numeros ingresada para generear randoms
        :param minimo: valor minimo para generar random
        :param maximo: valor maximo para generar random
        :return:
        """
        x = 0
        lista = []
        while x < n:
            numeroAleatorio = random.randint(minimo, maximo)
            lista.append(numeroAleatorio)
            x += 1
        return lista
    """Es un metodo para generar una lista ya ordenada """
    def listaOrdenada(self, n):
        """
        :param n: valor para generar lista
        :return:
        """
        x = 1
        lista = []
        while x <= n:
            lista.append(x)
            x += 1
        return lista
    """Es un metodo para generar una lista invertida"""
    def listaInvertida(self, n):
        """
        :param n: valor para generar lista
        :return:
        """
        x = n
        i = 1
        lista = []
        while x >= i:
            lista.append(x)
            x -= 1
        return lista

    """Método para calcular el tiempo de ejecución del algoritmo burbuja"""
    def burbujaTime(self, lista):
        """
        :param lista: Lista ingresada
        """
        inicio = time.time()
        AgoritmoDeOrdenamiento().burbuja(lista)
        fin = time.time()
        print("El tiempo de ejecución fue de:", "{:.4}".format(fin - inicio), "Segundos")

    """Método para calcular el tiempo de ejecución del algoritmo seleccion"""
    def seleccionTime(self, lista):
        """
        :param lista: Lista ingresada
        """
        inicio = time.time()
        AgoritmoDeOrdenamiento().seleccion(lista)
        fin = time.time()
        print("El tiempo de ejecución fue de:", "{:.4}".format(fin - inicio), "Segundos")

    """Método para calcular el tiempo de ejecución del algoritmo radixSort"""
    def radixSortTime(self, lista):
        """
        :param lista: Lista ingresada
        """
        inicio = time.time()
        AgoritmoDeOrdenamiento().radixSort(lista)
        fin = time.time()
        print("El tiempo de ejecución fue de:", "{:.4}".format(fin - inicio), "Segundos")

    """Método para calcular el tiempo de ejecución del algoritmo quickSort"""
    def quickSortTime(self, lista):
        """
        :param lista: Lista ingresada
        """
        inicio = time.time()
        AgoritmoDeOrdenamiento().quickSort(lista)
        fin = time.time()
        print("El tiempo de ejecución fue de:", "{:.4}".format(fin - inicio), "Segundos")

    """Método para calcular el tiempo de ejecución del algoritmo mergeSort"""
    def mergeSortTime(self, lista):
        inicio = time.time()
        AgoritmoDeOrdenamiento().mergeSort(lista)
        fin = time.time()
        print("El tiempo de ejecución fue de:", "{:.4}".format(fin - inicio), "Segundos")
