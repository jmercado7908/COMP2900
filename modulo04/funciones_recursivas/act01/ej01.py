def suma_naturales(n):
    if n == 0:
        return 0
    else:
        return n + suma_naturales(n-1)
    
# Pruebas con diferentes valores de n
prueba1 = suma_naturales(2)
print(f"Prueba #1 con valor de 2: {prueba1}")

prueba2 = suma_naturales(5)
print(f"Prueba #2 con valor de 5: {prueba2}")

prueba3 = suma_naturales(10)
print(f"Prueba #3 con valor de 10: {prueba3}")