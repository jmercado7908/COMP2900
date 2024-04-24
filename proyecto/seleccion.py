from timeit import timeit

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

for caso in range(1,4):
    archivo = 'promedio_caso'
    if (caso == 1):
        archivo = 'peor_caso'
    elif (caso == 2):
        archivo = 'mejor_caso'

    print('--------------------')
    print(f'** TIPO DE CASO {archivo}')

    for corridas in range(10000, 110000, 10000):
        lista = []
        f = open(f"{archivo}.dat", "r")
        for n in f:
            lista.append(n)
        f.close()

        del lista[corridas:] # 10000 elements (debe borrar 90000 elementos)

        print(f'Array: {len(lista)} elementos')
        print(f'  Organizando {corridas} datos ... Favor esperar ...')
        tiempo = timeit(lambda:selection_sort(lista),number=1)
        print(f'  Tiempo: {tiempo} segs')