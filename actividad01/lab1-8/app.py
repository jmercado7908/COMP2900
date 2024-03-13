def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    return contador

ejemplo_cadena = "Mi nombre es Johnny Mercado y vivo en Camuy"
cantidad_vocales = contar_vocales(ejemplo_cadena)
print(ejemplo_cadena)
print(f"La cantidad de vocales en {ejemplo_cadena} es de: {cantidad_vocales}")