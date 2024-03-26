import timeit
import random

# Funciones para hacer una búsqueda en una lista de valores no ordenados.

# Generación de datos de prueba
random.seed(0)  # Para resultados reproducibles
numbers = [random.randint(0, 10000) for _ in range(1000)]
number_to_find = numbers[-1]

# Enfoque 1: usando un ciclo for
def search_for(number, numbers): 
    for i in range(len(numbers)):
        if numbers[i] == number:
            return i
    return -1 

# Enfoque 2: usando la función index()
def search_index(number, numbers):
    try:
        return numbers.index(number) 
    except ValueError:
        return -1

# Ejecución de timeit para ambos códigos
time_for = timeit.timeit(lambda: search_for(number_to_find, numbers), number=10000)
time_index = timeit.timeit(lambda: search_index(number_to_find, numbers), number=10000)

# Presentación de resultados
print(f"Tiempo total usando ciclo for: {time_for:.7f} segundos para 10000 ejecuciones.")
print(f"Tiempo total usando la función index(): {time_index:.7f} segundos para 10000 ejecuciones.")