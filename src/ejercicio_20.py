mayor = -1
while True:
    edad = int(input("Introduce una edad (-1 para terminar): "))
    if edad == -1:
        break
    if edad > mayor:
        mayor = edad
if mayor == -1:
    print("No se ingresaron edades válidas.")
else:
    print("La edad mayor ingresada es:", mayor)
