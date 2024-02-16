N = int(input("Introduce el número de elementos: "))
numeros = [int(input("Introduce el número {}: ".format(i+1))) for i in range(N)]
suma = sum(numeros)
promedio = suma / N
print("Suma:", suma)
print("Promedio:", promedio)
