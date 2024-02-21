import random

lista = ['piedra','papel','tijera']

while True:
    computadora = random.choice(lista)
    jugador = None

    while jugador not in lista:
        jugador = input('piedra, papel o tijera? ').lower()

    if jugador == computadora:
        print('Computadora: ', computadora)
        print('Jugador: ', jugador)
        print('Empate')
    elif jugador == 'piedra':
        if computadora == 'papel':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Computadora gano')
        if computadora == 'tijera':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Jugador gano')

    elif jugador == 'papel':
        if computadora == 'piedra':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Jugador gano')
        if computadora == 'tijera':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Computadora gano')

    elif jugador == 'tijera':
        if computadora == 'piedra':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Computadora gano')
        if computadora == 'papel':
            print('Computadora: ', computadora)
            print('Jugador: ', jugador)
            print('Jugador gano')
    

    jugar_de_nuevo = input('Deseas seguir jugando (si/no): ').lower()
    if jugar_de_nuevo != 'si':
        break
print('Adios')