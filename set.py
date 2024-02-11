utensilios = {"tenedor","cuchara","cuchillo"}
platos = {"bol", "plato","taza"}

utensilios.add("cucharita")
utensilios.remove("tenedor")
# utensilios.pop()
# utensilios.clear()

utensilios.update(platos)
# print(utensilios.difference(platos))
print(utensilios.intersection(platos))

for i in utensilios:
    print(i)
# print(utensilios)