# coding=utf-8

def minutos_de_la_semana(semanas):
    """
    >>> minutos_de_la_semana(1)
    10080

    >>> minutos_de_la_semana(2)
    20160
    """
    return semanas * 7 * 24 * 60
    pass


def obtener_residuo_sin_mod(numerador, divisor):
    """
    >>> obtener_residuo_sin_mod(28,7)
    0
    >>> obtener_residuo_sin_mod(30,7)
    2
    """
    return numerador - int(numerador / divisor) * divisor


def divisible_entre_3(numero):
    """
    >>> divisible_entre_3(9)
    True
    >>> divisible_entre_3(7)
    False
    """
    return obtener_residuo_sin_mod(numero, 3) == 0


def cuadrado_de_un_conjunto(numeros):
    """
    Given a set of numbers return a set of the numbers squared
    >>> cuadrado_de_un_conjunto({1,2,3,4,5,5,5})
    {16, 1, 4, 9, 25}
    """
    return set(numero ** 2 for numero in numeros)


def potencia_de_2_en_conjunto(numeros):
    """
    Given a set of numbers return the powers of two of those numbers
    >>> potencia_de_2_en_conjunto({0,1,2,3,4})
    {8, 1, 2, 4, 16}
    """
    return set(2 ** pot for pot in numeros)


def producto_de_dos_conjuntos(xs, ys):
    """
    >>> producto_de_dos_conjuntos({1,2,3},{3,4,5})
    {3, 4, 5, 6, 8, 9, 10, 12, 15}
    """
    nums = set()
    for num1 in xs:
        for num2 in ys:
            nums.add(num1 * num2)
    return nums



def producto_de_conjuntos_sin_duplicados(xs, ys):
    """
    >>> producto_de_conjuntos_sin_duplicados({1,2,3},{3,4,5})
    {3, 4, 5, 6, 8, 9, 10, 12, 15}
    """
    return set(producto_de_dos_conjuntos(xs, ys))



def interseccion(Ss, Ts):
    """
    >>> interseccion({1, 2, 3, 4},{3, 4, 5, 6})
    {3, 4}
    """
    inter = set()
    for num1 in Ss:
        for num2 in Ts:
            if num1 == num2:
                inter.add(num1)
                break
    return inter


def promedio_de_lista(lista):
    """
    >>> promedio_de_lista([20, 10, 15, 75])
    30
    """
    suma = 0
    for numero in lista:
        suma += numero
    return int(suma / len(lista))


def producto_cartesiano(Xs, Ys):
    """
    >>> producto_cartesiano(['A','B','C'],[1,2,3])
    [['A', 1], ['A', 2], ['A', 3], ['B', 1], ['B', 2], ['B', 3], ['C', 1], ['C', 2], ['C', 3]]
    """
    producto = []
    for x in Xs:

        for y in Ys:
            producto.append([x, y])
    return producto
