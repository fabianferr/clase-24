N = int(input("Introduce el número de elementos: "))
numeros = [int(input("Introduce el número {}: ".format(i+1))) for i in range(N)]
numeros_impares = [num for num in numeros if num % 2 != 0]
promedio = sum(numeros_impares) / len(numeros_impares)
print("Promedio de los números impares:", promedio)
