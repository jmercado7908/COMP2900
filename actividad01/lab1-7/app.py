def es_numero_entero(cadena):
    if not cadena:
        return False
    if cadena[0] == '-' and len(cadena) > 1:
        cadena = cadena[1:]  
    for caracter in cadena:
        if not caracter.isdigit():
            return False
    return True

cadena_a_validar = "2988"
resultado = es_numero_entero(cadena_a_validar)
print(f"¿'{cadena_a_validar}' es un número entero?: {resultado}")

cadena_a_validar = "298.56"
resultado = es_numero_entero(cadena_a_validar)
print(f"¿'{cadena_a_validar}' es un número entero?: {resultado}")