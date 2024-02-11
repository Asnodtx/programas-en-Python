def suma(*args):
    suma = 0
    for i in args:
        suma += i
    return suma
    
print(suma(1, 5, 3, 2, 7))