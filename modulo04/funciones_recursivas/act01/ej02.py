def potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente == 1:
        return base
    else:
        return base * potencia(base, exponente - 1)

# Pruebas de la función con diferentes valores de base y exponente
base1 = 2
exponente1 = 5
resultado1 = potencia(base1, exponente1)
print(f"{base1}^{exponente1} = {resultado1}")

base2 = 3
exponente2 = 3
resultado2 = potencia(base2, exponente2)
print(f"{base2}^{exponente2} = {resultado2}")

base3 = 5
exponente3 = 0
resultado3 = potencia(base3, exponente3)
print(f"{base3}^{exponente3} = {resultado3}")