numeros = [5, 3, 7, 3, 2, 3, 8, 3, 9]

elemento_a_contar = 3

cantidad_apariciones = 0

for numero in numeros:
    if numero == elemento_a_contar:
        cantidad_apariciones += 1

print(f"Arreglo: {numeros}")
print(f"Elemento a contar: {elemento_a_contar}")
print(f"Cantidad de veces en el arreglo: {cantidad_apariciones}")