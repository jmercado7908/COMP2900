arreglo = [3, 6, 9, 12, 15]

print(f"Arreglo: {arreglo}")

ultimo_elemento = arreglo[-1]

for i in range(len(arreglo) - 1, 0, -1):
    arreglo[i] = arreglo[i-1]

arreglo[0] = ultimo_elemento

print(f"Arreglo con los elementos rotados: {arreglo}")