# 2. Administración de Actividades Diarias
actividades = ["tarea1", "tarea2", "tarea3", "tarea4", "tarea5"]
print("Actividades por realizar hoy:", actividades)

# Entrada del usuario
tarea_solucion = input("¿Usted realizó todas las tareas del día de hoy? (si/no): ").strip().lower()

if tarea_solucion == "si":
    print("Usted realizó todas las tareas del día de hoy.")
elif tarea_solucion == "no":
    tareas_incompletas = input("¿Cuál tarea le faltó por completar?: ")
    print("A usted le faltó realizar estas tareas:", tareas_incompletas, "en comparación con:", actividades)
else:
    print("Respuesta no válida. Por favor, responda con 'si' o 'no'.")

