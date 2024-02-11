def hola(**nombre):
#    print('Hola ' + kwargs['nombre'] + ' ' + kwargs['apellido'] + ' ' + kwargs['segundo_nombre'])
    print('Hola', end = ' ')
    for clave, valor in nombre.items():
        print(valor, end = ' ')
        
hola(titulo = 'Señor', nombre = 'Jesus', apellido = 'Marentes', segundo_nombre = 'Python')