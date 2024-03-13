numeros = [34, 12, 5, 66, 2, 89, 45, 23]

print(f"Arreglo original: {numeros}")

for i in range(len(numeros)):
    for j in range(0, len(numeros) - i - 1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print(f"Arreglo ordenado: {numeros}")
