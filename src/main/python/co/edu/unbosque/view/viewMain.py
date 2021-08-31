from src.main.python.co.edu.unbosque.controller.Controller import numerosAleatorios, tiempoDeEjecucion
from src.main.python.co.edu.unbosque.model.AgoritmoDeOrdenamiento import mergeSort, burbuja, seleccion, radixSort, \
    quickSort


def crearArray(n):
    lista = []

    menu = """Elija como desea ingresar los valores del arreglo
    [1] Manual
    [2] Aleatoria
    >Opcion: """

    opcion = int(input(menu))

    while not ((opcion > 0) and (opcion <= 2)):
        print("<< Ingrese una opcion valida >>")
        opcion = int(input(menu))

    if opcion == 1:
        x = 1
        while x <= n:
            valor = int(input(f"Ingrese el {x} valor: "))
            lista.append(valor)
            x += 1
    elif opcion == 2:
        lista = numerosAleatorios(n, 0, 30)

    return lista


def algoritmos(lista):
    print("(Algoritmo burbuja)", tiempoDeEjecucion(burbuja(lista)))
    print("(Algoritmo seleccion)", tiempoDeEjecucion(seleccion(lista)))
    print("(Algoritmo radixSort)", tiempoDeEjecucion(radixSort(lista)))
    print("(Algoritmo quickSort)", tiempoDeEjecucion(quickSort(lista)))
    print("(Algoritmo mergeSort)", tiempoDeEjecucion(mergeSort(lista)))


menu = """Ingrese el tamaño del vector
    > Cantidad de Numeros: """

opcion = int(input(menu))

array = crearArray(opcion)
algoritmos(array)
