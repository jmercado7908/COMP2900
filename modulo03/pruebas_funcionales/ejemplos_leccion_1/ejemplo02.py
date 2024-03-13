def clasificar_numero(num):
    if num > 0:
        return "Positivo"
    elif num < 0:
        return "Negativo"
    else:
        return "Cero"
# Prueba
assert clasificar_numero(5) == "Positivo", "El valor NO es positivo."
assert clasificar_numero(-3) == "Negativo", "El valor NO es negativo."
assert clasificar_numero(0) == "Cero", "La clasificación no escorrecta."