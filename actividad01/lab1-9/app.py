import random

def generar_numeros_aleatorios(cantidad, minimo, maximo):
    numeros_aleatorios = []
    for _ in range(cantidad):
        numero = random.randint(minimo, maximo)
        numeros_aleatorios.append(numero)
    return numeros_aleatorios

cantidad_numeros = 10
minimo = 1
maximo = 100
lista_aleatorios = generar_numeros_aleatorios(cantidad_numeros, minimo, maximo)
print(f"Cantidad de numeros son: {cantidad_numeros} con un mínimo de: {minimo} y un máximo de: {maximo}")
print(f"Los números aleatorios generados son: {lista_aleatorios}")