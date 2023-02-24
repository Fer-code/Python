#é como uma lista que não pode modificar
tupla = (1, 10, 12,14)

lista_animal = ["Arara", "Boi", "Cabrito", "Zebra"]

print(len(tupla))

#conversão
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)


lista = list(tupla)
print(type(lista))
lista[0] = 1000
print(lista)