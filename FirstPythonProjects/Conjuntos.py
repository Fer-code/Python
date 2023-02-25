# number = int(input("Numero: "))

# conjunto = {1, 2, 3, 4} #não tem duplicidade em um conjunto
# conjunto.add(number)
# conjunto.discard(2) #descartar
# print(conjunto)

#UNIÃO DE CONJUNTOS
con1 = {1, 3, 5, 7, 100}
print(con1)
con2 = {2, 4, 6, 8, 100}
print(con2)
conU = con1.union(con2)
print(conU)

#INTERSECTION
conI = con1.intersection(con2)
print(conI)

#DIFERENÇA
conD = con1.difference(con2)
print(conD)
conD2 = con2.difference(con1)
print(conD2)

#DIFERENÇA SIMETRICA
conDS = con1.symmetric_difference(con2)
print(conDS)

#SUBCONJUNTO
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_b.issubset(conjunto_a)
print(conjunto_subset)

#
lista2 = ["cachorro", "gato", "gato", "sapo", "cachorro"]
conjunto_lista2 = set(lista2)
print(lista2, conjunto_lista2)
