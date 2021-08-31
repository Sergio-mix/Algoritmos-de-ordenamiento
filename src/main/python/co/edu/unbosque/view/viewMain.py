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
    print(tiempoDeEjecucion(burbuja(lista)))
    print(tiempoDeEjecucion(seleccion(lista)))
    print(tiempoDeEjecucion(radixSort(lista)))
    print(tiempoDeEjecucion(quickSort(lista)))
    print(tiempoDeEjecucion(mergeSort(lista)))


menu = """Ingrese el tamaño del vector
    [1] 4000
    [2] 40000
    [3] 400000
    [4] 4000000
    [5] 40000000
    > Opcion: """

opcion = int(input(menu))

while not ((opcion > 0) and (opcion <= 5)):
    print("<< Ingrese una opcion valida >>")

    opcion = int(input(menu))

if opcion == 1:
    array = crearArray(4000)
    algoritmos(array)
elif opcion == 2:
    array = crearArray(40000)
    algoritmos(array)
elif opcion == 3:
    array = crearArray(400000)
    algoritmos(array)
elif opcion == 4:
    array = crearArray(4000000)
    algoritmos(array)
elif opcion == 5:
    array = crearArray(40000000)
    algoritmos(array)
