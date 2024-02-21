try:
    with open('leer.txt') as file:
        print(file.read())
except FileNotFoundError:
    print('El archivo no fue encontrado')
