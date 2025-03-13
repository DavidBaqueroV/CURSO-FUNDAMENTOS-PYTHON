# Desarrollar una (list) de números
num = [1, 2, 3, 4, 5, 2, 6, 2, 7]

# Solicitar un número al usuario
numero_a_eliminar = int(input("Introduzca el número que desea eliminar: "))

# Delet todas las ocurrencias del número en la lista
while numero_a_eliminar in num:
    num.remove(numero_a_eliminar)

# Presentar la lista final
print("Lista final después de eliminar el número:", num)
