numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

arreglo_invertido = []

for i in range(len(numeros)-1, -1, -1):
    arreglo_invertido.append(numeros[i])

print(f"Arreglo: {numeros}")
print(f"Arreglo invertido: {arreglo_invertido}")