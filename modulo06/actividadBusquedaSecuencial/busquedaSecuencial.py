def busqueda_secuencial(lista, objetivo):
    for index, value in enumerate(lista):
        if value == objetivo:
            return index
    return -1

# Ejemplo de uso de la función
lista = [5, 3, 9, 2, 8, 1]
objetivo = 6

index = busqueda_secuencial(lista, objetivo)
if index != -1:
    print(f"El valor {objetivo} se encontró en la posición {index}.")
else:
    print(f"El valor {objetivo} no se encontró en la lista.")