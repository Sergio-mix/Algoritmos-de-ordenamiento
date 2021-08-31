# Algoritmo de ordenamiento burbuja
def burbuja(lista):
    tamaño = len(lista)
    for numPasada in range(tamaño - 1, 0, -1):
        for i in range(numPasada):
            if lista[i] > lista[i + 1]:
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp
    return lista


# Algoritmo de ordenamiento por seleccion
def seleccion(lista):
    tamaño = len(lista)
    for i in range(tamaño - 1):
        for j in range(i + 1, tamaño):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


# Algoritmo de ordenamiento Radix
def radixSort(lista):
    RADIX = 10
    maxLength = False
    tmp, placement = -1, 1

    while not maxLength:
        maxLength = True
        cubos = [list() for _ in range(RADIX)]
        for i in lista:
            tmp = i // placement
            cubos[tmp % RADIX].append(i)
            if maxLength and tmp > 0:
                maxLength = False

        a = 0
        for b in range(RADIX):
            salto = cubos[b]
            for i in salto:
                lista[a] = i
                a += 1
        placement *= RADIX
    return lista


# Algoritmo de ordenamiento QuickSort
def quickSort(lista):
    izquierda = []
    centro = []
    derecha = []
    tamaño = len(lista)
    if tamaño > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        return quickSort(izquierda) + centro + quickSort(derecha)
    else:
        return lista


# Algoritmo de ordenamiento MergeSort
def mergeSort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        mergeSort(izquierda)
        mergeSort(derecha)
        i = 0
        j = 0
        k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] <= derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
    return lista
