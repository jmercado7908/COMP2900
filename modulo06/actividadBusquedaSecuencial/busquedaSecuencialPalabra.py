def busqueda_secuencial(lista, palabra):
    for palabra in lista:
        if palabra == objetivo:
            return True
    return False

#Ejemplo de uso de la función
palabras = ["Manzana", "Pera", "Banana", "Uvas", "Kiwi", "Cherry", "Limon", "Fresa", "Naranja", "Melon"]
objetivo = "Parcha"

if busqueda_secuencial(palabras, objetivo):
    print(f"La palabra '{objetivo}' está en la lista.")
else:
    print(f"La palabra '{objetivo}' no está en la lista.")