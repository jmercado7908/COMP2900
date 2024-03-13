numeros = [11, 22, 33, 44, 55, 66, 77, 88, 99]

elemento_a_eliminar = 44

numeros_sin_elemento = []

for numero in numeros:
    if numero != elemento_a_eliminar:
        numeros_sin_elemento.append(numero)

print(f"Arreglo: {numeros}")
print(f"Elemento a eliminar: {elemento_a_eliminar}")
print(f"Arreglo con el elemento eliminado: {numeros_sin_elemento}")