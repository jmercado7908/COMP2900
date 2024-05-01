import random
import time

def busqueda_secuencial(lista, valor_objetivo):
    for i, valor in enumerate(lista):
        if valor == valor_objetivo:
            return i
    return -1

def busqueda_binaria(lista, valor_objetivo):
    bajo = 0
    alto = len(lista) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio] == valor_objetivo:
            return medio
        elif lista[medio] < valor_objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    return -1

def generar_lista_ordenada(tamano):
    lista = [random.randint(0, 1000000) for _ in range(tamano)]
    lista.sort()
    return lista

def medir_tiempo_busqueda(lista, valor_objetivo, funcion_busqueda):
    inicio = time.time()
    posicion = funcion_busqueda(lista, valor_objetivo)
    tiempo_tomado = time.time() - inicio
    return tiempo_tomado, posicion

def main():
    tamanos = [1000, 50000, 100000]
    listas = {tamano: generar_lista_ordenada(tamano) for tamano in tamanos}
    valor_objetivo = 500000  # Un valor objetivo común para todas las búsquedas

    for tamano, lista in listas.items():
        tiempo_secuencial, pos_secuencial = medir_tiempo_busqueda(lista, valor_objetivo, busqueda_secuencial)
        tiempo_binario, pos_binario = medir_tiempo_busqueda(lista, valor_objetivo, busqueda_binaria)
        
        print(f"Lista de tamaño {tamano}:")
        print(f"Tiempo búsqueda secuencial: {tiempo_secuencial:.6f} segundos. Posición: {pos_secuencial}")
        print(f"Tiempo búsqueda binaria: {tiempo_binario:.6f} segundos. Posición: {pos_binario}")
        print("-----")

if __name__ == "__main__":
    main()
    