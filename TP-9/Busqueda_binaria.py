def busqueda_lineal(lista, objetivo):
    for i  in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

numeros = [2, 23, 7, 9]
objetivo = 4
resultado = busqueda_lineal(numeros, objetivo)
print(f"El numero {objetivo} se encuentra en el indice = {resultado}")