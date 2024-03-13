def contar_apariciones_letra(cadena, letra):
    contador = 0
    for caracter in cadena:
        if caracter == letra:
            contador += 1
    return contador

ejemplo_cadena = "Trabajo para el Negociado del Cuerpo de Bomberos de Puerto Rico"
letra_a_buscar = "e"
cantidad_apariciones = contar_apariciones_letra(ejemplo_cadena, letra_a_buscar)
print(f"{ejemplo_cadena}")
print(f"Buscando la cantidad de: {letra_a_buscar} en el mensaje")
print(f"La cantidad es de: {cantidad_apariciones}")