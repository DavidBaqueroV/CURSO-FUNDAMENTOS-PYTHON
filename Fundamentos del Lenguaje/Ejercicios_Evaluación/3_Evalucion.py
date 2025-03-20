# 3. Filtrado y Transformación de Texto
entrada = input("Ingrese cualquier tipo de texto: ")

resultado = ""

for caracter in entrada:
    if caracter.isalpha():
        resultado += caracter

print("Texto filtrado:", resultado)