from src.main.python.co.edu.unbosque.controller.Controller import Controller

"""
Clase View, contiene toda la parte visualizable
 por consola del programa
"""
class View:
    """Crea un array segun las opciones del usuario"""
    def crearArray(self, n):
        """
        :param n variable a recibir:
        :return : el array
        """
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
            lista = Controller().numerosAleatorios(n, 0, n)

        return lista
    """Metodo menu que abre el contenido del programa """
    def menu(self):
        """
        Contenido del programa
        """
        global listaOrdenada, listaInvertida
        print("⋆﹥━━━━━━━━━━━━━━━━━━━━━﹤⋆ MENU ⋆﹥━━━━━━━━━━━━━━━━━━━━━﹤⋆")

        menu = """Ingrese el tamaño del vector
            > Cantidad de Numeros: """
        opcion = int(input(menu))

        listaOrdenada = Controller().listaOrdenada(opcion)
        listaInvertida = Controller().listaInvertida(opcion)

        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        array = self.crearArray(opcion)
        print(""" """)
        print("Ordenando lista...")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Algoritmo burbuja")
        Controller().burbujaTime(array)
        print(""" """)
        print("lista Ordenada")
        Controller().burbujaTime(listaOrdenada)
        print(""" """)
        print("lista Invertida")
        Controller().burbujaTime(listaInvertida)
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Algoritmo seleccion")
        Controller().seleccionTime(array)
        print(""" """)
        print("lista Ordenada")
        Controller().seleccionTime(listaOrdenada)
        print(""" """)
        print("lista Invertida")
        Controller().seleccionTime(listaInvertida)
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Algoritmo radixSort")
        Controller().radixSortTime(array)
        print(""" """)
        print("lista Ordenada")
        Controller().radixSortTime(listaOrdenada)
        print(""" """)
        print("lista Invertida")
        Controller().radixSortTime(listaInvertida)
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Algoritmo quickSort")
        Controller().quickSortTime(array)
        print(""" """)
        print("lista Ordenada")
        Controller().quickSortTime(listaOrdenada)
        print(""" """)
        print("lista Invertida")
        Controller().quickSortTime(listaInvertida)
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("Algoritmo mergeSort")
        Controller().mergeSortTime(array)
        print(""" """)
        print("lista Ordenada")
        Controller().mergeSortTime(listaOrdenada)
        print(""" """)
        print("lista Invertida")
        Controller().mergeSortTime(listaInvertida)
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
