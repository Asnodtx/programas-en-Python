from oppauto import  Auto

auto_1 = Auto("Chevy", "Corvette", 2023,"Azul")
auto_2 = Auto("Ford", "Mustang", 2022,"Rojo")

print(auto_1.marca)
print(auto_1.modelo)
print(auto_1.ano)
print(auto_1.color)
print('\n')
print(auto_2.marca)
print(auto_2.modelo)
print(auto_2.ano)
print(auto_2.color)

print('\n')
auto_1.llantas = 1
print(auto_1.llantas)
