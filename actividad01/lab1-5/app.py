def encontrar_indice(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

lista_prueba = [1, 2, 3, 4, 5, 6]
elemento_a_buscar = 4

indice = encontrar_indice(lista_prueba, elemento_a_buscar)
print(lista_prueba)
print(f'El índice del elemento {elemento_a_buscar} es: {indice}')