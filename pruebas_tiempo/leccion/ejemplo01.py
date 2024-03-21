import timeit

def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
        return resultado

def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n-1)
    
# Tiempo del enfoque iterativo
tiempo_iterativo = timeit.timeit('factorial_iterativo(10)', globals=globals(), number=1000)
# Tiempo del enfoque iterativo
tiempo_recursivo = timeit.timeit('factorial_recursivo(10)', globals=globals(), number=1000)
print(f"Tiempo Iterativo: {tiempo_iterativo} segundos")
print(f"Tiempo Recursivo: {tiempo_recursivo} segundos")