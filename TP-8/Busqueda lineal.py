def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

numeros = [1, 2, 3, 4, 7, 9]
objetivo = 7
resultado = busqueda_binaria(numeros, objetivo)
print(f"El número {objetivo} se encuentra en el índice: {resultado}")






