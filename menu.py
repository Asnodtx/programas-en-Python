
def accion1():
    print('Has elegido la opción 1')


def accion2():
    print('Has elegido la opción 2')


def accion3():
    print('Has elegido la opción 3')


def salir():
    print('Saliendo')
    
opciones = {
    '1': ('Opcion 1', accion1),
    '2': ('Opcion 2', accion2),
    '3': ('Opcion 3', accion3),
    '4': ('Salir', salir)
}

opcion = input('Elige una opcion: ')
if opcion in opciones:
    print(opciones[opcion][0])  
    opciones[opcion][1]()  
else:
    print('Opcion no valida')
