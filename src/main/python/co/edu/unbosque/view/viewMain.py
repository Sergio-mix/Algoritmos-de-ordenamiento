from src.main.python.co.edu.unbosque.controller.Controller import numerosAleatorios, burbujaTime, seleccionTime, \
    radixSortTime, quickSortTime, mergeSortTime


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

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
array = crearArray(opcion)
print(""" """)
print("Ordenando lista...")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
burbujaTime(array)
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
seleccionTime(array)
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
radixSortTime(array)
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
quickSortTime(array)
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
mergeSortTime(array)
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
