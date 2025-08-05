contador = 0
while True:
    palabra = input("Escribe una palabra ('fin' para terminar): ").lower()
    if palabra == "fin":
        break
    contador += 1
print("Palabras leídas:", contador)
