from random import randint


def crearArray(n):
    array = [0] * n  # Ceacion del vector
    menu = """Elija como desea ingresar los valores del arreglo
    [1] Manual
    [2] Aleatoria
    >Opcion: """
    opcion = int(input(menu))
    while not ((opcion > 0) and (opcion <= 2)):
        print("<< Ingrese una opcion valida >>")
        opcion = int(input(menu))

    for i in range(0, len(array)):
        if opcion == 1:
            valor = int(input(f"Ingrese el {i + 1} valor: "))
        else:
            valor = randint(1, n)
            array[i] = valor
    return array


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
elif opcion == 2:
    array = crearArray(40000)
elif opcion == 3:
    array = crearArray(400000)
elif opcion == 4:
    array = crearArray(4000000)
elif opcion == 5:
    array = crearArray(40000000)
print(array)

