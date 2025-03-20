# Desarrollado por: David Santiago Baquero Villarraga. ficha:3147247
# solucion primer ejercicio
import re
import random

numero_secreto = random.randint(1, 100)
intento = None

print("¡Bienvenido al juego! Adivina el número secreto entre 1 y 100.")

while intento != numero_secreto:
    intento = int(input("Introduce tu número: "))

    if intento < numero_secreto:
        print("El número secreto es mayor.")
    elif intento > numero_secreto:
        print("El número secreto es menor.")
    else:
        print("¡Felicidades! Has adivinado el número.")

# solucion segundo ejercicio


def es_contraseña_segura(contraseña):
    if (len(contraseña) >= 8 and
        re.search(r'[A-Z]', contraseña) and
        re.search(r'[a-z]', contraseña) and
            re.search(r'\d', contraseña)):
        return True
    return False


while True:
    contraseña = input("Introduce una contraseña segura: ")
    if es_contraseña_segura(contraseña):
        print("Contraseña segura. ¡Bienvenido!")
        break
    else:
        print("La contraseña no es segura. Debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número.")
# solucion tercer ejercicio
edad = int(input("Introduce tu edad: "))
invitacion = input("¿Tienes invitación? (sí/no): ").strip().lower()

if edad >= 18 and invitacion == "sí":
    print("Acceso concedido. ¡Bienvenido al evento!")
else:
    print("Acceso denegado. No cumples los requisitos.")
# solucion cuarto ejercicio
numero = int(input("Introduce un número entero: "))
factorial = 1

for i in range(1, numero + 1):
    factorial *= i

print(f"El factorial de {numero} es {factorial}.")
# solucion quinto ejercicio
numero = int(input("Introduce un número: "))
limite = 10  # Se puede cambiar el límite si se desea

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, limite + 1):
    print(f"{numero} x {i} = {numero * i}")
