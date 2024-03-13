import math

from ejemplo01 import calcular_promedio
from ejemplo02 import clasificar_numero
from ejemplo03 import imprimir_numeros
from ejemplo04 import calcular_area_circulo
from ejemplo05 import buscar_elemento
  
# Prueba ejemplo 1
assert calcular_promedio(4, 6) == 5, "El promedio calculado no es correcto."

# Prueba ejemplo 02
assert clasificar_numero(5) == "Positivo", "La clasificación NO es correcta."
assert clasificar_numero(-3) == "Negativo", "El valor NO es negativo."
assert clasificar_numero(0) == "Cero", "La clasificación no es correcta."

#Prueba ejemplo 03
assert imprimir_numeros() == 10, "El ciclo NO corrió correctamente"

#Prueba ejemplo 04
assert calcular_area_circulo(1) == math.pi, "El área calculada NO es correcta."

#Prueba ejemplo 05
arreglo = [1, 2, 3, 4, 5]
assert buscar_elemento(arreglo, 3), "El elemento no fue encontrado cuando debería."