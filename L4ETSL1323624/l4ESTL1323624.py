#Numero1
# Definir la lista de precios
precios = (50, 75, 46, 22, 80, 65, 8,)

# Función para obtener el precio mayor
def obtener_mayor_precio(lista):
    mayor_precio = lista[0]
    for precio in lista:
        if precio > mayor_precio:
            mayor_precio = precio 
    return mayor_precio
mayor_precio = obtener_mayor_precio(precios)
print("El mayor precio es:", mayor_precio)
#Numero2
abecedario = "abcdefghijklmnñopqrstuvwxyz"
resultado = [letra for indice, letra in enumerate(abecedario) if (indice + 1) % 3 != 0]
print("Lista resultante:", resultado)
#numero3
print("Introduce palabras para la lista. Introduce 'fin' para terminar:")
palabras = []
while True:
    palabra = input("Palabra: ")
    if palabra == "fin":
        break 
    palabras.append(palabra)
print("Lista de palabras:", palabras)

buscar_palabra = input("Introduce la palabra que deseas encontrar: ")
contador = palabras.count(buscar_palabra)
print(f"La palabra '{buscar_palabra}' aparece {contador} veces en la lista.")

