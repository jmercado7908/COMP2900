import timeit

# Suma de todos los números enteros de 1 a un número determinado n.

# Enfoque 1: usando un ciclo for para recorrer todos los números 
# de 1 a n y sumarlos
def suma_for(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma

# Enfoque 2: fórmula matemática para calcular la suma de 
# una serie aritmética
def suma_formula(n):
    return (n * (n+1)) // 2

# Valores de prueba
n = 10000  # Un valor grande para n

# Ejecución de timeit para ambos códigos
time_for = timeit.timeit(lambda: suma_for(n), number=10000)
time_formula = timeit.timeit(lambda: suma_formula(n), number=10000)

# Presentación de resultados
print(f"Tiempo total usando ciclo for: {time_for:.7f} segundos para 10000 ejecuciones.")
print(f"Tiempo total usando la fórmula matemática: {time_formula:.7f} segundos para 10000 ejecuciones.")