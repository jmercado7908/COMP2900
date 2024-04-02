def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

# Pruebas de la función con diferentes pares de números
num1 = 48
num2 = 18
resultado1 = mcd(num1, num2)
print(f"MCD({num1}, {num2}) = {resultado1}")

num3 = 60
num4 = 24
resultado2 = mcd(num3, num4)
print(f"MCD({num3}, {num4}) = {resultado2}")

num5 = 105
num6 = 140
resultado3 = mcd(num5, num6)
print(f"MCD({num5}, {num6}) = {resultado3}")