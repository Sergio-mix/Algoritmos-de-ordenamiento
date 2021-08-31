from src.main.python.co.edu.unbosque.controller.Controller import numerosAleatorios, burbujaTime, seleccionTime, \
    radixSortTime, quickSortTime, mergeSortTime, listaOrdenada, listaInvertida


def crearArray(n):
    lista = []

    menu = """Elija como desea ingresar los valores del arreglo
    [1] Manual
    [2] Aleatoria
    > Opcion: """

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
        lista = numerosAleatorios(n, 0, 9)

    return lista


print("⋆﹥━━━━━━━━━━━━━━━━━━━━━﹤⋆ MENU ⋆﹥━━━━━━━━━━━━━━━━━━━━━﹤⋆")

menu = """Ingrese el tamaño del vector
    > Cantidad de Numeros: """
opcion = int(input(menu))

listaOrdenada = listaOrdenada(opcion)
listaInvertida = listaInvertida(opcion)

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
array = crearArray(opcion)
print(""" """)
print("Ordenando lista...")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("Algoritmo burbuja")
burbujaTime(array)
print(""" """)
print("lista Ordenada")
burbujaTime(listaOrdenada)
print(""" """)
print("lista Invertida")
burbujaTime(listaInvertida)
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("Algoritmo seleccion")
seleccionTime(array)
print(""" """)
print("lista Ordenada")
seleccionTime(listaOrdenada)
print(""" """)
print("lista Invertida")
seleccionTime(listaInvertida)
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("Algoritmo radixSort")
radixSortTime(array)
print(""" """)
print("lista Ordenada")
radixSortTime(listaOrdenada)
print(""" """)
print("lista Invertida")
radixSortTime(listaInvertida)
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("Algoritmo quickSort")
quickSortTime(array)
print(""" """)
print("lista Ordenada")
quickSortTime(listaOrdenada)
print(""" """)
print("lista Invertida")
quickSortTime(listaInvertida)
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("Algoritmo mergeSort")
mergeSortTime(array)
print(""" """)
print("lista Ordenada")
mergeSortTime(listaOrdenada)
print(""" """)
print("lista Invertida")
mergeSortTime(listaInvertida)
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
