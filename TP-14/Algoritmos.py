import time
import random

def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def ordenamiento_seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def ordenamiento_insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

def ordenamiento_rapido(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return ordenamiento_rapido(izquierda) + medio + ordenamiento_rapido(derecha)

def ordenamiento_fusion(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = ordenamiento_fusion(lista[:medio])
    derecha = ordenamiento_fusion(lista[medio:])
    return fusionar(izquierda, derecha)

def fusionar(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

def generar_lista(tamano):
    return [random.randint(1, 1000) for _ in range(tamano)]

tamanos = [100, 200, 500, 1000, 2000, 5000]
tiempos_burbuja = []
tiempos_seleccion = []
tiempos_insercion = []
tiempos_rapido = []
tiempos_fusion = []

for tamano in tamanos:
    lista = generar_lista(tamano)
    
    inicio = time.time()
    ordenamiento_burbuja(lista.copy())
    tiempos_burbuja.append(time.time() - inicio)
    
    inicio = time.time()
    ordenamiento_seleccion(lista.copy())
    tiempos_seleccion.append(time.time() - inicio)

    inicio = time.time()
    ordenamiento_insercion(lista.copy())
    tiempos_insercion.append(time.time() - inicio)

    inicio = time.time()
    ordenamiento_rapido(lista.copy())
    tiempos_rapido.append(time.time() - inicio)

    inicio = time.time()
    ordenamiento_fusion(lista.copy())
    tiempos_fusion.append(time.time() - inicio)


print("Tiempos de ejecución (en segundos):")
print("Tamaño\tBurbuja\tSelección\tInserción\tRápido\tFusión")
for i, tamano in enumerate(tamanos):
    print(f"{tamano}\t{tiempos_burbuja[i]:.6f}\t{tiempos_seleccion[i]:.6f}\t{tiempos_insercion[i]:.6f}\t{tiempos_rapido[i]:.6f}\t{tiempos_fusion[i]:.6f}")
