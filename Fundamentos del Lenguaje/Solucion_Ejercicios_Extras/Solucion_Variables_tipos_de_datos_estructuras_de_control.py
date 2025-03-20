#Desarrollado por David Santiago Baquero Villarraga ficha 3147247
# Solución Ejercicio 1: Calculadora Multiformato
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

suma = num1 + num2
diferencia = num1 - num2
producto = num1 * num2
division = num1 / num2 if num2 != 0 else "Indefinido"
residuo = num1 % num2 if num2 != 0 else "Indefinido"
potencia = num1 ** num2

print(f"Suma: {suma}\nDiferencia: {diferencia}\nProducto: {producto}\nDivisión: {division}\nResiduo: {residuo}\nPotencia: {potencia}")

# Solución Ejercicio 2: Conversión entre Sistemas Numéricos
decimal = int(input("Ingresa un número decimal: "))
print(
    f"Binario: {bin(decimal)}\nOctal: {oct(decimal)}\nHexadecimal: {hex(decimal)}")

num_bin = input("Ingresa un número binario: ")
print(f"Decimal: {int(num_bin, 2)}")

# Solución Ejercicio 3: Control de Precios y Descuentos
producto = input("Ingresa el nombre del producto: ")
precio = float(input("Ingresa el precio original: "))
descuento = precio * 0.10
precio_final = precio - descuento

print(f"Producto: {producto}\nPrecio original: {precio}\nDescuento: {descuento}\nPrecio final: {precio_final}")

# Solución Ejercicio 4: Análisis Detallado de una Frase
frase = input("Ingresa una frase: ")
caracter = input("Ingresa un carácter a contar: ")
print(
    f"Longitud: {len(frase)}\nPrimera letra: {frase[0]}\nÚltima letra: {frase[-1]}")
print(f"Mayúsculas: {frase.upper()}\nMinúsculas: {frase.lower()}")
print(f"El carácter '{caracter}' aparece {frase.count(caracter)} veces.")

# Solución Ejercicio 5: Cálculo de Bonificaciones Laborales
salario = float(input("Ingresa el salario actual: "))
años = int(input("Ingresa los años de trabajo: "))
bonificacion = salario * (0.05 * años)
total = salario + bonificacion

print(f"Salario: {salario}\nBonificación: {bonificacion}\nTotal: {total}")
