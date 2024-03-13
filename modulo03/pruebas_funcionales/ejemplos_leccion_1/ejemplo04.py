import math
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

# Prueba
assert calcular_area_circulo(1) == math.pi, "El área calculada NO es correcta."