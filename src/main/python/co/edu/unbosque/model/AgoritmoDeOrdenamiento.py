# Algoritmo de ordenamiento burbuja
def burbuja(lista):
    size = len(lista)
    for numPasada in range(size - 1, 0, -1):
        for i in range(numPasada):
            if lista[i] > lista[i + 1]:
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp


# Algoritmo de ordenamiento por seleccion
def seleccion(lista):
    size = len(lista)
    for i in range(size - 1):
        for j in range(i + 1, size):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]


# Algoritmo de ordenamiento QuickSort
def sort(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        return sort(izquierda) + centro + sort(derecha)
    else:
        return lista
