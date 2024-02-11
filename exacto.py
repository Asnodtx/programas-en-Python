# Solucion del problema del paracaidista que cae por el metodo exacto
# Jesus Emilio Marentes Vejar 

import math

gravedad = 9.8

def calcular_velocidad(masa_paracaidista, coeficiente_resistencia, tiempo):
    return gravedad * masa_paracaidista / coeficiente_resistencia * (1 - math.exp(-coeficiente_resistencia / masa_paracaidista * tiempo))

masa_paracaidista = float(input("Ingresa la masa del paracaidista en KG: "))
coeficiente_resistencia = float(input("Ingresa el coeficiente de resistencia en KG/S: "))

for tiempo in range(0, 11):  
    velocidad = calcular_velocidad(masa_paracaidista, coeficiente_resistencia, tiempo)
    print("La velocidad del paracaidista después de", tiempo, "segundos es:", velocidad, "m/s")
