def promedio(lista_numeros):
    suma = 0
    array_length = 0
    for valor in lista_numeros:
        suma = suma + valor
        array_length = array_length + 1
    return (suma / array_length)

lista_numeros = [5, 10, 25, 40, 60, 35]
print (lista_numeros)
print(f'El valor promedio de la lista es: {round(promedio(lista_numeros), 2)}')