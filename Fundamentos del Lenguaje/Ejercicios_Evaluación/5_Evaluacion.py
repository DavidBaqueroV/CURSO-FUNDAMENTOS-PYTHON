# 5. Aplicación de Operaciones sobre Valores Numéricos
valores = [10, 20, 30, 40, 50]
print("Valores iniciales:", valores)

suma = 0
for i in range(len(valores)):
    suma += valores[i]
print("Suma de valores:", suma)

eliminar = int(input("Ingrese el índice del valor a eliminar (1-5): ")) - 1
if 0 <= eliminar < len(valores):
    del valores[eliminar]
    print("Valores después de la eliminación:", valores)
else:
    print("Índice fuera de rango")

