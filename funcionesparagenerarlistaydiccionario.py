import random

def generar_lista_aleatoria(n, minimo=1, maximo=100):
    return [random.randint(minimo, maximo) for _ in range(n)]

def crear_diccionario_cuadrados(lista):
    return {i+1: lista[i]**2 for i in range(len(lista))}

def main():
    try:
        n = int(input("Ingrese la cantidad de números aleatorios que desea generar: "))
        lista = generar_lista_aleatoria(n)
        diccionario = crear_diccionario_cuadrados(lista)
        
        print("\nLista de números aleatorios:")
        print(lista)
        print("\nDiccionario con cuadrados:")
        for clave, valor in diccionario.items():
            print(f"{clave}: {valor}")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

main()