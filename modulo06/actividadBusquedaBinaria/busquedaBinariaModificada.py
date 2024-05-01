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
