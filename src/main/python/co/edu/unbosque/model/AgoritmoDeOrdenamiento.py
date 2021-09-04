class AgoritmoDeOrdenamiento:
    """
    Algoritmo de ordenamiento burbuja,
    """
    def burbuja(self, lista):
        """
        :param lista: lista introducida
        :return: lista ordenada
        """
        tamanio = len(lista)
        """ Un ciclo que pasa por el tamaño de la lista"""
        for numPasada in range(tamanio - 1, 0, -1):
            """ Ciclo que verifica y ordena"""
            for i in range(numPasada):
                if lista[i] > lista[i + 1]:
                    temp = lista[i]
                    lista[i] = lista[i + 1]
                    lista[i + 1] = temp
        return lista

    """Algoritmo de ordenamiento por seleccion"""
    def seleccion(self, lista):
        """
        :param lista: lista introducida
        :return: lista ordenada
        """
        tamanio = len(lista)
        for i in range(tamanio - 1):
            for j in range(i + 1, tamanio):
                if lista[i] > lista[j]:
                    lista[i], lista[j] = lista[j], lista[i]
        return lista

    """Algoritmo de ordenamiento Radix"""
    def radixSort(self, lista):
        """
        :param lista: lista introducida
        :return: lista ordenada
        """
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

    """Algoritmo de ordenamiento QuickSort"""
    def quickSort(self, lista):
        """
        :param lista: lista introducida
        :return: lista ordenada
        """
        if (len(lista) <= 1):
            return lista

        pivot = lista[len(lista) // 2]

        lt = [i for i in lista if i < pivot]
        eq = [pivot] * lista.count(pivot)
        gt = [i for i in lista if i > pivot]
        lista = self.quickSort(lt) + eq + self.quickSort(gt)
        return lista

    """Algoritmo de ordenamiento MergeSort"""
    def mergeSort(self, lista):
        """
        :param lista: lista introducida
        :return: lista ordenada
        """
        if len(lista) > 1:
            medio = len(lista) // 2
            izquierda = lista[:medio]
            derecha = lista[medio:]
            self.mergeSort(izquierda)
            self.mergeSort(derecha)
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
