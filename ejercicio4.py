N = int(input("Introduce el número de elementos: "))
numeros = [int(input("Introduce el número {}: ".format(i+1))) for i in range(N)]
numeros_no_cero = [num for num in numeros if num != 0]
promedio = sum(numeros_no_cero) / len(numeros_no_cero)
print("Promedio de los números no cero:", promedio)
