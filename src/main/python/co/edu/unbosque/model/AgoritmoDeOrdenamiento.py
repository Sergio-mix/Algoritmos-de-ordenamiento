# Algoritmo de ordenamiento burbuja
def burbuja(lista):
    size = len(lista)
    for numPasada in range(size - 1, 0, -1):
        for i in range(numPasada):
            if lista[i] > lista[i + 1]:
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp
    return lista


# Algoritmo de ordenamiento por seleccion
def seleccion(lista):
    size = len(lista)
    for i in range(size - 1):
        for j in range(i + 1, size):
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
        buckets = [list() for _ in range(RADIX)]
        for i in lista:
            tmp = i // placement
            buckets[tmp % RADIX].append(i)
            if maxLength and tmp > 0:
                maxLength = False

        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                lista[a] = i
                a += 1
        placement *= RADIX
    return lista


# Algoritmo de ordenamiento QuickSort
def quickSort(lista):
    izquierda = []
    centro = []
    derecha = []
    size = len(lista)
    if size > 1:
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
        mid = len(lista) // 2
        left = lista[:mid]
        right = lista[mid:]
        mergeSort(left)
        mergeSort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                lista[k] = left[i]
                i += 1
            else:
                lista[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            lista[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lista[k] = right[j]
            j += 1
            k += 1
    return lista
