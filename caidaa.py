#Jesus Emilio Marentes Vejar 

import math
g = 9.81

def velocidad_exacta(m, g, c, t, dt):
    v = [0]
    for i in range(1, len(t)): 
        v.append(g * m / c * (1 - math.exp(-c / m * t[i])))
        g = g - c * v[-2] / m
    return v

def velocidad_aproximada(m, g, c, t, dt):
    v = [0]
    for i in range(1, len(t)):  
        v.append((g - c * v[i-1] / m) * dt + v[i-1])  
        g = g - c * v[i] / m
    return v

def main(): 
    m = float(input("Introduce el valor de la masa del paracaidista: "))
    c = float(input("Introduce el coeficiente de resistencia: "))
    dt = float(input("Introduce el incremento del tiempo: "))

    t = [i * dt for i in range(51)]
    v_exacta = velocidad_exacta(m, g, c, t, dt)
    v_aproximada = velocidad_aproximada(m, g, c, t, dt)

    print("t     vexacta    vaproximada   |Error|")
    for i in range(len(t)):
        error = abs(v_exacta[i] - v_aproximada[i])
        print("{:.2f}  {:.6f}  {:.6f}  {:.6f}".format(t[i], v_exacta[i], v_aproximada[i], error))

if __name__ == "__main__":
    main()