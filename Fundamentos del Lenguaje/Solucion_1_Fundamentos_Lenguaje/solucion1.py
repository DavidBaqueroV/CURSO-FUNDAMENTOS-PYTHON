# DESARROLLADO POR: DAVID SANTIAGO BAQUERO VILLARRAGA

# SOLUCION PUNTO 1

# Primero vamos a crear un input en la cual el usuario puede ingresar

'''
Ahora crearemos la entrada de cantidad de frutos recolectados
'''

Frutos_Recolectados = float(
    input("Ingrese la cantidad de frutos recolectados: "))
Frutos_Producidos = float(input("Ingrese la cantidad de frutos producidos: "))

# crear la formula para la solucion del ejercicio

Indice_De_Cosecha = float(Frutos_Recolectados / Frutos_Producidos) * 100

# imprimimos por pantalla la salida de la solucion del ejercicio n°1

print(Indice_De_Cosecha)
