from timeit import timeit

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

for caso in range(1, 4):
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
    tiempo = timeit.timeit(lambda:bubble_sort(lista),number=1)
    print(f'  Tiempo: {tiempo} segs')