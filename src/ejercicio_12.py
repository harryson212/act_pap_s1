n = int(input("Introduce un número entero para calcular su factorial: "))
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print(f"El factorial de {n} es {factorial}")
