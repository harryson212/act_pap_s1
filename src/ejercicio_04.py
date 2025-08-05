total = 0
while True:
    num = int(input("Ingresa un número (0 para terminar): "))
    if num == 0:
        break
    total += num
print("La suma total es:", total)
