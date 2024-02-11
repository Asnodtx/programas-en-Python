fila = int(input("Ingrese las filas: "))
columna = int(input("Ingrese las columnas: "))
simbolo = input("Ingrese el simbolo: ")

for i in range(fila):
    for j in range(columna):
        print(simbolo, end = "")
    print()