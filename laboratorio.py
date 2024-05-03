# Ejercicio 1
def tipotriangulo(a, b, c):
    if a == b == c:
        return "equilátero"
    elif a == b or a == c or b == c:
        return "isósceles"
    else:
        return "escaleno"

def main():
    a = float(input("Ingrese el lado del primer: "))
    b = float(input("Ingrese el lado del segundo: "))
    c = float(input("Ingrese el lado del tercero: "))

    tipo = tipotriangulo(a, b, c)
    print("El triángulo es", tipo)

if __name__ == "__main__":
    main()

# Ejercicio 2
import math

print("Ingrese el radio: ")
radio = float(input())

def obtener_perimetro(r):
    perimetro = float(2 * r) * math.pi
    return perimetro

print("Perímetro: " + str(obtener_perimetro(radio)))

