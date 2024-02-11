import random

x = random.randint(1, 10)
y = random.random()

juego = ['Piedra', 'Papel', 'Tijera']
z = random.choice(juego)

cartas = ['1', '2', '3', '4', 'A', 'B', 'C']
random.shuffle(cartas)
print(cartas)