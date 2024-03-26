import timeit
import random

# Encontrar el número más grande en una lista de números.

# Enfoque 1: Utilizando la función max() de Python para encontrar el 
# número más grande en una lista.
def max_lista(lista):
    return max(lista)

# Enfoque 2: Recorriendo la lista y comparando cada número con un valor 
# de referencia para encontrar el número más grande
def max_iterativo(lista):
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo

# Generación de datos de prueba
random.seed(0)  # Para resultados reproducibles
lista = [random.randint(0, 10000) for _ in range(1000)]

# Ejecución de timeit para ambos códigos
time_max = timeit.timeit(lambda: max_lista(lista), number=10000)
time_iterativo = timeit.timeit(lambda: max_iterativo(lista), number=10000)

# Presentación de resultados
print(f"Tiempo total usando la funcion max(): {time_max:.7f} segundos para 10000 ejecuciones.")
print(f"Tiempo total recorriendo la lista y comparando cada numero: {time_iterativo:.7f} segundos para 10000 ejecuciones.")