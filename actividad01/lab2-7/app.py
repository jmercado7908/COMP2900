numeros = [15, 25, 35, 45, 55]

suma_total = 0

for numero in numeros:
    suma_total += numero

promedio = suma_total / len(numeros)

print(f"Arreglo: {numeros}")
print(f"El promedio del arreglo es de: {promedio}")