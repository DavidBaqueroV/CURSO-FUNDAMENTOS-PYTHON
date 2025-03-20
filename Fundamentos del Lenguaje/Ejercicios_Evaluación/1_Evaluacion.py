# 1. Procesamiento de Números del 1 al 20
numeros = list(range(1, 21))
divisibles = []
no_divisibles = []
suma_no_divisibles = 0

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        print(f"Posicion {i + 1}: {numeros[i]} es divisible por 2")
        divisibles.append(numeros[i])
    else:
        no_divisibles.append(numeros[i])
        suma_no_divisibles += numeros[i]

print("Suma de los numeros no divisibles por 2:", suma_no_divisibles)