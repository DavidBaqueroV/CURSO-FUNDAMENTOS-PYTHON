#DESARROLLADO POR: DAVID SANTIAGO BAQUERO VILLARRAGA

# Leer calificaciones parciales
parcial1 = float(input("Ingrese la primera calificación parcial: "))
parcial2 = float(input("Ingrese la segunda calificación parcial: "))
parcial3 = float(input("Ingrese la tercera calificación parcial: "))

# Leer examen final y trabajo final
examen_final = float(input("Ingrese la calificación del examen final: "))
trabajo_final = float(input("Ingrese la calificación del trabajo final: "))

# Calcular el promedio de parciales
promedio_parciales = (parcial1 + parcial2 + parcial3) / 3

# Calcular la calificación final
calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)

# Mostrar resultado
print(f"La calificación final es: {calificacion_final:.2f}")
