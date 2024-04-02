def coeficiente_binomial(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return coeficiente_binomial(n - 1, k - 1) + coeficiente_binomial(n - 1, k)

# Pruebas de la función con diferentes valores de n y k
n1, k1 = 5, 3
resultado1 = coeficiente_binomial(n1, k1)
print(f"{n1}C{k1} = {resultado1}")

n2, k2 = 6, 2
resultado2 = coeficiente_binomial(n2, k2)
print(f"{n2}C{k2} = {resultado2}")

n3, k3 = 10, 4
resultado3 = coeficiente_binomial(n3, k3)
print(f"{n3}C{k3} = {resultado3}")