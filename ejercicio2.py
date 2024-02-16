num = int(input("Introduce un número: "))
suma = sum(range(num + 1 if num % 2 != 0 else num + 2, num + 9, 2))
print(suma)
