def mayor(lista):
    valor_mayor = lista[0]
    for n in lista:
        if (n > valor_mayor):
            valor_mayor = n
    return valor_mayor

lista = [20, 22, 13, 10, 45, 33]
print(lista)
print(f'El valor mayor de la lista es: {mayor(lista)}')