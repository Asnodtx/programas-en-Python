# Solucion del problema del paracaidista que cae por el metodo aproximado
# Jesus Emilio Marentes Vejar 
import math

gravedad = 9.8

def calcular_velocidad(gravedad, masa_paracaidista, coeficiente_resistencia, tiempo_inicial, tiempo_final):
    velocidad_inicial = 0
    velocidad_final = (((masa_paracaidista) * (gravedad) - (coeficiente_resistencia) * (velocidad_inicial)) / (masa_paracaidista)) * (tiempo_final - tiempo_inicial) + velocidad_inicial
    return velocidad_final

masa_paracaidista = float(input("Ingresa la masa del paracaidista en KG: "))
coeficiente_resistencia = float(input("Ingresa el coeficiente de resistencia en KG/S: "))
tiempo_inicial = 0
tiempo_final = float(input("Ingresa el tiempo de caida en segundos: "))
num_iteraciones = int(input("Ingrese el numero de iteraciones: "))

velocidad = calcular_velocidad(gravedad, masa_paracaidista, coeficiente_resistencia, tiempo_inicial, tiempo_final)

print("La velocidad del paracaidista despues de", tiempo_final, "segundos es:", velocidad, "m/s")
