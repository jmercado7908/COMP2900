def invertir_cadena(cadena):
    if len(cadena) == 0:
        return ""
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])

# Pruebas de la función con diferentes cadenas
cadena1 = "Hola!"
resultado1 = invertir_cadena(cadena1)
print(f"Inverso de '{cadena1}': {resultado1}")

cadena2 = "Johnny"
resultado2 = invertir_cadena(cadena2)
print(f"Inverso de '{cadena2}': {resultado2}")

cadena3 = "Estructura de Datos"
resultado3 = invertir_cadena(cadena3)
print(f"Inverso de '{cadena3}': {resultado3}")