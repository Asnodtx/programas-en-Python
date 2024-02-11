capitales = {
    'EE.UU': 'Washington D.C',
    'Argentina': 'Benos Aires',
    'Chile': 'Santiago de chile',
    'Brasil': 'Brasilia',
    'cursos': ['Python', 'C++']
}

capitales.update({'Alemania': 'Berlin'})
capitales.pop('EE.UU')

# print(capitales.get('Argentina'))
# print(capitales.keys())
# print(capitales.values())
# print(capitales.items())

for key,value in capitales.items():
    print(key,value)