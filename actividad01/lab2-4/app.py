numeros = [34, 78, 56, 12, 89, 23, 45, 67]

elemento_a_buscar = 12

posicion_elemento = -1

for i, numero in enumerate(numeros):
    if numero == elemento_a_buscar:
        posicion_elemento = i
        break 

if posicion_elemento != -1:
    resultado = f"El elemento {elemento_a_buscar} se encuentra en la posición {posicion_elemento}."
else:
    resultado = f"El elemento {elemento_a_buscar} no se encuentra en el arreglo."

print(f"Arreglo: {numeros}")
print(resultado)