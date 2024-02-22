def calcular_parte_entera(numero, base):
    parte_entera = []
    while numero > 0:
        cociente = int(numero // base)
        residuo = int(numero % base)
        parte_entera.append(residuo)
        numero = cociente
    return parte_entera[::-1]

def calcular_parte_fraccionaria(numero, base, iteraciones = 10):
    resultado = []
    for _ in range(iteraciones):
        numero *= base
        parte_entera = int(numero)
        resultado.append(parte_entera)
        numero -= parte_entera
        if numero == 0:
            break
    return resultado
  
def main():
    base = 0
    numero = float(input('Ingrese el numero: '))

    while base < 2 or base > 9:
        base = float(input(str('Ingrese el la base (2 al 9): '))) 

    parte_entera = calcular_parte_entera(numero, base)
    resultado = calcular_parte_fraccionaria(numero - int(numero), base, 10) 
    print("La parte entera de {} en base {} es: {}".format(numero, base, parte_entera))
    print("La parte fraccionaria de {} en base {} es: {}".format(numero, base, resultado))

if __name__== "__main__":
    main()