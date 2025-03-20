# 4. Informe Interactivo de Alumnos
nombres = ["Ana", "Luis", "Carlos", "Marta"]
calificaciones = [85, 20, 78, 92]

print("Lista de alumnos y calificaciones:")
for i in range(len(nombres)):
    print(f"{i + 1}. {nombres[i]} - {calificaciones[i]}")

indice = int(input("Ingrese el número del alumno para ver su calificación: ")) - 1
if 0 <= indice < len(nombres):
    print(f"{nombres[indice]} tiene una calificación de {calificaciones[indice]}")
else:
    print("Índice fuera de rango")