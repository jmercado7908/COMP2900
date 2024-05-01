import random

def busqueda_binaria_insertar(lista, valor_objetivo):
    bajo = 0
    alto = len(lista) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        valor_medio = lista[medio]
        
        if valor_medio == valor_objetivo:
            return medio
        elif valor_medio < valor_objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    
    return bajo  # Devuelve la posición donde debería insertarse valor_objetivo

def generar_lista_ordenada(n, rango):
    lista = [random.randint(0, rango) for _ in range(n)]
    lista.sort()
    return lista

def main():
    # Generar lista aleatoria de 10 números en el rango de 0 a 100
    lista_aleatoria = generar_lista_ordenada(10, 100)
    print("Lista ordenada generada:", lista_aleatoria)
    
    # Solicitar al usuario que ingrese un número para buscar en la lista
    try:
        numero_usuario = int(input("Ingresa un número para buscar en la lista: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return
    
    # Buscar el número en la lista usando búsqueda binaria
    resultado = busqueda_binaria_insertar(lista_aleatoria, numero_usuario)
    
    # Determinar si el número estaba en la lista o no, y mostrar la información relevante
    if 0 <= resultado < len(lista_aleatoria) and lista_aleatoria[resultado] == numero_usuario:
        print(f"El número {numero_usuario} está en la lista en la posición {resultado}.")
    else:
        print(f"El número {numero_usuario} no está en la lista. Debería insertarse en la posición {resultado} para mantener la lista ordenada.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
    